# 1. სამი list-ი და მათგან მაქსიმალური რიცხვების ბეჭდვა
list1 = [5, 12, 7, 3, 9]
list2 = [8, 22, 15, 2, 14]
list3 = [6, 19, 11, 4, 17]

print("Max numbers:", max(list1), max(list2), max(list3))

# 2. სამი list-ი და მათგან მინიმალური რიცხვების ბეჭდვა
print("Min numbers:", min(list1), min(list2), min(list3))

# 3. სამი list-ი და მათი სიგრძის ბეჭდვა
list4 = ["a", "b", "c", "d", "e"]
list5 = ["x", "y", "z", "w", "v"]
list6 = [10, 20, 30, 40, 50, 60]

print("List lengths:", len(list4), len(list5), len(list6))

# 4. სამი list-ი და მათგან რიცხვების ჯამი
print("Sum of numbers:", sum(list1), sum(list2), sum(list3))

# 5. ოთხი list-ი მინიმუმ 10 ელემენტით
list7 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list8 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
list9 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
list10 = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]

# 5.1 პირველი list-ის პირველიდან მეოთხე ელემენტამდე ბეჭდვა
print("First 4 elements:", list7[:4])

# 5.2 მეორე list-ის მეოთხედან მერვე ელემენტამდე for ციკლით
print("4th to 8th elements:", [list8[i] for i in range(3, 8)])

# 5.3 მესამე list-ის მეცხრედან მეექვსე ელემენტამდე (უარყოფითი ინდექსებით)
print("9th to 6th elements (reverse):", list9[8:5:-1])

# 5.4 მეოთხე list-ის ყველა ელემენტი while ციკლით
i = 0
while i < len(list10):
    print(list10[i], end=" ")
    i += 1
print()

# 6. ფუნქცია, რომელიც list-ის მაქსიმუმს, მინიმუმს, ჯამს და სიგრძეს ბეჭდავს
def analyze_list(numbers):
    print("Max:", max(numbers))
    print("Min:", min(numbers))
    print("Sum:", sum(numbers))
    print("Length:", len(numbers))

# ფუნქციის გამოძახება მომხმარებლის შეყვანილი list-ით
user_list = list(map(int, input("Enter at least 5 numbers separated by space: ").split()))
analyze_list(user_list)
