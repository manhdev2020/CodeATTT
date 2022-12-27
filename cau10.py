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


def process(n):
    soUoc = SNT = 0
    for i in range(1, n+1):
        if n % i == 0:
            soUoc += 1
            if Miller_Rabin(i):
                SNT += 1
    return (soUoc, SNT)


def main():
    n = int(input("Nhập n: "))
    a = process(n)
    print("Số ước của %d là: %d\nSố ước nguyên tố nhỏ hơn %d là: %d" %
          (n, a[0], n, a[1]))


if __name__ == '__main__':
    main()
