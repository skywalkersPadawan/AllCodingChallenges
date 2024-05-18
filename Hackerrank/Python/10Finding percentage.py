def findAveragePercentage(records, studentName):
    if studentName in records:
        marks = records[studentName]
        averagePercentage = sum(marks) / len(marks)
        return "{:.2f}".format(averagePercentage)


if __name__ == "__main__":
    n = int(input())
    studentRecords = {}
    for i in range(n):
        record = input().split()
        name = record[0]
        marks = list(map(float, record[1:]))
        studentRecords[name] = marks

    studentNameToFind = input()
    result = findAveragePercentage(studentRecords, studentNameToFind)
    print(result)
