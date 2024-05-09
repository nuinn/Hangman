from time import sleep
sleep(1)

usecret = input("Write your secret word: ")

import os
# The screen clear function
def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')
# now call function we defined above
sleep(1)
screen_clear()

seclen = len(usecret)
secret = usecret.lower()
print("The secret word is",seclen,"characters long.\n")
s = " "
for char in secret:
    s = s + " " + "_"
print(s)
dashlen = len(s)
#print(dashlen)



print("\n")
sleep(2)

while True:
    ulives = input("Between 1 and 12, choose how many lives you'd like: ")
    try:
        lives = int(ulives)
        if lives > 0 and lives < 13:
            break
        else:
            print("Please enter a valid number.")
            continue
    except:
        print("Please enter a valid number.")
        continue

if lives == 1:
    adj = "insane!"
elif lives < 4:
    adj = "bloody risky!"
elif lives < 7:
    adj = "pretty daring!"
elif lives < 9:
    adj = "quite brave."
elif lives < 11:
    adj = "reasonable."
else:
    adj = "pretty pathetic!"
sleep(1)
print("\n")
if lives == 1:
    print("Just one life!! You must be",adj)
else:
    print(lives,"lives! That's",adj)
print("\n")
sleep(2)
wrong = list()
while True:
    uguess = input("Try a letter or guess the secret word: \n")
    guess = uguess.lower()
    if guess == secret:
        sleep(1)
        print("Congratulations!\n")
        sleep(1)
        print("You guessed",usecret,"correctly!\n")
        sleep(1)
        print("You win!\n")
        sleep(1)
        break
    if guess in wrong:
        print("You've already guessed", guess,"silly! Try something else!")
        continue
    gueslen = len(guess)
    if gueslen > 1:
        lives = lives - 1
        wrong.append(guess)
        wrong.sort()
        sleep(1)
        print("Sorry, but that's not the secret word.\n")
        sleep(1)
        if lives == 0:
            print("You're out of lives, sucker! You lose!\n")
            sleep(1)
            print("The secret word was:",usecret,"\n")
            sleep(1)
            print("Considering the amount of lives you had, that was",adj,"\n")
            sleep(1)
            break
        elif lives == 1:
            sleep(1)
            print("You only have one life left. Tread carefully!\n")
        else:
            sleep(1)
            print("You have",lives,"lives remaining.\n")
        sleep(1)
        print(s,"\n")
        print("Incorrect guesses:",wrong,"\n")
        continue
    indpos = secret.find(guess)
    if indpos < 0:
        lives = lives - 1
        wrong.append(guess)
        wrong.sort()
        sleep(1)
        print("Sorry, but",guess,"isn't in the secret word. Try again.\n")

        if lives == 0:
            sleep(1)
            print("You're out of lives, sucker! You lose!\n")
            sleep(1)
            print("The secret word was:",usecret,"\n")
            sleep(1)
            print("Considering the amount of lives you had, that was",adj,"\n")
            sleep(1)
            break
        elif lives == 1:
            sleep(1)
            print("You only have one life left. Tread carefully!\n")
        else:
            sleep(1)
            print("You have",lives,"lives remaining.\n")
        sleep(1)
        print(s,"\n")
        print("Incorrect guesses:",wrong,"\n")
        continue
    while indpos >= 0:
        sleep(1)
        pos = indpos + 1
        print("Yes,",guess,"is in the secret word!\n")
        double = pos * 2
        fro = double + 1
        minus = pos - 1
        data = secret[minus]

        reveal = s.replace("_",data)
        hash = s[double]

        s = s[:double] + data + s[fro:]
        sleep(1)
        print(s,"\n")
        print("Incorrect letters:",wrong,"\n")
#uchoice = input("Which number letter would you like to reveal? ")
#choice = int(uchoice)
#double = choice * 2
#fro = double + 1
#minus = choice - 1
#data = secret[minus]
#print(data)
#reveal = s.replace("_",data)
#hash = s[double]
#print(hash,"=",data)
#s = s[:double] + data + s[fro:]
#print(s)

        indpos = secret.find(guess,pos)
        continue
quit()







#spellsec = [secret[0],secret[1],secret[2],secret[3],secret[4],secret[5],secret[6],secret[7],secret[8],secret[9]]
#for character in spellsec:
    #print(character)

#while True:
#    guess = input("Guess the secret word: ")
#    gueslen = len(guess)
#    if guess == secret:
#        break
#    if gueslen != seclen:
#        print("Your guess is not the same length as the secret word! Try again...")
#        continue

#print("You guessed it! The secret word was:", secret)





#while True:
  #line = input('Guess my name: ')
  #if line == 'Marc' :
    #  break
  #if line[0] == 'M' :
    #  print("the first letter's right")
  #if line[1] == 'a' :
    #  print("the second letter's right")
  #if line[2] == 'r' :
    #  print("the third letter's right")
  #if line[3] == 'c' :
    #  print("the fourth letter's right")
  #continue
  #else:
    # print("That's not right at all, try again...")
#print("That's it, well done!")
