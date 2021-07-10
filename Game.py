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
    
def main():
    Game.run()

if __name__ == "__main__":
    main()
