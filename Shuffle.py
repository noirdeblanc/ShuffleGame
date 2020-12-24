# from random import the shuffle function
from random import shuffle

# fuction defined to take in players input
def Player_input():
    player_guess = ''
    while player_guess not in [0,1,2]:
         player_guess = int(input('Guess the location between 0 and 2'))
    return player_guess

# function defined to to shuffle the mylist 
def shuffle_list(mylist):
    shuffle(mylist)
    return mylist
    
''' A little bit of 
                    social distancing '''

# function to verify if  user input matches the shuffled list
def check_input(mylist, selected_number):
    if mylist[selected_number] == 'O':
        print('correct')
    else:
        print('wrong')
        print(mylist)


#Initial List
mylist =['','O','']
#Shuffled List
result = shuffle_list(mylist)
#Player Guess
selected_number = Player_input()
#Player Verification
check_input(result,selected_number)


