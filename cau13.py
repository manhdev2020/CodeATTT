def sangNT(n):
    a = [1]*(n+1)
    a[0] = a[1] = 0
    result = []
    for i in range(2, n+1):
        t = (int)(n/i)
        for j in range(2, t+1):
            a[i*j] = 0
    for i in range(2, n+1):
        if a[i]:
            result.append(i)
    return result


def process(n):
    arrayNT = sangNT(n)
    result = []
    for i in range(len(arrayNT) - 1):
        for j in range(i+1, len(arrayNT)):
            tong = arrayNT[i] + arrayNT[j]
            hieu = abs(arrayNT[i] - arrayNT[j])
            if tong in arrayNT and hieu in arrayNT:
                result.append((arrayNT[i],arrayNT[j]))
    return result

def main():
    n = int(input("Nhập n: "))
    print(process(n))


if __name__ == '__main__':
    main()
