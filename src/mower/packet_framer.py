from .__init__ import MalformedPacketException
import struct
from typing import Callable, Optional
from .data_stream import ReadableStream, WritableStream
from .packet import Request, Response
from .request_serializer import RequestSerializer
from .response_deserializer import ResponseDeserializer
import crcmod.predefined

class PacketFramer():
    request_serializer: RequestSerializer
    response_deserializer: ResponseDeserializer
    channel_id: int
    crc: Callable[[bytes], int]

    def __init__(self, request_serializer, response_deserializer):
        self.request_serializer = request_serializer
        self.response_deserializer = response_deserializer
        self.channel_id = 0
        self.crc = crcmod.predefined.mkPredefinedCrcFun('crc-8-maxim')

    def write(self, packet: Request, stream: WritableStream):
        # Serialize components
        payload = self.request_serializer.serialize(packet)
        length_bytes = struct.pack('<H', len(payload) + 8)
        channel_id_bytes = struct.pack('<I', self.channel_id)
        flag = bytes([1 if packet.head2 is not None else 0])
        header = bytes([0xFD]) + length_bytes + channel_id_bytes + flag

        # Calculate the CRCs
        header_crc = self.crc(header)
        full_crc = self.crc(header + bytes([header_crc]) + payload)

        # Write the packet
        stream.write_u8(0x02)
        stream.write_bytes(header)
        stream.write_u8(header_crc)
        stream.write_bytes(payload)
        stream.write_u8(full_crc)
        stream.write_u8(3)
        stream.flush()

    def read(self, stream: ReadableStream) -> Optional[Response]:
        if stream.length() < 10:
            return None
        
        if stream.read_u8() != 0x02:
            raise MalformedPacketException
            
        header = stream.read_bytes(8)
        if header[0] != 0xFD:
            raise MalformedPacketException

        header_crc = self.crc(header)
        if stream.read_u8() != header_crc:
            raise MalformedPacketException
            
        length = struct.unpack('<H', header[1:3])[0]

        if stream.length() < length - 6:
            return None
        
        channel_id = struct.unpack('<I', header[3:7])[0]
        flag = header[7]
        payload = stream.read_bytes(length - 8)

        payload_crc = self.crc(header + bytes([header_crc]) + payload)
        if stream.read_u8() != payload_crc:
            raise MalformedPacketException
        
        if stream.read_u8() != 3:
            raise MalformedPacketException

        if channel_id != self.channel_id:
            raise NotForUsPacketException # This isn't really exceptional but oh well, just need to ignore these packets

        return self.response_deserializer.deserialize(payload)
        
class NotForUsPacketException(Exception):
    pass
