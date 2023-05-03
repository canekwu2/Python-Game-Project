import pygame
vec = pygame.math.Vector2

class Camera:
    def __init__(self,player,):
        self.player=player
        self.offset = vec(0,0)
        self.offset_float=vec(0,0)
        self.DISPLAY_W,self.DISPLAY_H=1000,1000
        self.CONST = vec(self.DISPLAY_W/2,self.DISPLAY_H/2)

    def scroll(self):
        self.offset_float.x += (self.player.rect.x - self.offset_float.x - self.CONST.x)
        self.offset_float.y += (self.player.rect.y - self.offset_float.y - self.CONST.y)
        self.offset.x, self.offset.y = int(self.offset_float.x), int(self.offset_float.y)

