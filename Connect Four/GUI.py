#-------------------------------------------------------------------------------------------------------------------------------------
import pygame
from constants import *
import Test3 as connect_4
import sys
import math
import random
import time
import numpy as np 
import Node
#-------------------------------------------------------------------------------------------------------------------------------------
pygame.init()
myfont = pygame.font.SysFont(F1, 75 ,bold = True)
score_font = pygame.font.SysFont(F1, 30 ,bold = True)
response_time=[]
duration=0
turn = random.randint(PLAYER, AGENT)
# Initializing the Game Screen
screen = pygame.display.set_mode(SIZE)
#-------------------------------------------------------------------------------------------------------------------------------------
def print_avg_responseTime():
    total_time =0
    for i in range(len(response_time)):
        total_time= total_time + response_time[i]

    avg_responseTime= total_time/len(response_time)    
    print("AVERAGE RESPONSE TIME=",  avg_responseTime)    
    return avg_responseTime
#-------------------------------------------------------------------------------------------------------------------------------------
def update():
    pygame.display.update()
#-------------------------------------------------------------------------------------------------------------------------------------
def draw_score_board(screen):
    pygame.draw.rect(screen, GREY, (0, 0, COLUMN_COUNT*SQUARESIZE,ROW_COUNT*SQUARESIZE+SQUARESIZE),2)
