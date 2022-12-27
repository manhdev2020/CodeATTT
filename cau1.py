def check(n):
    d = 0
    for i in range(2, (int)(n/2)+1):
        if n % i == 0:
            d += 1
            if d > 2:
                break
    if d == 2:
        return True
    else:
        return False


def main():
    n = int(input())
    result = []
    for i in range(1, n+1):
        if check(i):
            result.append(i)
    if len(result) == 0:
        print("No")
    else:
        for i in result:
            print(i)


if __name__ == '__main__':
    main()
