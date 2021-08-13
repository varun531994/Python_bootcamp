#For integer n,return True if n is 10 within either 100 or 200:

def almost_there(n):
 
 return (abs(100 - n) <= 10) or (abs(200 - n) < = 10)
  

n = int(input("Enter value of n:"))
if n > 0:
  print(almost_there(n))