#-------------------------------------------------------------------------------------------------------------------------------------
def draw_board(board):
    for c in range(COLUMN_COUNT):
          for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE,SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2),int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
            pygame.draw.circle(screen, BLUE_BORDER, (int(c*SQUARESIZE+SQUARESIZE/2),int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS+3, 5)

    for c in range(COLUMN_COUNT):
          for r in range(ROW_COUNT):  
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), HEIGHT - int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
                pygame.draw.circle(screen, RED_BORDER, (int(c*SQUARESIZE+SQUARESIZE/2), HEIGHT - int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS, 8)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), HEIGHT - int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
                pygame.draw.circle(screen, YELLOW_BORDER, (int(c*SQUARESIZE+SQUARESIZE/2), HEIGHT - int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS, 8)
    
    
    pygame.draw.rect(screen, BLACK, (COLUMN_COUNT*SQUARESIZE,0, ROW_COUNT*SQUARESIZE+SQUARESIZE*4,SQUARESIZE*(ROW_COUNT+1)))
    pygame.draw.rect(screen, GREY, (0, 0, COLUMN_COUNT*SQUARESIZE,ROW_COUNT*SQUARESIZE+SQUARESIZE),2)

    display_score(board)

    # You MUST UPDATE EVERYTIME !!
    pygame.display.update()
#-------------------------------------------------------------------------------------------------------------------------------------
# This Function is to Display the Score in the GUI
def display_score(board):
    str1 = "Human Score: " + str(connect_4.scoring(board,1))
    score1 = score_font.render(str1, 1, RED)
    screen.blit(score1, (WIDTH + 40 , SQUARESIZE*2))
    str2 = "AI Agent Score: " + str(connect_4.scoring(board,2))
    score2 = score_font.render(str2, 1, YELLOW)
    screen.blit(score2, (WIDTH + 40 , SQUARESIZE*3-40))  
    str3 = "Time Taken\nBy AI Agent :\n " + f"{duration:.{5}f}"#str(duration)
    time = score_font.render(str3, 1, WHITE)
    screen.blit(time, (WIDTH + 40 , SQUARESIZE*4-60))
    #str4 = "Turn :\n " + str(turn)
    #player_turn = score_font.render(str4, 1, WHITE)
    #screen.blit(player_turn, (WIDTH + 40 , SQUARESIZE*5-60))
#-------------------------------------------------------------------------------------------------------------------------------------
def final_score(board):
    score = connect_4.scoring(board,AI_PIECE) - connect_4.scoring(board,PLAYER_PIECE)
    return score
#-------------------------------------------------------------------------------------------------------------------------------------
def draw_upper_rectangle(screen):
    pygame.draw.rect(screen,BLACK, (0,0,WIDTH,SQUARESIZE))
#-------------------------------------------------------------------------------------------------------------------------------------    
def play_game(depth, pruning,expected):    
    board = connect_4.create_board()
    gameover = False
    #turn = random.randint(PLAYER, AGENT)
    global turn
    turn = random.randint(PLAYER, AGENT)
    draw_board(board)
    pygame.display.update()
    k = depth
    alpha_beta = pruning
    expecti = expected
    turn_notTaken=True
    while not gameover:
        
        # The Input represents the "COLUMN" in which the player will
        # drop the piece from 0 to 6 (7 columns total)
        
        for event in pygame.event.get():
            # This must be included when creating any game using pygame
            if event.type == pygame.QUIT:
                sys.exit()

            # The following is to draw the upper part with the moving disc
            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen,BLACK, (0,0,WIDTH+SQUARESIZE*4,SQUARESIZE))
                posx = event.pos[0]
                if turn == PLAYER:
                    pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)
                    pygame.draw.circle(screen, RED_BORDER, (posx, int(SQUARESIZE/2)), RADIUS,8)
                    pygame.draw.rect(screen,BLACK, (WIDTH,0,SQUARESIZE*4,SQUARESIZE))

            pygame.draw.rect(screen, GREY, (0, 0, COLUMN_COUNT*SQUARESIZE,ROW_COUNT*SQUARESIZE+SQUARESIZE),2)
            pygame.display.update()  
            
            if event.type == pygame.MOUSEBUTTONDOWN:  
                # print(event.pos)
                pygame.draw.rect(screen,BLACK, (0,0,WIDTH,SQUARESIZE))  
        
                # Hymans's Turn (Player = Human)
                if turn == PLAYER:
                    print("turn = ",turn)
                    # We need to make sure that it is an integer, so cast to int
                    posx = event.pos[0]
                    col = int(math.floor(posx/SQUARESIZE))

                    if(connect_4.is_valid_location(board,col,expecti)):
                        row = connect_4.get_next_open_row(board,col)
                        print("\n next ope")
                        change_turn=connect_4.drop_piece(board,row,col,PLAYER_PIECE,expecti)
                        
                        #player1_score=scoring(board,PLAYER_PIECE)
                        #print("\nPlayer 1 Score = " , player1_score, "\n")
                        connect_4.print_board(board)
                        if(connect_4.check_game_over(board)):
                            gameover = True
                            print("GAME OVER!!")
                            print_avg_responseTime()

                        #if game_over:
                        #   gameover = True
                        if change_turn:
                            turn += 1
                            turn = turn % 2
                        else:
                            while True:
                                change_turn=connect_4.drop_piece(board,row,col,PLAYER_PIECE,expecti)
                                if change_turn: 
                                    break

                        #print_board(board)
                        draw_board(board)
                    #else:
                    #   print("Column is Full !")

                    
        
        # Agent Player
        if turn == AGENT and not gameover: 
            print("turn=",turn)
            k = depth
            alpha_beta = pruning
            expecti = expected

            if expecti:
                print("Expecti-MiniMax")
            if(alpha_beta):
                print("Alpha-Beta Pruning")

            node = Node.Node( np.copy(board), None)
            start = time.time()
            col = connect_4.solve(board, k, alpha_beta,expecti, node)
            end = time.time()
            global duration 
            duration = end - start
            response_time.append(duration)
            print("Time taken by agent=",end - start) # This will print the time taken in seconds
            connect_4.print_tree(node)
            #col = int(input("Player 2: "))
            if(connect_4.is_valid_location(board,col,expecti)):
                row = connect_4.get_next_open_row(board,col)
                change_turn=connect_4.drop_piece(board,row,col,AI_PIECE,expecti)
                draw_board(board)

                #AI_score=scoring(board,AI_PIECE)
                #print("\nAI Agent Score = " , AI_score, "\n")

                if(connect_4.check_game_over(board)):
                    gameover = True
                    print("GAME OVER!!")
                    print_avg_responseTime()
                # if game_over:
                #     gameover = True
                if change_turn:
                    turn += 1
                    turn = turn % 2
                else:
                    while True:
                        change_turn=connect_4.drop_piece(board,row,col,PLAYER_PIECE,expecti)
                        if change_turn: 
                            break    

        if gameover:
            print("Final Score: ", final_score(board))
            pygame.draw.rect(screen, BLACK, (0, SQUARESIZE*3, WIDTH, SQUARESIZE*2))
            pygame.draw.rect(screen, GREY, (0, SQUARESIZE*3, WIDTH, SQUARESIZE*2),2)
            label1 = myfont.render("GAME OVER", 1, GREY)
            screen.blit(label1, (150,SQUARESIZE*3+20))
            if final_score(board) > 0 :
                label = myfont.render("AI Agent Wins!!", 1, YELLOW)
                screen.blit(label, (20,SQUARESIZE*3+100))
            elif final_score(board) < 0 :
                label = myfont.render("Human Wins!!", 1, RED)
                screen.blit(label, (100,SQUARESIZE*3+100))
            else:
                label = myfont.render("TIE", 1, GREY)
                screen.blit(label, (20,SQUARESIZE*3+100))
            pygame.display.update()
            pygame.time.wait(3000)
