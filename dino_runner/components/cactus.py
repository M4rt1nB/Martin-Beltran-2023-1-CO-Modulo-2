import random

from dino_runner.components.obstacle import obstacle


class cactus(obstacle):
    def __init__(self, image):
        self.type = random.randints(0,2)
        super().__init__(image , self.type)
        self.rec.y = 325