class Solution:
    def absolute(self, I):
        absolute_value = abs(I)
        return absolute_value


# the main driver code will start here
def main():
    T = int(input())
    while T > 0:
        I = int(input())
        ob = Solution()
        print(ob.absolute(I))
        T -= 1


if __name__ == "__main__":
    main()
