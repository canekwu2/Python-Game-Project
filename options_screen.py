import pygame
from button import Button

import pygame
from button import Button

class OptionsScreen:
    def __init__(self, screen, game):
        self.screen = screen
        self.game = game
        # load the background image
        self.background_image = pygame.image.load('EngLyfe_TitleScreen.png').convert()
        # set the music volume label
        self.music_volume_label = pygame.font.SysFont('Arial', 32).render('Music Volume:', True, (255, 255, 255))
        # set the music volume slider
        self.music_volume_slider = pygame.Rect(300, 375, 400, 20)
        # create the back button
        self.back_button = Button('MainMenu_BackBtn.png', (850, 450), self.on_back_clicked)

    def update(self):
        pass

    def draw(self):
        # draw the background image
        self.screen.blit(self.background_image, (0, 0))
        # draw the music volume label
        self.screen.blit(self.music_volume_label, (300, 330))
        # draw the music volume slider
        pygame.draw.rect(self.screen, (255, 255, 255), self.music_volume_slider)
        slider_width = int(self.music_volume_slider.width * self.game.music_volume)
        slider_rect = pygame.Rect(self.music_volume_slider.x, self.music_volume_slider.y, slider_width, self.music_volume_slider.height)
        pygame.draw.rect(self.screen, (255, 0, 0), slider_rect)
        # draw the back button
        self.back_button.draw(self.screen)

    def handle_mouse_click(self, pos):
        # handle mouse clicks on the music volume slider
        if self.music_volume_slider.collidepoint(pos):
            self.game.music_volume = (pos[0] - self.music_volume_slider.x) / self.music_volume_slider.width
            if self.game.music:
                self.game.music.set_volume(self.game.music_volume)
        # handle mouse clicks on the back button
        elif self.back_button.rect.collidepoint(pos):
            self.on_back_clicked()


    def handle_key_press(self, key):
        pass

    def on_back_clicked(self):
        # switch back to the main menu screen
        self.game.set_current_screen(self.game.menu)
