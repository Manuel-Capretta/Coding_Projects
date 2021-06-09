import os
import random

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*5
deck2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*5

def deal(deck):
	hand = []

	random.shuffle(deck)
	card = deck.pop()
	if card == 11:card = "J"
	if card == 12:card = "Q"
	if card == 13:card = "K"
	if card == 14:card = "A"
	hand.append(card)
	return hand

def deal2(deck2):
	hand2 = []

	random.shuffle(deck2)
	card2 = deck2.pop()
	if card2 == 11:card2 = "J"
	if card2 == 12:card2 = "Q"
	if card2 == 13:card2 = "K"
	if card2 == 14:card2 = "A"
	hand2.append(card2)
	return hand2

def total(hand):
		total = 0
		for card in hand:
			if card == "J" or card == "Q" or card == "K":
				total+= 10
			elif card == "A":
					if total >= 11: 
						total+= 1
					else:
						total+= 11
			else: 
				total+= card
		return total

def total2(hand2):
		total2 = 0
		for card2 in hand2:
			if card2 == "J" or card2 == "Q" or card2 == "K":
				total2+= 10
			elif card2 == "A":
				if total2 >= 11: 
					total2+= 1
				else:
					total2+= 11
			else: 
				total2+= card2
		return total2

def hit(hand):
	card = deck.pop()
	if card == 11:card = "J"
	if card == 12:card = "Q"
	if card == 13:card = "K"
	if card == 14:card = "A"
	hand.append(card)
	return hand

def hit2(hand2):
	card2 = deck.pop()
	if card2 == 11:card2 = "J"
	if card2 == 12:card2 = "Q"
	if card2 == 13:card2 = "K"
	if card2 == 14:card2 = "A"
	hand2.append(card2)
	return hand2

def clear():
	if os.name == 'nt':
		os.system('CLS')
	if os.name == 'posix':
		os.system('clear')

def print_results(player2_hand, player_hand):
	clear()
	print("player 2 has a/n " + str(player2_hand) + " for a total of " + str(total(player2_hand)))
	print("player 1 haa a/n " + str(player_hand) + " for a total of " + str(total(player_hand)))

def blackjack(player2_hand, player_hand):
	if total(player_hand) == 21:
		print_results(player2_hand, player_hand)
		print("Congratulations! You got a Blackjack!\n")
	elif total(player2_hand) == 21:
		print_results(player2_hand, player_hand)		
		print("Sorry, you lose. The dealer got a blackjack.\n")

def score(player2_hand, player_hand):
	if total(player_hand) == 21:
		print_results(player2_hand, player_hand)
		print("Congratulations Player 1! You got a Blackjack!\n")
	elif total(player2_hand) == 21:
		print_results(player2_hand, player_hand)		
		print("Player 1 lost. Player 2 got a blackjack.\n")
	elif total(player_hand) > 21:
		print_results(player2_hand, player_hand)
		print("Player 1 busted. He lost.\n")
	elif total(player2_hand) > 21:
		print_results(player2_hand, player_hand)			   
		print("Player 2 busts. You win!\n")
	elif total(player_hand) < total(player2_hand):
		print_results(player2_hand, player_hand)
		print("Sorry Player 1. Your score isn't higher than the score of Player 2. You lost.\n")
	elif total(player_hand) > total(player2_hand):
		print_results(player2_hand, player_hand)			   
		print("Congratulations Player 1. Your score is higher than the score of Player 2. You win\n")		

def pchoice(player_hand, player2_hand, choice):
	choice = input("Player 1: Do you want to [H]it, [S]tand, or [Q]uit: ").lower()
	#players choice
	if choice == "h":
		hit(player_hand)
	elif choice == "s":
		score(player2_hand, player_hand)
	elif choice == "q":
		print("Bye!")
		exit()
	return player_hand, player2_hand, choice

def pchoice2(player2_hand, player_hand, choice2):
	choice2 = input("Player 1: Do you want to [H]it, [S]tand, or [Q]uit: ").lower()
	#players 2 choice
	if choice2 == "h":
		hit(player2_hand)
		score(player2_hand, player_hand)
	elif choice2 == "s":
		score(player2_hand, player_hand)
	elif choice2 == "q":
		print("Bye!")
		exit()
	return player_hand, player2_hand, choice2

def game():
  choice = 0
  choice2 = 0
  clear()
  print("WELCOME TO BLACKJACK!\n")
  player_hand = deal(deck)
  player2_hand = deal2(deck2)
  random_start = random.randint(1,2)
  if(random_start == 1):
    print_results(player2_hand, player_hand)
    blackjack(player2_hand, player_hand)
    if 22 > total(player_hand):
      pchoice(player_hand, player2_hand, choice)
      if(choice == "s"):
        pchoice2(player_hand, player2_hand, choice2)
      elif(choice == "h"):
        pchoice(player_hand, player2_hand, choice)
    else:
      print("Invalid Input. Please try again.")
      pchoice(player_hand, player2_hand, choice)
  else:
    print_results(player2_hand, player_hand)
    blackjack(player2_hand, player_hand)
    if 22 > total(player2_hand):
      pchoice2(player_hand, player2_hand, choice2)
      if(choice2 == "s"):
        pchoice(player_hand, player2_hand, choice)
      elif(choice2 == "h"):
        pchoice2(player_hand, player2_hand, choice)
    else:
      print("Invalid Input. Please try again.")
      pchoice2(player_hand, player2_hand, choice2)
	
if __name__ == "__main__":
   game()