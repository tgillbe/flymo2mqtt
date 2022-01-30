import context # type: ignore
from mower.chunking_write_stream import ChunkingWriteStream
import unittest

class TestChunkingWriteStream(unittest.TestCase):
    def test_write(self):
        values = []
        dut = ChunkingWriteStream(3, lambda bytes: values.append(bytes))
        dut.write_u8(0x03)
        dut.write_u32(0x12345678)
        self.assertEqual(values, [bytes([0x03, 0x78, 0x56])])
        dut.flush()
        self.assertEqual(values, [bytes([0x03, 0x78, 0x56]), bytes([0x34, 0x12])])
        
    def test_write_double_flush(self):
        values = []
        dut = ChunkingWriteStream(2, lambda bytes: values.append(bytes))
        dut.write_u32(0x12345678)
        self.assertEqual(values, [bytes([0x78, 0x56]), bytes([0x34, 0x12])])

if __name__ == '__main__':
    unittest.main()
