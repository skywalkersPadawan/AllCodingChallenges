import math


class Solution:
    def cToF(self, C):
        F = ((9 / 5) * C) + 32
        return F


def main():

    T = int(input())

    while T > 0:
        C = int(input())
        ob = Solution()
        print(math.floor(ob.cToF(C)))
        T -= 1


if __name__ == "__main__":
    main()
