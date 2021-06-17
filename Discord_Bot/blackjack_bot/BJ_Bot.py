#import os
#import random
import discord

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):

	async def test():
	  await	message.channel.send("Blackjack Test Starting")

	if message.content.startswith('//test'):
		await test()
		#await message.channel.send("Blackjack Test Starting")

		
'''
#Blackjack Game
#-------------------------------------------------------------------------------------------------------------------#

		deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

		async	def deal(deck):
					hand = []
					for i in range(1):
						random.shuffle(deck)
						card = deck.pop()
						if card == 11:card = "J"
						if card == 12:card = "Q"
						if card == 13:card = "K"
						if card == 14:card = "A"
						hand.append(card)
					return hand

		async	def total(hand):
					total = 0
					for card in hand:
						if card == "J" or card == "Q" or card == "K": total+= 10
						elif card == "A": 
								if total >= 1: total+= 1; 
								else: total+= 11 
						else: total+= card
					return total

		async	def hit(hand):
				card = deck.pop()
				if card == 11:card = "J"
				if card == 12:card = "Q"
				if card == 13:card = "K"
				if card == 14:card = "A"
				hand.append(card)
				return hand

		async	def clear():
				if os.name == 'nt':
					os.system('CLS')
				if os.name == 'posix':
					os.system('clear')

		async	def print_results(dealer_hand, player_hand):
				await clear()
				print("The dealer has a/n " + str(dealer_hand) + " for a total of " + str(total(dealer_hand)))
				print("You have a " + str(player_hand) + " for a total of " + str(total(player_hand)))

		async	def blackjack(dealer_hand, player_hand):
				if total(player_hand) == 21:
					print_results(dealer_hand, player_hand)
					print("Congratulations! You got a Blackjack!\n")
				elif total(dealer_hand) == 21:
					print_results(dealer_hand, player_hand)		
					print("Sorry, you lose. The dealer got a blackjack.\n")

		async	def score(dealer_hand, player_hand):
				if total(player_hand) == 21:
					print_results(dealer_hand, player_hand)
					print("Congratulations! You got a Blackjack!\n")
				elif total(dealer_hand) == 21:
					print_results(dealer_hand, player_hand)		
					print("Sorry, you lose. The dealer got a blackjack.\n")
				elif total(player_hand) > 21:
					print_results(dealer_hand, player_hand)
					print("Sorry. You busted. You lose.\n")
				elif total(dealer_hand) > 21:
					print_results(dealer_hand, player_hand)			   
					print("Dealer busts. You win!\n")
				elif total(player_hand) < total(dealer_hand):
					print_results(dealer_hand, player_hand)
					print("Sorry. Your score isn't higher than the dealers. You lose.\n")
				elif total(player_hand) > total(dealer_hand):
					print_results(dealer_hand, player_hand)			   
					print("Congratulations. Your score is higher than the dealers. You win\n")

		async	def Dealers_choice(player_hand, dealer_hand):
				if 22 > total(player_hand):
					choice = input("Do you want to [H]it, [S]tand, or [Q]uit: ").lower()
				else:
					choice = "s"
					await clear()
					#Dealers choice
				if choice == "h":
					hit(player_hand)
					while total(dealer_hand) < 17:
						await hit(dealer_hand)
					await score(dealer_hand, player_hand)
				elif choice == "s":
					while total(dealer_hand) < 17:
						await hit(dealer_hand)
					await score(dealer_hand, player_hand)
				elif choice == "q":
					print("Bye!")
					exit()

		async def game():
				choice = 0
				await clear()
				message.channel.send("Welcome to Blackjack")
				dealer_hand = deal(deck)
				player_hand = deal(deck)
				while choice != "q":
					print("The dealer is showing a " + str(dealer_hand[0]))
					print("You have a " + str(player_hand) + " for a total of " + str(total(player_hand)))
					await blackjack(dealer_hand, player_hand)

					await Dealers_choice(player_hand, dealer_hand)
		await game()

#-------------------------------------------------------------------------------------------------------------------#
'''

client.run('TOKEN')