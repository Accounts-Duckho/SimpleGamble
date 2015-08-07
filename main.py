'''#! /usr/bin/python'''
import random
# In my game , four card pack will be used
cardpack_1=[1,2,3,4,5,6,7,8,9,10]
cardpack_2=[1,2,3,4,5,6,7,8,9,10]
cardpack_3=[1,2,3,4,5,6,7,8,9,10]
cardpack_4=[1,2,3,4,5,6,7,8,9,10]
userCard=0
comCard=0
mod=0
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
def open(mod, round):
	global comCard
	if mod==1:
		print("Computer's card :", secondDraw(round))
		comCard=secondDraw(round)
	else:
		print("Computer's card :", firstDraw(round))		
		comCard=firstDraw(round)
def game(mod):
	round=0
	# array number starts at Zero
	while round+1 <= 20:
		round += 1
		open(mod, round)
	print("Finished")
def init():
	shuffle()
	mod=input("First = 1 , After = 2 : ")
init()
game(mod)
