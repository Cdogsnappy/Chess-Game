# -*- coding: utf-8 -*-
"""

"""
class Board(object):
    '''
    Creates board of None objects with default size of 8
    '''
    def __init__(self, size=8):
        self.board = [[None for _ in range(size)] for _ in range(size)]
        self.size = size
        
    def show(self):
        print(end="   ")
        for i in range(65, 65+self.size):
            print("{:^10}".format(chr(i)), end="")
        print()
        num = 8
        for row in self.board:
            print(str(num) + " |", end="")           #COLOR
            num-=1
            for item in row:
                if(item == None):
                    item = "-----"
                if(type(item) != str and type(item) != int and item.get_color() == "w"):
                    print('\033[38m' , end="")
                if(type(item) != str and type(item) != int and item.get_color() == "b"):
                    print('\033[35m' , end="")
                print("{:^9}".format(str(item)), end="")
                print('\033[m|', end="")
            print()
    
    def add(self, item, index=(-1,-1)):
        '''
        If the item is not a piece, must include index
        '''
        try: 
            self.board[item.get_index()[0]][item.get_index()[1]] = item
        except:
            self.board[index[0]][index[1]] = item
            
    
    def change(self, item, index):
        self.board[item.get_index()[0]][item.get_index()[1]] = None
        self.board[index[0]][index[1]] = item
        
    def remove(self, item):
        self.board[item.get_index()[0]][item.get_index()[1]] = None
        
    def nuke(self):
        for y in range(self.size):
            for x in range(self.size):
                self.board[y][x] = None
            
    def get_board(self):
        return self.board


class Piece(object):
    piece_value = 0.0
    name = "Default"
    possible_moves = []
    
    def __init__(self, color, board, index):
        """
        color: string "b" or "w"
        board: board object that it is operating on
        index : tuple (y,x)
        """
        self.color = color
        self.index = index
        self.board = board
        
    def allowed_moves(self):
        return self.possible_moves
    
    def get_name(self):
        return self.name
        
    def get_value(self):
        return self.piece_value
        
    def get_index(self):
        return self.index
    
    def set_index(self, index):
        self.index = index
        
    def get_color(self):
        return self.color
        
    def __str__(self):
        return self.name

        
class Pawn(Piece):
    piece_value = 1
    name = "Pawn"
    
    def __init__(self, color, board, index):
        Piece.__init__(self, color, board, index)
        self.is_first_move = True
        
    def allowed_moves(self):
        y = self.index[0]
        x = self.index[1]
        temp_list= []

        if(self.is_first_move):
             if(self.color == "w"):
                 temp_list.append((y-2,x))
             if(self.color == "b"):
                 temp_list.append((y+2,x))
        if(self.color == "w"):
            if(y != 0):
                temp_list.append((y-1,x))
                if(x != 0):
                    if(self.board.get_board()[y-1][x-1] != None and self.board.get_board()[y-1][x-1].get_color() == "b"):
                        temp_list.append((y-1,x-1))
                if(x != 7):
                    if(self.board.get_board()[y-1][x+1] != None and self.board.get_board()[y-1][x+1].get_color() == "b"):
                        temp_list.append((y-1,x+1))         
        if(self.color == "b"):
            if(y != 7):
                temp_list.append((y+1,x))
                if(x != 0):
                    if(self.board.get_board()[y+1][x-1] != None and self.board.get_board()[y+1][x-1].get_color() == "w"):
                        temp_list.append((y+1,x-1))
                if(x != 7):
                    if(self.board.get_board()[y+1][x+1] != None and self.board.get_board()[y+1][x+1].get_color() == "w"):
                        temp_list.append((y+1,x+1))  
        return temp_list
    
    def set_first_move(self):
        self.is_first_move = False


class Rook(Piece):
    piece_value = 5
    name = "Rook"

    def __init__(self,color,board,index):
        Piece.__init__(self,color, board, index)
        
    def allowed_moves(self):
        y = self.index[0]
        x = self.index[1]
        j = 0
        temp_list = []
        
        while x-j>0:
            j+=1
            if(self.board.get_board()[y][x-j] != None):
                if(self.board.get_board()[y][x-j].get_color() != self.color):
                    temp_list.append((y,x-j))
                break
            temp_list.append((y,x-j))
        j=0
        
        while x+j<7:
            j+=1
            if(self.board.get_board()[y][x+j] != None):
                if(self.board.get_board()[y][x+j].get_color() != self.color):
                    temp_list.append((y,x+j))
                break
            temp_list.append((y,x+j))
            
        j=0
            
        while y-j>0:
            j+=1
            if(self.board.get_board()[y-j][x] != None):
                if(self.board.get_board()[y-j][x].get_color() != self.color):
                    temp_list.append((y-j,x))
                break
            temp_list.append((y-j,x))
            
        j=0
            
        while y+j<7:
            j+=1
            if(self.board.get_board()[y+j][x] != None):
                if(self.board.get_board()[y+j][x].get_color() != self.color):
                    temp_list.append((y+j,x))
                break
            temp_list.append((y+j,x))
        
            
        return temp_list
            
            
