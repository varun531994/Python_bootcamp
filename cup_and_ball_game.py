from random import shuffle
def shuffle_list(my_list):

    shuffle(my_list)
    return my_list
    





def player_guess():
    
    guess = ''
    
    while guess not in ['0','1','2']:
        guess = input('Pick a number:0/1/2:-')
        
    return int(guess)
    
    



def check_guess(new_list,guess):
    if new_list[guess] == 'O':
        print("Got It!!!")
        print(new_list)
    else:
        print('WRONG!!')
        print(new_list)
        



new_list = ['','O','']

mixed_list = shuffle_list(new_list)

guess = player_guess()

check_guess(mixed_list,guess)

