import CardsMiniGame as card
import kahoot as k
import pygame

Screen = pygame.display.set_mode((1200,800))

card.setScreen(Screen)
pygame.init()
k.setVar()
if(card.start()):
    print("hi")
pygame.quit
