from .player import Player
from .player import Deck


class Board:
	#list of object players
	players = []

	#counting the turns
	turn_count = 0
	
	#history of cards played, except for active_cards 
	history_card = [] 
	
	#gameLoop
	gameRunning = True
	
	def __init__(self, multi_player :int):

		'''
		initialise the object

		:param multiplayer: An Interger that represent the amount of players that wants to play
		adding for the names of the players
		initilizing the decks and filling them with cards
		shuffle the decks
		and distributing the cards to the players
		'''

		self.multi_player = multi_player

		for i in range(multi_player):
			#asking name from players
			name =	str(input("Name of player {0}: ".format(i+1)))
			
			#adding of players in the game
			self.players.append(Player(name))
			
		#initialise deck
		self.deck = Deck()
		self.deck.fill_deck()
		self.deck.shuffle()
		self.players = self.deck.distribute(self.players)
	

	def description_game(self):
		"""description of how to play the game, basic rules 
		need to finish"""
	
	def print_history(self):
		'''
		function will take all the items added to the history(wich is the table) and print them
		chronologicly

		I chose here a print method instead of returning a value
		'''
		
		#printing the history of the game
		mssg = "HISTORY: \n"
		for item in self.history_card:
			mssg = mssg + item + "| "
		
		print(mssg+"\n")


	def check_input(self) -> int:
		'''
		function will validate if the userInput, thus the players hand, gets represented by an accetable intenger
		function will validate if the input is an Intenger
		function will ask to put a valid input until it gets one

		:return :An intenger that represents the card of the playe
		'''


		#validate the input, it must be an intenger
		input_validation = True
		while input_validation:
			playerInput = input("Enter a integer that represents a card: ")
			try:
				#check if it is an intenger 
				val = int(playerInput)
				#has to be valueble
				
				if val > (52 / self.multi_player)-(self.turn_count+1):
					print("it must be an intenger thats smaller!!")
				else:
					input_validation = False
			

			#throw error, if it's not an intenger
			except ValueError:
				print("try again, but this time give me a integer please")

		return val

	def logic(self, wich_player_is_it : int):


		'''
		function will check if input is valid
		function will add the card on the table (history)
		:param wich_player_is_it: describes wich player it is, as Intenger
		'''
		value = self.check_input()
		self.history_card.append(self.players[wich_player_is_it].cards[int(value)])
		self.players[wich_player_is_it].play(value)
	
	
	def start_game(self):
		'''
		function acts as the main gameloop
		switches between players 
		'''
		while self.gameRunning:
			# instructions of game


			#player1 may start
			for wich_player_is_it in range(self.multi_player):
				
				#printing the cards' history
				self.print_history()

				
				#print hand of player and his/her name
				print(self.players[wich_player_is_it])
				
				#checking the logic 
				self.logic(wich_player_is_it)

				print(self.turn_count)
				
				
				


			#counting the turns
			self.turn_count	+=1
				

				