class Bishop(Piece):
    piece_value = 3
    name = "Bishop"
    
    def __init__(self,color, board, index):
        Piece.__init__(self,color, board, index)
        
    def allowed_moves(self):
        y = self.index[0]
        x = self.index[1]
        j = 0
        temp_list = []
        
        #Up and right
        while(y-j>0 and x+j<7):
            j+=1
            if(self.board.get_board()[y-j][x+j] != None):
                if(self.board.get_board()[y-j][x+j].get_color() != self.color):
                    temp_list.append((y-j,x+j))
                break
            temp_list.append((y-j,x+j))
            
        j=0
        #Up and left
        while(y-j>0 and x-j>0):
            j+=1
            if(self.board.get_board()[y-j][x-j] != None):
                if(self.board.get_board()[y-j][x-j].get_color() != self.color):
                    temp_list.append((y-j,x-j))
                break
            temp_list.append((y-j,x-j))
            
        j=0
        #Down and left
        while(y+j<7 and x-j>0):
            j+=1
            if(self.board.get_board()[y+j][x-j] != None):
                if(self.board.get_board()[y+j][x-j].get_color() != self.color):
                    temp_list.append((y+j,x-j))
                break
            temp_list.append((y+j,x-j))
            
        j=0
        #Down and right
        while(y+j<7 and x+j<7):
            j+=1
            if(self.board.get_board()[y+j][x+j] != None):
                if(self.board.get_board()[y+j][x+j].get_color() != self.color):
                    temp_list.append((y+j,x+j))
                break
            temp_list.append((y+j,x+j))
      
                
        return temp_list
    
    
class Queen(Piece):
    name = "Queen"
    piece_value = 9
    
    def __init__(self,color,board,index):
        Piece.__init__(self,color,board,index)
        
    def allowed_moves(self):
        y = self.index[0]
        x = self.index[1]
        j = 0
        temp_list = []
        
        #Up and right
        while(y-j>0 and x+j<7):
            j+=1
            if(self.board.get_board()[y-j][x+j] != None):
                if(self.board.get_board()[y-j][x+j].get_color() != self.color):
                    temp_list.append((y-j,x+j))
                break
            temp_list.append((y-j,x+j))
            
        j=0
        #Up and left
        while(y-j>0 and x-j>0):
            j+=1
            if(self.board.get_board()[y-j][x-j] != None):
                if(self.board.get_board()[y-j][x-j].get_color() != self.color):
                    temp_list.append((y-j,x-j))
                break
            temp_list.append((y-j,x-j))
            
        j=0
        #Down and left
        while(y+j<7 and x-j>0):
            j+=1
            if(self.board.get_board()[y+j][x-j] != None):
                if(self.board.get_board()[y+j][x-j].get_color() != self.color):
                    temp_list.append((y+j,x-j))
                break
            temp_list.append((y+j,x-j))
            
        j=0
        #Down and right
        while(y+j<7 and x+j<7):
            j+=1
            if(self.board.get_board()[y+j][x+j] != None):
                if(self.board.get_board()[y+j][x+j].get_color() != self.color):
                    temp_list.append((y+j,x+j))
                break
            temp_list.append((y+j,x+j))
            
        j = 0
            
        while x-j>0:
            j+=1
            if(self.board.get_board()[y][x-j] != None):
                if(self.board.get_board()[y][x-j].get_color() != self.color):
                    temp_list.append((y,x-j))
                break
            temp_list.append((y,x-j))
        j=0
        
        while x+j<7:
            j+=1
            if(self.board.get_board()[y][x+j] != None):
                if(self.board.get_board()[y][x+j].get_color() != self.color):
                    temp_list.append((y,x+j))
                break
            temp_list.append((y,x+j))
            
        j=0
            
        while y-j>0:
            j+=1
            if(self.board.get_board()[y-j][x] != None):
                if(self.board.get_board()[y-j][x].get_color() != self.color):
                    temp_list.append((y-j,x))
                break
            temp_list.append((y-j,x))
            
        j=0
            
        while y+j<7:
            j+=1
            if(self.board.get_board()[y+j][x] != None):
                if(self.board.get_board()[y+j][x].get_color() != self.color):
                    temp_list.append((y+j,x))
                break
            temp_list.append((y+j,x))
        
        return temp_list
    
    
    
