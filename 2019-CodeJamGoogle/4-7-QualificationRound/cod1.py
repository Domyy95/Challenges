import sys


def scrivi(result):
    for i in range(0, len(result)):
        print("Case #{}: {} {}".format(i + 1, result[i][0], result[i][1]))


def ce_quattro(n):
    f = False
    n = int(n)
    s = str(n)
    for i in s:
        c = int(i)
        if c == 4:
            return True

    return False


def scomponi(n):
    stringa = str(n)
    stringa = stringa[::-1]
    dieci = 1
    ret = []
    for st in stringa:
        ret.append((st, dieci))
        dieci = dieci * 10

    return ret


def componi(n):
    numero = 0
    for num in n:
        numero = numero + int(num[0]) * int(num[1])
    return numero


def trova(n):
    n = int(n)
    s = scomponi(n)
    m2 = []
    for i in range(len(s)):
        if int(s[i][0]) == 4:
            s[i] = (3, s[i][1])
            m2.append((1, s[i][1]))

    n1 = componi(s)
    n2 = componi(m2)
    return (n1, n2)


def solution(L):
    results = []
    for n in L:
        results.append(trova(n))

    return results


if __name__ == "__main__":
    # N,L = parse_input(sys.argv[1])
    L = []
    N = int(input())
    for i in range(1, N + 1):
        n = input()
        L.append(n)

    result = solution(L)
    scrivi(result)
