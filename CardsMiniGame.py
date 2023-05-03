import pygame, random,GameObjects, os
startTime = pygame.time.get_ticks()
class CardsMiniGame():
    def __init__(self,screen):
        self.screen = screen
    
Screen = pygame.display.set_mode((1200,800))
def setScreen(screened):
    Screen = screened
#Creating filepath to access files in a folder
folder_path = 'CardPictures'
file_paths = []

files = os.listdir(folder_path)
for file in files:
    file_path = os.path.join(folder_path, file)
    file_paths.append(file_path)

background_img = pygame.image.load('pokerTable.jpeg')
background_img = pygame.transform.scale(background_img, (1200,800))
background_rect = background_img.get_rect()

#Create card group
card_group = pygame.sprite.Group()

def createCards():
    x=(Screen.get_width()-200)/3
    y = 600
    for i in range(3):
        card_group.add(GameObjects.Cards(file_paths[i],x,y,Screen,background_img))
        x=x+ 300
Win = None
def render():
    Screen.blit(background_img,background_rect)
    card_group.update()
    card_group.draw(Screen)

def start():
    Screen = pygame.display.set_mode((1000, 1000))
    pygame.init()
    running = True
    createCards()
    isClicked = None
    pregame = True
    redundant =GameObjects.Cards('backCard.png',600,300,Screen,background_img)
    redundant1 =GameObjects.Cards('backCard.png',600,300,Screen,background_img)
    redundant2 =GameObjects.Cards('backCard.png',600,600,Screen,background_img)
    redundant_Group = pygame.sprite.Group()
    RunOnce=False
    introImg = pygame.transform.scale(pygame.image.load("cardgameTitle.png"),(Screen.get_rect().width,Screen.get_rect().height))
    
    hey_img = pygame.transform.scale(pygame.image.load("cardGameIntro.png"),(Screen.get_rect().width,Screen.get_rect().height))
    while pygame.time.get_ticks() - startTime < 5000:
            Screen.blit(introImg,introImg.get_rect())
            pygame.display.update()
    
    midTime=pygame.time.get_ticks()
    while pygame.time.get_ticks() - midTime < 8000:
            Screen.blit(hey_img,hey_img.get_rect())
            pygame.display.update()
    while running:
        if pregame is True:
            render()   

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for sprite in card_group.sprites():
                    if sprite.rect.collidepoint(event.pos):
                        
                        isClicked = sprite.image
                        if RunOnce==False:
                            Screen.fill((0,0,0))
                            redundant.circleMovement()
                        
                            redundant1.moveToSpots(True,False)
                        
                            redundant2.moveToSpots(False,True)
                            redundant_Group.add(redundant,redundant1,redundant2)
                            pregame = False
                            Screen.blit(redundant.image,redundant.rect)
                            Screen.blit(redundant1.image,redundant1.rect)
                            Screen.blit(redundant2.image,redundant2.rect)
                            
                        
                for sprite in redundant_Group.sprites():
                    if RunOnce==True:
                        if sprite.rect.collidepoint(event.pos):
                            redundant.image = card_group.sprites()[0].image
                            redundant1.image = card_group.sprites()[1].image
                            redundant2.image = card_group.sprites()[2].image
                            Screen.blit(background_img,background_rect)
                            redundant_Group.update()
                            redundant_Group.draw(Screen)
                            # pygame.time.wait(500)
                            if sprite.image == isClicked:
                                
                                back_img = pygame.image.load('WinningForCardGame.png')
                                back_img = pygame.transform.scale(back_img, (Screen.get_width(),Screen.get_height()))
                                Screen.blit(back_img,Screen.get_rect())
                                newTime = pygame.time.get_ticks()
                                while pygame.time.get_ticks() - newTime < 5000:
                                    Screen.blit(back_img,(Screen.get_width(),Screen.get_height()))
                                    pygame.display.update()
                                return True
                            else:
                                
                                back_img = pygame.image.load('LosingForCardGame.png')
                                back_img = pygame.transform.scale(back_img, (Screen.get_width(),Screen.get_height()))
                                Screen.blit(back_img,Screen.get_rect())
                                endTime = pygame.time.get_ticks()
                                while pygame.time.get_ticks() - endTime < 5000:
                                    Screen.blit(back_img,(Screen.get_width(),Screen.get_height()))
                                    pygame.display.update()
                                return False
                RunOnce = True
            # clock.tick(60)
        pygame.display.flip()

        pygame.display.update()
        
    pygame.quit()