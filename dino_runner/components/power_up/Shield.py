from dino_runner.components.power_up.power_up import power_Up
from dino_runner.utils.constants import SHIELD, SHIELD_TYPE


class shield(power_Up):
    def __init__(self):
        super().__init__(SHIELD, SHIELD_TYPE)
