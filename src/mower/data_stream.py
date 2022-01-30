from typing import Optional, Protocol

class ReadableStream(Protocol):
    def length(self) -> int:
        ...

    def read_u8(self) -> int:
        ...

    def read_u16(self) -> int:
        ...

    def read_u32(self) -> int:
        ...

    def read_str(self) -> str:
        ...

    def read_bytes(self, length: Optional[int] = None) -> bytes:
        ...

class WritableStream(Protocol):
    def write_u8(self, value: int):
        ...

    def write_u16(self, value: int):
        ...

    def write_u32(self, value: int):
        ...

    def write_str(self, value: str):
        ...

    def write_bytes(self, value: bytes):
        ...

    def flush(self):
        ...
