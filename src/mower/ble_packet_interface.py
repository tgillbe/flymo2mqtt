from uuid import UUID
from pygatt.device import BLEDevice
from .chunking_write_stream import ChunkingWriteStream
from .packet_interface import PacketInterface
from .packet_framer import PacketFramer
from .packet import Request, Response

class BlePacketInterface():
    interface: PacketInterface

    def __init__(self, packet_framer: PacketFramer, device: BLEDevice, char_write: UUID, char_read: UUID):
        # The mower uses a bluetooth 4.2 chip and communicates with the app using a LE Secure Connection.
        # Make sure to bond otherwise the mower will not respond.
        device.bond()

        # Setup the write / read interfaces
        self.interface = PacketInterface(packet_framer, ChunkingWriteStream(20, lambda bytes: device.char_write(char_write, bytes, wait_for_response=False)))
        device.subscribe(char_read, lambda _, value: self.interface.receive(value), wait_for_response=False)

    def send(self, packet: Request) -> Response:
        return self.interface.send(packet)
