'''#! /usr/bin/python'''
import random
import os
import msvcrt
# 게임엔 4개의 카드팩이 필요합니다.
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
	print("오픈카드 :", secondDraw(round))
	comCard=secondDraw(round)
def betting():
	global userChip
	global bettingChip
	choice=0
	choice=int(input("배팅하시겠습니까? 네(1), 아니요(2) :"))
	if choice == 1:
		chips=int(input("얼마나 베팅하시겠습니까? : "))
		if chips <= userChip and chips != 0:
			bettingChip = chips
			userChip-=chips
		elif chips==0:
			print("최소 1개는 베팅해야합니다. 1개 배팅됩니다.")
			bettingChip = 1
			userChip-=1
		else:
			print("가진 칩 이상 베팅은 불가능합니다. 올인합니다.")
			bettingChip = userChip
			userChip=0
	else: 
		print("베팅안함")
def check(round):
	global userCard
	global comCard
	global bettingChip
	global userChip
	print("당신의 카드 :", firstDraw(round))
	userCard=firstDraw(round)
	print("[결과]")
	if userCard > comCard:
		print("승리")
		print("{get}개의 칩을 획득합니다.".format(get=2*bettingChip))
		userChip+=(2*bettingChip)
	elif userCard == comCard:
		print("무승부")
		userChip += bettingChip
	elif userCard < comCard:
		print("패배")
		print("{lose}개의 칩을 잃습니다.".format(lose=bettingChip))
	print("[유저 상태]")
	print("[칩] ",userChip)
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
	print("게임 종료")
def init():
	global userChip
	shuffle()
	userChip = 5
init()
game()
