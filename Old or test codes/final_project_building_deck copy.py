import random
from time import sleep

# Unicode variables representing suits
CLUB = "\u2663"
HEART = "\u2665"
DIAMOND = "\u2666"
SPADE = "\u2660"
suits = ['\u2663', '\u2665', '\u2666', '\u2660']*13
values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']*4
trial_deck = {}
for i in range(1, 53):
	trial_deck[i] = {
						'card': values[i-1] + ' ' + suits[i-1],
						'actual_value': []

					}

# Dictionary for a deck o 52 cards
DECK_DICT = {
				1: {'card': 'A ♣', 'value': [1, 11]},
				2: {'card': '2 ♥', 'value': [2]},
				3: {'card': '3 ♦', 'value': [3]},
				4: {'card': '4 ♠', 'value': [4]},
				5: {'card': '5 ♣', 'value': [5]},
				6: {'card': '6 ♥', 'value': [6]},
				7: {'card': '7 ♦', 'value': [7]},
				8: {'card': '8 ♠', 'value': [8]},
				9: {'card': '9 ♣', 'value': [9]},
				10: {'card': '10 ♥', 'value': [10]},
				11: {'card': 'J ♦', 'value': [10]},
				12: {'card': 'Q ♠', 'value': [10]},
				13: {'card': 'K ♣', 'value': [10]},
				14: {'card': 'A ♥', 'value': [1, 11]},
				15: {'card': '2 ♦', 'value': [2]},
				16: {'card': '3 ♠', 'value': [3]},
				17: {'card': '4 ♣', 'value': [4]},
				18: {'card': '5 ♥', 'value': [5]},
				19: {'card': '6 ♦', 'value': [6]},
				20: {'card': '7 ♠', 'value': [7]},
				21: {'card': '8 ♣', 'value': [8]},
				22: {'card': '9 ♥', 'value': [9]},
				23: {'card': '10 ♦', 'value': [10]},
				24: {'card': 'J ♠', 'value': [10]},
				25: {'card': 'Q ♣', 'value': [10]},
				26: {'card': 'K ♥', 'value': [10]},
				27: {'card': 'A ♦', 'value': [1, 11]},
				28: {'card': '2 ♠', 'value': [2]},
				29: {'card': '3 ♣', 'value': [3]},
				30: {'card': '4 ♥', 'value': [4]},
				31: {'card': '5 ♦', 'value': [5]},
				32: {'card': '6 ♠', 'value': [6]},
				33: {'card': '7 ♣', 'value': [7]},
				34: {'card': '8 ♥', 'value': [8]},
				35: {'card': '9 ♦', 'value': [9]},
				36: {'card': '10 ♠', 'value': [10]},
				37: {'card': 'J ♣', 'value': [10]},
				38: {'card': 'Q ♥', 'value': [10]},
				39: {'card': 'K ♦', 'value': [10]},
				40: {'card': 'A ♠', 'value': [1, 11]},
				41: {'card': '2 ♣', 'value': [2]},
				42: {'card': '3 ♥', 'value': [3]},
				43: {'card': '4 ♦', 'value': [4]},
				44: {'card': '5 ♠', 'value': [5]},
				45: {'card': '6 ♣', 'value': [6]},
				46: {'card': '7 ♥', 'value': [7]},
				47: {'card': '8 ♦', 'value': [8]},
				48: {'card': '9 ♠', 'value': [9]},
				49: {'card': '10 ♣', 'value': [10]},
				50: {'card': 'J ♥', 'value': [10]},
				51: {'card': 'Q ♦', 'value': [10]},
				52: {'card': 'K ♠', 'value': [10]}}

