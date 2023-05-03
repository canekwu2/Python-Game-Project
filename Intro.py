import pygame

class IntroDialogue():

    def __init__(self,screen):
        self.screen=screen
        self.dialogueCursor=0
        self.dialogue= [
            ["Hello future Engineers!","Welcome to Western, my name is","Professor Shaimaa."],
            ["To graduate from Western","you need to pass your","4 exams..."],
            ["All in the same day!"],
            ["Travel across campus to get to", "your exams in time"],
            ["If you fail your exams, you'll","lose (mental) health and fail the semester.",":("],
            ["But if you pass, you'll get","a cool leather jacket and","iron ring!"],
            ["Good luck!"] 
        ]

    def draw_text(self,text,size,x,y):
        y=200
        for line in text:
            font = pygame.font.Font("Bebas-Regular.ttf",size)
            text_surface = font.render(line, True, (0,0,0))
            text_rect = text_surface.get_rect()
            text_rect.center = (x,y)
            self.screen.blit(text_surface,text_rect)
            y+=20

    def start(self):
        running=True
        pygame.mixer.music.load("intro.mp3")
        pygame.mixer.music.play(loops=-1)

        while running:
            for event in pygame.event.get():
                if event.type ==pygame.QUIT:
                    running=False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(pygame.mouse.get_pos())
                if event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE:
                        self.dialogueCursor+=1
            
            if self.dialogueCursor==len(self.dialogue):
                break
            self.render()
        
    
    def render(self):
        professor = pygame.transform.scale(pygame.image.load("narrator.png"),(self.screen.get_rect().width,self.screen.get_rect().height))
        professor_rect = professor.get_rect()

        professor_rect.center=self.screen.get_rect().center
        self.screen.blit(professor,professor_rect)

        self.draw_text(self.dialogue[self.dialogueCursor],20,627,284)

    
        pygame.display.flip()



