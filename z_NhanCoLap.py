def NhanBinhPhuongCoLap(a, k, n):
    b = 1
    if (k == 0):
        return b
    else:
        binK = bin(k)[::-1]
        if (binK[0] == '1'):
            b = a
        print("%c %d %d" % (binK[0], a, b))
        for i in binK[1:-2]:
            a = (a*a) % n
            if (i == '1'):
                b = (a*b) % n
            print("%c %d %d" % (binK[0], a, b))
    return b


def main():
    a = int(input("a = "))
    k = int(input("k = "))
    n = int(input("n = "))
    print(NhanBinhPhuongCoLap(a, k, n))


if (__name__ == "__main__"):
    main()
