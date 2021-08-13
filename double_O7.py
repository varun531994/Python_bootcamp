def spy_game(nums):

    code = [0,0,7,'x']
    
    for num in nums:
        if num == code[0]:
            code.pop(0)   # code.remove(num) also works
       
    return len(code) == 1
    

x = input("Is there a spy among us?.Want to find out?yes/no:")

if x.lower() == 'yes':
 print(spy_game(nums)
else:
 pass