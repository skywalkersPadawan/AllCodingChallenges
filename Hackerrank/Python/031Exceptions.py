numberOfTests = int(input())
for i in range(numberOfTests):
    try:
        firstNumber, secondNumber = map(int, input().split())
        print(firstNumber // secondNumber)
    except Exception as e:
        print("Error Code:", e)
