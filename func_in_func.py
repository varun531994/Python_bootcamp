#ame = 'This is a Global String'

def greet():
 name = input('What is your name?:')
 def hello():
  print('Hi '+name)
 hello()
 

x = input('Say hi:')
if x.lower() =='hi':
 print(greet())
else:
 quit