# Player variables, atributes, and methods
class Player(object):
	player_hand = []
	hand_value = 0
	has_ace = False
	balance = 1000
	bet = 0

	def __init__(self, name):
		self.name = name

	# Returns all player attributes
	# Just for troubleshooting
	def __repr__(self):
		return "Name: {}, Player Hand: {}, Hand Val: {}, Has Ace: {}, Balance = {}, Bet = {}". format(self.name, self.player_hand, self.hand_value, self.has_ace, self.balance, self. bet)


	def show_balance(self):
		"""Prints the current balance """
		print("{} currently has ${}.".format(self.name, self.balance))

	def show_hand(self):
		"""Shows what's in the player's current hand"""
		to_print = []
		for i in range(len(player_1.player_hand)):
			to_print.append(player_1.player_hand[i][0])
		print("[" + "]  [".join(to_print) + "]")

	def get_wager(self):
		"""Gets the player's bet"""
		while True:
			try:
				wager = int(input("How much would you like to bet? (Minimum is $10)." \
								  + "\n" + "Bet: $ "))
				if wager < 10:
					print("\n" + "The minimum bet is $10.  Please try again..." + "\n")
					sleep(1)
				elif wager > self.balance:
					print("\n" + "You cannot bet more money than you have!" \
					+  " You bet ${}, but you only have ${}.".format(wager, self.balance) \
					+ " Please try again..." + "\n")
					sleep(1)
				else:
					self.bet += wager
					print("\n" + ("=" * 32) + "\n" \
						+ "Your bet for this hand is ${}.".format(self.bet) \
						+ "\n" + ("=" * 32) + "\n")
					sleep(1)
					break
			except:
				print("\n" + "Your bet must be a integar number. Please try again..." + "\n")
				sleep(1)

	def get_card(self):
		"""Gets a card for the player """
		card_key = shuffled_cards.give_one_card()
		hand_card = [DECK_DICT[card_key]["card"], DECK_DICT[card_key]["value"]]
		self.player_hand.append(hand_card)

	def check_if_ace(self):
		"""Checks if card is an Ace"""
		if self.player_hand[len(self.player_hand)-1][0][0] == "A":
			self.has_ace = True

	def set_hand_values(self):
		"""Add card value to hand value"""
		self.hand_value += self.player_hand[len(self.player_hand)-1][1][0]

	def double_down_bet(self):
		"""Doubles the player's bet for doubling down """
		self.bet *= 2
		return self.bet

	"""THIS NEEDS TO BE CHANGED FOR WHATEVER VARIABLES ARE WIN LOSS!"""
	def update_balance(self):
		"""Updates the balance """
		if hand_won == True:
			self.balance += self.bet
		elif hand_won == False:
			self.balance -= self.bet

	def reset_player_attr(self):
		""" Resets the player's hand"""
		self.player_hand = []
		self.hand_value = 0
		self.has_ace = False
		self.bet = 0


# Card_Deck Class: variables and methods
class Card_Deck(object):
	deck = []

	def new_deck(self):
		self.deck = [x for x in range(1,53)]

	def shuffle(self):
		"""Shuffles the deck. """
		random.shuffle(self.deck)

	def give_one_card(self):
		"""Removes card from the deck and 'deals' it """
		card = self.deck.pop()
		return card

# Get Deck of cards
shuffled_cards = Card_Deck()

# get a player name
def get_player_name():
	while True:
		user_name = input("\nPlease enter your name: ")
		if not user_name:
			print("You must enter a name to play.  Please try again...")
			sleep(1)
		else:
			return user_name
			break

# tell player how to play Black Jack
def instructions():
	rules = """The point of the game is to beat the dealer's hand without
			going over 21. You will be dealt 2 cards, as will the dealer
			but only one of the dealer's cards will be shown. You can choose
			to stand (s) - stop being dealt cards, or hit (h) - continue
			to be dealth cards. All face cards are worth 10, an Ace can be
			either 1 or 11.
			The Dealer must continue to take cards until they are at a hard 17
			or above (Please Note: Ace + 6 = Soft 17, dealer must hit).
			To quit at any time, press 'q'.
			[WILL ADD BETTING STUFF LATER]
			"""
	return rules


