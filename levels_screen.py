import pygame
from button import Button
import kahoot
from winning_screen import WinningScreen
from losing_screen import LosingScreen

class LevelsScreen:
    def __init__(self, screen, game):
        self.screen = screen
        self.game = game
        #load the background image
        self.background_image = pygame.image.load('EngLyfe_TitleScreen.png').convert()
        # create the back button
        self.back_button = Button('MainMenu_BackBtn.png', (850, 450), self.on_back_clicked)
        # create the level buttons
        self.level1_button = Button('MainMenu_BackBtn.png', (200, 200), self.on_level1_clicked)
        self.level2_button = Button('MainMenu_BackBtn.png', (200, 250), self.on_level2_clicked)
        self.level3_button = Button('MainMenu_BackBtn.png', (200, 300), self.on_level3_clicked)
        self.level4_button = Button('MainMenu_BackBtn.png', (200, 350), self.on_level4_clicked)

    def update(self):
        pass

    def draw(self):
        # draw the background image
        self.screen.blit(self.background_image, (0, 0))
        # draw the back button
        self.back_button.draw(self.screen)
        # draw the level buttons
        self.level1_button.draw(self.screen)
        self.level2_button.draw(self.screen)
        self.level3_button.draw(self.screen)
        self.level4_button.draw(self.screen)

    def handle_mouse_click(self, pos):
        # handle mouse clicks on buttons
        if self.level1_button.rect.collidepoint(pos):
            self.on_level1_clicked()
        elif self.level2_button.rect.collidepoint(pos):
            self.on_level2_clicked()
        elif self.level3_button.rect.collidepoint(pos):
            self.on_level3_clicked()
        elif self.back_button.rect.collidepoint(pos):
            self.on_back_clicked()

    def handle_key_press(self, key):
        pass

    def on_level1_clicked(self):
        kahoot.start()
        

    def on_level2_clicked(self):
        ws = WinningScreen(self.screen)
        ws.start()

    def on_level3_clicked(self):
        ls = LosingScreen(self.screen)
        ls.start()

    def on_level4_clicked(self):
        pass

    def on_back_clicked(self):
        #switch back to the main menu screen
        self.game.set_current_screen(self.game.menu)