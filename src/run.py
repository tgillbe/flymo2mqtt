#!/usr/bin/env python3

import argparse
import sys
from typing import cast
from uuid import UUID
from binascii import Error, hexlify
from time import sleep
import logging

from hass.state_updater import StateUpdater
from mower.activity import MowerActivity
from mower.state import MowerStatus
from mower.mqtt_packet_interface import MqttPacketInterface
from mower.packet_framer import PacketFramer
from mower.packets import GetActivityRequest, GetModelRequest, GetModelResponse, GetOverrideRequest, GetOverrideResponse, GetStateRequest, GetStateResponse, GetSwPackageVersionStringRequest, GetSwPackageVersionStringResponse, IsOperatorLoggedInRequest, IsOperatorLoggedInResponse, SetProtocolVersionRequest, get_responses, ConnectRequest, ConnectResponse, EnterOperatorPinRequest, GetActivityResponse
from mower.request_serializer import RequestSerializer
from mower.response_deserializer import ResponseDeserializer
import paho.mqtt.client as mqtt

logger = logging.getLogger(__name__)
logging.basicConfig(level = logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

parser = argparse.ArgumentParser(description='Flymo EasiLife bluetooth/mqtt client.')
parser.add_argument('--mac', metavar='address', type=str, help='mac address of lawnmower', required=True)
parser.add_argument('--mqttserver', metavar='ip', type=str, help='mqtt server address', required=True)
parser.add_argument('--name', metavar='name', type=str, help='name of lawnmower for hass', default="Flymo")
parser.add_argument('--mqttport', metavar='port', type=int, help='mqtt server port', default=1883)

args = parser.parse_args()

discovery_topic = "homeassistant"
availability_topic = "vacuum/availability"
command_topic = "vacuum/command"
state_topic = "vacuum/state"

mqtt_client = mqtt.Client()
updater = StateUpdater(
    mqtt_client,
    discovery_topic,
    availability_topic,
    command_topic,
    state_topic,
    {
        "start": lambda: logger.log("Start"),
    })
mqtt_client.on_message = lambda _, __, msg: logger.debug(f"MQTT: {msg.topic} {msg.qos} {msg.payload}")
mqtt_client.loop_start()
mqtt_client.connect(args.mqttserver, args.mqttport, 60)
updater.subscribe()

characteristic_device_name = UUID('00002a00-0000-1000-8000-00805f9b34fb')
service_control = UUID('98bd0001-0b0e-421a-84e5-ddbf75dc6de4')
characteristic_write = UUID('98BD0002-0B0E-421A-84E5-DDBF75DC6DE4')
characteristic_read = UUID('98BD0003-0B0E-421A-84E5-DDBF75DC6DE4')

framer = PacketFramer(RequestSerializer(), ResponseDeserializer(get_responses()))

try:
    logger.debug("Configuring packet interface")
    interface = MqttPacketInterface(framer, mqtt_client, args.mac, service_control, characteristic_write, characteristic_read)
    logger.debug("Sending connect")
    response = cast(ConnectResponse, interface.send(ConnectRequest(1568252304, 0, "Main")))
    logger.debug(f'Link ID {response.new_link_id}')
    framer.channel_id = response.new_link_id

    interface.send(SetProtocolVersionRequest(1))

    response = cast(GetModelResponse, interface.send(GetModelRequest()))
    logger.debug(f'Type {response.device_type}, variant: {response.device_variant}')

    interface.send(EnterOperatorPinRequest(1234))
    response = cast(IsOperatorLoggedInResponse, interface.send(IsOperatorLoggedInRequest()))
    if not response.operator_logged_in:
        raise Error()

    response = cast(GetSwPackageVersionStringResponse, interface.send(GetSwPackageVersionStringRequest()))
    logger.debug(f'Version {response.sw_package_version}')
except Exception:
    logger.exception("Failed connecting")
    sys.exit()

logger.info("Connected")


activity_map = {
    MowerActivity.CHARGING: "docked",
    MowerActivity.GOING_HOME: "returning",
    MowerActivity.LEAVING: "cleaning",
    MowerActivity.MOWING: "cleaning",
    MowerActivity.NONE: "idle",
    MowerActivity.PARKED_IN_CHARGING_STATION: "docked",
    MowerActivity.STOPPED_IN_GARDEN: "error",
    MowerActivity.UNKNOWN: "error",
}

test = cast(GetOverrideResponse, interface.send(GetOverrideRequest()))

while True:
    try:
        activity = MowerActivity(cast(GetActivityResponse, interface.send(GetActivityRequest())).mower_activity)
        logger.debug(f'Activity: {activity}')
        updater.update(args.name, True, 0, activity_map[activity])
    except Exception:
        logger.exception("Failed to get activity")
    sleep(60)
