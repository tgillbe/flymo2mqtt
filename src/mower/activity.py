from enum import Enum

class MowerActivity(Enum):
    CHARGING = 0
    GOING_HOME = 1
    LEAVING = 2
    MOWING = 3
    NONE = 4
    PARKED_IN_CHARGING_STATION = 5
    STOPPED_IN_GARDEN = 6
    UNKNOWN = 7
