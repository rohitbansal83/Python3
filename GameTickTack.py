def selectplayer():
	symbol = input("Please Select X or O for Player 1: ")
	global d
	if (symbol =='X' ):
		d = {'X':'P1','O':'P2','P1':'X','P2':'O'}
	else:
		d = {'X':'P2','O':'P1','P1':'O','P2':'X'}


def isgamewon():
	global b
	global d
	for x in range(3):
		if b[0][x] == b[1][x] == b[2][x] and b[0][x]!='E':
			return d[b[0][x]]
		if b[x][0] == b[x][1] == b[x][2] and b[x][0] !='E':
			return d[b[x][0]]
	if b[1][1]!='E' and (b[0][0] == b[1][1] == b[2][2] or b[0][2] == b[1][1] == b[2][0]):
		return d[b[1][1]]
	return 'N'

def isgamedrawn():
	global b
	for x in range(3):
		l = b[:][x] 
		if l.count('X') == 0 or l.count('O') == 0:
			return False
		l = b[x][:] 
		if l.count('X') == 0 or l.count('O') == 0:
			return False
	l= [b[0][0],b[1][1],b[2][2]]
	if l.count('X') == 0 or l.count('O') == 0:
		return False
	l= [b[0][2],b[1][1],b[2][0]]
	if l.count('X') == 0 or l.count('O') == 0:
		return False
	return True

def getinputp1():
	row= input("(Player 1) Select the row for next move: ")
	col= input("(Player 1) Select the col for next move: ")
	putinput (d['P1'],row,col)

def getinputp2():
	row= input("(Player 2) Select the row for next move: ")
	col= input("(Player 2) Select the col for next move: ")
	putinput (d['P2'],row,col)

	
def putinput(move,row,col):
	global b

	b[int(row)-1][int(col)-1] = move
	print (b[0])
	print (b[1])
	print (b[2])


		
def game():
	global b
	drawboard()
	selectplayer()
	winner = isgamewon()
	while winner == 'N' and isgamedrawn()==False:
		getinputp1()
		winner = isgamewon()
		if winner!='N':
			print ("Congratulation Player "+	winner +". You have won!")
			print(b[0])
			print(b[1])
			print(b[2])
			break
		elif isgamedrawn():
			print ("Game Drawn!")
			break

		getinputp2()
		winner = isgamewon()
		if winner!='N':
			print ("Congratulation Player "+	winner +". You have won!")
			break
		elif isgamedrawn():
			print ("Game Drawn!")
			break

def playmore():
	
	global gamecount
	gamecount = input("do you want to playmore: ")
	if gamecount == 'Y' or gamecount =='y':
		return True
	else:
		return False
        
def gameset():
	game()
	while playmore():
		game()	
	else:
		print ("Game Over!")        

b = [['E','E','E'],['E','E','E'],['E','E','E']]
d = {}
gamecount ='Y'
gameset()