import pygame
import json

class Spritesheet:
    def __init__(self,fileName):
        self.filename=fileName
        #convert() spritesheet to pixel format of window
        self.spriteSheet= pygame.image.load(fileName).convert()
        self.meta_deta = self.filename.replace('png','json')
        with open(self.meta_deta) as f:
            self.data =json.load(f)
        f.close()

    def getSprite(self,x,y,w,h):
        sprite =pygame.Surface((w,h))
        #sprite.set_colorkey((0,0,0)), will make a certain color transparent in the image
        sprite.blit(self.spriteSheet,(0,0),(x,y,w,h))
        return sprite
    
    def parseSprite(self,name):
        sprite = self.data["nodes"][name]["image"]
        x,y,w,h=sprite["x"],sprite["y"],sprite["w"],sprite["h"]
        image = self.getSprite(x,y,w,h)
        return image
