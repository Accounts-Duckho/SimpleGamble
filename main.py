import random
# In my game , four card pack will be used
cardpack_1=[1,2,3,4,5,6,7,8,9,10]
cardpack_2=[1,2,3,4,5,6,7,8,9,10]
cardpack_3=[1,2,3,4,5,6,7,8,9,10]
cardpack_4=[1,2,3,4,5,6,7,8,9,10]
def shuffle():
	random.shuffle(cardpack_1)
	random.shuffle(cardpack_2)
	random.shuffle(cardpack_3)
	random.shuffle(cardpack_4)
def initialize():
	shuffle()
