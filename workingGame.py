import pygame,time
from spritesheet import Spritesheet
from Tile import *
from Player import Player
from Camera import Camera

#load up basic window
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1000,1000))
running = True

mySpriteSheet = Spritesheet("sp1.png")
map = TileMap('EngLyffe.csv',mySpriteSheet)
guy = Player("Guy.png",map)
camera = Camera(guy)

guy.setCurrentTile()

def render():
    guy.update()
    camera.scroll()
    screen.fill((0,0,0))
    map.draw_map(screen,(0 - camera.offset.x, 0 - camera.offset.y))
    guy.draw(screen,(guy.rect.x - camera.offset.x, guy.rect.y - camera.offset.y))
    #screen.blit(guy.current_image,(guy.rect.x - camera.offset.x, guy.rect.y - camera.offset.y))
    pygame.display.flip()



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False

        #Key pressed
        if event.type == pygame.KEYDOWN and not guy.disableInput:
            if event.key == pygame.K_w and guy.currentTile.WASD['W']!=None:
                guy.moving,guy.FACING_BACKWARD="W",False
            elif event.key == pygame.K_s and guy.currentTile.WASD['S']!=None:
                guy.moving,guy.FACING_BACKWARD="S",True
            elif event.key == pygame.K_a and guy.currentTile.WASD['A']!=None:
                guy.moving,guy.FACING_LEFT="A",True
            elif event.key==pygame.K_d and guy.currentTile.WASD['D']!=None:
                guy.moving,guy.FACING_LEFT="D",False

        
    
    render()
    time.sleep(0.05)
    
pygame.quit()