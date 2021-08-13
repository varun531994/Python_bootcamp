choice = 'wrong'
acceptable_range = range(0,10)

within_range = False


while choice.isdigit() == False or within_range == False:
        choice = input("Please enter a number between (0 - 10): ")
        
        if choice.isdigit() == False:
            print('Please enter a digit!!')
        else:
          pass
            
        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                within_range = False 
         
        else:
          pass        
print(choice)