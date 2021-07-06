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
    pieceValue = 0.0
    name = "Default"
    
    def __init__(self, color, index = (0,0)):
        self.color = color
        self.index = index
        
    def allowed_moves(self):
        self.index = (0,0)
        
    def get_value(self):
        return self.pieceValue
        
    def get_index(self):
        return self.index
    
    def set_index(self, index):
        self.index = index
        
    def __str__(self):
        return self.name + ":" + "Color: " + self.color + " Location " + self.index + " Value: " + self.pieceValue
        
        
class Pawn(Piece):
    pieceValue = 1
    name = "Pawn"
    
    def __init__(self, color, index):
        Piece.__init__(color, index)
        
thing = Pawn("white", (1,2))
print(thing)
        
   
""" 
Rook:
    
    
    
Bishop:
    
    
    
Knight:
    
    
    
King:
    
    
    
Queen:
    
    
"""
    