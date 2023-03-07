import pygame

from dino_runner.components.obstacles.Cactus import cactus
from dino_runner.utils.constants import SMALL_CACTUS



class Obstaclemanager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            Cactus = cactus(SMALL_CACTUS)
            self.obstacles.append(Cactus)

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed)

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
