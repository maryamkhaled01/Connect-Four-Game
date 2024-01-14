# --------------------------------------------------------------------------------------------------------------------------------------
#                       Connect Four - Trial ONE
# --------------------------------------------------------------------------------------------------------------------------------------
import numpy as np
import math
from constants import *
import random
import Node
# --------------------------------------------------------------------------------------------------------------------------------------
Last_row_pieces = 0
last_row_pieces_minmax = 0
last_state_key=0
# --------------------------------------------------------------------------------------------------------------------------------------
print ("\nWelcome to our Connect Four Game!\n")
# --------------------------------------------------------------------------------------------------------------------------------------
def create_board():
    board = np.zeros((ROW_COUNT,COLUMN_COUNT), dtype=int)
    return board

# --------------------------------------------------------------------------------------------------------------------------------------
def check_game_over(board):
    for i in range (COLUMN_COUNT):
        if board[ROW_COUNT-1][i]==0:
            return False
    return True    
# --------------------------------------------------------------------------------------------------------------------------------------
def drop_piece(board,row,col,piece,expecti):
    if expecti:
        random_num = random.randint(1, 10)
        if col==0 or col==COLUMN_COUNT-1: 
            if col==0:
                if random_num <=6 and is_valid_location(board,col,False):
                    row=get_next_open_row(board,col)
                    board[row][col] = piece
                    return True
                elif is_valid_location(board,col+1,False):
                    row=get_next_open_row(board,col+1)
                    board[row][col+1] = piece
                    return True
            if col==COLUMN_COUNT-1:
                if random_num <=6 and is_valid_location(board,col,False):
                    row=get_next_open_row(board,col)
                    board[row][col] = piece
                    return True
                elif is_valid_location(board,col-1,False):
                    row=get_next_open_row(board,col-1)
                    board[row][col-1] = piece
                    return True       
        else:
            if random_num <=6:
                if is_valid_location(board,col,False):
                    row=get_next_open_row(board,col)
                    board[row][col] = piece
                    return True
                else:
                    random_num= 7    
            elif random_num >6 and random_num <=8 and is_valid_location(board,col-1,False):
                row=get_next_open_row(board,col-1)
                board[row][col-1] = piece
                return True
            elif  is_valid_location(board,col+1,False):
               row=get_next_open_row(board,col+1)
               board[row][col+1] = piece 
               return True
        return False    
    else:
     board[row][col] = piece
     return True
# --------------------------------------------------------------------------------------------------------------------------------------
def drop_piece_minimax(board,row,col,piece):
    #print ("\n row=",row,"\tcol=",col)
    #print(board)
    board[row][col] = piece
# --------------------------------------------------------------------------------------------------------------------------------------
def is_valid_location(board, col,expecti):
    if expecti:
        if col > 0 and col < COLUMN_COUNT-1:
            return board[ROW_COUNT-1][col-1] == 0 or  board[ROW_COUNT-1][col] == 0 or board[ROW_COUNT-1][col+1] == 0
        if col == 0:
            return board[ROW_COUNT-1][col] == 0 or board[ROW_COUNT-1][col+1] == 0
        if col == COLUMN_COUNT-1:
            return board[ROW_COUNT-1][col-1] == 0 or board[ROW_COUNT-1][col] == 0
    else:
        return board[ROW_COUNT-1][col] == 0
# --------------------------------------------------------------------------------------------------------------------------------------
def get_next_open_row(board, col):
    for r in range (ROW_COUNT):
        if board[r][col] == 0:
            '''
            if r == ROW_COUNT-1:
                global Last_row_pieces
                Last_row_pieces += 1
                print("HEYYYY Last_row_pieces=",Last_row_pieces)
                '''
        # return the first empty row
            return r
