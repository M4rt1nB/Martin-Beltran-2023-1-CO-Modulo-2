from dino_runner.components.power_up.power_up import power_Up
from dino_runner.utils.constants import HAMMER, HAMMER_TYPE


class hammer(power_Up):
    def __init__(self):
        super().__init__(HAMMER, HAMMER_TYPE)
