"""Permainan Tradisional Oooosom"""

import random

def play():
        user = input ( "Sila pilih: 'B' for Batu, 'A' for Air, 'C' for Burung\n")
        computer = random.choice (['A','B','C'])
        
        if user == computer:
            return ' Anda seri '

        
        if win(user, computer):
            return ' Tahniah, anda menang ! '

        return ' Anda kalah! '

play( )

def is_win( player, opponent):

        if ( player == 'B' and oppponent == 'C') or ( player == 'A' and opponent == 'B') or ( player == 'c' and opponent == 'B'):
            return True

