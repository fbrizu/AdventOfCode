input = open('9').readlines()[0].strip()
#input = 'ADVENT'
#input = 'A(1x5)BC'
#input = '(3x3)XYZ'
#input = 'A(2x2)BCD(2x2)EFG'
#input = '(6x1)(1x3)A'
#input = 'X(8x2)(3x3)ABCY'

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

p1()