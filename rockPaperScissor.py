import random
user_choice=int(input("entre your choice: Type 0 for Rock,1 for Paper,2 for Scissors ."))
computer_choice=random.randint(0,2)
print("computer chose:")
print(computer_choice)
if user_choice >2:
    print("please enter valid choice")

elif computer_choice==user_choice:
    print("it is draw.")
elif computer_choice>user_choice:
    print("you lose.")
elif user_choice>computer_choice:
    print("you win.")
elif computer_choice==0 and user_choice==2:
    print("you lose:")
elif user_choice==0 and computer_choice==2:
    print("you win.")
