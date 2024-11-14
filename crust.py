from enum import IntEnum, auto

class Crust(IntEnum):

    THIN = auto()
    THICK = auto()
    PAN = auto()

    def __str__(self) -> str:
        if self.value == Crust.PAN:
            return "pan"
        elif self.value == Crust.THICK:
            return "thick"
        elif self.value == Crust.THIN:
            return "thin"
        return "ERROR"