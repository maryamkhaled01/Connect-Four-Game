import pygame
import pygame_gui
import sys
from constants import *
import button

pygame.init()

font3 = pygame.font.SysFont(F3,50)

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Input Depth K")

manager = pygame_gui.UIManager(SIZE)

text_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((300, 350), (500, 100)), manager=manager,object_id='#main_text_entry')


clock = pygame.time.Clock()

def draw_text(text,font,color,x,y):
    img = font.render(text,True,color)
    screen.blit(img,(x,y))

def get_input():
    while True:

        screen.fill(BLACK)
        UI_REFRESH_RATE = clock.tick(60)/1000
        draw_text("Enter K (Max Depth) ", font3 , WHITE, 300, 200)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and
                event.ui_object_id == '#main_text_entry'):
                k_str = event.text
                k = int(k_str)
                return k
            manager.process_events(event)
        
        manager.update(UI_REFRESH_RATE)

        manager.draw_ui(screen)

        pygame.display.update()
    

# print("K input = ", get_input())