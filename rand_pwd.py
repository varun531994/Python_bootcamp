import random
import string


length = int(input("Enter the length of the password:"))

all = string.ascii_letters + string.digits + string.punctuation
pass = "".join(random.sample(all,length))

print(password)