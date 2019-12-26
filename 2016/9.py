input = open('9').readlines()[0].strip()
#input = 'ADVENT'
#input = 'A(1x5)BC'
#input = '(3x3)XYZ'
#input = 'A(2x2)BCD(2x2)EFG'
#input = '(6x1)(1x3)A'
#input = 'X(8x2)(3x3)ABCY'
#input = '(27x12)(20x12)(13x14)(7x10)(1x12)A'
#input = '(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN'

def p1():
    n = 1
    r = 1
    a = ''
    parsing = False
    i = 0
    p = []
    while i < len(input):
        if input[i] == '(':
            p = []
            parsing = True
            i += 1
        if parsing:
            while input[i] != ')':
                p.append(input[i])
                i += 1
            s = ''.join(p)
            s = s.split('x')
            n = int(s[0])
            r = int(s[1])
            parsing = False
            i += 1
        if not parsing:
            for _ in range(r):
                a += input[i:i+n]
            i += n
            n = 1
            r = 1
    print(len(a))

def calc_char(s, times):
    num = 0
    parsing = False
    i = 0
    n = 1
    r = 1
    while i < len(s):
        if s[i] == '(':
            p = []
            parsing = True
            i += 1
        if parsing:
            while s[i] != ')':
                p.append(s[i])
                i += 1
            ss = ''.join(p)
            ss = ss.split('x')
            n = int(ss[0])
            r = int(ss[1])
            parsing = False
            i += 1
        if not parsing:
            if not '(' in s[i:i+n]:
                num += n * r
            else:
                num += calc_char(s[i:i+n],r)
            i += n
            n = 1
            r = 1
    return num * times

def p2():
    print(calc_char(input, 1))

p1()
p2()