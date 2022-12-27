import random


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

def main():
    a = int(input('Nhập a: '))
    k = int(input('Nhập k: '))
    n = int(input('Nhập n: '))
    result = NhanBinhPhuongCoLap(a, k ,n)
    print(result)
    if Miller_Rabin(result, 3):
        print(f'{a} ^ {k} mod {n} là số nguyên tố')
    else:
        print(f'{a} ^ {k} mod {n} là hợp số')
        

if __name__ == '__main__':
    main()