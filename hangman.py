import random
import requests                                              # module to take data from api
url="https://random-word-api.herokuapp.com/word?number=1"
response=requests.get(url)
given_word = (response.json()[0])

print(" Lets play Hangman ".center(150,'*'))


while 1:                                                                      #to select toughness
    level=input("level you want to play (e for easy and t for tough):" )

    if level == "e":
        hint=random.choice(given_word)+""+ random.choice(given_word)           #to take 2 hints
    elif level == "t":
        hint=""
    else:
        print("choose correct level before starting game")
        continue
    break
    

for char in given_word:                                                       #iterate
    if char in hint :
        print(char,end=" ")
    else :
    
        print("_",end=" ")


    



guessed = ""+hint                                                        # to store hint
lives = 5
while lives>0:
        guess = input(" enter a letter you gussed: ")
        if  guess in given_word :
           print(guess, "in given word")
        else :
           lives -=1
           print("your letter", guess,"not in given word")
           print("lives left = ", lives)
        guessed = guessed + guess
        wrong_guess = 0
        for char in given_word:
            if char in guessed:
                 print(char , end="")
            else:
                 print("-",end="")
                 
                 wrong_guess += 1
        if wrong_guess == 0: 
            print (" is your word  congratulation  ")
            break
else :
    print("\nbetter luck next time") 
    print (given_word ," is your word ")      
    