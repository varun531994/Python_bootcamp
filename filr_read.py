#Write code that will count the number of capital letters in a file. Your code should work even if the file is too big to fit in memory.

with open("C:/Users/Varun/Desktop/myfile.txt") as fh:
 count = 0
 tx = fh.read() 
for character in tx:
    if character.isupper():
        count += 1
print(count)