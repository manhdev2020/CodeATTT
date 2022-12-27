import random

def Miller_Rabin(n, k=10):
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
        y = pow(a, r, n) # a^r mod n, nhân bình phương có lặp
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


def sangNT(start, b):
    a = [1]*(b+1)
    a[0] = a[1] = 0
    result = []
    for i in range(2, b+1):
        t = (int)(b/i)
        for j in range(2, t+1):
            a[i*j] = 0
    for i in range(start, b+1):
        if a[i] == 1:
            result.append(i)
    return result


def process(a, b):
    arrayNT = sangNT(a, b)
    print(arrayNT)
    s = sum(arrayNT)
    print(f'tong la: {s}')
    if Miller_Rabin(s):
        return True
    return False


def main():
    a = int(input('Nhập A: '))
    b = int(input('Nhập B: '))
    if process(a, b):
        print("YES")
    else:
        print('NO')


if __name__ == '__main__':
    main()
