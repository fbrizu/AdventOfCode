input = open('12').readlines()

def isint(n):
    try:
        int(n)
        return True
    except ValueError:
        return False

def p1():
    r = {}
    for i in range(4):
        r[chr(ord('a') + i)] = 0
    r['c'] = 1
    pc = 0
    while pc < len(input):
        line = input[pc]
        s = line.strip().split()
        if line.startswith('cpy'):
            if isint(s[1]):
                r[s[2]] = int(s[1])
            else:
                r[s[2]] = r[s[1]]
            pc += 1
        elif line.startswith('inc'):
            r[s[1]] += 1
            pc += 1
        elif line.startswith('dec'):
            r[s[1]] -= 1
            pc += 1
        elif line.startswith('jnz'):
            jump = False
            if isint(s[1]):
                jump = int(s[1]) != 0
            else:
                jump = r[s[1]] != 0
            if jump:
                if isint(s[2]):
                    pc += int(s[2])
                else:
                    pc += r[s[2]]
            else:
                pc += 1
    print(r['a'])

p1()

#cpy 41 a
#inc a
#inc a
#dec a
#jnz a 2
#dec a