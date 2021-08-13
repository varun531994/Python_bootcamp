#Write a function to print out the number of prime numbers that exist upto and including the given number:
#0 and 1 are not considered prime

def count_primes2(num):
    primes = [2]
    x = 3
    if num < 2:
        return 0
    while x <= num:
        for y in primes:  
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)
    

x = int(input('Enter the number:'))

if x > 0:
 print(count_primes2(x))
else:
 print('ERROR')