##### DEALER FUNCTIONS #####
class Dealer():
	"""Creating the dealer in Blackjack"""
	deck = shuffled_cards.deck

	def dealer_get_initial_cards(self):
		"""Get dealer's initial two cards"""
		first_card = shuffled_cards.give_one_card()
		second_card = shuffled_cards.give_one_card()
		user_list[0]['current_hand'].append(first_card)
		user_list[0]['current_hand'].append(second_card)

	def get_dealer_face_up_card(self):
		"""printing out only the first of dealer's cards"""
		print('Dealer:\t', DECK_DICT[user_list[0]['current_hand'][0]]['card'])

	def get_dealer_two_card_sum(self):
		"""Getting sum of dealer's two cards, and returning their total along with
		length of the first and second card (to check which is an ace)."""
		total = 0
		card_1_ace = dealer.check_if_ace(user_list[0]['current_hand'][0])
		card_2_ace = dealer.check_if_ace(user_list[0]['current_hand'][1])
		if card_1_ace == False and card_2_ace == False: # neither is an ace
			total += DECK_DICT[user_list[0]['current_hand'][0]]['value'][0] + DECK_DICT[user_list[0]['current_hand'][1]]['value'][0] # sum of both cards
		elif card_1_ace == True and card_2_ace == True: # both are aces - very rare
			total = 12
		elif card_1_ace == True: # card 1 is an Ace
			total += DECK_DICT[user_list[0]['current_hand'][0]]['value'][1] + DECK_DICT[user_list[0]['current_hand'][1]]['value'][0] # sum of both cards (where first is Ace = 11)
		elif card_2_ace == True: # card 2 is an Ace
			total += DECK_DICT[user_list[0]['current_hand'][0]]['value'][0] + DECK_DICT[user_list[0]['current_hand'][1]]['value'][1] # sum of both cards (where second is Ace = 11)
		return total, card_1_ace, card_2_ace

	def check_if_ace(self, card):
		"""Checking if card is an Ace"""
		if len(DECK_DICT[card]['value']) == 2:
			return True
		else:
			return False


	def less_than_18(self, total, card_1_ace, card_2_ace):
		"""If card is a soft 17 or less """
		if (card_1_ace == False and card_2_ace == False): # make sure no Aces
			soft_card = False
			while True:
				curr_card = shuffled_cards.give_one_card() # take card from deck
				user_list[0]['current_hand'].append(curr_card) # add to dealer's current hand
				temp_total = total + DECK_DICT[curr_card]['value'][0]

				if dealer.check_if_ace(curr_card) and total < 11: # if new card is an ace and total is less than 11
					total += 11
					soft_card = True
				elif dealer.check_if_ace(curr_card) and total >= 11: # if new card is an ace and total is >= 11
					total += 1
				elif soft_card == True and temp_total >= 22: # 'busted' w/ soft hand;  not real bust
					total = temp_total - 10
					soft_card = False
				else:
					total += DECK_DICT[curr_card]['value'][0]

				dealer.print_dealer_cards(running_total=total, turn=False) # print dealer cards after getting next card

				if total >= 17:
					break
			return total
		else:	# if ace exists in one/both of dealer's first two cards
			soft_card = True # assume it is a 'soft hand' (since it is either AA, A2, A3, A4, A5, A6)
			while True:
				curr_card = shuffled_cards.give_one_card() # take card from deck
				user_list[0]['current_hand'].append(curr_card) # add to dealer's current hand
				curr_card_value = DECK_DICT[curr_card]['value'][0] # Ace will always = 1 in this case
				temp_total = total + curr_card_value

				if temp_total >= 22 and soft_card: # check if dealer busts with soft hand
					total = temp_total - 10 # we previously assumed Ace is 11, this brings it back down by 10 so A = 1
					soft_card = False
				elif temp_total >= 22 and soft_card == False: # dealer busts
					total = temp_total
				#elif temp_total <= 21: # if we have a card that doesnt bust
				#	total = temp_total
				else:
					total = temp_total

				dealer.print_dealer_cards(turn = False, running_total=total) # print dealer cards after getting next card

				if total >= 17:
					break
			return total


	def dealer_cards_check_total(self):
		"""This will see if total is hard 17, > hard 17, or less than 18 """
		total, card_1_ace, card_2_ace = dealer.get_dealer_two_card_sum() # getting sum of first 2 cards in dealer's hand
		dealer.print_dealer_cards(running_total=total, turn = True) # Initial print out of dealer's 2 cards
		if total > 17 :
			return total
		elif total == 17 and card_1_ace == False and card_2_ace == False: # total is hard 17
			return total
		elif total <= 17: # soft 17 or less
			return dealer.less_than_18(total, card_1_ace, card_2_ace)



	def print_dealer_cards(self, running_total, turn):
		""" Print the dealer's current hand"""

		if turn == True:
			print('Dealer\'s Hand:\n-----------\n') # header
			for card in user_list[0]['current_hand']:
				print(DECK_DICT[card]['card'])
				turn = False
				sleep(1)
			print('Calculating...')
			sleep(1)
			print('\n\tTotal: ', running_total)
			sleep(1)

		else:
			print(DECK_DICT[user_list[0]['current_hand'][-1]]['card'])
			sleep(1)
			print('Calculating...')
			sleep(1)
			print('\n\tTotal: ', running_total)
			sleep(1)



