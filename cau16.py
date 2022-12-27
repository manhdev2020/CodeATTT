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


def sinhMang(n):
    array = []
    for i in range(n):
        array.append(random.randint(0, 9999999999999999))
    return array


def process(n):
    array = sinhMang(n)
    result = []
    for i in array:
        if Miller_Rabin(i, 3):
            result.append(i)
    return result


def main():
    n = int(input("Nhập n: "))
    print("Mảng sinh ngẫu nhiên: ")
    print(sinhMang(n))
    print("Số nguyên tố trong mảng ngẫu nhiên trên: ")
    print(process(n))


if __name__ == '__main__':
    main()
