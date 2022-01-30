from typing import Callable, Dict
import paho.mqtt.client as mqtt
import json

class StateUpdater():
    client: mqtt.Client
    discovery_topic: str
    command_topic: str
    state_topic: str
    commands: Dict[str, Callable[[], None]]
    active: Dict[str, bool]

    def __init__(self, client: mqtt.Client, discovery_topic: str, availability_topic: str, command_topic: str, state_topic: str, commands: Dict[str, Callable[[], None]]):
        self.client = client
        self.discovery_topic = discovery_topic
        self.availability_topic = availability_topic
        self.command_topic = command_topic
        self.state_topic = state_topic
        self.commands = commands
        self.active = {}
        client.message_callback_add(self.command_topic, lambda _, __, msg: self.command_received(msg))
        client.will_set(self.availability_topic, "offline")

    def subscribe(self):
        self.client.subscribe(self.command_topic)

    def command_received(self, msg):
        if msg.topic == self.command_topic:
            command = msg.payload.decode()
            if command in self.commands:
                self.commands[command]()

    def update(self, name: str, availble: bool, battery_level: int, state: str):
        if not name in self.active:
            self.active[name] = False
        if not self.active[name]:
            self.active[name] = True
            # Discovery
            self.client.publish(f"{self.discovery_topic}/vacuum/{name}/config", json.dumps({
                "availability": [
                    {
                        "topic": self.availability_topic
                    }
                ],
                "device": {
                    "identifiers": [name]
                },
                "name": name,
                "schema": "state",
                "state_topic": self.state_topic,
                "command_topic": self.command_topic,
                "supported_features": ["start", "stop", "return_home"]
            }), retain=True)
        self.client.publish(self.availability_topic, "online" if availble else "offline", retain=True)
        self.client.publish(self.state_topic, json.dumps({
            "battery_level": battery_level,
            "state": state,
        }), retain=True)
