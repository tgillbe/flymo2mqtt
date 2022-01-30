from enum import Enum

class MowerStatus(Enum):
    CHECK_SAFETY = 0
    CONNECTING = 1
    DISCONNECTED = 2
    ERROR = 3
    FATAL_ERROR = 4
    IN_OPERATION = 5
    OFF = 6
    PAUSED = 7
    PENDING = 8
    PENDING_START = 9
    RESTRICTED = 10,
    STOPPED = 11,
    UNKNOWN = 12,
    WAITING_FOR_PIN = 13
