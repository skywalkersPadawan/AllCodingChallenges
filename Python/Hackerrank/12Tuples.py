if __name__ == "__main__":
    n = int(input())
    elements = input().split()
    integerTuple = tuple(map(int, elements))
    print(hash(integerTuple))