def get_outcome(dealer_final_total, player_final_total):
	print('FINAL OUTCOME\n-----------')
	if dealer_final_total > 21:
		print('Dealer busts! You win.')
	elif dealer_final_total < player_final_total:
		print('You win!\n\nDealer: {}\n{}: {}'.format(dealer_final_total, user_list[1]['name'], player_final_total))
	elif dealer_final_total > player_final_total:
		print('You lose!\n\nDealer: {}\n{}: {}'.format(dealer_final_total, user_list[1]['name'], player_final_total))
	elif dealer_final_total == player_final_total:
		print('Push!\n\nDealer: {}\n{}: {}'.format(dealer_final_total, user_list[1]['name'], player_final_total))


# list of players, may not need
user_list = [
			{
			'name': 'dealer',
			'current_hand': [ ]
			},
			{
			'name': '',
			'current_hand': [],
			'total_money': 1000,
			'current_bet': 0
			}
]
#vidya's code

deck = [2, 37, 28, 47, 6, 35, 22, 44, 29, 24, 51, 23, 13, 20, 14, 48, 43, 18, 32, 7, 10, 41, 1, 19, 30, 11, 52, 5, 25, 34, 50, 12, 45, 46, 36, 8, 27, 15, 40, 16, 26, 39, 17, 3, 38, 33, 21, 31, 9, 42, 4, 49]

user_list = [
			{
			'name': 'dealer',
			'current_hand': []
			},
			{
			'name': '',
			'current_hand': [],
			'total_money': 1000,
			'current_bet': 0
			}


]

#code




def check_if_ace(card):
	if len(DECK_DICT[card]['value']) == 2:
		return True
	else:
		return False

def shuffle_deck(deck):
	shuffled_list = []
	for key in deck.keys():
		shuffled_list.append(key)
	random.shuffle(shuffled_list)
	return shuffled_list


def deal_card(deck, user):
	current_card = shuffled_cards.give_one_card()
	return current_card

def tally2(user):


def tally(user):
	total = []
	# card1 = check_if_ace(user_list[1]['current_hand'][0])
	# card2 = check_if_ace(user_list[1]['current_hand'][1])
	# if player_1.has_ace == False:
	# 	total.append(player_1.hand_value) #make two values anyway
	# 	total.append(player_1.hand_value)
	# elif card1 and card2:
	# 	total = [2,12]
	# elif card1:
	# 	total = [(DECK_DICT[user_list[1]['current_hand'][1]]['value'][0]+1),(DECK_DICT[user_list[1]['current_hand'][1]]['value'][0]+11)]
	# elif card2:
	# 	total = [(DECK_DICT[user_list[1]['current_hand'][0]]['value'][0]+1),(DECK_DICT[user_list[1]['current_hand'][0]]['value'][0]+11)]
	if len(user_list[1]['current_hand'])==2: # If there are two cards (same value..print one)
		if total[0] == total[1]:
			print("tally: ", total[0])
		elif total[0]<total[1]:
			print("your tally can be ",total[0], " or ", total[1])
	if len(user_list[1]['current_hand'])>2:  #if more cards have been added
		for c in new_cards:
			if check_if_ace(c)==False:       #if the new card is NOT an ace
				total[1]+= DECK_DICT[c]['value'][0]
				total[0]+= DECK_DICT[c]['value'][0]
			elif check_if_ace(c):            #if it IS an ace:
				if card1 or card2:           #need to check if any other card is an ace
					total[0]+= 1             #need to add corresponding ace values
					total[1]+= 1
				else:
					total[0]+=1
					total[1]+=11
	try:
		if total[0] > 21:
			print('bust!')
	except:
		if total[1] >21:
			print("can't use this tally: ", total[1])
	print('tally:' ,total)
	return total

def blackjack(user):
	if len(user_list[1]['current_hand'])==2:
		if tally(user)==21:
			return True
	else:
		False

def print_hand(user):
	for x in user_list[1]['current_hand']:
		print('your cards: ', DECK_DICT[x]['card'])
	return user_list[1]['current_hand']

