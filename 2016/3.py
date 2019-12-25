input = open('3').readlines()

def p1():
	count = 0
	for line in input:
		nums = line.split()
		l = []
		for n in nums:
			l.append(int(n))
		l.sort()
		if l[0] + l[1] > l[2]:
			count += 1
	print(count)
	
def p2():
	count = 0
	l = []
	for line in input:
		nums = line.split()
		for n in nums:
			l.append(int(n))
	i = 0
	c = 0
	while i < len(l):
		t = []
		t.append(l[i])
		t.append(l[i+3])
		t.append(l[i+6])
		#print(str(i) + ' ' + str(t[0]) + ' ' + str(t[1]) + ' ' + str(t[2]))
		c = (c+1)%3
		if c == 0:
			i += 7
		else:
			i += 1
		t.sort()
		if t[0] + t[1] > t[2]:
			count += 1
	print(count)

p1()
p2()