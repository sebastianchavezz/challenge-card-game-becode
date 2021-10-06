from .card import Card
import random




class Player:
	
	#number of cards
	numbers_of_cards = 0
	
	#name of player
	name = ""
	
	
	def __init__(self, name : str):
		'''
		initialise object
		:param name : takes a string and pass it to the players' name
		initialise the cards for the player
		'''
		self.name = name
		self.cards = []

	

	def play(self,players_input : int):
		'''
		function will print the card that the player wished to play
		function will delete that players' card from hand
		:param player_input: Intenger represents the cards that player wants to play
		'''
		print(self.cards[players_input])

		self.cards.pop(players_input)
		

	
	def print_name(self):
		'''
		function will print the name of the player that's playing
		'''
		print(self.name)
	

	
	def __str__(self) -> str:
		'''
		function will print wich players' turn it is
		will print intenger that represent wich card you can play
		will count the amount of cards there are and save it in numbers_of_cards of the object
		:return: return a multiline string
		'''
		mssg = "name player: "+self.name+ "\n"
		mssg = mssg + "-----------------------\n"	
		count =0
		for item in self.cards:
			mssg = mssg + str(count)+":"+ "\t" + item +"\n"
			count += 1
		self.numbers_of_cards = count
		return mssg



class Deck:

	#represents the amount of players that plays
	players = []
	#represents the deck of cards
	cards = []


	def __init__(self):
		'''
		initialise cards
		'''
		self.card = Card()
		

	
	def fill_deck(self):
		'''
		function will make a deck of cards from card object
		function will take every value and icon and combine it
		function will have an array of strings that represents the 52 cards in a deck
		'''
		for i in range(0,4):
			for j in range(0,13):
				temp_print = "{0} {1}".format(self.card.get_value[j],self.card.get_icon[i])
				self.cards.append(temp_print)
				
		
	#shuffle the list, deck 
	def shuffle(self):
		random.shuffle(self.cards)
		
	
	def distribute(self, players: Player) -> Player:
		'''
		function will distribute the deck of cards evenly for all the players
		function will do it in an alternating way, so the first player gets the first card, 
		second player gets the second card, etc..

		:param players: expects a list of players object to distribute the cards
		:return : A list of the players with their deck of cards 
		'''
		self.players = players
		for i in range(len(self.players)):
			for j in range(i,52,len(self.players)):
				
				self.players[i].cards.append(self.cards[j])	

		return self.players