def hit(deck,user):
		new_card = deal_card(deck, user_list[1])
		user_list[1]['current_hand'].append(new_card)
		return new_card

new_cards= []
deck = shuffle_deck(DECK_DICT) # deck is a list of shuffled numbers
								#correlating to values in DECK_DICT
def double_down(user_list):
	"""Player can double their bet and will only receive 1 card """
	curr_card = shuffled_cards.give_one_card()
	user_list[1]['current_hand'].append(curr_card)
	new_cards.append(curr_card)
	total = tally(user_list[1])[1]
	return total



# Create instance of dealer
dealer =  Dealer()

### START OF GAME/WHILE LOOP ###

print("Welcome to Blackjack!\n",instructions())

# Get the player's name
player_1 = Player(get_player_name())

# variable for while loop
black_jack_running = True

# Start the game while loop!
while black_jack_running == True:

	# Get new deck and shuffle
	shuffled_cards.new_deck()
	shuffled_cards.shuffle()

	# Get the player's bet
	player_1.get_wager()

	# Deal a card to the player, check if it's an ace
	# increment value of hand, repeat for 2nd card
	# player_1.get_card()
	# player_1.check_if_ace()
	# player_1.set_hand_values()
	#
	# player_1.get_card()
	# player_1.check_if_ace()
	# player_1.set_hand_values()

	# Show the player's hand:
	# player_1.show_hand()

	""" Break to stop while loop until rest of code filled in"""
	black_jack_running = False

	# Create instance of Dealer

	# Deal out cards to dealer
	dealer.dealer_get_initial_cards()

	# Put tally of cards and show one of the dealer's cards
	dealer.get_dealer_face_up_card()
	## Get total of player cards  - if total is 21,
	# Ask if player wants to hit or stand



	#deal cards to user
	user_list[1]['current_hand'].append(deal_card(deck,user_list[1]))
	user_list[1]['current_hand'].append(deal_card(deck,user_list[1]))
	print('first hand: ', user_list[1]['current_hand'])
	print('your hand: ', DECK_DICT[user_list[1]['current_hand'][0]]['card'], DECK_DICT[user_list[1]['current_hand'][1]]['card'])
	tally(user_list[1]) # tally first two cards

	turn_1 = True
	while True:
		if blackjack(user_list[1]):
			print('blackjack!')
			break
		hs_input = input('Would you like to hit (h), stand (s), or double down (d)?' )


		if hs_input.lower() in ['d', 'dd', 'double', 'double down'] and turn_1:
			total = double_down(user_list)
			player_1.double_down_bet()
			turn_1 = False
			print('You doubled down! Total: ', total)
			break
		elif hs_input.lower() in ['s', 'stand']:# Function for standing
			# player cards tally
			
			turn_1 = False
			break
		elif hs_input.lower() in ['h', 'hit']:
			new_cards.append(hit(deck,user_list[1]))
			turn_1 = False
			for x in (user_list[1]['current_hand']):
				print('your cards now: ', DECK_DICT[x]['card'])
			#print('new tally: ', tally(user_list[1]))
			if tally(user_list[1])[0]>21:
				print(tally(user_list[1])[1])
			if tally(user_list[1])[1]>21:
				print(tally(user_list[1])[0])
			if tally(user_list[1])[1]>21 and tally(user_list[1])[0]>21:
				print('you lost!')
				break
			#print('card: ', DECK_DICT[hit()]['value'])
			print(user_list[1]['current_hand'])
			continue
		else:
			print('Please only put hit (h) or stand (s)')
			continue
	else:
		print('Please only put hit (h) or stand (s)')
		continue
	print(deck)



	# Dealer gets one or more cards

	# Show dealer cards
	# Do we want to do this one card at a time?
	dealer_final_total= dealer.dealer_cards_check_total() # will give us the dealer's cards

	# Get total of user's hand

	#get_outcome(dealer_final_total, player_total)

	# Adjust player balance (money)
	player_1.update_balance()

	# Reset the player's hand to empty list
	player_1.reset_player_attr()

	# Ask if player would like to play again
	while True:
		play_again = input('Would you like to play again (yes/no)? ')
		if play_again.lower() in "yes":
			continue
		elif play_again.lower() in "no":
			print('Thanks for playing!')
			black_jack_running = False
			break
