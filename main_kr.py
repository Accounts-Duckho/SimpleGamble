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
def draw(code):
	if code >= 0 and code <= 9:
		return cardpack_1[code]
	if code >= 10 and code <= 19:
		return cardpack_2[code-10]
	if code >= 20 and code <= 29:
		return cardpack_3[code-20]
	if code >= 30  and code <= 39:
		return cardpack_4[code-30]
def open(round):
	global comCard
	comCode=2*round-1
	comCard=draw(comCode)
	print("오픈카드 :", comCard)
def betting():
	global userChip
	global bettingChip
	choice=0
	choice=int(input("배팅하시겠습니까? 네(1), 죽겠습니다(2) :"))
	if choice == 1:
		chips=int(input("얼마나 베팅하시겠습니까? 개수 , 올인(777): "))
		if chips <= userChip and chips != 0:
			bettingChip = chips
			userChip-=chips
		elif chips==0:
			print("최소 1개는 베팅해야합니다. 1개 배팅됩니다.")
			bettingChip = 1
			userChip-=1
		elif chips==777:
			print("올인합니다.")
			bettingChip = userChip
			userChip=0			
		else:
			print("Error betting() #2")
	elif choice == 2:
		print("죽습니다.")
	else: 
		print("Error betting() #1")
def check(round):
	global userCard
	global comCard
	global bettingChip
	global userChip
	myCode=2*round-2
	userCard=draw(myCode)
	print("당신의 카드 :", userCard)
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
	# init number is zero
	while round < 20 and userChip!=0:
		round += 1
		os.system('cls')
		open(round)
		betting()
		check(round)
		userCard=0
		comCard=0
		bettingChip=0
		msvcrt.getch()
	os.system('cls')
	print("게임 종료")
def init():
	global userChip
	shuffle()
	userChip = 15
init()
game()
