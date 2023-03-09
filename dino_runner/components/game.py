import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, FONT_STYLE , SHIELD_TYPE , DEFAULT_TYPE
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manger import Obstaclemanager
from dino_runner.components.menu import menu
from dino_runner.components.counter import Counter
from dino_runner.components.power_up.power_manager import powerUpmanager


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
        self.obstacle_manager = Obstaclemanager()
        self.menu = menu(self.screen)
        self.running = False
        self.score = Counter()
        self.death_count = Counter()
        self.highest_score = Counter()
        self.power_up_manager = powerUpmanager()
        self.dramas =  pygame.mixer.Sound('de.mp3')
        self.rela = pygame.mixer.Sound('rela.mp3')
        
    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.dramas.stop()
                self.rela.stop()
                self.show_menu()
        pygame.display.quit()
        pygame.quit()      
                

    def run(self):
        self.menu.sound.stop()
        self.rela.play()
        self.reset_game()
        # Game loop: events - update - draw
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
        self.obstacle_manager.update(self)
        self.power_up_manager.update(self)
        self.score.update()
        self.update_game_speed()

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((250, 250, 250))
        self.draw_background()
        self.changue_color()
        self.player.drawn(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.draw_power_up_time()
        self.score.draw(self.screen)
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
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2
        
        if self.death_count.count == 0:
            self.menu.draw(self.screen, 'Press any key to start ...')
        else:
            self.update_highest_score()
            self.menu.draw(self.screen, ' Press any key to restart')
            self.menu.draw(self.screen, f'Game over', half_screen_width, 100, )
            self.menu.draw(self.screen, f'Your score: {self.score.count}', half_screen_width, 350, )
            self.menu.draw(self.screen, f'Highest score: {self.highest_score.count}', half_screen_width, 400, )
            self.menu.draw(self.screen, f'Total deaths: {self.death_count.count}', half_screen_width, 450, )
        
        self.screen.blit(ICON, (half_screen_width - 50, half_screen_height - 140))
        
        self.menu.update(self)
                
    def update_game_speed(self):
        if self.score.count % 500 == 0 and self.game_speed < 1000:
            self.game_speed += 10
            self.dramas.play()
            self.rela.stop()
        if  self.score.count % 1000 == 0:
            self.dramas.stop()
            self.rela.play()
          

            
        else:
            self.game_speed 
            
            
    def update_highest_score(self):
        if self.score.count > self.highest_score.count:
            self.highest_score.set_count(self.score.count)
            
    def reset_game(self):
        self.obstacle_manager.reset_obstacles()
        self.score.reset()
        self.game_speed = self.GAME_SPEED
        self.player.reset()
        self.power_up_manager.reset_power_ups()
    
    
    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_time_up - pygame.time.get_ticks()) / 1000, 2)

            if time_to_show >=0:
                self.menu.draw(self.screen,f'{self.player.type.capitalize()}enable for {time_to_show}secodns', 500, 50)
                self.menu.sound.stop()
            else:
                self.has_power_up = False
                self.player.type = DEFAULT_TYPE


    def changue_color(self):
        if  self.score.count > 500 and self.score.count < 1000 or self.score.count > 1500 and self.score.count < 2000 or self.score.count > 2500 and self.score.count < 3000  :
            self.screen.fill((0,0,0))
            
        
            
     
            