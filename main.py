from utils.game import *
import os

def main():
	
	#game loop

	running = True

	while running:
		"""
		while the game is running
		we clear the terminal (this only works with unix-based bash)
		ask for user input
		"""

		os.system("clear")
		user_input = input("Amount of players: ")
		
		"""
		manage user input
		chek if user input is integer
	 	only intengers are allowed
		"""

		try:
			val = int(user_input)


		except ValueError:
			print("Please enter a integer")
			print("closing app...")
			running= False	

		"""
		only the amount of players acceptable, 
		where the cards can be divided evenly 
		"""
		if 52 % val == 0:
			""" 
			calling the board object to start the game,
			:param val: gives the value of the amount of player that want to play
			"""
			board = Board(val)
			board.start_game()

		
		else:
			print("this amount of players is not acceptable!")
		
		

			
	
		


if __name__ == "__main__":
	main()			








