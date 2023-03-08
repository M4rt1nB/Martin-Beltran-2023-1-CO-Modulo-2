import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, FONT_STYLE
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manger import Obstaclemanager
from dino_runner.components.menu import menu



class Game:
    GAME_SPEED = 20
    def __init__(self):
        
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = self.GAME_SPEED
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.obstacle = Obstaclemanager()
        self.menu = menu("press any key to star", self.screen)
        self.running = False
        self.score = 0
        self.best = []
        self.death_count = 0

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()


    def run(self):
        # Game loop: events - update - draw
        self.obstacle.reset_obstacles()
        self.game_speed = self.GAME_SPEED
        self.score = 0
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle.update(self)
        self.update_score()
        

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.player.drawn(self.screen)
        self.obstacle.draw(self.screen)
        self.draw_score()
        self.draw_background()
        pygame.display.update()
        pygame.display.flip()
        

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def show_menu(self):
        self.menu.reset_screen_color(self.screen)
        half_screen_width = SCREEN_WIDTH // 2
        half_screen_height = SCREEN_HEIGHT // 2

        if self.death_count == 0:
            self.menu.draw(self.screen)
        else:
            self.menu.update_message("ops you dont jump")
            self.menu.draw(self.screen)
            self.menu.best_message(f'best score: {max(self.best)}')
            self.menu.draw(self.screen)
            self.menu.point_message(f'score: {self.score}')
            self.menu.draw(self.screen)
            self.menu.dead_message(f'deads: {self.death_count}')
            self.menu.draw(self.screen)


            
       


        self.menu.draw(self.screen)
        
        self.screen.blit(ICON, (half_screen_width - 50, half_screen_height - 140))

        self.menu.updated(self)


    def update_score(self):
        self.score += 1
        

        if self.score % 100 == 0 and self.game_speed < 500:
            self.game_speed += 5   


    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f'score: {self.score}', True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (1000, 50)
        self.screen.blit(text, text_rect)

        
