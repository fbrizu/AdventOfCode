import numpy as np

input = open('2').readlines()
pad = [[1,2,3],[4,5,6],[7,8,9]]
pad_2 = [[0,0,1,0,0],[0,2,3,4,0],[5,6,7,8,9],[0,10,11,12,0],[0,0,13,0,0]]
x = 1
y = 1

def move(d, p):
	global x
	global y
	new_x = 0
	new_y = 0
	if d == 0: #up
		new_y = y-1
	elif d == 1:
		new_x = x+1
	elif d == 2:
		new_y = y+1
	elif d == 3:
		new_x = x-1
	if d==1 or d==3:
		if new_x>=0 and new_x<len(p[0]) and p[y][new_x] != 0:
			x = new_x
	if d==0 or d==2:
		if new_y>=0 and new_y<len(p) and p[new_y][x] != 0:
			y = new_y

def solve(p,start_x,start_y):
	global x
	global y
	x = start_x
	y = start_y
	for line in input:
		for c in line:
			if c == 'U':
				move(0,p)
			elif c == 'R':
				move(1,p)
			elif c == 'D':
				move(2,p)
			elif c == 'L':
				move(3,p)
		print(str(p[y][x]) + ' ',end='')
	print('')
		
	
solve(pad,1,1)
solve(pad_2,0,2)