
def bin1():
    a = 2
    print(a)
    b = bin(a)
    print(b)
    print(type(b))
    c = 1
    print(c << 2)

def bin2():
    bb = 0
    for n in range(16):
        b = 1 << n
        bb = bb | b
        print(n,b,bin(b),bin(bb))
    
    for n in range(48,64):
        b = 1 << n
        bb = bb | b
        print(n,b,bin(b),bin(bb))

    

if __name__ == '__main__':
    bin2()