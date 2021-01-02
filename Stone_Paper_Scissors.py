import random
tie=0
tries=0
score_ur=0
score_comp=0
user_ins=""
array_names=["stone","paper","scissor"]
print(array_names)
start_input=input("Do you want to start the game?\n")
if start_input=="yes" or start_input=="yup" or start_input=="s":
    score_final = int(input("How many points Do you want to play for?🤔\n"))
    print("Your final score is:",score_final)
while score_ur<=score_final:
 if score_comp!=score_final and score_ur!=score_final:
   # print("test for the if condition")
    random_num = random.randint(0, 2)
    random_ins=array_names[random_num]
   #print(random_ins)
    print("What do you want to prefer Enter numbers")
    print("1-stone")
    print("2-paper")
    user_ins_num=int(input("3-scissor\n"))
    if   (user_ins_num==1):
       user_ins="stone"
    elif (user_ins_num==2):
       user_ins="paper"
    elif (user_ins_num==3):
       user_ins="scissor"
    else:
        print("You have to enter a vaild number between 1 to 3 to select the tool you need")

    if random_ins=="stone" and user_ins=="stone":
                    print(random_ins+" vs "+user_ins)
                    print("It is a tie! Try again")
                    print("Your score 👇🏻")
                    print(score_ur)
                    print("Computer score 👇🏻")
                    print(score_comp)
                    tie+=1
                    tries+=1
    elif random_ins=="stone" and user_ins=="paper":
            print(random_ins + " vs " + user_ins)
            score_ur+=1
            print("Good!!!")
            print("Your score 👇🏻")
            print(score_ur)
            print("Computer score 👇🏻")
            print(score_comp)
            tries+=1
    elif random_ins=="stone" and user_ins=="scissor":
            print(random_ins + " vs " + user_ins)
            score_comp+=1
            print("Oops!!!")
            print("Your score 👇🏻")
            print(score_ur)
            print("Computer score 👇🏻")
            print(score_comp)
            tries+=1
    elif random_ins=="paper" and user_ins=="paper":
            print(random_ins+" vs "+user_ins)
            print("It is a tie! Try again")
            print("Your score 👇🏻")
            print(score_ur)
            print("Computer score 👇🏻")
            print(score_comp)
            tie += 1
            tries += 17
    elif random_ins=="paper" and user_ins=="scissor":
            print(random_ins + " vs " + user_ins)
            score_ur += 1
            print("Good!!!")
            print("Your score 👇🏻")
            print(score_ur)
            print("Computer score 👇🏻")
            print(score_comp)
            tries += 1
    elif random_ins=="paper" and user_ins=="stone":
            print(random_ins + " vs " + user_ins)
            score_comp += 1
            print("Oops!!!")
            print("Your score 👇🏻")
            print(score_ur)
            print("Computer score 👇🏻")
            print(score_comp)
            tries += 1
    elif random_ins=="scissor" and user_ins=="scissor":
            print(random_ins + " vs " + user_ins)
            print("It is a tie! Try again")
            print("Your score 👇🏻")
            print(score_ur)
            print("Computer score 👇🏻")
            print(score_comp)
            tie += 1
            tries += 17
    elif random_ins=="scissor" and user_ins=="paper":
            print(random_ins + " vs " + user_ins)
            score_comp += 1
            print("Oops!!!")
            print("Your score 👇🏻")
            print(score_ur)
            print("Computer score 👇🏻")
            print(score_comp)
            tries += 1
    elif random_ins=="scissor" and user_ins=="stone":
            print(random_ins + " vs " + user_ins)
            score_ur += 1
            print("Good!!!")
            print("Your score 👇🏻")
            print(score_ur)
            print("Computer score 👇🏻")
            print(score_comp)
            tries += 1
    else:
            print("I am sorry!")
            print("Some thing is wrong")
#else:
   #print("Ok Bye!! See you later")
    #print(user_ins)
 elif score_ur==score_final:
     print("You have won the match 😃")
     #print("You have taken ", end=" ")
     #print(tries, end=" ")


     break
 else:
     print("Computer has won the match 😰😥")
     break
