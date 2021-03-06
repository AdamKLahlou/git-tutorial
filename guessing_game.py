#! /usr/bin/python3
# The random package is needed to choose a random number
import random
# Define the game in a function
def guess_loop():
	i = 0
	print("Type your name")
	user = str(input())
	# This is the number the user will have to guess, chosen randomly in between 1 and 100
	number_to_guess = random.randint(1, 100)
	print("I have in mind a number in between 1 and 100, can you find it?")
	# Replay the question until the user finds the correct number
	while True: 
		i = i + 1
		try :
			if i == 5 :
				print("Max number of tests exceeded, the number wasn't",guess)
				return
			# Read the number the user inputs
			guess = int(input())
			# Compare it to the number to guess
			if guess > number_to_guess:
				print("The number to guess is lower")
			elif guess < number_to_guess:
				print("The number to guess is higher")
			else:
				# The user found the number to guess, let’s exit 
				print("You just found the number, it was indeed",guess)
				print("Congratulations ",user)
				return
		# A ValueError is raised by the int() function if the user inputs something else than a number
		except ValueError as err:
			print("Invalid input , please enter an integer")
# Launch the game
guess_loop()