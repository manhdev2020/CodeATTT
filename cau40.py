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
        y = pow(a, r, n)  # a^r mod n, nhân bình phương có lặp
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


def gcd(a, b):
    if (b == 0):
        return a
    return gcd(b, a % b)


def process(a, n):
    result = []
    d = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if Miller_Rabin(gcd(a[i], a[j]), 3) and (a[i], a[j]) not in result and (a[j], a[i]) not in result:
                result.append((a[i], a[j]))
                d += 1
    return (result, d)


def main():
    n = int(input('Nhập số phần tử của mảng: '))
    a = []
    for i in range(n):
        a.append(int(input(f'Nhập phần tử thứ {i+1}: ')))
    result = process(a, n)
    if result[1] == 0:
        print('Không tồn tại cặp số nào thỏa mã')
    else:
        print(f'Số cặp số thỏa mãn là: {result[1]}')
        print('Các cặp số thỏa mãn là:')
        for i in result[0]:
            print(f'\t{i}')


if __name__ == '__main__':
    main()
