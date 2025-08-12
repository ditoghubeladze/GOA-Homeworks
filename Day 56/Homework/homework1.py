def multiply_by_two(numbers):
    result = []
    for num in numbers:
        result.append(num * 2)
    return result

numbers = []

for i in range(5):
    num = int(input("შეიყვანე რიცხვი: "))
    numbers.append(num)

def words_length(words):
    lengths = []
    for word in words:
        lengths.append(len(word))
    return lengths


students = []

for i in range(3):  # 3 სტუდენტი მაგალითად
    name = input("სტუდენტის სახელი: ")
    grades = []
    for j in range(3):  # 3 ქულა თითოეულისთვის
        grade = float(input(f"{name}-ის ქულა {j+1}: "))
        grades.append(grade)
    average = sum(grades) / len(grades)
    students.append((name, average))


def filter_long_strings(words):
    result = []
    for word in words:
        if len(word) > 3:
            result.append(word)
    return result