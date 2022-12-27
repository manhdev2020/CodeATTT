def gcd(a, b):
    if (b == 0):
        return a
    return gcd(b, a % b)


def process(m, n, d):
    result = []
    for i in range(m, n):
        for j in range(m, n):
            if gcd(i, j) == d:
                result.append((i, j))
    return result


def main():
    m = int(input("Nhập M: "))
    n = int(input("Nhập N: "))
    d = int(input("Nhập D: "))
    print("Các cặp số thỏa mãn là: ")
    result = process(m, n, d)
    for i in result:
        print(i)


if __name__ == '__main__':
    main()
