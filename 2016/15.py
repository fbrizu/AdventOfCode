input = open('15').readlines()

def p1():
    pos = []
    for line in input:
        x = (int)(line.split()[3])
        y = (int)(line.split()[11][:-1])
        pos.append((x,y))
    ans = 0
    while(True):
        found = True
        for i,(x,y) in enumerate(pos):
            if (y+ans+i+1)%x != 0:
                found = False
        if found:
            print(ans)
            return ans
        ans += 1

def p2():
    pos = []
    for line in input:
        x = (int)(line.split()[3])
        y = (int)(line.split()[11][:-1])
        pos.append((x,y))
    pos.append((11,0))
    ans = 0
    while(True):
        found = True
        for i,(x,y) in enumerate(pos):
            if (y+ans+i+1)%x != 0:
                found = False
        if found:
            print(ans)
            return ans
        ans += 1

p1()
p2()