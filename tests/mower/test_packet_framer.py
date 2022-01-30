import context # type: ignore
from mower.in_memory_stream import InMemoryStream
from mower.packet_framer import PacketFramer
import unittest
from mower.packets import get_responses, ConnectRequest, ConnectResponse, GetModelRequest, GetModelResponse, SetProtocolVersionRequest, SetProtocolVersionResponse
from mower.request_serializer import RequestSerializer
from mower.response_deserializer import ResponseDeserializer

class TestPacketFramer(unittest.TestCase):
    def test_write(self):
        stream = InMemoryStream()
        dut = PacketFramer(RequestSerializer(), ResponseDeserializer([]))
        for request, expected_bytes in self.requests:
            dut.write(request, stream)
            value = stream.bytes.getvalue()
            stream.truncate_start()
            self.assertEqual(bytes(expected_bytes), value)
            dut.channel_id = 1568252304

    def test_read(self):
        dut = PacketFramer(RequestSerializer(), ResponseDeserializer(get_responses()))
        for expected_response, data in self.responses:
            stream = InMemoryStream(bytes(data))
            response = dut.read(stream)
            self.assertIsInstance(response, type(expected_response))
            for key in dir(expected_response):
                if not key.startswith('__') and key != 'parameters' and not callable(getattr(expected_response, key)):
                    self.assertEqual(getattr(response, key), getattr(expected_response, key))
            dut.channel_id = 1568252304

    def test_read_truncated_data(self):
        data = bytes([
            0x02, # Start
            0xFD, # Header?
            0x0D, 0x00, # Length
            0x00, 0x00, 0x00, 0x00, # Channel ID
            0x00, # Flag
            0x63, # Header CRC
            0x15, # Packet type
            0x90, 0xA1, 0x79, 0x5D,
            0x30, 0x03
        ])
        dut = PacketFramer(RequestSerializer(), ResponseDeserializer([ConnectResponse]))
        for i in range(len(data)):
            self.assertEqual(dut.read(InMemoryStream(data[:i])), None)

    requests = [
        (
            ConnectRequest(1568252304, 0, "Main"),
            [
                0x02, # Start
                0xFD, # Header?
                0x16, 0x00, # Length
                0x00, 0x00, 0x00, 0x00, # Channel ID
                0x00, # Flag
                0x2E, # Header CRC
                0x14, # ConnectRequest.get_head()
                0x90, 0xA1, 0x79, 0x5D, # ConnectRequest.link_id
                0x00, 0x00, 0x00, 0x00, # ConnectRequest.node_type
                0x4D, 0x61, 0x69, 0x6E, 0x00, # ConnectRequest.name
                0x4C, # Full CRC
                0x03 # End
            ]
        ),
        (
            SetProtocolVersionRequest(1),
            [0x02, 0xFD, 0x0A, 0x00, 0x90, 0xA1, 0x79, 0x5D, 0x00, 0xDE, 0x08, 0x01, 0x28, 0x03]
        ),
        (
            GetModelRequest(),
            [0x02, 0xFD, 0x10, 0x00, 0x90, 0xA1, 0x79, 0x5D, 0x01, 0xF0, 0x00, 0xAF, 0x5A, 0x12, 0x09, 0x00, 0x00, 0x00, 0xB7, 0x03]
        )
    ]

    responses = [
        (
            ConnectResponse(1568252304),
            [
                0x02, # Start
                0xFD, # Header?
                0x0D, 0x00, # Length
                0x00, 0x00, 0x00, 0x00, # Channel ID
                0x00, # Flag
                0x63, # Header CRC
                0x15, # Packet type
                0x90, 0xA1, 0x79, 0x5D,
                0x30, 0x03
            ]
        ),
        (
            SetProtocolVersionResponse(1, 1),
            [0x02, 0xFD, 0x0B, 0x00, 0x90, 0xA1, 0x79, 0x5D, 0x00, 0xE3, 0x09, 0x01, 0x01, 0x14, 0x03]
        ),
        (
            GetModelResponse(30, 3),
            [0x02, 0xFD, 0x13, 0x00, 0x90, 0xA1, 0x79, 0x5D, 0x01, 0xB7, 0x01, 0xAF, 0x5A, 0x12, 0x09, 0x00, 0x00, 0x02, 0x00, 0x1E, 0x03, 0xC6, 0x03]
        )
    ]

if __name__ == '__main__':
    unittest.main()
