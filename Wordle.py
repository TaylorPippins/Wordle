import random
import sys
def getRandomWord():
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        file = open("words.txt", "r")
        words = [word.strip() for word in file.readlines()]
        return random.choice(words)

def printGuessColors(guess, answer):
    for i in range(len(answer)):
        if guess[i]==answer[i]:
            print (guess[i]+" - Green")
        elif guess[i]not in answer:
            print (guess[i]+" - Red")
        else:
            print (guess[i]+" - Yellow")
def main():
    answer = getRandomWord()
    guess=input("Enter a 5 letter guess?\n")
    attempts=1
    while attempts<7:
        if attempts==6:
            printGuessColors(guess,answer)
            print(f'You lost. The answer was {answer}.')
            break
        elif guess==answer:
            printGuessColors(guess,answer)
            print(f'You Won! That took {attempts} guess(es).')
            break
        else:
            attempts+=1
            printGuessColors(guess,answer)
            guess=input("Enter a 5 letter guess?\n")
main()
