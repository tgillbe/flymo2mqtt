import context # type: ignore
import unittest
from collections import namedtuple
from mower.data_stream import ReadableStream, WritableStream
from mower.in_memory_stream import InMemoryStream
from mower.packet_interface import PacketInterface

class TestPacketInterface(unittest.TestCase):
    def test_send(self):
        write_stream = InMemoryStream()
        tx_packet = {}
        res_3 = {}
        res_4 = {}

        def write_mock(packet, stream: WritableStream):
            self.assertEqual(packet, tx_packet)
        def read_mock(stream: ReadableStream):
            value = stream.read_bytes()
            if value == bytes([3, 2, 1]):
                return res_3
            elif value == bytes([4, 3, 2, 1]):
                return res_4
            else:
                return None
        Framer = namedtuple('Framer', ['write', 'read'])
        framer = Framer(
            write=write_mock,
            read=read_mock,
        )
        dut = PacketInterface(framer, write_stream)
        dut.receive(bytes([4, 3]))
        dut.receive(bytes([2, 1]))
        self.assertEqual(dut.send(tx_packet), res_4)
        dut.receive(bytes([3]))
        dut.receive(bytes([2]))
        dut.receive(bytes([1]))
        self.assertEqual(dut.send(tx_packet), res_3)

if __name__ == '__main__':
    unittest.main()
