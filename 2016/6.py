input = open('6').readlines()

def solve(p1):
    v = []
    for _ in range(8):
        v.append({})
    for line in input:
        line = line.replace('\n', '')
        ind = 0
        for c in line:
            if c in v[ind]:
                v[ind][c] += 1
            else:
                v[ind][c] = 1
            ind += 1
    a = ''
    for p in v:
        p = {k:v for k,v in sorted(p.items(), key=lambda x: x[1], reverse=p1)}
        a += list(p.keys())[0]
    print(a)

solve(True) #p1
solve(False) #p2