# --------------------------------------------------------------------------------------------------------------------------------------
def scoring(board, player_num):
    score=0
    # Check horizontal locations for win
    for r in range(ROW_COUNT):
        for c in range(COLUMN_COUNT-3):
            if board[r][c] == player_num and board[r][c+1] == player_num and board[r][c+2] == player_num and board[r][c+3] == player_num:
                score += 1
                c=c+3
                while c + 1 < COLUMN_COUNT and board[r][c+1] == player_num:
                    score += 1
                    c += 1
                break
    # Check vertical locations for win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == player_num and board[r+1][c] == player_num and board[r+2][c] == player_num and board[r+3][c] == player_num:
                score += 1
                r = r+3
                while r + 1 < ROW_COUNT and board[r+1][c] == player_num:
                    score += 1
                    r += 1
                break

    # Check positively sloped diagonals
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == player_num and board[r+1][c+1] == player_num and board[r+2][c+2] == player_num and board[r+3][c+3] == player_num:
                score += 1
                r = r+3
                c = c+3 
                while r + 1 < ROW_COUNT and c+1 < COLUMN_COUNT and board[r+1][c] == player_num:
                    score += 1
                    r += 1
                    c += 1
                break

    # Check negatively sloped diagonals
    for c in range(COLUMN_COUNT-3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == player_num and board[r-1][c+1] == player_num and board[r-2][c+2] == player_num and board[r-3][c+3] == player_num:
                score += 1
                r = r-3
                c = c+3
                while r - 1 >=0 and c+1 < COLUMN_COUNT and board[r-1][c+1] == player_num:
                    score += 1
                    r -= 1
                    c += 1
                break

    # If no win condition is met
    return score
# --------------------------------------------------------------------------------------------------------------------------------------
def print_board(board):
    print(np.flip(board, 0), "\n")
# --------------------------------------------------------------------------------------------------------------------------------------
def get_valid_locations(board):
	valid_locations = []
	for col in range(COLUMN_COUNT):
		if is_valid_location(board, col,False):
			valid_locations.append(col)
	return valid_locations
# --------------------------------------------------------------------------------------------------------------------------------------
# def evaluate_window(window, piece):
#     # by default the oponent is the player
#     opponent_piece = PLAYER_PIECE

#     # if we are checking from the player's perspective, then the oponent is AI
#     if piece == PLAYER_PIECE:
#         opponent_piece = AI_PIECE

#     # initial score of a window is 0
#     score = 0

#     # based on how many friendly pieces there are in the window, we increase the score
#     if window.count(piece) == 4:
#         score += 100
#     elif window.count(piece) == 3 and window.count(0) == 1:
#         score += 5
#     elif window.count(piece) == 2 and window.count(0) == 2:
#         score += 2

#     # or decrese it if the oponent has 3 in a row
#     if window.count(opponent_piece) == 3 and window.count(0) == 1:
#         score -= 4 

#     return score
  
def evaluate_window(window, piece):
    # by default, the opponent is the player
    opponent_piece = PLAYER_PIECE if piece == AI_PIECE else AI_PIECE

    # initial score of a window is 0
    score = 0

    # based on how many friendly pieces there are in the window, we increase the score
    if window.count(piece) == 4:
        score += 100
    elif window.count(piece) == 3 and window.count(0) == 1:
        score += 5
    elif window.count(piece) == 2 and window.count(0) == 2:
        score += 2

    # or decrease it if the opponent has 3 to 7 in a row
    opponent_count = window.count(opponent_piece)
    empty_count = window.count(0)

    if 3 <= opponent_count <= 7 and empty_count == 1:
        # Block opponent's potential winning move
        score -= 1000

    return score
  
# --------------------------------------------------------------------------------------------------------------------------------------
# scoring the overall attractiveness of a board after a piece has been droppped
def score_position(board, piece):

    score = 0

    # score center column --> we are prioritizing the central column because it provides more potential winning windows
    center_array = [int(i) for i in list(board[:,COLUMN_COUNT//2])]
    center_count = center_array.count(piece)
    score += center_count * 6

    # below we go over every single window in different directions and adding up their values to the score
    # score horizontal
    for r in range(ROW_COUNT):
        row_array = [int(i) for i in list(board[r,:])]
        for c in range(COLUMN_COUNT - 3):
            window = row_array[c:c + 4]
            score += evaluate_window(window, piece)

    # score vertical
    for c in range(COLUMN_COUNT):
        col_array = [int(i) for i in list(board[:,c])]
        for r in range(ROW_COUNT-3):
            window = col_array[r:r+4]
            score += evaluate_window(window, piece)

    # score positively sloped diagonals
    for r in range(3,ROW_COUNT):
        for c in range(COLUMN_COUNT - 3):
            window = [board[r-i][c+i] for i in range(4)]
            score += evaluate_window(window, piece)

    # score negatively sloped diagonals
    for r in range(3,ROW_COUNT):
        for c in range(3,COLUMN_COUNT):
            window = [board[r-i][c-i] for i in range(4)]
            score += evaluate_window(window, piece)

    return score
#--------------------------------------------------------------------
def get_next_open_row_minmax(board, col):
    for r in range (ROW_COUNT):
        if board[r][col] == 0:
        # return the first empty row
            return r
#-------------------------------------------------------------------
# check if the node is terminal
def is_terminal_node(board):
    for col in range(COLUMN_COUNT):
        if board[ROW_COUNT-1][col] == 0:
                  return False      
    return True
#-------------------------------------------------------------------
def maximize(board, depth, alpha, beta, node):
     #print("Maxxxxxxxxxxxxxxx")
     valid_location = get_valid_locations(board)
     max_column = None
     max_utility = -math.inf 
     if depth == 0 or is_terminal_node(board):
        if is_terminal_node(board):
            AI_score=scoring(board, AI_PIECE)
            Human_score=scoring(board,PLAYER_PIECE)
            if AI_score > Human_score:
                node.value = 10000000
                return (None, 10000000)
            else:
                node.value = -10000000
                return (None, -10000000)
          #print("MAXIMIZE")
          #print_board(board)
        else:
          node.value = score_position(board,AI_PIECE)
          return None, score_position(board,AI_PIECE)
     for col in valid_location:
        row = get_next_open_row_minmax(board, col)
        b_copy = board.copy()
        child =drop_piece_minimax(b_copy, row, col, AI_PIECE)
        child_node = Node.Node(child,node)
        node.children.append(child_node)
        utility = minimize(b_copy, depth-1, alpha, beta, child_node)[1]
        if utility > max_utility:
            max_column = col
            max_utility = utility
        if alpha is not None and beta is not None:
                    if max_utility >= beta:
                        break
                    if max_utility > alpha:
                        alpha = max_utility
     node.value = max_utility
     return max_column, max_utility
#-------------------------------------------------------------------
def minimize(board, depth, alpha, beta, node):
     #print("MINNNNNNNNNNNNNNNNNNNNNN")
     valid_location = get_valid_locations(board)
     min_column = None
     min_utility = math.inf
     if depth == 0 or is_terminal_node(board):
        if is_terminal_node(board):
            AI_score=scoring(board, AI_PIECE)
            Human_score=scoring(board,PLAYER_PIECE)
            if AI_score > Human_score:
                node.value = 10000000
                return (None, 10000000)
            else:
                node.value = -10000000
                return (None, -10000000)
        else:
          node.value = score_position(board,AI_PIECE)
          return None, score_position(board,AI_PIECE)
     for col in valid_location:
        row = get_next_open_row_minmax(board, col)
        b_copy = board.copy()
        child = drop_piece_minimax(b_copy, row, col, PLAYER_PIECE)
        child_node = Node.Node(child,node)
        node.children.append(child_node)
        utility = maximize(b_copy, depth-1, alpha, beta, child_node)[1]
        if utility < min_utility:
            min_column = col
            min_utility = utility
        if alpha is not None and beta is not None:
                if min_utility <= alpha:
                    break
                if min_utility < beta:
                    beta = min_utility
     node.value = min_utility
     return min_column, min_utility
#-------------------------------------------------------------------
def expectimaximize(board, depth):
     #print("Maxxxxxxxxxxxxxxx")
     valid_location = get_valid_locations(board)
     max_column = None
     max_utility = -math.inf     
     if depth == 0 or is_terminal_node(board):
        if is_terminal_node(board):
            AI_score=scoring(board, AI_PIECE)
            Human_score=scoring(board,PLAYER_PIECE)
            if AI_score > Human_score:
                #node.value = 10000000
                return (None, 10000000)
            else:
                #node.value = -10000000
                return (None, -10000000)
          #print("MAXIMIZE")
          #print_board(board)
        else:
          #node.value = score_position(board,AI_PIECE)
          return None, score_position(board,AI_PIECE)
     for col in valid_location:
        utility = chance(board, depth, col,True)
        if utility > max_utility:
            max_column = col
            max_utility = utility
     return max_column, max_utility
#-------------------------------------------------------------------
def chance(board, depth, col,maximize):
    if maximize:
        row = get_next_open_row_minmax(board, col)
        b_copy1 = board.copy()
        drop_piece_minimax(b_copy1, row, col, AI_PIECE)
        utility_desiredCol = expectiminimize(b_copy1, depth-1)[1]
        if col==0 or col==COLUMN_COUNT-1: 
            if col==0:    
                row = get_next_open_row_minmax(board, 1)
                if row == None:
                    utility_stochasticCol=0
                else:
                    b_copy2 = board.copy()
                    drop_piece_minimax(b_copy2, row, col, AI_PIECE)
                    utility_stochasticCol = expectiminimize(b_copy2, depth-1)[1]
                return 0.6*int(utility_desiredCol) + 0.4*int(utility_stochasticCol)
            
            if col==COLUMN_COUNT-1:    
                row = get_next_open_row_minmax(board, COLUMN_COUNT-2)
                if row == None:
                    utility_stochasticCol=0
                else:
                    b_copy2 = board.copy()
                    drop_piece_minimax(b_copy2, row, col, AI_PIECE)
                    utility_stochasticCol = expectiminimize(b_copy2, depth-1)[1]
                return 0.6*int(utility_desiredCol) + 0.4*int(utility_stochasticCol)
        else:
            row = get_next_open_row_minmax(board, 1)
            if row == None:
                utility_stochasticCol1=0
            else: 
                b_copy2 = board.copy()
                drop_piece_minimax(b_copy2, row, col, AI_PIECE)
                utility_stochasticCol1 = expectiminimize(b_copy2, depth-1)[1]  
            row = get_next_open_row_minmax(board, 1)
            if row == None:
                utility_stochasticCol2=0
            else: 
                b_copy3 = board.copy()
                drop_piece_minimax(b_copy2, row, col, AI_PIECE)
                utility_stochasticCol2 = expectiminimize(b_copy3, depth-1)[1]
            return 0.6*int(utility_desiredCol) + 0.2*int(utility_stochasticCol1) + 0.2*int(utility_stochasticCol2)
 
    else:
        row = get_next_open_row_minmax(board, col)
        b_copy1 = board.copy()
        drop_piece_minimax(b_copy1, row, col, PLAYER_PIECE)
        utility_desiredCol = expectimaximize(b_copy1, depth-1)[1]
        if col==0 or col==COLUMN_COUNT-1: 
            if col==0:    
                row = get_next_open_row_minmax(board, 1)
                if row == None:
                    utility_stochasticCol=0
                else:
                    b_copy2 = board.copy()
                    drop_piece_minimax(b_copy2, row, col, PLAYER_PIECE)
                    utility_stochasticCol = expectimaximize(b_copy2, depth-1)[1]
                return 0.6*int(utility_desiredCol) + 0.4*int(utility_stochasticCol)
            
            if col==COLUMN_COUNT-1:    
                row = get_next_open_row_minmax(board, COLUMN_COUNT-2)
                if row == None:
                    utility_stochasticCol=0
                else:
                    b_copy2 = board.copy()
                    drop_piece_minimax(b_copy2, row, col, PLAYER_PIECE)
                    utility_stochasticCol = expectimaximize(b_copy2, depth-1)[1]
                return 0.6*int(utility_desiredCol) + 0.4*int(utility_stochasticCol) 
        else:
            row = get_next_open_row_minmax(board, col-1)
            if row == None:
                utility_stochasticCol1=0
            else:
                b_copy2 = board.copy()
                drop_piece_minimax(b_copy2, row, col, PLAYER_PIECE)
                utility_stochasticCol1 = expectimaximize(b_copy2, depth-1)[1]  
            row = get_next_open_row_minmax(board, col+1)
            if row == None:
                utility_stochasticCol2=0
            else: 
                b_copy3 = board.copy()
                drop_piece_minimax(b_copy3, row, col, PLAYER_PIECE)
                utility_stochasticCol2 = expectimaximize(b_copy3, depth-1)[1]  
            return 0.6*int(utility_desiredCol) + 0.2*int(utility_stochasticCol1) + 0.2*int(utility_stochasticCol2)
#-------------------------------------------------------------------
def expectiminimize(board, depth):
     #print("MINNNNNNNNNNNNNNNNNNNNNN")
     valid_location = get_valid_locations(board)
     min_column = None
     min_utility = math.inf
     if depth == 0 or is_terminal_node(board):
        if is_terminal_node(board):
            AI_score=scoring(board, AI_PIECE)
            Human_score=scoring(board,PLAYER_PIECE)
            if AI_score > Human_score:
                return (None, 10000000)
            else:
                return (None, -10000000)
          #print("MAXIMIZE")
          #print_board(board)
        else:
          return None, score_position(board,AI_PIECE)
     for col in valid_location:
        # row = get_next_open_row_minmax(board, col)
        # b_copy = board.copy()
        # drop_piece(b_copy, row, col, AI_PIECE)
        utility = chance(board, depth-1,col,False)
        if utility < min_utility:
            min_column = col
            min_utility = utility
     return min_column, min_utility
#-------------------------------------------------------------------
def solve(board, depth, alpha_beta_pruning,expecti, node):
        # reset the data
        #self.__explored = {}
        #self.__tree = Tree()

        #create root for the tree to be used as temporary parent
        #self.__tree.create_node('root','root')
        if alpha_beta_pruning:
            (t, val) = maximize(board,depth,-math.inf,math.inf, node)
        else:
            (t, val) = maximize(board,depth, None , None, node)
        
        if expecti:
            (t, val) = expectimaximize(board,depth)
        if not isinstance(t, int):
            valid_location = get_valid_locations(board)
            if len(valid_location)>1:
                return valid_location[random.randint(0, len(valid_location)-1)]
            else:
                 return valid_location[0]
        return t
#-------------------------------------------------------------------------------------------------------------------------------------
# visited = []
# queue = []
# def print_tree(parent):
#     node = parent
#     print("Node\tDepth")
#     visited.append(node)
#     queue.append([node, 0])
#     depth = 0
#     while queue:
#         n, depth = queue.pop(0)
#         if n.children is None:
#             break
#         print(n.value,"\t", depth)
#         for child in n.children:
#             if child not in visited:
#                 visited.append(child)
#                 queue.append([child,depth+1])
visited = []
stack = []
def print_tree(parent):
    node = parent
    visited.append(node)
    expanded_nodes = 1
    stack.append([node, 0])
    depth = 0
    while stack:
        n, depth = stack.pop()
        if n.children is None:
            break
        print("\t"*depth, n.value)
        for child in n.children:
            if child not in visited:
                visited.append(child)
                expanded_nodes += 1
                stack.append([child,depth+1])
    
    print("Number of Expanded Nodes:", expanded_nodes)