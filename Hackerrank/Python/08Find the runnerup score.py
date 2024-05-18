def findRunnerUpScore(scores):
    uniqueScores = sorted(set(scores), reverse=True)
    return uniqueScores[1]


if __name__ == "__main__":
    n = int(input())
    scores = list(map(int, input().split()))

    runnerUpScore = findRunnerUpScore(scores)
    print(runnerUpScore)