class Knight(Piece):
    name = "Knight"
    piece_value = 3
    
    def __init__(self, color, board, index):
        Piece.__init__(self, color,board,index)
        
    def allowed_moves(self):
        y = self.index[0]
        x = self.index[1]
        temp_list = []
        
        if(x+2<8 and y+1<8):
            if(self.board.get_board()[y+1][x+2] == None):
                temp_list.append((y+1,x+2))
            elif(self.board.get_board()[y+1][x+2].get_color() != self.color):
                    temp_list.append((y+1,x+2))
                
            
        if(x+1<8 and y+2<8):
            if(self.board.get_board()[y+2][x+1] == None):
                temp_list.append((y+2,x+1))
            elif(self.board.get_board()[y+2][x+1].get_color() != self.color):
                temp_list.append((y+2,x+1))
                
            
        if(x+2<8 and y-1>-1):
            if(self.board.get_board()[y-1][x+2] == None):
                temp_list.append((y-1,x+2))
            elif(self.board.get_board()[y-1][x+2].get_color() != self.color):
                temp_list.append((y-1,x+2))
                
            
        if(x-2>-1 and y-1>-1):
            if(self.board.get_board()[y-1][x-2] == None):
                temp_list.append((y-1,x-2))
            elif(self.board.get_board()[y-1][x-2].get_color() != self.color):
                temp_list.append((y-1,x-2))
            
        if(x-2>-1 and y+1<8):
            if(self.board.get_board()[y+1][x-2] == None):
                temp_list.append((y+1,x-2))
            elif(self.board.get_board()[y+1][x-2].get_color() != self.color):
                temp_list.append((y+1,x-2))
            
        if(x+1<8 and y-2>-1):
            if(self.board.get_board()[y-2][x+1] == None):
                temp_list.append((y-2,x+1))
            elif(self.board.get_board()[y-2][x+1].get_color() != self.color):
                temp_list.append((y-2,x+1))
            
        if(x-1>-1 and y+2<8):
            if(self.board.get_board()[y+2][x-1] == None):
                temp_list.append((y+2,x-1))
            elif(self.board.get_board()[y+2][x-1].get_color() != self.color):
                temp_list.append((y+2,x-1))
            
        if(x-1>-1 and y-2>-1):
            if(self.board.get_board()[y-2][x-1] == None):
                temp_list.append((y-2,x-1))
            elif(self.board.get_board()[y-2][x-1].get_color() != self.color):
                temp_list.append((y-2,x-1))
            
        return temp_list
    
    
class King(Piece):
    name ="King"
    piece_value = 0
    
    def __init__(self,color,board,index):
        Piece.__init__(self,color,board,index)
        
    def allowed_moves(self):
        y = self.index[0]
        x = self.index[1]
        temp_list = []
        
        if(x+1<8 and y+1<8):
            if(self.board.get_board()[y+1][x+1] == None):
                temp_list.append((y+1,x+1))
            elif(self.board.get_board()[y+1][x+1].get_color() != self.color):
                temp_list.append((y+1,x+1))
            
        if(x+1<8):
            if(self.board.get_board()[y][x+1] == None):
                 temp_list.append((y,x+1))
            elif(self.board.get_board()[y][x+1].get_color() != self.color):
                temp_list.append((y,x+1))
            
        if(y+1<8):
            if(self.board.get_board()[y+1][x] == None):
                temp_list.append((y+1,x))
            elif(self.board.get_board()[y+1][x].get_color() != self.color):
                temp_list.append((y+1,x))
            
        if(x-1>-1 and y-1>-1):
            if(self.board.get_board()[y-1][x-1] == None):
                temp_list.append((y-1,x-1))
            elif(self.board.get_board()[y-1][x-1].get_color() != self.color):
                temp_list.append((y-1,x-1))
    
        if(x-1>-1):
            if(self.board.get_board()[y][x-1] == None):
                temp_list.append((y,x-1))
            elif(self.board.get_board()[y][x-1].get_color() != self.color):
                temp_list.append((y,x-1))
            
        if(y-1>-1):
            if(self.board.get_board()[y-1][x] == None):
                temp_list.append((y-1,x))
            elif(self.board.get_board()[y-1][x].get_color() != self.color):
                temp_list.append((y-1,x))
            
        if(x-1>-1 and y+1<8):
            if(self.board.get_board()[y+1][x-1] == None):
                temp_list.append((y+1,x-1))
            elif(self.board.get_board()[y+1][x-1].get_color() != self.color):
                temp_list.append((y+1,x-1))
            
        if(x+1<8 and y-1>-1):
            if(self.board.get_board()[y-1][x+1] == None):
                temp_list.append((y-1,x+1))
            elif(self.board.get_board()[y-1][x+1].get_color() != self.color):
                temp_list.append((y-1,x+1))
            
        return temp_list
        
                

def show_spots(board, piece):
    tempindex = piece.get_index()
    board.add(1, tempindex)
    for space in piece.allowed_moves():
        board.add(0, (space[0],space[1]))
        
chess_board = Board()
# bishop_piece = Bishop("w", chess_board.board, (3,4))
# knight_piece = Knight("w", chess_board.board,(5,5))
# chess_board.change(4, 0, 5)
# chess_board.change(7, 7, 28)
# chess_board.change(5,4, bishop_piece)
# show_spots(chess_board.board, bishop_piece)
# chess_board.show()

# print()
# chess_board.nuke()
# rook_piece = Rook("w", chess_board.board,(7,1))
# show_spots(chess_board.board, rook_piece)
# chess_board.show()

# chess_board.nuke()
# show_spots(chess_board.board, knight_piece)
# chess_board.show()

# thing = Pawn("white", chess_board, (1,2))
# print(thing)

# chess_board.nuke()
# king_piece = King("w", chess_board, (2,4))
# show_spots(chess_board, king_piece)
# chess_board.show()

# thing = Pawn("white", chess_board, (1,2))
# print(thing)

