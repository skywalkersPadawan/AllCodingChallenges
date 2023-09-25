if __name__ == "__main__":
    M = int(input().strip())
    set_M = set(map(int, input().strip().split(" ")))
    N = int(input().strip())
    set_N = set(map(int, input().strip().split(" ")))

    for outerLoopVariable in sorted(set_M ^ set_N):
        print(outerLoopVariable)
