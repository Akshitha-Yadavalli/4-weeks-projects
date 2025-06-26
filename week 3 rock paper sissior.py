import random
user_wins=0
computer_wins=0
options=["rock","paper","scissors"]

while True:
    user_input=input("type rock/paper/scissors or Q to quit:").lower()
    if user_input=="q":
        break
    if user_input not in ["rock","paper","scissors"]:
        continue
    random_number=random.randint(0,2)
    computer_pick=options[random_number]
    print("Computer picked", computer_pick+".")
    if user_input=="rock"or computer_pick=="scissors":
        print("You won!")
        user_wins+=1
      
    elif user_input=="paper"or computer_pick=="rock":
        print("You won!")
        user_wins+=1
       
    elif user_input=="scissors"or computer_pick=="paper":
        print("You won!")
        user_wins+=1
    else:
        print("you lost!")
        computer_wins+=1
print("you won",user_wins,"times.")
print("the computer won",computer_wins,"times.")
       
    
print("Goodbye!")
