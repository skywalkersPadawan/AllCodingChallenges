from collections import namedtuple

number = int(input())
fields = input().split()

total_marks = 0
for i in range(number):
    students = namedtuple("student", fields)
    MARKS, CLASS, NAME, ID = input().split()
    student = students(MARKS, CLASS, NAME, ID)
    total_marks += int(student.MARKS)
print("{:.2f}".format(total_marks / number))
