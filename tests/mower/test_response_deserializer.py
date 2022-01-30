import context # type: ignore
from mower.response_deserializer import ResponseDeserializer
from mower.packets import ConnectResponse, GetStateResponse
import unittest
from mower import StatusError

class TestResponseDeserializer(unittest.TestCase):
    def test_deserialize(self):
        parsed = ResponseDeserializer([ConnectResponse]).deserialize(bytes([
            0x15, 0x90, 0xA1, 0x79, 0x5D
        ]))
        self.assertIsInstance(parsed, ConnectResponse)
        self.assertEqual(parsed.new_link_id, 1568252304)

    def test_deserialize_error(self):
        self.assertRaises(StatusError, lambda: ResponseDeserializer([GetStateResponse]).deserialize(bytes([
            0x01, 0xaf, 0x8c, 0x16, 0x00, 0x00, 0x05, 0x00, 0x00
        ])))

if __name__ == '__main__':
    unittest.main()
