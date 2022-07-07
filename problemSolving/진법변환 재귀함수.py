b2 = []
o8 = []
h16 = []
hex_ = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}

def base2(n):
    if n == 1:
        b2.append(1)
        return
    else:
        b2.append(n%2)
        return base2(n//2)

def base8(n):
    if n <= 7:
        o8.append(n)
        return
    else:
        o8.append(n%8)
        return base8(n//8)

def base16(n):
    if n <= 9:
        h16.append(n)
        return
    elif n <= 15:
        h16.append(hex_[n])
        return

    if n % 16 == 0:
        h16.append(0)
        return base16(n//16)
    else:
        if n % 16 <= 9:
            h16.append(n%16)
        elif n % 16 <= 15:
            h16.append(hex_[n%16])
        return base16(n//16)

n = int(input('10진수 입력 -->'))
base2(n)
base8(n)
base16(n)
print('2진수 :', *b2[::-1])
print('8진수 :', *o8[::-1])
print('16진수 :', *h16[::-1])