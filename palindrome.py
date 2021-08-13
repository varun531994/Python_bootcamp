#Write a program in Python to check if a sequence is a Palindrome.

a = input('Enter a sequence:')
b = a[::-1]
print(b)
if a == b:
    print('It is a palindrome')
else:
 print('Not a palindrome')