from enum import Enum


class MoveType(Enum):
    MOVE_OK = 0
    MOVE_CAPTURE = 1
    MOVE_ILLEGAL = 2
