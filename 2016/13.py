input = 1358
#input = 10

def isWall(x,y):
    n = x*x + 3*x + 2*x*y + y + y*y + input
    b = '{0:b}'.format(n)
    count = 0
    for c in b:
        if c == '1':
            count += 1
    return count % 2 == 1

def p1():
    xinit = 1
    yinit = 1
    xn = 31
    yn = 39
    seen = []
    search = [(xinit,yinit)]
    dist = {}
    dist[(xinit,yinit)] = 0

    while len(search) > 0:
        x,y = search.pop(0)
        seen.append((x,y))
        if x > 0 and not isWall(x-1,y) and not (x-1,y) in seen and not (x-1,y) in search:
            search.append((x-1,y))
            if not (x-1,y) in dist:
                dist[(x-1,y)] = dist[(x,y)]+1
        if y > 0 and not isWall(x,y-1) and not (x,y-1) in seen and not (x,y-1) in search:
            search.append((x,y-1))
            if not (x,y-1) in dist:
                dist[(x,y-1)] = dist[(x,y)]+1
        if not isWall(x+1,y) and not (x+1,y) in seen and not (x+1,y) in search:
            search.append((x+1,y))
            if not (x+1,y) in dist:
                dist[(x+1,y)] = dist[(x,y)]+1
        if not isWall(x,y+1) and not (x,y+1) in seen and not (x,y+1) in search:
            search.append((x,y+1))
            if not (x,y+1) in dist:
                dist[(x,y+1)] = dist[(x,y)]+1
        if (xn,yn) in dist:
            print(dist[xn,yn])
            break

def p2():
    xinit = 1
    yinit = 1
    seen = []
    search = [(xinit,yinit)]
    dist = {}
    dist[(xinit,yinit)] = 0

    while len(search) > 0:
        x,y = search.pop(0)
        seen.append((x,y))
        if x > 0 and not isWall(x-1,y) and not (x-1,y) in seen and not (x-1,y) in search:
            search.append((x-1,y))
            if not (x-1,y) in dist:
                dist[(x-1,y)] = dist[(x,y)]+1
        if y > 0 and not isWall(x,y-1) and not (x,y-1) in seen and not (x,y-1) in search:
            search.append((x,y-1))
            if not (x,y-1) in dist:
                dist[(x,y-1)] = dist[(x,y)]+1
        if not isWall(x+1,y) and not (x+1,y) in seen and not (x+1,y) in search:
            search.append((x+1,y))
            if not (x+1,y) in dist:
                dist[(x+1,y)] = dist[(x,y)]+1
        if not isWall(x,y+1) and not (x,y+1) in seen and not (x,y+1) in search:
            search.append((x,y+1))
            if not (x,y+1) in dist:
                dist[(x,y+1)] = dist[(x,y)]+1
    count = 0
    for v in dist:
        if dist[v] <= 50:
            count += 1
    print(count)

#p1()
p2()