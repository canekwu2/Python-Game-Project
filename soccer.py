import pygame
import random

class SoccerGame():
    def __init__(self,screen):
        self.screen=screen
        self.clock = pygame.time.Clock()

        self.player = SoccerPlayer(self.screen)
        self.ball = Ball(self.screen)

        self.score =0


    def start(self):
        
        running = True
        self.player.rect.bottom=self.screen.get_rect().bottom+5
        self.player.rect.x=self.screen.get_rect().width/2
        startTime = pygame.time.get_ticks()

        self.goalPost =pygame.transform.scale(pygame.image.load("goalPost.png"),(100,100))
        self.goalRect = self.goalPost.get_rect()

        introImg = pygame.transform.scale(pygame.image.load("SoccerIntro.png"),(self.screen.get_rect().width,self.screen.get_rect().height))
        while pygame.time.get_ticks() - startTime < 5000:
            self.screen.blit(introImg,introImg.get_rect())
            pygame.display.update()


        self.render()

        while running:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running=False
                if event.type==pygame.MOUSEBUTTONDOWN:
                    print(pygame.mouse.get_pos())
                
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a] and self.player.rect.x>0:
                self.player.rect.x-=self.player.speed
            elif keys[pygame.K_d] and (self.player.rect.x+self.player.rect.width)<self.screen.get_rect().width:
                self.player.rect.x+=self.player.speed

            self.ball.collision(self.screen,self.player)

            if self.ball.rect.colliderect(self.goalRect):
                self.score+=1
                self.ball.speed+=0.3
                self.ball.rect.center=(random.randint(25,self.screen.get_rect().width-25),162)
                self.ball.yDir=1

            if self.ball.rect.centery==self.screen.get_rect().height:
                self.score-=1
                self.ball.rect.center=(random.randint(25,self.screen.get_rect().width-25),162)


            if self.score==2:
                return True
            elif self.score==-1:
                return False

            
            if self.ball.rect.y>=self.screen.get_rect().height:
                self.ball.rect.center=(random.randint(25,self.screen.get_rect().width-25),162)
                self.ball.yDir=1
                self.score-=1

    
            self.render()
            self.clock.tick(60)
    
    def render(self):
        background = pygame.transform.scale(pygame.image.load("field.jpeg"),(self.screen.get_rect().width,self.screen.get_rect().height))
        self.screen.blit(background,background.get_rect())
        self.goalRect.center=(self.screen.get_rect().width/2,0)
        self.screen.blit(self.goalPost,self.goalRect)
        self.screen.blit(self.ball.image,self.ball.rect)
        self.screen.blit(self.player.image,self.player.rect)
        self.ball.update()
        pygame.display.flip()


class SoccerPlayer(pygame.sprite.Sprite):
    def __init__(self,screen):
        self.image = pygame.transform.scale(pygame.image.load("soccerPlayer.png"),(150,75))
        self.rect=self.image.get_rect()
        self.speed = 10
        self.screen=screen
    





class Ball(pygame.sprite.Sprite):
    def __init__(self,screen):
        self.screen=screen
        self.image = pygame.transform.scale(pygame.image.load("ball.png"),(50,50))
        self.rect=self.image.get_rect()
        self.rect.center=(random.randint(25,self.screen.get_rect().width-25),162)

        self.speed=2

        self.yDir=1
        self.xDir = random.choice([-1,1])

    def setScreen(self,screen):
        self.screen=screen
    
    def update(self):
        self.rect=self.rect.move(self.xDir*self.speed,self.yDir*self.speed)
    
    def collision(self,screen,p):

        if self.rect.top<=0 or self.rect.colliderect(p):
            self.yDir=-self.yDir
        if self.rect.x<=0 or (self.rect.x+self.rect.width)>=screen.get_rect().width:
            self.xDir=-self.xDir
