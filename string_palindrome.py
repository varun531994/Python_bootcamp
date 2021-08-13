a = input('Enter your phrase:')
b = a[::-1]

if a == b.lower():
 print("It is a palindrome!")
 
else:
 print("It is not a palindrome!")