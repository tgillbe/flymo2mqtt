from queue import Queue
from uuid import UUID
from .chunking_write_stream import ChunkingWriteStream
from .packet_interface import PacketInterface
from .packet_framer import PacketFramer
from .packet import Request, Response
import paho.mqtt.client as mqtt
import logging

logger = logging.getLogger(__name__)

def bytes_to_str(bytes: bytes) -> str:
    return ','.join([str(b) for b in bytes])

def str_to_bytes(value: str) -> bytes:
    return bytes([int(s) for s in value.decode().split(',')])

class MqttPacketInterface():
    interface: PacketInterface
    read_topic: str

    def on_message(self, msg):
        if msg.topic == self.read_topic and not msg.retain:
            value = str_to_bytes(msg.payload)
            self.interface.receive(value)

    def __init__(self, packet_framer: PacketFramer, client: mqtt.Client, mac: str, service_control: UUID, char_write: UUID, char_read: UUID):
        # TODO: Connect check not working
        # q = Queue()
        # def message_received(msg):
        #     q.put(msg)
        # client.on_message = lambda client, userdata, msg: message_received(msg)
        # client.subscribe(f"{mac}/Connected", qos=2)
        # message = q.get(1, timeout=1)
        # client.on_message = None
        # if message.payload.decode() == "false":
        #     raise Exception("Device not connected")

        # Setup the write / read interfaces
        def send(bytes: bytes):
            logger.debug(f"TX: {bytes.hex()}")
            client.publish(f"{mac}/{service_control}/{char_write}/Set", bytes_to_str(bytes), qos=2)
        self.interface = PacketInterface(packet_framer, ChunkingWriteStream(20, lambda bytes: send(bytes)))
        self.read_topic = f"{mac}/{service_control}/{char_read}"
        client.message_callback_add(self.read_topic, lambda _, __, message: self.on_message(message))
        client.subscribe(self.read_topic, qos=2)

    def send(self, packet: Request) -> Response:
        return self.interface.send(packet)
