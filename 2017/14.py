input = 'ugkiagan'
#input = 'flqrgnkx'

def knot_hash(s):
    l = [i for i in range(256)]
    lengths = [ord(i) for i in s]
    lengths.append(17)
    lengths.append(31)
    lengths.append(73)
    lengths.append(47)
    lengths.append(23)
    curr = 0
    skip = 0
    for _ in range(64):
        for n in lengths:
            i1 = curr
            i2 = curr+n-1
            while i1 < i2:
                temp = l[i1 % len(l)]
                l[i1 % len(l)] = l[i2 % len(l)]
                l[i2 % len(l)] = temp
                i1 += 1
                i2 -= 1
            curr += n + skip
            skip += 1
    h = []
    for j in range(16):
        x = 0
        for i in range(16):
            if i == 0:
                x = l[j*16+i]
            else:
                x ^= l[j*16+i]
        h.append(x)
    a = ''
    for n in h:
        t = hex(n)[2:]
        if len(t) == 1:
            t = '0' + t
        a += t
    return a

def print_board(g):
    xlen = len(g[0])
    ylen = len(g)
    for j in range(ylen):
        for i in range(xlen):
            if g[j][i]:
                print('#', end='')
            else:
                print('.', end='')
        print('')

def hex_to_bit(d):
    return bin(int(d, 16))[2:].zfill(len(d)*4)

def p1():
    g = []
    for _ in range(128):
        g.append([False] * 128)
    for n in range(128):
        s = '{}-{}'.format(input, n)
        h = knot_hash(s)
        for i,c in enumerate(hex_to_bit(h)):
            if c == '1':
                g[n][i] = True
    #print_board(g)
    count = 0
    for j in range(128):
        for i in range(128):
            if g[j][i]:
                count += 1
    print(count)

def traverse(g,i,j,t):
    seen = []
    search = [(i,j)]
    while len(search) > 0:
        ii,jj = search[0]
        if ii > 0 and g[jj][ii-1] and not (ii-1,jj) in seen and not (ii-1,jj) in search:
            search.append((ii-1,jj))
        if jj > 0 and g[jj-1][ii] and not (ii,jj-1) in seen and not (ii,jj-1) in search:
            search.append((ii,jj-1))
        if ii < len(g[0])-1 and g[jj][ii+1] and not (ii+1,jj) in seen and not (ii+1,jj) in search:
            search.append((ii+1,jj))
        if jj < len(g)-1 and g[jj+1][ii] and not (ii,jj+1) in seen and not (ii,jj+1) in search:
            search.append((ii,jj+1))
        x = search.pop(0)
        seen.append(x)
        t.append(x)
    return t

def p2():
    input = open('14').readlines()
    g = []
    for _ in range(128):
        g.append([False] * 128)
    for j,line in enumerate(input):
        for i,c in enumerate(line):
            if c == '#':
                g[j][i] = True
    count = 0
    for j in range(128):
        for i in range(128):
            if g[j][i]:
                count += 1
    t = []
    #8292
    a = 0
    for j in range(128):
        for i in range(128):
            if g[j][i] and not (i,j) in t:
                t = traverse(g,i,j,t)
                a += 1
    print(a)

p1()
p2()