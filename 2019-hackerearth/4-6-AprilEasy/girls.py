import sys


def scrivi(result):
    for i in range(0, len(result)):
        print("Case #{}: {} ".format(i + 1, result[i]))


if __name__ == "__main__":
    line1 = input()
    N, K, P, Q = line1.split(" ")

    L = float(P) / float(Q)

    line2 = input()
    a = list(line2.split(" "))

    a.sort()

    max = 0
    for i in range(0, len(a)):
        t = True
        j = i + 1
        while t and j < len(a):
            if float(a[j]) / int(a[i]) > L or j == len(a) - 1:
                if int(j - i) > max:
                    max = j - i
                t = False
            j = j + 1

    max = max + int(K)
    if max > int(N):
        print(N)
    else:
        print(max)
