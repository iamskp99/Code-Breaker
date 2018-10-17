#We will be importing random func to generate_code
import random
#Get guess

def get_guess():

    return list(input("What is your guess? : "))


#Generate computer CODE

def generate_code():

    digits = [str(num) for num in range(10)]

    random.shuffle(digits)
    return digits[:3]

y = generate_code()

#Generating the clues

def generate_clues(code,user_guess):
    if user_guess == code:
        return "CODE CRACKED"

    clues = []
    for ind,num in enumerate(user_guess):
         if num == code[ind]:
             clues.append("Match")

         elif num in code :
             close.append("Close")

    if clues == []:
       return ["Nope"]

    else:
       return clues

#Game logic

print("Welcome Code Breaker")

secret_code = generate_code()

clue_report = []

while clue_report != "CODE CRACKED!":

    guess = get_guess()

    clue_report = generate_clues(guess,secret_code)

    print("Here is the result of your guess : ")
    for clue in clue_report:

       print(clue)
