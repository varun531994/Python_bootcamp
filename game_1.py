game_list = ['','','']

def display_game(game_list):
    print('Here is the current list: ')
    print(game_list)


def position_choice():

    choice = 'wrong'
    
    
    while choice not in ['0','1','2']:
        
        choice = input("Please enter a number between (0/1/2): ")
        
        if choice not in ['0','1','2']:
            print('Please enter the right digit!!')
            
               
    return int(choice)
    



def replacement_choice(game_list,position):
    user_placement = input("Type a string to place at the position: ")
    
    game_list[position] = user_placement
    
    return game_list
    
    
    
    



def gameon_choice():
    choice = 'wrong'
    
    
    while choice not in ['Y','N']:
        
        choice = input("Keep Playing? (Y or N)")
        
        if choice not in ['Y','N']:
            print("Sorry I don't understand,please choose Y or N")
            
               
    if choice == 'Y':
        print('OKAY')
        return True
    else:
        print('BYE')
        return False




game_on = True
game_list = ['','','']

while game_on:
    display_game(game_list)
    position = position_choice()
    game_list = replacement_choice(game_list,position)
    display_game(game_list)
    game_on = gameon_choice()
    display_game(game_list)