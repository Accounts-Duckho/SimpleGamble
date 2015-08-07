'''#! /usr/bin/python'''
import random
# In my game , four card pack will be used
cardpack_1=[1,2,3,4,5,6,7,8,9,10]
cardpack_2=[1,2,3,4,5,6,7,8,9,10]
cardpack_3=[1,2,3,4,5,6,7,8,9,10]
cardpack_4=[1,2,3,4,5,6,7,8,9,10]
userCard=0
comCard=0
userChip=0
bettingChip=0
def shuffle():
	random.shuffle(cardpack_1)
	random.shuffle(cardpack_2)
	random.shuffle(cardpack_3)
	random.shuffle(cardpack_4)
# First start, first draw 
def firstDraw(round):
	if round >= 1 and round <= 5:
		return cardpack_1[(2*round)-2]
	if round >= 6 and round <= 10:
		return cardpack_2[(2*round)-12]
	if round >= 11 and round <= 15:
		return cardpack_3[(2*round)-22]
	if round >= 16 and round <= 20:
		return cardpack_4[(2*round)-32]
def secondDraw(round):
	if round >= 1 and round <= 5:
		return cardpack_1[(2*round)-1]
	if round >= 6 and round <= 10:
		return cardpack_2[(2*round)-11]
	if round >= 11 and round <= 15:
		return cardpack_3[(2*round)-21]
	if round >= 16 and round <= 20:
		return cardpack_4[(2*round)-31]
def open(round):
	global comCard
	print("Computer's card :", secondDraw(round))
	comCard=secondDraw(round)
def betting():
	global userChip
	global bettingChip
	choice=0
	choice=int(input("Would you bet this game? Yes(1), No(2) :"))
	if choice == 1:
		chips=int(input("How much? : "))
		if chips <= userChip:
			bettingChip = chips
		else:
			print("Your all chips betted")
			bettingChip = userChip
	else: 
		print("No Bet")		
def game():
	round=0
	# array number starts at Zero
	while round+1 <= 20:
		round += 1
		open(round)
		betting()
	print("Finished")
def init():
	global userChip
	shuffle()
	userChip = 5
init()
game()
