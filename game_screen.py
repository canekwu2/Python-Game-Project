import pygame
from workingGame import run_game

class GameScreen:
    def __init__(self, screen, game):
        self.screen = screen
        self.game = game
        # load the background image
        self.background_image = pygame.image.load('EngLyfe_TitleScreen.png').convert()


    def update(self):
        run_game(self.game)

    def draw(self):
        # draw the background image
        # self.screen.blit(self.background_image, (0, 0))
        pass


    def handle_mouse_click(self, pos):
        pass

    def handle_key_press(self, key):
        pass