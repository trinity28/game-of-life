import pygame,time,sys
from random import randint
from pygame.locals import *
import copy

HEIGHT=100
WIDTH=100

SCALE=10
SCREEN=pygame.display.set_mode((WIDTH*SCALE,HEIGHT*SCALE))

def create_blank():
	board=[[0 for x in range(WIDTH)]for y in range(HEIGHT)]
	return board




def get_Cell(board,x,y):
	if x in range(WIDTH) and y in range(HEIGHT):
			return board[x][y]
	else:
		return 0
def isAlive(board,x,y):
	if board[x][y]==1:
		return True
	else:
		return False
def count_neighbour(board,x,y):
	count=0
	
	for i in range(x-1,x+2):
		for j in range(y-1,y+2):
				if not(i==x and j==y):
					count+=board[i][j]
	
	return count

def update(board,count):

	if(count<2 or count>3):
		return 0
	elif(count==3):
		return 1
	else:
		return board[i][j]


pygame.init()

screen=pygame.display.set_mode((WIDTH*5,HEIGHT*5),0,32)
board=create_blank()

clock=pygame.time.Clock()
RED = (255, 0, 0)
BlACK=(0,0,0)
fps=1000




board[1][5]=1;
board[1][6]=1;
board[2][5]=1;
board[2][6]=1;
board[11][5]=1;
board[11][6]=1;
board[11][7]=1;
board[12][4]=1;
board[12][8]=1;
board[13][3]=1;
board[13][9]=1;
board[14][3]=1;
board[14][9]=1;
board[15][6]=1;
board[16][4]=1;
board[16][8]=1;
board[17][5]=1;
board[17][6]=1;
board[17][7]=1;
board[18][6]=1;
board[21][3]=1;
board[21][4]=1;
board[21][5]=1;
board[22][3]=1;
board[22][4]=1;
board[22][5]=1;
board[23][2]=1;
board[23][6]=1;
board[25][1]=1;
board[25][2]=1;
board[25][6]=1;
board[25][7]=1;
board[35][3]=1;
board[35][4]=1;
board[36][3]=1;
board[36][4]=1;
board[35][22]=1;
board[35][23]=1;
board[35][25]=1;
board[36][22]=1;
board[36][23]=1;
board[36][25]=1;
board[36][26]=1;
board[36][27]=1;
board[37][28]=1;
board[38][22]=1;
board[38][23]=1;
board[38][25]=1;
board[38][26]=1;
board[38][27]=1;
board[39][23]=1;
board[39][25]=1;
board[40][23]=1;
board[40][25]=1;
board[41][24]=1;
#b = copy.deepcopy(board)
while True:
	b = copy.deepcopy(board)
	screen.fill((255,255,255))
	for event in pygame.event.get():
		if event.type==QUIT:
			pygame.quit()
			sys.exit()



	for i in range(WIDTH-1):
		for j in range(HEIGHT-1):
			
			c=count_neighbour(board,i,j)
			
			b[i][j]=update(board,c)




	for i in range(WIDTH-1):
		for j in range(HEIGHT-1):
			if b[i][j]==1:
				pygame.draw.rect(screen, RED, (i*10, j*10, 10,10))
				
				
				
			else:
				pygame.draw.rect(screen, BlACK, (i*10, j*10, 10, 10),8)

	board = copy.deepcopy(b)
	
	

	




	

	




	clock.tick(fps)



	pygame.display.update()







	
