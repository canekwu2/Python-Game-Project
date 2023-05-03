import pygame
from spriteSheet import Spritesheet
import math
import json

class Character(pygame.sprite.Sprite):

    def __init__(self,level,stats,spriteSheet,moves):
        pygame.sprite.Sprite.__init__(self)
        #tuple, [MH,attack,defense,speed]
        self.stats = stats
        self.level=level
        self.enableControls=True
        self.spritesheet=spriteSheet
        #tuple, 4 move objects
        self.moves=moves

#Player class; maintains player information (customization, stats, movement, etc)
class Player(Character):
    def __init__(self,spriteSheet,map,character):
        Character.__init__(self,5,tuple([100,1,1,1]),spriteSheet,([0,0,0,0]))
        #if True, no player input
        self.disableInput = False
        #number denoting player character chosen by user
        self.playerNum=character
        #if reached 0, game over
        self.currentHealth=self.stats[0]

        #reference to Tilemap
        self.map = map

        #W - forwards, A - left, S - backwards, D - right
        self.moving = ""
        self.FACING_LEFT,self.FACING_BACKWARD=False,False
        self.loadFrames()

        #currentTile keeps track of potential movement across map
        self.currentTile=None

        #self.rect =self.idle_frames_left[0].get_rect()
        self.rect = self.spriteImage.get_rect()
        
        #starting position of player coordinates
        self.rect.center = map.getTile("healNode4").rect.center


        self.destinationTile = self.map.getTile("enemyNode45")
        #win flag to check if player has won a minigame or not
        self.winFlag =None
        self.winCounter=0

        #velocity of player, state of player, image of player
        self.current_frame=0
        self.last_updated=0
        self.velocity=5
        self.velocity_x=0
        self.velocity_y=0
        self.state='idle'
        self.current_image = self.spriteImage
        #self.current_image = self.idle_frames_left[0] (image blit onto screen, only spriteImage for now)

    def setCurrentTile(self):
        self.currentTile= pygame.sprite.spritecollide(self,self.map.nodeGroup,False)[0]


    #determines everything needed for the player character in the current game loop iteration
    def update(self):
        #creating variables
        next_pos = (0,0)
        self.velocity_x=0
        self.velocity_y=0
        ruy=0
        rux=0

        #if moving,
        if self.moving!="":
            #disable input until movement is complete
            self.disableInput=True
            #get destinationTile from map.getTile(), using reference from the currentTile's direction array (which holds the names of potential tiles reachable from it)
            self.destinationTile=self.map.getTile(self.currentTile.WASD[self.moving])

            #distance vector between player and destinationTile
            #if destinationTile is 0, distance will be 0 and no movement will occur
            r = (self.destinationTile.rect.center[0]-self.rect.center[0],self.destinationTile.rect.center[1]-self.rect.center[1])
            rmag = math.sqrt((r[0]**2)+(r[1]**2))
            #unit vector in the direction from player to destination
            rux =r[0]/rmag
            ruy=r[1]/rmag

        #components of displacement vector of player
        self.velocity_x=self.velocity*rux
        self.velocity_y=self.velocity*ruy
        #if currently moving to a destination and player has collided with the destinationTile
        if self.destinationTile!=None and self.rect.collidepoint(self.destinationTile.rect.center):
            #set player to center of destinationTile
            self.rect.center=self.destinationTile.rect.center
            #enable inputs
            self.disableInput=False
            #set currentTile
            self.currentTile=self.destinationTile
            #remove destinationTile (no longer moving)
            self.destinationTile=None
            #idle state
            self.moving=""
            #initiate interact with tile (will start minigame and return a winFlag or nothing will occur)
            self.winFlag = self.currentTile.interact()
            self.updateHealth()


        #move player closer to destinationNode 
        self.rect.x+=self.velocity_x
        self.rect.y+=self.velocity_y

        self.set_state()
        #self.animate()

    #not in use
    #sets the state of the player
    def set_state(self):
        self.state = 'idle'
        if self.velocity_x>0 and self.velocity_y==0:
            self.state = 'moving right'
        elif self.velocity_x<0 and self.velocity_y==0:
            self.state = 'moving left'
        elif self.velocity_x==0 and self.velocity_y>1:
            self.state = 'moving backwards'
        elif self.velocity_x==0 and self.velocity_y<0:
            self.state = 'moving forwards'

    def updateHealth(self):
        if self.winFlag:
            self.winCounter+=1
        elif self.winFlag==False:
            self.currentHealth-=25

    #Not in use
    #animation method; keeps track on how/where the player is moving to animation movement
    def animate(self):
        #add clock.tick to game loop
        #time in ms since game began
        now = pygame.time.get_ticks()
        if self.state=='idle':
            #update animation every 200 milliseconds (play around with this to check how good it looks)
            if now-self.last_updated>200:
                self.last_updated=now
                self.current_frame = (self.current_frame + 1) % len(self.idle_frames_left)
                if self.FACING_LEFT:
                    self.current_image = self.idle_frames_left[self.current_frame]
                elif not self.FACING_LEFT:
                    self.current_image = self.idle_frames_right[self.current_frame]
                if self.FACING_BACKWARD:
                    self.current_image = self.idle_frames_backward[self.current_frame]
                elif not self.FACING_BACKWARD:
                    self.current_image = self.idle_frames_forward[self.current_frame]
        else:
            if now-self.last_updated>100:
                self.last_updated=now
                self.current_frame = (self.current_frame + 1) % len(self.walking_frames_left)
                if self.state =='moving left':
                    self.current_image = self.walking_frames_left[self.current_frame]
                elif self.state == 'moving right':
                    self.current_image = self.walking_frames_right[self.current_frame]
                elif self.state == 'moving forward':
                    self.current_image = self.walking_frames_forward[self.current_frame]
                elif self.state == 'moving backward':
                    self.current_image = self.walking_frames_backward[self.current_frame]

    #draws player onto screen
    def draw(self,display,rect):
        display.blit(self.current_image,rect)


    #diagonal movement will be set to left or right movement
    def loadFrames(self):
        #temporary spritesheets until character customization starts
        #self.spritesheet.parseSprite("idleframe1.png"),self.spritesheet.parseSprite("idleframe2.png")
        #left
        self.idle_frames_left=[]
        self.walking_frames_left=[]

        #right
        self.idle_frames_right = []
        for frame in self.idle_frames_left:
            #(image to flip, flip in x, flip in y)
            self.idle_frames_right.append(pygame.transform.flip(frame,True,False))
        self.walking_frames_right = []
        for frame in self.idle_frames_left:
            self.idle_frames_right.append(pygame.transform.flip(frame,True,False))

        #forwards
        self.idle_frames_forward=[]
        self.walking_frames_forward=[]
        #backwards
        self.idle_frames_backward=[]
        self.walking_frames_backward=[]


        # if statement to choose the player image on map
        if self.playerNum == 1:
            self.spriteImage = pygame.transform.scale(pygame.image.load("character1.png"),(32,32))
        elif self.playerNum == 2:
            self.spriteImage = pygame.transform.scale(pygame.image.load("character2.png"),(32,32))




#Not used, ran out of time

class Enemy(Character):
    def __init__(self,level,stats,spriteName,moves):
        super.__init__(level,stats,spriteName,moves)

        self.sS = Spritesheet("enemySpriteSheet.png")
        #AEOStudent.png,EngStudent1.png,EngStudent2.png,Garfield,Goose,Tim
        self.image = self.sS.parseSprite(spriteName)

        #working calculation for xp gained from a given battle
        temp = 0
        for i in self.stats:
            temp+=self.stats[i]
        self.reward=(max(self.stats)/temp)*self.level*10

class Attack():
    
    def __init__(self,atk,acc,attackName,ani):
        
        self.attackData = Spritesheet("attacks.png")

        self.power = atk
        self.accuracy = acc
        #image blit'ed once attack begins
        self.attack = self.attackData.parseSprite(attackName)
        self.attackName=attackName
        #String telling system what type of attack it is (throw the image, character moves,image spawns upwards from opponent, image spawns upwards from user) 
        self.animation = ani

    def use(self):
        pass

