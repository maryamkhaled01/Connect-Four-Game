import pygame
from constants import *
import button
import GUI
import input

pygame.init()

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Game")

run = True

# Defining Fonts
font3 = pygame.font.SysFont(F3,40)

# Loading The Button Images
minimax_img = pygame.image.load('minimax.png').convert_alpha()
alpha_beta_img = pygame.image.load('alpha_beta.png').convert_alpha()
expected_img = pygame.image.load('expected.png').convert_alpha()

# Creating the Buttons
minimax_button = button.Button(175,75,minimax_img,1.5)
alpha_beta_button = button.Button(175,275,alpha_beta_img,1.5)
expected_button = button.Button(175,475,expected_img,1.5)

def draw_text(text,font,color,x,y):
    img = font.render(text,True,color)
    screen.blit(img,(x,y))


while run:
    screen.fill(BLACK)

    #draw_text("Hello, Welcome to the Game!",font3,WHITE,200,200)

    pruning = False
    expected = False
    k = 0

    # Handling Functions from our Buttons
    if minimax_button.draw(screen) == 1:
        print("MINIMAX")
        pruning = False
        expected = False
        k = input.get_input() 
        GUI.play_game(k, pruning, expected)
        run = False
        
    elif alpha_beta_button.draw(screen):
        print("ALPHA-BETA")
        pruning = True
        expected = False
        k = input.get_input() 
        GUI.play_game(k, pruning, expected)
        run = False

    elif expected_button.draw(screen):
        print("EXPECTED")
        pruning = False
        expected = True
        k = input.get_input() 
        GUI.play_game(k, pruning, expected)
        run = False

    # The Event Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit()