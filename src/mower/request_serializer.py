from .in_memory_stream import InMemoryStream
from .packet import Request

class RequestSerializer():
    def serialize(self, request: Request) -> bytes:
        data = InMemoryStream()
        for parameter in request.parameters:
            value = getattr(request, parameter.name)
            if parameter.type == "u8":
                data.write_u8(value)
            elif parameter.type == "u16":
                data.write_u16(value)
            elif parameter.type == "u32":
                data.write_u32(value)
            elif parameter.type == "str":
                data.write_str(value)
            elif parameter.type == "bool":
                data.write_u8(1 if value else 0)
            else:
                raise NotImplementedError()
        payload = data.bytes.getvalue()
        data.truncate_start()
        # Why are there these different kinds of packets? Some kind of passthrough??
        if request.head2 is not None:
            data.write_u8(0x00)
            data.write_u8(0xAF)
            data.write_u16(request.head)
            data.write_u16(request.head2)
            data.write_u16(len(payload))
        else:
            data.write_u8(request.head)
        data.write_bytes(payload)
        return data.bytes.getvalue()
