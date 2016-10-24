#http://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html

import random

def game_one():
	count = 0
	while True:
		userInput = raw_input('Guess the number between 1 and 9: ')
		if userInput == 'exit':
			return False
		
		guessNumber = int(userInput)
		randomNumber = random.randint(1, 9)
		count = (count + 1)
		if guessNumber > randomNumber:
			print ("You are too high. Random number was {0}. Try again".format(randomNumber)) 
			continue
		elif guessNumber < randomNumber:
			print ("You are too low. Random number was {0}. Try again".format(randomNumber))
			continue
		elif guessNumber == randomNumber:
			print ("You win!: ")
			print randomNumber
			print 'Count of guesses you have taken was {0}'.format(randomNumber)
			return False
game_one ()	
