# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 12:20:15 2021

@author: Martin
"""

import BoardPieces as bp

class Game(object):
    move_number = 0
    whites = []
    blacks = []
    save_moves = []
    board = bp.Board()
    wking = bp.Piece("w", board, (-1,-1))
    bking = bp.Piece("b", board, (-1,-1))
    
    def move(board, move_set):
        '''
        Checks if the piece is allowed to move on that turn
        Checks if move is in allowed moves
        Then moves piece on board
        If attacking, removes piece from overall list of white or black pieces and from board
        Checks pawn's first move and promotion
        '''
             
        allowed_moves = Game.board.get_board()[move_set[0]][move_set[1]].allowed_moves()
        move_to = (move_set[2],move_set[3])
        print("Debugging piece and allowed moves:", Game.board.get_board()[move_set[0]][move_set[1]], allowed_moves)
        
        if(move_to in allowed_moves):
            if(Game.save_moves != []):
                if(move_to in Game.save_moves):
                    "".split()
                else:
                    print("That move will not save you.")
                    return None
                    
            if(Game.board.get_board()[move_set[0]][move_set[1]].get_name() == "Pawn"):
                #Trigger pawn's set_first_move function after the first move
                Game.board.get_board()[move_set[0]][move_set[1]].set_first_move()
                
            #Try to remove a piece, don't error out if there isn't actually a piece at move site        
            try: 
                dead_piece = Game.board.get_board()[move_set[2]][move_set[3]]
                if(Game.board.get_board()[move_set[0]][move_set[1]].get_color() == "w"):
                    Game.blacks.remove(dead_piece)
                if(Game.board.get_board()[move_set[0]][move_set[1]].get_color() == "b"):
                    Game.whites.remove(dead_piece)
            except(ValueError):
                "".split() #Do nothing
                
            #Actual move
            Game.board.get_board()[move_set[2]][move_set[3]] = Game.board.get_board()[move_set[0]][move_set[1]]
            Game.board.get_board()[move_set[2]][move_set[3]].set_index((move_set[2], move_set[3]))
            Game.board.get_board()[move_set[0]][move_set[1]] = None
            
            #Check for promotion
            if(Game.board.get_board()[move_set[2]][move_set[3]].get_name() == "Pawn"):
                if(Game.board.get_board()[move_set[2]][move_set[3]].get_color() == "b" and move_set[0] == 7):
                    while(True):
                        try: 
                            prom = input("Pawn has reach the end of the board, what do you want to promote it to, Queen, Bishop, Rook, or Knight(q/b/r/k)?")
                            assert prom == "q" or prom == "b" or prom == "r" or prom == "k"
                            break
                        except(AssertionError):
                            print("Input q, r, b, or k")
                            continue
                    switcher={
                        "q" : bp.Queen(Game.board.get_board()[move_set[2]][move_set[3]].get_color(), Game.board, (move_set[2], move_set[3])),
                        "b" : bp.Bishop(Game.board.get_board()[move_set[2]][move_set[3]].get_color(), Game.board, (move_set[2], move_set[3])),
                        "r" : bp.Rook(Game.board.get_board()[move_set[2]][move_set[3]].get_color(), Game.board, (move_set[2], move_set[3])),
                        "k" : bp.Knight(Game.board.get_board()[move_set[2]][move_set[3]].get_color(), Game.board, (move_set[2], move_set[3])),
                        }
                    Game.board.get_board()[move_set[2]][move_set[3]] = switcher.get(prom)
                if(Game.board.get_board()[move_set[2]][move_set[3]].get_color() == "w" and move_set[0] == 0):
                    while(True):
                        try: 
                            prom = input("Pawn has reach the end of the board, what do you want to promote it to, Queen, Bishop, Rook, or Knight(q/b/r/k)?")
                            assert prom == "q" or prom == "b" or prom == "r" or prom == "k"
                            break
                        except(AssertionError):
                            print("Input q, r, b, or k")
                            continue
                    switcher={
                        "q" : bp.Queen(Game.board.get_board()[move_set[2]][move_set[3]].get_color(), Game.board, (move_set[2], move_set[3])),
                        "b" : bp.Bishop(Game.board.get_board()[move_set[2]][move_set[3]].get_color(), Game.board, (move_set[2], move_set[3])),
                        "r" : bp.Rook(Game.board.get_board()[move_set[2]][move_set[3]].get_color(), Game.board, (move_set[2], move_set[3])),
                        "k" : bp.Knight(Game.board.get_board()[move_set[2]][move_set[3]].get_color(), Game.board, (move_set[2], move_set[3])),
                        }
                    Game.board.get_board()[move_set[2]][move_set[3]] = switcher.get(prom)
                    
            #increase move num and show board
            Game.move_number+=1
            Game.board.show()
            
        else:
            print("Debugging piece and allowed moves:", Game.board.get_board()[move_set[0]][move_set[1]], allowed_moves)
            print("That move is not allowed.")
            
    def sim_move(board, move_set, color):
        temporary_piece = None
        
        allowed_moves = Game.board.get_board()[move_set[0]][move_set[1]].allowed_moves()
        move_to = (move_set[2],move_set[3])
        print("Debugging piece and allowed moves:", Game.board.get_board()[move_set[0]][move_set[1]], allowed_moves)
        
        if(move_to in allowed_moves):
            if(Game.board.get_board()[move_set[0]][move_set[1]].get_name() == "Pawn"):
                #Trigger pawn's set_first_move function after the first move
                Game.board.get_board()[move_set[0]][move_set[1]].set_first_move()
                
                
            #Actual move
            temporary_piece = Game.board.get_board()[move_set[2]][move_set[3]]
            Game.board.get_board()[move_set[2]][move_set[3]] = Game.board.get_board()[move_set[0]][move_set[1]]
            Game.board.get_board()[move_set[2]][move_set[3]].set_index((move_set[2], move_set[3]))
            Game.board.get_board()[move_set[0]][move_set[1]] = None
            
            if(color == "w"):
                if(Game.is_check_w() == None):
                    Game.board.get_board()[move_set[0]][move_set[1]] = Game.board.get_board()[move_set[2]][move_set[3]]
                    Game.board.get_board()[move_set[0]][move_set[1]].set_index((move_set[0], move_set[1]))
                    Game.board.get_board()[move_set[2]][move_set[3]] = temporary_piece
                    return True
                
            if(color == "b"):
                if(Game.is_check_b() == None):
                    Game.board.get_board()[move_set[0]][move_set[1]] = Game.board.get_board()[move_set[2]][move_set[3]]
                    Game.board.get_board()[move_set[0]][move_set[1]].set_index((move_set[0], move_set[1]))
                    Game.board.get_board()[move_set[2]][move_set[3]] = temporary_piece
                    return True
                
            Game.board.get_board()[move_set[0]][move_set[1]] = Game.board.get_board()[move_set[2]][move_set[3]]
            Game.board.get_board()[move_set[0]][move_set[1]].set_index((move_set[0], move_set[1]))
            Game.board.get_board()[move_set[2]][move_set[3]] = temporary_piece
            return False
            
            
            
                    
            
  
    def move_input():
        '''
        Converts input of a#;b# to list [y-from, x-from, y-to, x-to]
        Input of a# returns available moves of that piece
        Fails if there is no piece in from index
        '''
    
        while(True):
            move = input("what is your move? ")
            
            try:
                switcher={
                        "a" : 0,
                        "b" : 1,
                        "c" : 2,
                        "d" : 3,
                        "e" : 4,
                        "f" : 5,
                        "g" : 6,
                        "h" : 7
                        }
                
                if(len(move) == 2 and (move[0].isalpha() and move[1].isdigit())):
                    val = [8-int(move[1]),switcher.get(move[0])]
                    print("Allowed moves of " + str(Game.board.get_board()[val[0]][val[1]]) + str(Game.board.get_board()[val[0]][val[1]].allowed_moves()))
                    continue
                
                assert move[0].isalpha() and move[1].isdigit() and move[2] ==";" and move[3].isalpha() and move[4].isdigit()
               
                val = [8-int(move[1]),switcher.get(move[0]),8-int(move[4]),switcher.get(move[3])]
                assert Game.board.get_board()[val[0]][val[1]] != None
                return val
        
            except(AssertionError):
                print("Please input valid indicies")
                continue
            
    def is_check_b():
        '''
        If king in an opposite colored piece's allowed_moves, signal a check
        Color is of current turn's king
        '''
        checkers = []
        for piece in Game.whites:
            if(Game.bking.get_index() in piece.allowed_moves()):
                checkers.append(piece)
        
        if(checkers!=[]):
            return checkers
        
        return None
    
    def is_check_w():
        checkers = []
        for piece in Game.blacks:
            if(Game.wking.get_index() in piece.allowed_moves()):
                checkers.append(piece)
            if(checkers!= []):
                return checkers
            
        return None
            
    
    def is_checkmate():
        '''
        If it is a player's turn and the king has no available moves
        and is in an allowed_moves of an opposite color piece
        and recalculating every possible move of other pieces would not release the check
        return True
        '''
        if(Game.is_check_b() == None and Game.is_check_w() == None):
            return None
        
        checkers = []
        checker_moves = []
        save_moves = []
        if(Game.move_number%2 == 0):
            checkers = Game.is_check_w() 
            for piece in checkers:
                checker_moves.append(piece.allowed_moves())
            for piece in Game.whites:
                for move in piece.allowed_moves():
                    for check_move in checker_moves:
                        if(move == check_move):
                            if(Game.board[move[0],move[1]].getColor=="w"):
                                continue
                            if(Game.sim_move(Game.board,[piece.index[0],piece.index[1],move[0],move[1]],"w") == True):
                                save_moves.append(move)
                            
            if(save_moves == []):
                return "b"
            return save_moves
        
        
        if(Game.move_number%2 != 0):
            checkers = Game.is_check_b() 
            for piece in checkers:
                checker_moves.append(piece.allowed_moves())
            for piece in Game.blacks:
                for move in piece.allowed_moves():
                    for check_move in checker_moves:
                        if(move == check_move):
                            if(Game.board[move[0],move[1]].getColor=="b"):
                                continue
                            if(Game.sim_move(Game.board,[piece.index[0],piece.index[1],move[0],move[1]],"b") == True):
                                save_moves.append(move)
                            
            if(save_moves == []):
                return "w"
            return save_moves
                            
                            
                            
                            
                        
        "".split()
        
    def run_console():
        '''
        Initializes pieces on board
        Loops turns until checkmate
        '''
        
        #Create Pawns
        for i in range(len(Game.board.get_board()[1])):
            piece = bp.Pawn("b", Game.board, (1,i))
            Game.board.add(piece)
            Game.blacks.append(piece)
            piece = bp.Pawn("w", Game.board, (6,i))
            Game.board.add(piece)
            Game.whites.append(piece)
            
        #Rooks
        for i in range(0,8,7):
            piece = bp.Rook("b", Game.board, (0,i))
            Game.board.add(piece)
            Game.blacks.append(piece)
            piece = bp.Rook("w", Game.board, (7,i))
            Game.board.add(piece)
            Game.whites.append(piece)
            
        #Knights
        for i in range(1,7,5):
            piece = bp.Knight("b", Game.board, (0,i))
            Game.board.add(piece)
            Game.blacks.append(piece)
            piece = bp.Knight("w", Game.board, (7,i))
            Game.board.add(piece)
            Game.whites.append(piece)
            
        #Bishop
        for i in range(2,7, 3):
            piece = bp.Bishop("b", Game.board, (0,i))
            Game.board.add(piece)
            Game.blacks.append(piece)
            piece = bp.Bishop("w", Game.board, (7,i))
            Game.board.add(piece)
            Game.whites.append(piece)
            
        #Queens
        if(True): #For collapsing purposes
            piece = bp.Queen("b", Game.board, (0,3))
            Game.board.add(piece)
            Game.blacks.append(piece)
            piece = bp.Queen("w", Game.board, (7,3))
            Game.board.add(piece)
            Game.whites.append(piece)
        
        #Kings
        if(True):
            Game.bking = bp.King("b", Game.board, (0,4))
            Game.board.add(Game.bking)
            Game.blacks.append(Game.bking)
            Game.wking = bp.King("w", Game.board, (7,4))
            Game.board.add(Game.wking)
            Game.whites.append(Game.wking)

        Game.board.show()
        '''Should we just have the pieces be represented by the first initial
        instead of the whole word?'''
        
        #TO TEST IF LISTS INTIALIZED CORRECTLY
        # print("BLACK")
        # for item in blacks:
        #     print(item.get_name(), item.get_index())
        # print("WHITE")
        # for item in whites:
        #     print(item.get_name(), item.get_index())
        
        '''
        Game loop:
        Tell user whose turn it is
        Take input
        if not checkmate, continue
        '''
        
        
        while(Game.is_checkmate() != "w" and Game.is_checkmate != "b"):
            if(Game.move_number%2 == 0):
                print("It is white's turn")
                if(Game.is_check_w() != None):
                    save_moves = Game.is_checkmate()
                    print("White king is checked")
                    '''SOMEHOW NEED TO FORCE AN UNCHECKING MOVE, DUPLICATE BOARD TEST MAYBE'''
                move_set = Game.move_input()
                if(Game.board.get_board()[move_set[0]][move_set[1]].get_color() == "w"):
                    if(Game.board.get_board()[move_set[2]][move_set[3]] == None):
                        Game.move(Game.board, move_set)
                    elif(Game.board.get_board()[move_set[2]][move_set[3]].get_color() == "b"):
                        Game.move(Game.board, move_set)
                    else:
                        print("You cannot attack your own piece.")
                else:
                    print("You must pick a white piece.")
               
                
            if(Game.move_number % 2 != 0):
                print("It is black's turn")
                if(Game.is_check_b() != None):
                    save_moves = Game.is_checkmate()
                    print("Black king is checked")
                    '''SOMEHOW NEED TO FORCE AN UNCHECKING MOVE'''
                move_set = Game.move_input()
                if(Game.board.get_board()[move_set[0]][move_set[1]].get_color() == "b"):
                    if(Game.board.get_board()[move_set[2]][move_set[3]] == None):
                        Game.move(Game.board, move_set)
                    elif(Game.board.get_board()[move_set[2]][move_set[3]].get_color() == "w"):
                        Game.move(Game.board, move_set)
                    else:
                        print("You cannot attack your own piece.")
                        continue
                else:
                    print("You must pick a black piece.")
                    continue
                
        if(Game.is_checkmate() == "w"):
            print ("Black has no more possible moves, white has won the game.")
            
        else:
            print ("White has no more possible moves, black has won the game.")
            
            
        
    def run_gui():
        "".split()
        
    
def main():
    Game.run_console()

if __name__ == "__main__":
    main()
        
        
# print(str(input_checker("A7:F3")))

