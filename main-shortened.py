
import random

'''
1 = snanke

2 = water

3 = gun
'''

computer = random.choice([1, 2, 3])

myChoice = {"s": 1, "w": 2, "g":3}
reversechoice = {1: "Snake", 2: "Water", 3: "gun"}

n = input("Enter your choice: ")

choice = myChoice[n]

print(f"You Chose {reversechoice[choice]} \nComputer chose {reversechoice[computer]}")



# THE BELOW LOGIC IS WRITTEN ON THE BASIS OF (COMPUTER - CHOICE) 

if (computer-choice==-1 or computer-choice == 2):
    print("YOu lose!")

elif(computer == choice):
    print("It's a draw!")

else:
    print("You win! ")




# if(computer == choice):
#     print("It's a draw! ")

# else:
#     if(computer == 1 and choice == 2):
#         print("You lose! ")

#     elif(computer == 1 and choice == 3):
#         print("You win! ")

    
#     elif(computer == 2 and choice == 1):
#         print("You win! ")

    
#     elif(computer == 2 and choice == 3):
#         print("You Lose! ")

    
#     elif(computer == 3 and choice == 1):
#         print("You Lose! ")

    
#     elif(computer == 3 and choice == 2):
#         print("You win! ")



    
    


