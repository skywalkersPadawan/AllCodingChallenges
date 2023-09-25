from itertools import product

firstNumber = map(int, input().split())
secondNumber = map(int, input().split())

print(*product(firstNumber, secondNumber))
