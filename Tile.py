import pygame, csv, os
import spriteSheet
import json
from soccer import SoccerGame
import CardsMiniGame as CardsGame
from catchGrade import CatchGame
import kahoot as k

#Tile sprite class; positions the player can exist on
class Tile(pygame.sprite.Sprite):
    #initialize method
    def __init__(self, image, x, y,name, spritesheet):
        pygame.sprite.Sprite.__init__(self)
        #image, rect, name
        self.image = spritesheet.parseSprite(image)
        self.rect = self.image.get_rect()
        self.name=name
        self.rect.x, self.rect.y = x, y

        #load mapData from json file
        with open("movement.json","r") as mp:
            self.mapData=json.load(mp)


        #The coordinates of the nodes the user can move to from a given node
        #Will be empty if movement in a certain direction isn't possible
        self.WASD = {}
        #Lists of animations to play according to which direction the user moves in
        #Path of their movement
        self.pathAnimations = {}
        
    #draw the tile onto surface
    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

    #set the movement data to the node
    def setMovement(self,name):
        #load WASD
        self.WASD=self.mapData[name]["WASD"]
        #load pathAnimations (Not in use)
        self.pathAnimations=self.mapData[name]["pathAnimation"]

        screen = pygame.display.set_mode((1000,529))
        #load minigame
        #if dungeonNode, minigame is playable. If not, None
        m = self.mapData.get(name).get("minigame")
        if m=="soccer":
            self.minigame=SoccerGame(screen)
        elif m=="study":
            self.minigame=CatchGame(screen)
        elif m=="card":
            self.minigame=CardsGame
            CardsGame.setScreen(screen)
        elif m=="kahoot":
            self.minigame=k
            k.setScreen(screen)
        else:
            self.minigame=None
            


    def interact(self):
        if self.minigame is not None:
            if self.minigame is k:
                self.minigame.setVar()
            return self.minigame.start()
        else:
            return None

            
    
        



class TileMap:
    def __init__(self, filename, spritesheet):
        self.nodeGroup = pygame.sprite.Group()

        self.tile_size = 32
        #positions to plae tiles when loading map
        self.start_x, self.start_y = 0, 0
        self.spritesheet = spritesheet
        self.tiles = self.load_tiles(filename)
        self.map_surface = pygame.Surface((self.map_w, self.map_h))
        self.map_surface.set_colorkey((0, 0, 0))
        self.load_map()

    def draw_map(self,surface,pos):
        surface.blit(self.map_surface, pos)

    def load_map(self):
        for tile in self.tiles:
            tile.draw(self.map_surface)
    
    def read_csv(self, filename):
        map = []
        with open(os.path.join(filename)) as data:
            data = csv.reader(data, delimiter=',')
            for row in data:
                map.append(list(row))
        return map
    
    def load_tiles(self, filename):
        tiles = []
        map = self.read_csv(filename)
        x, y = 0, 0
        hC=int(0)
        eC=int(0)
        dC=int(0)
        for row in map:
            x = 0
            for tile in row:
                #empty space
                if tile == '-1':
                    #increment start_x and start_y to position to place next tile 
                    self.start_x, self.start_y = x * self.tile_size, y * self.tile_size
                #Healing node
                elif tile == '0':
                    tileName = "healNode"+str(hC)
                    t = Tile("healNode.png", x * self.tile_size, y * self.tile_size,tileName, self.spritesheet)
                    t.setMovement(tileName)
                    self.nodeGroup.add(t)
                    tiles.append(t)
                    hC+=1
                elif tile == '2':
                    tileName="enemyNode"+str(eC)
                    t=Tile("enemyNode.png", x * self.tile_size, y * self.tile_size,tileName, self.spritesheet)
                    t.setMovement(tileName)
                    self.nodeGroup.add(t)
                    tiles.append(t)
                    eC+=1
                elif tile == '14':
                    tileName="dungeonNode"+str(dC)
                    t=Tile("dungeonNode.png", x * self.tile_size, y * self.tile_size,tileName, self.spritesheet)
                    t.setMovement(tileName)
                    self.nodeGroup.add(t)
                    tiles.append(t)
                    dC+=1
                elif tile == '9':
                    tiles.append(Tile("clearedNode.png", x * self.tile_size, y * self.tile_size,"clearedNode", self.spritesheet))
                elif tile == '7':
                    tiles.append(Tile("vertRoad.png", x * self.tile_size, y * self.tile_size,"verticalRoad", self.spritesheet))
                elif tile == '4':
                    tiles.append(Tile("horizRoad.png", x * self.tile_size, y * self.tile_size,"horizontalRoad", self.spritesheet))
                elif tile == '12':
                    tiles.append(Tile("sidewalk.png", x * self.tile_size, y * self.tile_size,"sidewalk", self.spritesheet))
                # Move to next tile in current row
                x += 1


            # Move to next row
            y += 1
            # Store the size of the tile map
        self.map_w, self.map_h = x * self.tile_size, y * self.tile_size
        return tiles
    
    


    def resetMap(self):
        mapData = {}
        for i in self.nodeGroup.sprites():
            mapData[i.name]={
                "WASD":{"W":None,"A":None,"S":None,"D":None},
                "position":i.rect.center,
                "pathAnimation":{"W":[],"A":[],"S":[],"D":[]}
                } 

        with open("movement.json", 'w') as out:
            json.dump(mapData, out,indent=1)
    
    def getTile(self,name):
        for i in self.nodeGroup:
            if i.name==name:
                return i
        else:
            return None
            


