# -*- coding: utf-8 -*-
"""

"""
class Board(list):
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




class Rook(Piece):
    piece_value = 5
    name = "Rook"
    
    def __init(self,color,index):
        Piece.__init__(self,color,index)
        
    def allowed_moves(self):
        y = self.index[0]
        x = self.index[1]
        temp_list = []
        
        for j in range(x-1,0):
            if(self.board[y][j] != None):
                temp_list.append((y,j))
                break
            temp_list.append((y,j))
            
        for j in range(x+1,9):
            if(self.board[y][j] != None):
                temp_list.append((y,j))
                break
            temp_list.append((y,j))
            
        for j in range(y-1,0):
            if(self.board[j][x] != None):
                temp_list.append((j,x))
                break
            temp_list.append((j,x))
            
        for j in range(y+1,9):
            if(self.board[j][j] != None):
                temp_list.append((j,x))
                break
            temp_list.append((j,x))
            
        return temp_list
            
            
            
            
class Bishop(Piece):
    piece_value = 3
    name = "Bishop"
    
    def __init__(self,color,index,board):
        Piece.__init__(self,color,index,board)
        
    def allowed_moves(self):
        y = self.index[0]
        x = self.index[1]
        iy = 8-y
        ix = 8-x
        temp_list = []
        
        
        #up and right
        if(ix<y):
            for j in range(1,ix+1):
                if(self.board[y-j][x+j] != None):
                    temp_list.append((y-j,x+j))
                    break
                temp_list.append((y-j,x+j))
                
        elif(y<ix or y==ix):
            for j in range(1,y+1):
                if(self.board[y-j][x+j] != None):
                    temp_list.append((y-j,x+j))
                    break
                temp_list.append((y-j,x+j))
                
   
                
        #up and left
        if(x<y):
            for j in range(1, x+1):
                if(self.board[y-j][x-j] != None):
                    temp_list.append((y-j,x-j))
                    break
                temp_list.append((y-j,x-j))
                
        elif(y<x or y==x):
            for j in range(1, y+1):
                if(self.board[y-j][x-j] != None):
                    temp_list.append((y-j,x-j))
                    break
                temp_list.append((y-j,x-j))
                

                
                
        #down and right
        if(ix<iy):
            for j in range(1, ix+1):
                if(self.board[y+j][x+j] != None):
                    temp_list.append((y+j,x+j))
                    break
                temp_list.append((y+j,x+j))
                
        elif(iy<ix or iy==ix):
            for j in range(1, iy+1):
                if(self.board[y+j][x+j] != None):
                    temp_list.append(y+j,x+j)
                    break
                temp_list.append(y+j,x+j)
            
                
        #down and left
        if(x<iy):
            for j in range(1,x+1):
                if(self.board[y][x-j] != None):
                    temp_list.append((y+j,x-j))
                    break
                temp_list.append((y+j,x-j))
                
        elif(iy<x or iy==x):
            for j in range(1, iy+1):
                if(self.board[y+j][x-j] != None):
                    temp_list.append((y+j,x-j))
                    break
                temp_list.append((y+j,x-j))
                
      
                
        return temp_list
                
          
        
chess_board = Board()
bishop_piece = Bishop("White",(5,4), chess_board)
chess_board.change(4, 0, 5)
chess_board.change(7, 7, 28)
chess_board.change(5,4, bishop_piece)
chess_board.show_board()
possible_moves = bishop_piece.allowed_moves()


        
        
   
""" 
Rook:
    
    
    
Bishop:
    
    
    
Knight:
    
    
    
King:
    
    
    
Queen:
    
    
"""
    