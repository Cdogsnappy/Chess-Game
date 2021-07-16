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
    
    def move(board, move_set):
        count = 0
        move_list = board.board[move_set[1]][move_set[0]].allowed_moves()
        move_to = (move_set[3],move_set[2])
        for j in range(len(move_list)):
            if(move_list[j] == move_to):
                count+=1
                
        if(count == 0):
            board.board[move_set[3]][move_set[2]] = board.board[move_set[1]][move_set[0]]
            board.board[move_set[1]][move_set[0]] = None
            Game.move_number+=1
            
        else:
            print("That move is not allowed.")
            
            
            
            
    def attack(board, move_set):
        
        count = 0
        move_list = board.board[move_set[1]][move_set[0]].allowed_moves()
        move_to = (move_set[3],move_set[2])
        for j in range(len(move_list)):
            if(move_list[j] == move_to):
                count+=1
                
        if(count == 0):
            dead_piece = board.board[move_set[3]][move_set[2]]
            if(board.board[move_set[1]][move_set[0]].get_color == "w"):
                for j in range(len(Game.blacks)):
                    if(Game.blacks[j] == dead_piece):
                        Game.blacks.remove[j]
                        
            if(board.board[move_set[1]][move_set[0]].get_color == "b"):
                for j in range(len(Game.whites)):
                    if(Game.whites[j] == dead_piece):
                        Game.whites.remove[j]
                        
            board.board[move_set[3]][move_set[2]] = board.board[move_set[1]][move_set[0]]
            board.board[move_set[1]][move_set[0]] = None
            Game.move_number+=1
            
        else:
            print("That move is not allowed.")
            
            
  
    def move_input():
    
        move = input("what is your move? ")
    
        while(True):
            try:
                assert move[0].isalpha() and move[1].isdigit() and move[2] ==":" and move[3].isalpha() and move[4].isdigit()
               
                switcher={
                    "A" : 0,
                    "B" : 1,
                    "C" : 2,
                    "D" : 3,
                    "E" : 4,
                    "F" : 5,
                    "G" : 6,
                    "H" : 7
                    }
            
                return [8-int(move[1]),switcher.get(move[0]),8-int(move[4]),switcher.get(move[3])]
        
            except(AssertionError):
                print("There was an error, please try again")
                move = input("What is your move? ")
                continue
            
    def is_check():
        '''
        If the opposite color king is in your allowed_moves, signal a check
        '''
    
    def is_checkmate():
        '''
        If it is a player's turn and the king has no available moves
        and is in an allowed_moves of an opposite color piece
        and recalculating every possible move of other pieces would not release the check
        return True
        '''
        "".split()
        
    def run_console():
        board = bp.Board()
        
        #Create Pawns
        for i in range(len(board.get_board()[1])):
            pawn = bp.Pawn("b", board, (1,i))
            board.add(pawn)
            blacks.append(pawn)
            pawn = bp.Pawn("w", board, (6,i))
            board.add(pawn)
            whites.append(pawn)
            
        #Rooks
        for i in range(0,8,7):
            rook = bp.Rook("b", board, (0,i))
            board.add(rook)
            blacks.append(rook)
            rook = bp.Rook("w", board, (7,i))
            board.add(rook)
            whites.append(rook)
            
        #Knights
        for i in range(1,7,5):
            knight = bp.Knight("b", board, (0,i))
            board.add(knight)
            blacks.append(knight)
            knight = bp.Knight("w", board, (7,i))
            board.add(knight)
            whites.append(knight)
            
        #Bishop
        for i in range(2,7, 3):
            bishop = bp.Bishop("b", board, (0,i))
            board.add(bishop)
            blacks.append(bishop)
            bishop = bp.Bishop("w", board, (7,i))
            board.add(bishop)
            whites.append(bishop)
            
        #Queens
        queen = bp.Queen("b", board, (0,3))
        board.add(queen)
        blacks.append(queen)
        queen = bp.Queen("w", board, (7,3))
        board.add(queen)
        whites.append(queen)
        
        #Kings
        king = bp.King("b", board, (0,4))
        board.add(king)
        blacks.append(king)
        king = bp.King("w", board, (7,4))
        board.add(king)
        whites.append(king)

        board.show()
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
        
        
        while(Game.is_checkmate() == None):
            "is_checkmate will return None if no checkmate, otherwise it will return the color of the king that is checkmated."
            if(Game.move_number%2 == 0):
                print("It is white's turn")
                move_set = Game.move_input()
                if(board.board[move_set[1]][move_set[0]].get_color == "w"):
                    if(board.board[move_set[3]][move_set[2]] == None):
                        Game.move(board, move_set)
                    if(board.board[move_set[3]][move_set[2]].get_color == "b"):
                        Game.attack(board, move_set)
                    else:
                        print("You cannot attack your own piece.")
                else:
                    print("You must pick a white piece.")
                    
               
                
            if(Game.move_number % 2 != 0):
                print("It is black's turn")
                move_set = Game.move_input()
                if(board.board[move_set[1]][move_set[0]].get_color == "w"):
                    if(board.board[move_set[3]][move_set[2]] == None):
                        Game.move(move_set)
                    if(board.board[move_set[3]][move_set[2]].get_color == "b"):
                        Game.attack(move_set)
                    else:
                        print("You cannot attack your own piece.")
                        continue
                else:
                    print("You must pick a black piece.")
                    continue
                
            
            
        
    def run_gui():
        "".split()
        
    
def main():
    Game.run_console()

if __name__ == "__main__":
    main()
        
        
# print(str(input_checker("A7:F3")))

