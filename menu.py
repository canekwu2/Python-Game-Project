import pygame
from button import Button

class Menu:
    def __init__(self, screen, game):
        self.screen = screen
        self.game = game
        # load the background image
        self.background_image = pygame.image.load('EngLyfe_TitleScreen.png').convert()
        # create the buttons
        self.play_button = Button("MainMenu_PlayBtn.png", (400, 300), self.on_play_clicked)
        self.customization_button = Button("MainMenu_CustomizationBtn.png", (400, 340), self.on_customization_clicked)
        self.levels_button = Button("MainMenu_LevelsBtn.png", (400, 380), self.on_levels_clicked)
        self.options_button = Button("MainMenu_OptionsBtn.png", (400, 420), self.on_options_clicked)
     

    def update(self):
        pass

    def draw(self):
        # draw the background image
        self.screen.blit(self.background_image, (0, 0))
        # draw the buttons
        self.play_button.draw(self.screen)
        self.customization_button.draw(self.screen)
        self.levels_button.draw(self.screen)
        self.options_button.draw(self.screen)
       
    def handle_mouse_click(self, pos):
        # handle mouse clicks on buttons
        if self.play_button.rect.collidepoint(pos):
            self.on_play_clicked()
        elif self.customization_button.rect.collidepoint(pos):
            self.on_customization_clicked()
        elif self.levels_button.rect.collidepoint(pos):
            self.on_levels_clicked()
        elif self.options_button.rect.collidepoint(pos):
            self.on_options_clicked()

    def handle_key_press(self, key):
        pass

    def on_play_clicked(self):
        # switch to the game screen
        self.game.set_current_screen(self.game.game_screen)

    def on_customization_clicked(self):
        # switch to the customization screen
        self.game.set_current_screen(self.game.customization_screen)

    def on_levels_clicked(self):
        # switch to the levels screen
        self.game.set_current_screen(self.game.levels_screen)

    def on_options_clicked(self):
        # switch to the options screen
        self.game.set_current_screen(self.game.options_screen)
