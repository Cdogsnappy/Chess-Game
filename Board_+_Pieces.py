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
    piece_value = 0.0
    name = "Default"
    possible_moves = []
    
    def __init__(self, color, board, index = (0,0)):
        self.color = color
        self.index = index
        self.board = board
        
    def allowed_moves(self):
        return self.possible_moves
        
    def get_value(self):
        return self.piece_value
        
    def get_index(self):
        return self.index
    
    def set_index(self, index):
        self.index = index
        
    def get_color(self):
        return self.color
        
    def __str__(self):
        return self.name + ": " + "Color:" + self.color + " Location" + str(self.index) + " Value:" + str(self.piece_value)
        
        
class Pawn(Piece):
    is_first_move = True
    piece_value = 1
    name = "Pawn"
    
    def __init__(self, color, index):
        Piece.__init__(self, color, index)
        
    def allowed_moves(self):
        y = self.index[0]
        x = self.index[1]
        temp_list= []

        if(self.is_first_move):
             if(self.color == "w"):
                 temp_list.append((y+2,x))
             if(self.color == "b"):
                 temp_list.append((y-2,x))
             self.is_first_move = False
        if(self.color == "w"):
            if(y != 0):
                temp_list.append((y+1,x))
                if(x != 0):
                    if(self.board[y-1][x-1] != None and self.board[y-1][x-1].get_color() == "b"):
                        temp_list.append((y+1,x-1))
                if(x != 7):
                    if(self.board[y-1][x-1] != None and self.board[y-1][x-1].get_color() == "b"):
                        temp_list.append((y+1,x+1))         
        if(self.color == "b"):
            if(y != 7):
                temp_list.append((y-1,x))
                if(x != 0):
                    if(self.board[y-1][x-1] != None and self.board[y-1][x-1].get_color() == "w"):
                        temp_list.append((y-1,x-1))
                if(x != 7):
                    if(self.board[y-1][x-1] != None and self.board[y-1][x-1].get_color() == "w"):
                        temp_list.append((y-1,x+1))     
            

        
thing = Pawn("white", (1,2))
print(thing)
        
   
""" 
Rook:
    
    
    
Bishop:
    
    
    
Knight:
    
    
    
King:
    
    
    
Queen:
    
    
"""
    