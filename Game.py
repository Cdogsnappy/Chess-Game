# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 12:20:15 2021

@author: Martin
"""

import BoardPieces

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
        
        
print(str(input_checker("A7:F3")))
                    