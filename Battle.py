import pygame

class Battle():
    
    def __init__(self,player,enemy,screen):
        self.screen=screen
        self.player=player
        self.enemy=enemy





    def start(self):
        running=True
        self.battle = BattleMenu(self.screen,self,["Fight","Status","Run"])



        self.currentMenu = self.battle
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running=False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(pygame.mouse.get_pos())
                if event.type == pygame.KEYDOWN:
                    if event==pygame.K_BACKSPACE and self.currentMenu is not self.battle:
                        self.currentMenu=self.currentMenu.previous
                
                self.currentMenu.checkMenuInput()
            

            self.renderMenu()
        
        pygame.quit()

    def render(self):
        #Background
        background_Image = pygame.transform.scale(pygame.image.load("BattleBg.png"),(self.screen.get_rect().width,self.screen.get_rect().height))
        self.screen.blit(background_Image,(0,0))

        #Player
        #self.screen.blit(self.player.battleSprite,self.player.battleSprite.get_rect())
        #self.player.battleSprite.get_rect().bottom=(208,393)

        #Enemy
        #self.screen.blit(self.enemy.image,self.enemy.image.get_rect())
        #self.enemy.image.get_rect().bottom=(814,189)

    
    def renderMenu(self):
        #Battle Menu
        self.render()
        menuFrame = pygame.transform.scale(pygame.image.load("battleMenu.png"),(406,144))
        self.screen.blit(menuFrame,(self.screen.get_rect().width-menuFrame.get_rect().width,385))
        self.currentMenu.render()
        pygame.display.flip()






class BattleMenu():
    def __init__(self,screen,battle,options,pM=None):
        self.screen=screen
        self.battle=battle

        self.previous = pM
        self.options=options
        #0->Fight, 1->Status, 2->Run, 3->N/A
        self.state=0


        self.offset= -45
        self.optionPos = [(701,432),(846,432),(701,490),(846,490)]


    def render(self):
        self.draw_cursor()
        for i in range(len(self.options)):
            self.draw_text(self.options[i],30,self.optionPos[i][0],self.optionPos[i][1])

    def checkMenuInput(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.state = self.state%2
            self.render()
        elif keys[pygame.K_a]:
            if self.state<=1:
                self.state=0
            else:
                self.state=2
        elif keys[pygame.K_s]:
            self.state = 2 + (self.state%2)
        elif keys[pygame.K_d]:
            if self.state<=1:
                self.state=1
            else:
                self.state=3
        elif keys[pygame.K_SPACE]:
            self.handle_key_press()

    def handle_key_press(self):
        if self.state==0:
            pass
        elif self.state==1:
            pass
        elif self.state==2:
            pass
        elif self.state==3:
            pass

    def draw_cursor(self):
        self.cursor = pygame.transform.scale(pygame.image.load("battleCursor.png"),(25,25))
        self.cursor_rect = self.cursor.get_rect()
        self.cursor_rect.center = (self.optionPos[self.state][0]+self.offset,self.optionPos[self.state][1])
        self.screen.blit(self.cursor,self.cursor_rect)

    def draw_text(self,text,size,x,y):
        font = pygame.font.Font("Bebas-Regular.ttf",size)
        text_surface = font.render(text, True, (0,0,0))
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.screen.blit(text_surface,text_rect)

class StatsMenu(BattleMenu):
    def __init__(self,screen,battle,options=None,pM=None):
        BattleMenu.__init__(self,screen,battle,options,pM)
        
    
    def render(self):
        health = "Mental Health - "+str(self.battle.player.stats[0])
        attack = "Attack - "+str(self.battle.player.stats[1])
        defense = "Defense - "+str(self.battle.player.stats[2])
        speed = "Speed - "+str(self.battle.player.stats[3])
        self.draw_text(health,30,781,417)
        self.draw_text(attack,30,781,437)
        self.draw_text(defense,30,781,457)
        self.draw_text(speed,30,781,477)
