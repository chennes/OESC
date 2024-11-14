from enum import IntEnum, auto

class Sauce(IntEnum):
    PESTO = auto()
    WHITE = auto()
    TOMATO = auto()
    OLIVE_OIL = auto()
    MOTOR_OIL = auto()

    def __str__(self) -> str:
        if self.value == Sauce.MOTOR_OIL:
            return "motor oil"
        if self.value == Sauce.OLIVE_OIL:
            return "olive oil"
        if self.value == Sauce.PESTO:
            return "pesto"
        if self.value == Sauce.TOMATO:
            return "tomato"
        if self.value == Sauce.WHITE:
            return "white"