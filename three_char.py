#For a string,return a string where for every charachter in the orignal string there are three charachters.

def char_3(text):
 result = ''
 for char in text:
  result += char*3
 return result
 
  
   
  

x = input('Enter your string:')
a = input("Enter yes/no:")
if a.lower() == 'yes':
 print(char_3(x))
else:
 print('Incorrect!')