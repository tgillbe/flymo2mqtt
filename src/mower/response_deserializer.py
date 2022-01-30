from typing import Callable, Dict, List
from .in_memory_stream import InMemoryStream
from .result_code import ResultCode
from .packet import Response
from . import MalformedPacketException, StatusError

class ResponseDeserializer():
    response_map: Dict[int, Callable[[], Response]]
    
    def __init__(self, response_generators: List[Callable[[], Response]]):
        self.response_map = {}
        for gen in response_generators:
            instance = gen()
            if instance.head2 is not None:
                self.response_map[(instance.head << 16) + instance.head2] = gen
            else:
                self.response_map[instance.head] = gen

    def deserialize(self, data: bytes) -> Response:
        stream = InMemoryStream(data)
        head = stream.read_u8()
        if head == 1:
            # V2 packets?
            if stream.read_u8() != 0xAF:
                raise MalformedPacketException
            head1 = stream.read_u16()
            head2 = stream.read_u16()
            status = ResultCode(stream.read_u8())
            stream.read_u16() # This is probably length - but we don't need it?
            if status != ResultCode.OK:
                raise StatusError(f"Unexpected status: {status}")
            head = (head1 << 16) + head2
        response_geneartor = self.response_map.get(head, None)
        if response_geneartor is None:
            raise NotImplementedError(f"Could not find packet with ID {head}")
        
        response = response_geneartor()
        for parameter in response.parameters:
            value = None
            if parameter.type == "u8":
                value = stream.read_u8()
            elif parameter.type == "u16":
                value = stream.read_u16()
            elif parameter.type == "u32":
                value = stream.read_u32()
            elif parameter.type == "str":
                value = stream.read_str()
            elif parameter.type == "bool":
                value = stream.read_u8() != 0
            else:
                raise NotImplementedError()
            setattr(response, parameter.name, value)
        return response
