# -*- coding: utf-8 -*-
"""

"""
class Board(object):
    '''
    Creates board of None objects with default size of 8
    '''
    def __init__(self, size=8):
        self.board = [[None for _ in range(size)] for _ in range(size)]
        
    def show_board(self):
        #need a cleaner way to print
        for row in self.board:
            print(row)
            
    def change(self, y, x, item):
        self.board[y][x] = item
        
chess_board = Board()

chess_board.change(4, 0, 5)
chess_board.change(7, 7, 28)
chess_board.show_board()


class Piece(object):
    
    def __init__(self, color):
        self.pieceValue = 0.0
        self.color = color
        
        
        
"""
Pawn:
    
    
Rook:
    
    
    
Bishop:
    
    
    
Knight:
    
    
    
King:
    
    
    
Queen:
    
    
"""
    