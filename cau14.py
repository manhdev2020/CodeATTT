def sangNT(n):
    a = [1]*(n+1)
    a[0] = a[1] = 0
    result = []
    for i in range(2, n+1):
        t = (int)(n/i)
        for j in range(2, t+1):
            a[i*j] = 0
    for i in range(100, n+1):
        if a[i]:
            result.append(i)
    return result


def process():
    arrayNT = sangNT(999)
    for i in arrayNT:
        reverse = str(i)[::-1]
        z = int(reverse)
        j = int(z ** (1/3))
        if (j * j * j == z):
            print(i)


def main():
    process()


if __name__ == '__main__':
    main()
