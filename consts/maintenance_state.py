from enum import Enum, auto


class MaintenanceState(Enum):
    NONE = auto()
    NEEDED = auto()
    REQUIRED = auto()
    OVERDUE = auto()