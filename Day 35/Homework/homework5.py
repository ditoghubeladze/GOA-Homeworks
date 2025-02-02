list7 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list8 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
list9 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
list10 = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]



print(list7[:4])


print([list8[i] for i in range(3, 8)])


print(list9[8:5:-1])

i = 0
while i < len(list10):
    print(list10[i], end=" ")
    i += 1
print()