

def display_game(game_list1,game_list2,game_list3):
    
    print('Here is the current list: ')
    print('   |   |')
    print(' ' + game_list1[0] + '  | ' + game_list1[1] + '  | ' + game_list1[2])
    print('   |   |')
    print('===========')
    print('   |   |')
    print(' ' + game_list1[0] + '  | ' + game_list2[1] + '  | ' + game_list2[2])
    print('   |   |')
    print('===========')
    print('   |   |')
    print(' ' + game_list3[0] + '  | ' + game_list3[1] + '  | ' + game_list3[2])
    print('   |   |')


def position_choice():

    choice = 'wrong'
    
    
    while choice not in ['0','1','2']:
        
        choice = input("Please enter a number between (0/1/2): ")
        
        if choice not in ['0','1','2']:
            print('Please enter the right digit!!')
            
               
    return int(choice)

def replacement_choice(game_list1,game_list2,game_list3,position):
    user_placement = input("Type a string to place at the position: ")
    row_number = input("Enter the row in which to place the string(1/2/3): ")
    if row_number == '1':
     game_list1[position] = user_placement
    elif row_number == '2':
     game_list2[position] = user_placement
    elif row_number == '3':
     game_list3[position] = user_placement
    else:
     print("Please enter correct row number")
    
    
    return game_list1
    return game_list2
    return game_list3

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
game_list1 = ['','','']
game_list2 = ['','','']
game_list3 = ['','','']

while game_on:
    display_game(game_list1,game_list2,game_list3)
    position = position_choice()
    game_list = replacement_choice(game_list1,game_list2,game_list3,position)
    display_game(game_list1,game_list2,game_list3)
    game_on = gameon_choice()
    display_game(game_list1,game_list2,game_list3)
    if game_list1[0] == game_list1[1] == game_list1[2] == 'O' or game_list1[0] == game_list1[1] == game_list1[2] == 'X':
     print("You Won!!")
    elif game_list2[0] == game_list2[1] == game_list2[2] == 'O' or game_list2[0] == game_list2[1] == game_list2[2] == 'X':
     print("You Won!!")
    elif game_list3[0] == game_list3[1] == game_list3[2] == 'O' or game_list3[0] == game_list3[1] == game_list3[2] == 'X':
     print("You Won!!")
    elif game_list1[0] == game_list2[0] == game_list3[0] == 'O' or game_list1[0] == game_list2[0] == game_list3[0] == 'X':
     print("You Won!!")
    elif game_list1[1] == game_list2[1] == game_list3[1] == 'O' or game_list1[1] == game_list2[1] == game_list3[1] == 'X':
      print("You Won!!")
    elif game_list1[2] == game_list2[2] == game_list3[2] == 'O' or game_list1[2] == game_list2[2] == game_list3[2] == 'X':
     print("You Won!!")
    elif game_list1[0] == game_list2[1] == game_list3[2] == 'O' or game_list1[0] == game_list2[1] == game_list3[2] == 'X':
     print("You Won!!")
    elif game_list1[2] == game_list2[1] == game_list3[0] == 'O' or game_list1[2] == game_list2[1] == game_list3[0] == 'X':
     print("You Won!!")
    else:
     pass
     
    

