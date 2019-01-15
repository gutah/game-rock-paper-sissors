'''
Author: Gustavo Maciel
E-mail: g-maciel@outlook.com
Description: Python study through Rock, paper and scissor game.

'''

#Perguntar os dados de dois usuários
#Usar while
#Rock, Paper, Scissors
#rand.int(1,3)

def compare(u1, u2):
    
    if u1 == u2:
        print("It's a Tie!")
    
    elif u1 == "paper" or 2:
        if u2 == "Scissors" or 3:
            print("Sissor Win!")
        else:
            print("Paper Win!")
    
    elif u1 == "rock" or 1:
        if u2 == "Scissor" or 3:
            print("Scissor Win!")
        else:
            else("Paper win!")
    
    elif u1 == "scissor" or 3:
        if u2 == "paper" or 2:
            print("Paper win!")
        else:
            print("Rock win!")
    

player_1 = input("Player 1: What's your name?")
player_2 = input("Player 2: What's your name?")

while True:
    u1 = input('Choose:\n 1->Rock\n 2->Paper\n 3->Scissors').lower()
    u2 = input('Choose:\n 1->Rock\n 2->Paper\n 3->Scissors').lower()
    compare(u1, u2)