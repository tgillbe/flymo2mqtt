from .chunking_write_stream import ChunkingWriteStream
from .data_stream import WritableStream
from .in_memory_stream import InMemoryStream
from .packet_framer import NotForUsPacketException, PacketFramer
from .packet import Request, Response
from queue import Empty, Queue
import logging

logger = logging.getLogger(__name__)

class PacketInterface():
    packet_framer: PacketFramer
    write_stream: WritableStream
    receive_stream: InMemoryStream
    receive_queue: Queue

    def __init__(self, packet_framer: PacketFramer, write_stream: WritableStream):
        self.packet_framer = packet_framer
        self.write_stream = write_stream
        self.receive_stream = InMemoryStream()
        self.receive_queue = Queue()

    def send(self, packet: Request) -> Response:
        retry = 0
        while True:
            logger.debug(f"Sending {type(packet).__name__}")
            self.packet_framer.write(packet, self.write_stream)
            try:
                while True:
                    try:
                        response = self.packet_framer.read(self.receive_stream)
                        if response is not None:
                            self.receive_stream.truncate_start()
                            logger.debug(f"Received {type(response).__name__}")
                        if isinstance(response, packet.response):
                            return response
                        
                        # Seek to the end and write the new data
                        n = self.receive_stream.bytes.getbuffer().nbytes
                        self.receive_stream.bytes.seek(n)
                        data = self.receive_queue.get(block=True, timeout=3)
                        self.receive_stream.write_bytes(data)

                        # Rewind the receive stream
                        self.receive_stream.bytes.seek(0)
                    except NotForUsPacketException:
                        pass
            except Empty:
                # Timed out waiting on the queue
                retry = retry + 1
                if retry == 3:
                    raise
    
    def receive(self, data: bytes):
        logger.debug(f"RX: {data.hex()}")
        self.receive_queue.put(data)
