import enum


class Status(enum.Enum):
    ready = 1
    damaged = 2
    repairing = 3
    destroyed = 4
    upgrading = 5
