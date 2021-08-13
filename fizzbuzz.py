#Write a program that prints integers from 1 to 100.For multiples of 3 print "Fizz",for multiples of 5 print "Buzz",For multiples of both 3 and 5 print "FizzBuzz".

for num in range(1,101):
 if num%3==0 and num%5==0:
  print(num,":FizzBuzz")
 if num % 3 == 0:
  print(num,":Fizz")
 elif num % 5 == 0:
  print(num,":Buzz")