import pygame
from button import Button
import menu

# this class will be called when the flag for the battle is set to true
class WinningScreen:
    def __init__(self, screen):
        self.screen = screen
        # load the background image
        self.background_image = pygame.image.load('winning_screen-Congratulations.png').convert()
        #create the back button
        self.back_button = Button('MainMenu_BackBtn.png', (850, 450), self.on_back_clicked)

    def start(self):
        running=True
        pygame.mixer.music.load("winning_screen-music.ogg")
        pygame.mixer.music.play(loops=-1)

        while running:
            self.render()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running=False
                elif event.type==pygame.MOUSEBUTTONDOWN:
                    #self.handle_mouse_click(pygame.mouse.get_pos())
                    if self.back_button.rect.collidepoint(pygame.mouse.get_pos()):
                        running = False


        pygame.quit()

    def render(self):
        background_img = pygame.transform.scale(self.background_image,(self.screen.get_rect().width,self.screen.get_rect().height))
        self.screen.blit(background_img,background_img.get_rect())
        self.back_button.draw(self.screen)
        pygame.display.flip()

    def draw(self):
        #draw the background image
        self.screen.blit(self.background_image, (0, 0))
        #draw the back button
        self.back_button.draw(self.screen)

    def handle_mouse_click(self, pos):
        # handle mouse clicks on the back button
        if self.back_button.rect.collidepoint(pos):
            self.on_back_clicked()

    def on_back_clicked(self):
        self.running = False