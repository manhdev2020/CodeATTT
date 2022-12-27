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


def sinhSNT():
    z = random.randint(0, 1000)
    while not Miller_Rabin(z, 3):
        z = random.randint(0, 1000)
    return z


def process():
    p = sinhSNT()
    q = sinhSNT()
    while p == q:
        q = sinhSNT()

    result = []
    for i in range(100):
        if Miller_Rabin(pow(i, p, q), 3):
            result.append(str(i))
    return (p, q, result)


def main():
    result = process()
    print(f'Với p = {result[0]} và q = {result[1]} các số a thỏa mã là: {", ".join(result[2])}.')

if __name__ == '__main__':
    main()
