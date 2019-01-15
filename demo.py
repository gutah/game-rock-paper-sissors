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
        return "It's a Tie!"
    
    elif u1 == "paper":
        if u2 == "Scissors"
            print("Sissor Win!")
        else:
            print("Paper Win!")
    
    elif u1 == "rock":
        if u2 == "Scissor"
            print("Scissor Win!")
        else:
            else("Paper win!")
    
    elif u1 == "scissor":
        if u2 == "paper":
            print("Paper win!")
        else:
            print("Rock win!")
    

player_1 = input("What's your name?")
player_2 = "Computer"

while True:
    u1 = input('Choose:\n 1)Rock\n 2)Paper\n 3)Scissors').lower()
    u2 = input('Choose:\n 1)Rock\n 2)Paper\n 3)Scissors').lower()
    compare(u1, u2)