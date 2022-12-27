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
    for i in arrayNT:
        b = i + 2
        if b in arrayNT:
            result.append((i, b))
    return result

def main():
    n = int(input("Nhập n: "))
    result = process(n)
    for i in result:
        print(i)

if __name__ == '__main__':
    main()
