import pygame
import random 
from button import ButtonText
# Set the game state

class Kahoot():
    def __init__(self):
        self.questions = questions
        self.current_question = 0


# Initialize Pygame
pygame.init()
startTime= pygame.time.get_ticks()
# Create the window
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Kahoot Game")
Screen = pygame.display.set_mode((1200,800))

#define set the screen to be the screen being used from the main game
def setScreen(screened):
    screen = screened

# Set the window dimensions
WIDTH = screen.get_width()
HEIGHT = screen.get_height()
# Set the colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Set the fonts
FONT_LARGE = pygame.font.Font(None, 72)
FONT_MEDIUM = pygame.font.Font(None, 36)
FONT_SMALL = pygame.font.Font(None, 24)

#Set the background
background_img =pygame.image.load('kahootstylebackground.png')
background_img = pygame.transform.scale(background_img, (WIDTH,HEIGHT))
background_rect = background_img.get_rect()

#render 
def render():
    screen.blit(background_img,background_rect)

# Set the question data
questions = [
    {
        "question": "What is the capital of France?",
        "answers": ["Paris", "Berlin", "Madrid", "Rome"],
        "correct": "Paris"
    },
    {
        "question": "What is the largest country in the world?",
        "answers": ["Canada", "China", "Russia", "USA"],
        "correct": "Russia"
    },
    {
        "question": "What is the highest mountain in the world?",
        "answers": ["Kilimanjaro", "Mount Everest", "Mount Fuji", "Mount McKinley"],
        "correct": "Mount Everest"
    }
    ,
    {
        "question": "What course is mandatory to become an engineer world wide?",
        "answers": ["Calculus", "Business", "Writing", "Depression"],
        "correct": "Calculus"
    }
    ,
    {
        "question": "Who is the all time leading scorer in the NBA?",
        "answers": ["Lebron James", "Michael Jordan", "Kevin Durant", "Kareem Abdul-Jabbar"],
        "correct": "Lebron James"
    }
    ,
    {
        "question": "What does an engineer receive upon graduating?",
        "answers": ["A hard hat", "A ring", "An engineering jacket", "Boiler suit"],
        "correct": "A ring"
    }
    ,
    {
        "question": "What is the worst engineering first year course?",
        "answers": ["Materials", "Statics", "Design", "Business"],
        "correct": "Statics"
    }
    ,
    {
        "question": "What is the common Beyblade phrase?",
        "answers": ["Let it rip!", "I choose you!", "It's hero time!", "Believe in the heart of the cards!"],
        "correct": "Let it rip!"
    }
    ,
    {
        "question": "What is the characteristic of a tuple?",
        "answers": ["immutable", "mutable", "encapsulated by {}", "has key words"],
        "correct": "immutable"
    }
    ,
    {
        "question": "What is the russian currency?",
        "answers": ["Peso", "Rupee", "Ruble", "Pound"],
        "correct": "Ruble"
    }
]



def setVar():
    game_state = "menu"
    current_question = 0
    score = 0




#Create buttons
group_of_buttons = []

# Create the main menu
def create_menu():
    render()
    title_text = FONT_LARGE.render("Welcome to Kahoot", True, BLACK)
    screen.blit(title_text, (WIDTH/2 - title_text.get_width()/2, 50))
    start_text = FONT_MEDIUM.render("Press SPACE to start", True, BLUE)
    screen.blit(start_text, (WIDTH/2 - start_text.get_width()/2, HEIGHT/2 - start_text.get_height()/2))
    pygame.display.flip()

# Create the question screen
def create_question(current_question):
    # global current_question
    render()
    question_text = FONT_MEDIUM.render(questions[current_question]["question"], True, WHITE)
    screen.blit(question_text, (WIDTH/2 - question_text.get_width()/2, 50))
    answer_y = 150
    i = 0
    # create the buttons that will contain the options to choose as answers for the question.
    for answer in questions[current_question]["answers"]:
        
        answer_text = FONT_SMALL.render(answer, True, BLACK)
        
        group_of_buttons.append(ButtonText(answer,[screen.get_width()/2 - 100,answer_y],render))
        group_of_buttons[i].draw(screen)
        #change which option is being looked at and change the height for which the next button will be drawn
        i +=1
        answer_y += 70
    
    pygame.display.flip()




# Create the score screen
def create_score(score):
    # global score
    render()
    score_text = FONT_MEDIUM.render(f"Your score: {score}", True, BLACK)
    screen.blit(score_text, (WIDTH/2 - score_text.get_width()/2, HEIGHT/2 - score_text.get_height()/2))
    pygame.display.flip()

# Main game loop

def start():
    screen = pygame.display.set_mode((1000, 1000))
    introImg = pygame.transform.scale(pygame.image.load("KahootTitle.png"),(screen.get_rect().width,screen.get_rect().height))
    while pygame.time.get_ticks() - startTime < 5000:
                screen.blit(introImg,introImg.get_rect())
                pygame.display.update()
    game_state = "menu"
    current_question = 0
    score = 0

    create_menu()
    running = True
    
    
    while running:
        clicked = False
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type== pygame.MOUSEBUTTONDOWN:
                for btn in group_of_buttons:
                    if btn.rect.collidepoint(event.pos):
                        if questions[current_question]["correct"] == btn.text:
                            score += 1
                        group_of_buttons.clear()
                        clicked = True
                if clicked ==True:
                    clicked == False
                    current_question +=1
                    if current_question < len(questions):
                        create_question(current_question)
                    else:
                        game_state = "score"
                        create_score(score)
                        pygame.time.wait(2000)
                        if score >5:
                            return True
                        if score <=5:
                            return False

            elif event.type == pygame.KEYDOWN:
                if game_state == "menu" and event.key == pygame.K_SPACE:
                    game_state = "question"  
                    create_question(current_question)
                    
                

        # Update the display
        pygame.display.update()

    # Quit Pygame
    pygame.quit()


