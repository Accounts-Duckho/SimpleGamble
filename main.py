'''#! /usr/bin/python'''
import random
import os
import msvcrt
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
			userChip-=chips
		elif chips==0:
			print("minimum is 1")
			bettingChip = 1
			userChip-=1
		else:
			print("Your all chips betted")
			bettingChip = userChip
			userChip=0
	else: 
		print("No Bet")
def check(round):
	global userCard
	global comCard
	global bettingChip
	global userChip
	print("Your Card :", firstDraw(round))
	userCard=firstDraw(round)
	print("[Result]")
	if userCard > comCard:
		print("User Win")
		print("User get {get} chips".format(get=2*bettingChip))
		userChip+=(2*bettingChip)
	elif userCard == comCard:
		print("Draw")
		userChip += bettingChip
	elif userCard < comCard:
		print("User Lose")
		print("User lose {lose} chips".format(lose=bettingChip))
	print("[Status]")
	print("[chip] ",userChip)
def game():
	global userCard
	global comCard
	global bettingChip
	global userChip
	round=0
	# array number starts at Zero
	while round+1 <= 20 or userChip==0:
		os.system('cls')
		round += 1
		open(round)
		betting()
		check(round)
		userCard=0
		comCard=0
		bettingChip=0
		msvcrt.getch()
	print("Finished")
def init():
	global userChip
	shuffle()
	userChip = 5
init()
game()
