import enum


class Status(enum.Enum):
    ready = 0,
    damaged = 1,
    upgrading = 2,
    repairing = 3,
    destroyed = 4
