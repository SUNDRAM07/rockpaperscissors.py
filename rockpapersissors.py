import random
user_wins=0
comp_wins=0

user_name=input("ENTER YOUR NAME PLAYER: ")   

while True:
    choices=["rock","paper","scissors"]
    user_input=input("CHOOSE /ROCK/PAPER/SCISSORS or Q to quit ").lower()
       
    if user_input=="q":
        print(user_name+" you quit at final score "+str(user_wins)+" and a computer score of "+str(comp_wins) )
        break
    if user_input not in ["rock","paper","scissors"]:
        print("invalid choice bitch..")            
        continue
    else:
        random_choice=random.randrange(0,3)    
        #1:rock 2:paper 3:scissors
        if user_input==choices[random_choice]:
            print("Computer chose:",choices[random_choice])
            print("man its a tie a 1/3 chance..")
        elif random_choice == 0:
            if user_input== "paper":
                print("Computer chose:",choices[random_choice])
                user_wins += 1
                print("You lucky son of a bitch")
            else:
                comp_wins +=1
                print("Computer chose:",choices[random_choice])
                print("Dont lose hope man")
        elif random_choice == 1:
            if user_input == "scissors":
                print("Computer chose:",choices[random_choice])
                user_wins +=1
                print("You lucky son of a bitch")
            else:
                comp_wins +=1
                print("Computer chose:",choices[random_choice])
                print("Dont lose hope man")
        elif random_choice == 2:
            if user_input =="rock":
                print("Computer chose:",choices[random_choice])
                user_wins +=1
                print("You lucky son of a bitch")
            else:
                comp_wins +=1
                print("Computer chose:",choices[random_choice])
                print("Dont lose hope man")
print("Goodbye!!")