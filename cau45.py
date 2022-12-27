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


def sinhMangA(n):
    result = []
    for _ in range(n):
        temp = random.randint(2, 9999999999999999999)
        while not Miller_Rabin(temp, 3):
            temp = random.randint(2, 9999999999999999999)
        result.append(temp)
    return result


def main():
    n = int(input('Nhập N: '))
    A = sinhMangA(n)
    print(f'A = {A}')
    A = sorted(A)
    m = abs(A[0] - A[1])
    for i in range(1, n-1):
        m = min(m, abs(A[i] - A[i+1]))
    print(f'Khoảng cách nhỏ nhất là: {m}')


if __name__ == '__main__':
    main()
