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


def process(l, r):
    result = 0
    for i in range(l, r):
        for j in range(i+1, r+1):
            y = z = 0  # y = F(i); z = F(j)
            if Miller_Rabin(i):
                y = i
            if Miller_Rabin(j):
                z = j
            result += y * z
    return result


def main():
    l = int(input("Nhập L: "))
    r = int(input("Nhập R: "))
    print(process(l, r))


if __name__ == '__main__':
    main()
