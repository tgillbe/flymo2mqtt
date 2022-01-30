import context # type: ignore
from mower.request_serializer import RequestSerializer
from mower.packets import ConnectRequest
import unittest

class TestRequestSerializer(unittest.TestCase):
    def test_serialize(self):
        self.assertEqual(
            bytes([0x14, 0x90, 0xA1, 0x79, 0x5D, 0x00, 0x00, 0x00, 0x00, 0x4D, 0x61, 0x69, 0x6E, 0x00]),
            RequestSerializer().serialize(ConnectRequest(1568252304, 0, "Main")))

if __name__ == '__main__':
    unittest.main()
