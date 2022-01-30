from typing import Callable, Optional
from .in_memory_stream import InMemoryStream

class ChunkingWriteStream():
    buffer: InMemoryStream
    max_length: int
    callback: Callable[[bytes], None]

    def __init__(self, max_length: int, callback: Callable[[bytes], None]):
        self.buffer = InMemoryStream()
        self.max_length = max_length
        self.callback = callback
    
    def write_u8(self, value: int):
        self.buffer.write_u8(value)
        self.flush_if_full()

    def write_u16(self, value: int):
        self.buffer.write_u16(value)
        self.flush_if_full()

    def write_u32(self, value: int):
        self.buffer.write_u32(value)
        self.flush_if_full()

    def write_str(self, value: str):
        self.buffer.write_str(value)
        self.flush_if_full()

    def write_bytes(self, value: bytes):
        self.buffer.write_bytes(value)
        self.flush_if_full()

    def flush_if_full(self):
        flush_count = self.buffer.bytes.tell() // self.max_length
        if flush_count != 0:
            self.flush(flush_count * self.max_length)

    def flush(self, length: Optional[int] = None):
        if length == None:
            length = self.buffer.bytes.tell()
        data = self.buffer.bytes.getvalue()[:length]
        
        # Remove the consumed data from the buffer
        self.buffer.truncate_start(length)
        
        # Write the requested number of bytes out in up to max_length
        position = 0
        while length > 0:
            write_len = min(self.max_length, length)
            self.callback(data[position:position + write_len])
            position = position + write_len
            length = length - write_len
