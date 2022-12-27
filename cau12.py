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
    for i in range(n):
        z = sum(arrayNT[i:i+4])
        if z > n:
            break
        if z in arrayNT:
            s = []
            for z in arrayNT[i:i+4]:
                s.append(str(z))
            result.append(s)
    return result



def main():
    n = int(input("Nhập n: "))
    print(sangNT(n))
    result = process(n)
    for i in result:
        print(f"Các số đó là: {(', ').join(i)} ", end=' | ')
        s = 0
        for z in i:
            s += int(z)
        print(s)
        


if __name__ == '__main__':
    main()
