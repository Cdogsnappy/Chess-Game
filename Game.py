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

        board.show()
        
def input_checker(move):
    
    first_coord = (0,0)
    second_coord = (0,0)
    
    while(True):
        try:
            assert move[0].isalpha() and move[1].isalnum() and move[3] ==":" and move[4].isalpha() and move[5].isalnum()
            
            switcher={
                "a" or "A" : 0,
                "b" or "B" : 1,
                "c" or "C" : 2,
                "d" or "D" : 3,
                "e" or "E" : 4,
                "f" or "F" : 5,
                "g" or "G" : 6,
                "h" or "H" : 7
                }
            
            first_coord = (int(move[1]),switcher.get(move[0]))
            second_coord = (int(move[4]),switcher.get(move[5]))
            
            return [first_coord,second_coord]
        
        except(AssertionError):
            print("There was an error, please try again")
            continue
    
def main():
    Game.run()

if __name__ == "__main__":
    main()
