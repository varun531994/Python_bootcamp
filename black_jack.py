#Given three integers between 1 and 11.If their sum is less than or equal to 21,return their sum.If their sum exceeds 21 and there is an 11,reduce total sum by 10.Finally even after adjustment the sum exceeds 21,return "BUST".

def blackjack(a,b,c):
    
    if sum((a,b,c)) <= 21:
        return sum((a,b,c))
    elif sum((a,b,c)) <=31 and 11 in (a,b,c):
        return sum((a,b,c)) - 10
    else:
        return 'BUST'
   
  
d = input("Do you want to play blackjack:yes/no")
x = int(input("Enter a:"))
y= int(input("Enter b:"))
z = int(input("Enter c:"))

if d.lower() == 'yes':
 print(blackjack(x,y,z))
else:
 print("Lose it!!")