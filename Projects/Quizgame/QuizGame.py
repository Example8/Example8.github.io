print("Welcome to my Computer Quiz!")

playing = input("Do you want to play? ")
score = 0

if playing.lower() != "yes":
    quit()

print ("Okay! Let's play :)")

answer = input("What does Cpu stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("incorrect!")

answer = input("What does Gpu stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("incorrect!")
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print("incorrect!")
answer = input("What does Psu stand for? ")
if answer.lower() == "power supply":
    print('Correct!')
    score += 1
else:
    print("incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")