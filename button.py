import pygame

class ButtonText:
    def __init__(self, text, pos, callback):
        # create the font
        self.font = pygame.font.SysFont('Arial', 32)
        #create text
        self.text = text
        # create the text image
        self.text_image = self.font.render(text, True, (255, 255, 255))
        # set the position of the button
        self.rect = pygame.Rect(pos[0], pos[1], self.text_image.get_width() + 20, self.text_image.get_height() + 20)
        # set the callback function
        self.callback = callback
    

    def draw(self, surface):
        # draw the button background
        pygame.draw.rect(surface, (0, 0, 255), self.rect)
        # draw the text
        surface.blit(self.text_image, (self.rect.x + 10, self.rect.y + 10))

    def handle_event(self, event):
        pass

    def handle_mouse_click(self, pos):
        # call the callback function if the button is clicked
        if self.rect.collidepoint(pos):
            self.callback()



class Button:
    def __init__(self, image_path, pos, callback):
        # load the button image
        self.image = pygame.image.load(image_path).convert_alpha()
        # set the position of the button
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        # set the callback function
        self.callback = callback

    def draw(self, surface):
        # draw the button image
        surface.blit(self.image, self.rect)

    def handle_event(self, event):
        pass

    def handle_mouse_click(self, pos):
        # call the callback function if the button is clicked
        if self.rect.collidepoint(pos):
            self.callback()
