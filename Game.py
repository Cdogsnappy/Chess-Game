# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 12:20:15 2021

@author: Martin
"""

import BoardPieces as bp

class Game(object):
    def run():
        board = bp.Board()
        whites = []
        blacks = []
        
        #Create Pawns
        for i in range(len(board.get_board()[1])):
            pawn = bp.Pawn("b", board, (1,i))
            board.add(pawn)
            blacks.append(pawn)
        for i in range(len(board.get_board()[6])):
            pawn = bp.Pawn("w", board, (6,i))
            board.add(pawn)
            whites.append(pawn)
            
        #Rooks
        for i in range(0,8,7):
            rook = bp.Rook("b", board, (0,i))
            board.add(rook)
            blacks.append(rook)
        for i in range(0,8,7):
            rook = bp.Rook("w", board, (7,i))
            board.add(rook)
            whites.append(rook)
            
        #Knights
        for i in range(1,7,5):
            knight = bp.Knight("b", board, (0,i))
            board.add(knight)
            blacks.append(knight)
        for i in range(1,7,5):
            knight = bp.Knight("w", board, (7,i))
            board.add(knight)
            whites.append(knight)
            
        #Bishop
        for i in range(2,7, 3):
            bishop = bp.Bishop("b", board, (0,i))
            board.add(bishop)
            blacks.append(bishop)
        for i in range(2,7, 3):
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
        
def input_checker(move):
    print("idk what this function is please just let me push already")
    
def move_input():
    
    move = input("what is your move?")
    first_coord = (0,0)
    second_coord = (0,0)
    
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
            
            first_coord = (int(move[1]),switcher.get(move[0]))
            second_coord = (int(move[4]),switcher.get(move[3]))
            
            return [first_coord,second_coord]
        
        except(AssertionError):
            print("There was an error, please try again")
            move = input("What is your move?")
            continue
    
def main():
    Game.run()

if __name__ == "__main__":
    main()
        
        
# print(str(input_checker("A7:F3")))

