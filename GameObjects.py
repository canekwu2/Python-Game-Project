import pygame, random, math


class Character (pygame.sprite.Sprite):
    def __init__(self,name,stats,moves,img_path):
        super().__init__()
        self.image = pygame.image.load(img_path)
        self.name =name
        self.stats = stats
        self.moves = moves

class Enemy (Character):
    def __init__(self, name, stats, moves, img_path,bossFlag,decision):
        super().__init__(name, stats, moves, img_path)
        self.bossFlag = bossFlag
        self.decision = decision

class Player(Character):
    def __init__(self, name, stats, moves, img_path,bag,currentPosition,move):
        super().__init__(name, stats, moves, img_path)
        self.bag=bag
        self.currentPosition = currentPosition
        self.move = move

class Functionals():
    def __init__(self,name,description,effect):
        self.name = name
        self.description = description
        self.effect = effect

class Items(Functionals):
    def __init__(self,image,name,description,effect):
        super().__init__(name,description,effect)
        self.image = image


class Attack(Functionals):
    def __init__(self,priority,name,description,effect,animation): 
        super().__init__(name,description,effect)
        self.priority = priority
        self.animation = animation

class Game():
    def __init__(self,map,player):
        self.map = map
        self.player = player

class Graph():
    def __init__(self,head):
        self.head = head

class Node():
    def __init__(self,nodeType,enemy,loot,dialogue,next,prev,location):
        self.nodeType = nodeType
        self.enemy= enemy
        self.loot = loot
        self.dialogue = dialogue
        self.next = next
        self.prev = prev
        self.location = location
class createMiniGame():
    pass
class Cards(pygame.sprite.Sprite):
        def __init__(self,source,x,y,screen,background ):
            super().__init__()
            self.image = pygame.image.load(source).convert_alpha()
            self.image=pygame.transform.scale(self.image, (125, 125))
            self.rect = self.image.get_rect()  
            self.rect.center = (x,y)
            self.x = x
            self.y = y
            self.screen = screen
            self.background = background
            #self.background_image= pygame.image.load(background)
            self.background_rect=self.background.get_rect()
        def circleMovement(self):
            angle = 0
            radius = 100
            angular_speed = 1

            for i in range(60):
                pygame.time.wait(100)
                self.x = int(600 + radius * math.cos(math.degrees(angle)))
                self.y = int(400 + radius * math.sin(math.degrees(angle)))
                self.rect.center=(self.x, self.y)
                angle += angular_speed
        
                self.screen.blit(self.background,self.background_rect)
                self.screen.blit(self.image,self.rect) 
                pygame.display.flip()
                
            self.screen.fill((0,0,0))
            pygame.display.flip()
            pygame.time.wait(2000)
            self.rect.x = 600
            self.rect.y = 500
            self.screen.blit(self.background,self.background_rect)
            self.screen.blit(self.image,self.rect) 

        def moveToSpots(self,right,left):
                self.rect.y = 500
                if left == True:
                    self.rect.x = 300
                    
                if right == True:
                    self.rect.x =900
                # self.screen.blit(self.background,self.background_rect)
                self.screen.blit(self.image,self.rect) 
                pygame.display.update()
                pygame.time.wait(100)
            
        
       
# pygame.init()
# screen = pygame.display.set_mode((800, 600))

# Create a card object and move it in a circular motion

