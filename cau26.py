def sangNT(n):
    a = [1]*(n+1)
    a[0] = a[1] = 0
    result = []
    for i in range(2, n+1):
        t = (int)(n/i)
        for j in range(2, t+1):
            a[i*j] = 0
    for i in range(2, int(n ** (1/2)) + 1):
        if a[i]:
            result.append(i)
    return result


def process(n):
    arrayNT = sangNT(n)
    result = []
    for k in range(2, n):
        for i in arrayNT:
            if k % i == 0 and k % (i * i) == 0 and k not in result:
                result.append(k)
    return result


def main():
    n = int(input('Nhập N: '))
    print(process(n))


if __name__ == '__main__':
    main()
