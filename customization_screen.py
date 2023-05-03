import pygame
from button import Button
from spriteSheet import Spritesheet



import pygame
from button import Button


class CustomizationScreen:


    def __init__(self, screen, game=None):
        self.screen = screen
        self.game = game
      
        # load the background image
        self.background_image = pygame.image.load('EngLyfe_TitleScreen.png').convert()
        # create the back button
        self.back_button = Button('MainMenu_BackBtn.png', (850, 450), self.on_back_clicked)



        ####################################################-----------------
        # Load the character images
        self.character1_image = pygame.image.load("character1.png")
        self.character2_image = pygame.image.load("character2.png")

        # Define character rects
        self.character1_rect = self.character1_image.get_rect()
        self.character2_rect = self.character2_image.get_rect()

        # Position the characters in the center of the screen
        self.character1_rect.center = (self.screen.get_width() // 2 - self.character1_rect.width // 2 - 40, self.screen.get_height() // 2 +100)
        self.character2_rect.center = (self.screen.get_width() // 2 + self.character2_rect.width // 2 + 40, self.screen.get_height() // 2 +100)

        # Text settings
        self.font = pygame.font.Font(None, 55)
        self.text_color = (255, 255, 255)
        self.selected_character_text = ""

         ####################################################-----------------




    def update(self):
        pass

    

        
    def draw(self):
        # draw the background image
        self.screen.blit(self.background_image, (0, 0))

    
        #pygame.draw.rect(self.screen, (255, 0, 0), slider_rect)
        # draw the back button
        self.back_button.draw(self.screen)





          ####################################################-----------------
        # Draw the characters
        self.screen.blit(self.character1_image, self.character1_rect)
        self.screen.blit(self.character2_image, self.character2_rect)

        # Draw selected character text
        if self.selected_character_text:
            text = self.font.render(self.selected_character_text, True, self.text_color)
            text_rect = text.get_rect()
            text_rect.centerx = self.screen.get_width() // 2
            text_rect.y = 450
            self.screen.blit(text, text_rect)
          ####################################################-----------------

      
        

    def handle_mouse_click(self, pos):
        # handle mouse clicks on the back button
        if self.back_button.rect.collidepoint(pos):
            self.on_back_clicked()


 ####################################################-----------------
        elif self.character1_rect.collidepoint(pos):
            self.select_character(1)
        elif self.character2_rect.collidepoint(pos):
            self.select_character(2)
 ####################################################-----------------




    def handle_key_press(self, key):
        pass

    def on_back_clicked(self):
        # switch back to the main menu screen
        self.game.set_current_screen(self.game.menu)



 ####################################################-----------------
    def select_character(self, character_number):
        if character_number == 1:
            self.selected_character_text = "Character 1 selected"
            self.game.character = 1

        elif character_number == 2:
            self.selected_character_text = "Character 2 selected"
            self.game.character = 2