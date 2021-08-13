#Prime numbers:

x = int(input("Enter the number:"))


if x % 2 == 0 or x % 3 == 0 or x % 5 == 0 or x % 7 == 0:
 print('Its not a Prime number!!')
 
else:
  print(f'{x} is a prime number!')
  