import pygame
import random
#Sprite class for Grades in Catch The Grade mini game
class Grade(pygame.sprite.Sprite):

    def __init__(self,screen):
        pygame.sprite.Sprite.__init__(self)
        #speed of grades
        self.gradeSpeed = 5
        self.screen = screen
        #random choice of whether a grade is good or bad
        if random.randint(0,1)==0:
            self.image =pygame.transform.scale(pygame.image.load("F.png"),(50,50))
            self.letter = "F"
        else:
            self.image = pygame.transform.scale(pygame.image.load("A.png"),(50,50))
            self.letter = "A"
        #rectangle and image of grade
        self.rect = self.image.get_rect()
        #start grade at random position at top of screen
        self.rect.x=random.randint(0,self.screen.get_rect().width-self.rect.width)
        self.rect.y=0
    
    #update function for grades; moves grades and kills grades if they reach bottom of screen
    def update(self):
        self.rect.y+=self.gradeSpeed
        if self.rect.y>self.screen.get_rect().height:
            self.kill()

    


#Student sprite class
class Student(pygame.sprite.Sprite):
    #image, rectangle, and speed of player
    def __init__(self):
        self.image =pygame.transform.scale(pygame.image.load("EngStudent.png").convert_alpha(),(100,100))
        self.rect = self.image.get_rect()
        
        self.playerSpeed=5

#catch the grade minigame
class CatchGame():

    #initializing starting variables
    def __init__(self,screen):
        #Student set
        self.student = Student()
        self.student.rect.bottom = screen.get_rect().bottom
        #screen loaded in
        self.screen = screen

        #score counter; if counter=10, win, else if counter=-10, lose
        self.gradeCounter = 0

        #grades sprite group
        self.grades = pygame.sprite.Group()


        self.clock = pygame.time.Clock()

    #render function to maintain background, player, and grades
    def render(self):
        #score counter on screen
        font = pygame.font.Font(None, 36)
        score = "Score:"+str(self.gradeCounter)
        text = font.render(score, True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.x=0
    
        #background
        background_Image = pygame.transform.scale(pygame.image.load("libraryBackground.jpeg"),(self.screen.get_rect().width,self.screen.get_rect().height))
        self.screen.blit(background_Image,(0,0))

        #player and grades
        self.screen.blit(self.student.image,self.student.rect)
        self.screen.blit(text,text_rect)
        self.grades.update()
        self.grades.draw(self.screen)
        #reset screen
        pygame.display.flip()
    
    #loads grades into grades Group
    def loadGrade(self,amount):
        for i in range(amount):
            self.grades.add(Grade(self.screen))


    #method called to start the minigame; returns true or false to denote a win or lose
    def start(self):
        running = True
        startTime = pygame.time.get_ticks()
        gradeAmount = 1

        #load 1 grade to start, then increase
        self.loadGrade(gradeAmount)

        #Intro image loaded in to explain the game
        introImg = pygame.transform.scale(pygame.image.load("loadingCatchGrades.jpg"),(self.screen.get_rect().width,self.screen.get_rect().height))
        #keep on screen for 5 seconds
        while pygame.time.get_ticks() - startTime < 5000:
            self.screen.blit(introImg,introImg.get_rect())
            pygame.display.update()


        self.render()
        #game loop
        while running:
            #event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running=False
                #if a key pressed, move student left or right depending on input
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a and self.student.rect.x>=0:
                        self.student.rect.x -= self.student.playerSpeed
                    elif event.key == pygame.K_d and self.student.rect.x<=(self.screen.get_rect().width-self.student.rect.width):
                        self.student.rect.x += self.student.playerSpeed

            #inputs
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a] and self.student.rect.x>=0:
                self.student.rect.x -= self.student.playerSpeed
            elif keys[pygame.K_d] and self.student.rect.x<=(self.screen.get_rect().width-self.student.rect.width):
                self.student.rect.x += self.student.playerSpeed

            #if player collides with a grade, increment or decrement score and remove collided grade
            for grade in pygame.sprite.spritecollide(self.student, self.grades, False):
                if grade.letter=="F":
                    self.gradeCounter-=1
                else:
                    self.gradeCounter+=1
                self.grades.remove(grade)
                grade.kill()
                self.loadGrade(gradeAmount)
            
            #if no grades on screen, load another grade
            if len(self.grades)==0:
                self.loadGrade(gradeAmount)
            
            #win/lose check
            if int(self.gradeCounter)==10:
                return True
            elif int(self.gradeCounter)==-10:
                return False

            #render
            self.render()
            #maintain frame rate
            self.clock.tick(60)
        
        pygame.quit()





























