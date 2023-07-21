def findSecondLowest(student):
    grades = set([student[1] for student in students])
    secondLowestGrade = sorted(grades)[1]
    secondLowestStudents = sorted(
        [student[0] for student in students if student[1] == secondLowestGrade]
    )

    return secondLowestStudents


if __name__ == "__main__":
    n = int(input())
    students = []
    for i in range(n):
        name = input()
        grade = float(input())
        students.append([name, grade])

    secondLowestStudents = findSecondLowest(students)
    for student in secondLowestStudents:
        print(student)
