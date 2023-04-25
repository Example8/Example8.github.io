name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go left or right? ").lower()

if answer == "left": # 1 
    answer = input("You come to a river you can walk around it or you can swim across it. Type (walk/swim)").lower()

if answer == "swim": #1.2
    print("You attempted to swim across but you were eaten by an alligator. Game over!")
    exit()
if answer == "walk": #1.3
    print("You have wandered off a cliff and died.Game over.")
    exit()
    
if answer == "right": # 2-Continue
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back? (cross/back) ").lower()

    if answer == "back":
        print("You go back to the main road. Do you want to walk down the Road? (yes/no) ").lower()

    if answer == "yes":
        print("You walk down the road and and a car drives by. Do you hitchhike? (yes/no) ").lower()

    if answer == "yes":
        print("A couple cars go by and no one picks you up. It starts to snow and it becomes dark.Do you sleep or keep walking? (sleep/walk)").lower()

    if answer == "sleep":
        print("You fall asleep and pass away from hypothermia. Game over ")
        exit()
    if answer == "walk":
        print("You start walking for a couple miles and no cars come by. Suddenly a car comes swerving down the road with no lights on and smacks you with there car, and keeps driving. You are dead Game Over!")
        exit()
    if answer == "cross":
        print("You have crosssed the riggity bridge and made it to the other side. You see a lights down a ways do you go to civilazation or follow the river more downstream? (follow/downstream)").lower()
        
    if answer == "downstream":
        print("You follow the stream for a couple miles. You run into a mountain lion and it eats you. Game over")
        exit()
    if answer == "follow":
        print("You have followed the lights and have found Civilazation! Congratulation you have won the game.")
        exit()

else:
    print('Not a valid option. You lose.')
