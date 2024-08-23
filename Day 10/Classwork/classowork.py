# 1. დაწერეთ conditional statmenet-ის 8 მაგალითი, გამოიყენეთ and და or.

print(True and False)
print(True and True)
print(False and False)
print(False and True)

print(True or False)
print(True or True)
print(False or False)
print(False or True)


# 2. დაწერეთ comparison operator-ებზე 9 მაგალითი (>, <, >=..)

print(3 > 4)
print(5 > 2)
print(7 < 9)
print(12 < 4)
print(8 >= 2)
print(9 >= 10)
print(7 != 4)
print(10 != 10)
print(11 <= 10)
print( 1 <= 0)


# 3. გადააქციეთ True და False ინტეჯერებად და დაპრინტეთ.

num1 = int(5 > 0)
num2 = int(10 > 11)

print(num1)

print(num2)

print(num1 or num2)


# 4. მომხმარებელს ინფუთით შემოატანინეთ რიცხვი, თუ 5-ზე მეტია, გამოიტანოს True.


user_number = int(input("enter number:"))


print(bool(user_number) > 5)