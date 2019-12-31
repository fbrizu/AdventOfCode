def checksum(n):
    r = []
    i = 0
    while i+1 < len(n):
        if n[i]^n[i+1] == 0:
            r.append(1)
        else:
            r.append(0)
        i += 2
    if len(r) % 2 == 1:
        return r
    else:
        return checksum(r)

#print(checksum([1,1,0,0,1,0,1,1,0,1,0,0]))

def dragon(a, l):
    b = []
    for i in range(len(a)):
        if a[len(a) - 1 - i] == 0:
            b.append(1)
        else:
            b.append(0)
    r = a + [0] + b
    if len(r) >= l:
        return r[0:l]
    else:
        return dragon(r,l)

#print(dragon([1,1,1,1,0,0,0,0,1,0,1,0],25))

def solve(input, l):
    n = []
    for c in input:
        n.append(int(c))
    r = checksum(dragon(n,l))
    for n in r:
        print(n, end='')

#solve('10000',20)

solve('01110110101001000',272)
solve('01110110101001000',35651584)