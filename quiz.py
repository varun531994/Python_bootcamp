print("Welcome to the QUIZ!!!!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay let's Play !!!!! :-}")

score = 0

answer = input("What does CPU stand for? ")

if answer.lower() == "central processing unit":
    print("That's Right!!")
    score += 1
else:
    print("Incorrect :{")

answer = input("What does GPU stand for? ")

if answer.lower() == "graphics processing unit":
    print("That's Right!!")
    score += 1
else:
    print("Incorrect :{")


answer = input("What does RAM stand for? ")

if answer.lower() == "random access memory":
    print("That's Right!!")
    score += 1
else:
    print("Incorrect :{")


print("You got " +str(score) + " questions correct")
print("You got" ,score,"right!")
print("You got {0} questions right".format(score))
print(f'You got {score} questions correct!!')