import random


def Miller_Rabin(n, k):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    # tìm s, r sao cho n - 1 = 2^s * r với r là số lẻ
    s = 0
    r = n - 1
    while r % 2 == 0:
        s += 1
        r //= 2
    for _ in range(k):
        a = random.randrange(2, n - 1)
        y = NhanBinhPhuongCoLap(a, r, n) # a^r mod n, nhân bình phương có lặp
        if (y != 1 and y != n-1):
            j = 1
            while (j <= s-1 and y != n-1):
                y = (y*y) % n
                if (y == 1):
                    return False
                j += 1
            if (y != n-1):
                return False
    return True

def NhanBinhPhuongCoLap(a, k, n):
    b = 1
    if (k == 0):
        return b
    else:
        binK = bin(k)[::-1]
        if (binK[0] == '1'):
            b = a
        for i in binK[1:-2]:
            a = (a*a) % n
            if (i == '1'):
                b = (a*b) % n
    return b

def sntDuoi(n):
    i = n
    while not Miller_Rabin(i, 3):
        i -= 1
    return i


def sntTren(n):
    i = n
    while not Miller_Rabin(i, 3):
        i += 1
    return i


def timK(n):
    if n <= 1:
        return sntTren(n)
    tren = sntTren(n)
    duoi = sntDuoi(n)
    dodai1 = tren - n
    dodai2 = n - duoi
    if dodai1 == dodai2 or dodai2 < dodai1:
        return duoi
    return tren


def main():
    a = int(input('Nhập số báo danh: '))
    k = timK(a)
    print(f'k = {k}')
    print(NhanBinhPhuongCoLap(a, k, 123456))


if __name__ == '__main__':
    main()
