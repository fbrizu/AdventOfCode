input = open('18').readlines()

def isint(n):
    try:
        int(n)
        return True
    except ValueError:
        return False

def p1():
    r = {}
    for i in range(26):
        r[chr(ord('a') + i)] = 0
    pc = 0
    freq = 0
    while pc < len(input):
        ins = input[pc].split()
        if ins[0] == 'snd':
            if isint(ins[1]):
                freq = int(ins[1])
            else:
                freq = r[ins[1]]
            pc += 1
        elif ins[0] == 'set':
            if isint(ins[2]):
                r[ins[1]] = int(ins[2])
            else:
                r[ins[1]] = r[ins[2]]
            pc += 1
        elif ins[0] == 'add':
            if isint(ins[2]):
                r[ins[1]] += int(ins[2])
            else:
                r[ins[1]] += r[ins[2]]
            pc += 1
        elif ins[0] == 'mul':
            if isint(ins[2]):
                r[ins[1]] *= int(ins[2])
            else:
                r[ins[1]] *= r[ins[2]]
            pc += 1
        elif ins[0] == 'mod':
            if isint(ins[2]):
                r[ins[1]] %= int(ins[2])
            else:
                r[ins[1]] %= r[ins[2]]
            pc += 1
        elif ins[0] == 'rcv':
            a = freq
            pc += 1
            break
        elif ins[0] == 'jgz':
            b = False
            if isint(ins[1]):
                b = int(ins[1]) > 0
            else:
                b = r[ins[1]] > 0
            if b > 0:
                if isint(ins[2]):
                    pc += int(ins[2])
                else:
                    pc += r[ins[2]]
            else:
                pc += 1
    print(a)

f0 = []
f1 = []

class Program:
    def __init__(self, r, pc, num):
        self.r = r
        self.pc = pc
        self.num = num

p2_ans = 0

def run(p : Program):
    global p2_ans
    while p.pc < len(input):
        ins = input[p.pc].split()
        if ins[0] == 'snd':
            if isint(ins[1]):
                if p.num == 0:
                    f1.append(int(ins[1]))
                    #print('P0 sends {}'.format(ins[1]))
                else:
                    p2_ans += 1
                    f0.append(int(ins[1]))
                    #print('P1 sends {}'.format(ins[1]))
            else:
                if p.num == 0:
                    f1.append(p.r[ins[1]])
                    #print('P0 sends {}'.format(p.r[ins[1]]))
                else:
                    p2_ans += 1
                    f0.append(p.r[ins[1]])
                    #print('P1 sends {}'.format(p.r[ins[1]]))
            p.pc += 1
        elif ins[0] == 'set':
            if isint(ins[2]):
                p.r[ins[1]] = int(ins[2])
            else:
                p.r[ins[1]] = p.r[ins[2]]
            p.pc += 1
        elif ins[0] == 'add':
            if isint(ins[2]):
                p.r[ins[1]] += int(ins[2])
            else:
                p.r[ins[1]] += p.r[ins[2]]
            p.pc += 1
        elif ins[0] == 'mul':
            if isint(ins[2]):
                p.r[ins[1]] *= int(ins[2])
            else:
                p.r[ins[1]] *= p.r[ins[2]]
            p.pc += 1
        elif ins[0] == 'mod':
            if isint(ins[2]):
                p.r[ins[1]] %= int(ins[2])
            else:
                p.r[ins[1]] %= p.r[ins[2]]
            p.pc += 1
        elif ins[0] == 'rcv':
            if p.num == 0:
                if len(f0) > 0:
                    rr = f0.pop(0)
                    p.r[ins[1]] = rr
                    #print('P0 reads {}'.format(rr))
                else:
                    return
            else:
                if len(f1) > 0:
                    rr = f1.pop(0)
                    p.r[ins[1]] = rr
                    #print('P1 reads {}'.format(rr))
                else:
                    return
            p.pc += 1
            break
        elif ins[0] == 'jgz':
            b = False
            if isint(ins[1]):
                b = int(ins[1]) > 0
            else:
                b = p.r[ins[1]] > 0
            if b > 0:
                if isint(ins[2]):
                    p.pc += int(ins[2])
                else:
                    p.pc += p.r[ins[2]]
            else:
                p.pc += 1

def p2():
    r0 = {}
    for i in range(26):
        r0[chr(ord('a') + i)] = 0
    r1 = {}
    for i in range(26):
        r1[chr(ord('a') + i)] = 0
    r1['p'] = 1
    p0 = Program(r0,0,0)
    p1 = Program(r1,0,1)

    run(p0)
    run(p1)
    while len(f0) > 0 or len(f1) > 0:
        run(p0)
        run(p1)
    print(p2_ans)


p1()
p2()