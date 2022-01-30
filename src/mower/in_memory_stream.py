from io import BytesIO
from typing import Optional
import struct

class InMemoryStream():
    bytes: BytesIO

    def __init__(self, initial_bytes: bytes = bytes()):
        self.bytes = BytesIO(initial_bytes)

    def length(self):
        return self.bytes.getbuffer().nbytes - self.bytes.tell()

    def truncate_start(self, position: Optional[int] = None):
        if position is None:
            position = self.bytes.tell()
        data = self.bytes.getvalue()[position:]
        self.bytes.seek(0)
        self.bytes.truncate()
        self.bytes.write(data)

    def write_u8(self, value: int):
        self.bytes.write(bytearray([value & 0xFF]))

    def write_u16(self, value: int):
        self.bytes.write(struct.pack('<H', value))

    def write_u32(self, value: int):
        self.bytes.write(struct.pack('<I', value))

    def write_str(self, value: str):
        self.bytes.write(value.encode('iso-8859-1'))
        self.bytes.write(bytearray([0]))

    def write_bytes(self, value: bytes):
        self.bytes.write(value)

    def flush(self):
        pass

    def read_u8(self) -> int:
        return self.bytes.read(1)[0]

    def read_u16(self) -> int:
        return struct.unpack('<H', self.bytes.read(2))[0]

    def read_u32(self) -> int:
        return struct.unpack('<I', self.bytes.read(4))[0]

    def read_str(self) -> str:
        str = bytearray()
        while True:
            value = self.bytes.read(1)[0]
            if value == 0:
                break
            else:
                str.append(value)
        return str.decode('iso-8859-1')

    def read_bytes(self, length: Optional[int] = None) -> bytes:
        return self.bytes.read(length)
