input = open('1').readlines()[0].split(', ')

def p1():
	x = 0
	y = 0
	dir = 0
	for d in input:
		if d[0] == 'R':
			dir = (dir + 1) % 4
		else:
			dir = (dir - 1 + 4) % 4
		if dir == 0:
			y += int(d[1:])
		elif dir == 1:
			x += int(d[1:])
		elif dir == 2:
			y -= int(d[1:])
		elif dir == 3:
			x -= int(d[1:])
	print('p1: ' + str(abs(x) + abs(y)))
	

visited = set()

def add_visited(xpos,ypos):
	if not (xpos,ypos) in visited:
		visited.add((xpos,ypos))
		return True
	return False

def p2():
	x = 0
	y = 0
	dir = 0
	done = False
	for d in input:
		if done:
			break
		len = int(d[1:])
		if d[0] == 'R':
			dir = (dir + 1) % 4
		else:
			dir = (dir - 1 + 4) % 4
		if dir == 0:
			for i in range(len):
				y += 1
				if not add_visited(x,y):
					done = True
					break
		elif dir == 1:
			for i in range(len):
				x += 1
				if not add_visited(x,y):
					done = True
					break
		elif dir == 2:
			for i in range(len):
				y -= 1
				if not add_visited(x,y):
					done = True
					break
		elif dir == 3:
			for i in range(len):
				x -= 1
				if not add_visited(x,y):
					done = True
					break
	print('p2: ' + str(abs(x) + abs(y)))
	
p1()
p2()