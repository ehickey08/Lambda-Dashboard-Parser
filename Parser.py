import csv

with open('data.txt', 'r') as file:
    data = []
    student = []
    for index, line in enumerate(file):
        if index % 11 == 0:
            data.append(student)
            student = []
        student.append(line.strip())
    data.append(student)

with open('data.csv', 'w+', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    for student in data:
        writer.writerow(student)