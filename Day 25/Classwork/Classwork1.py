# შექმენით 3 ცვლადი, პირველში და მეორეში მომხმარებელმა უნდა შემოიტანოს რიცხვი ხოლო მესამეში რაიმე ოპერატორი
#  (-, +, /, *) გააკეთეთ კალკულატორის სადაც პირველ რიცხვს გამრავლდება, გაიყოფა, მიემატება ან გამოაკლდება მეორე რიცხვი

print("This is Calculator you can calculate anything here.")


num1 = int(input("Enter first number: "))

num2 = int(input("Enter second number: "))

operator = input("Enter operator (-, +, /, *): ")


if operator == "-":
    print(num1 - num2)
elif operator == "+":
    print(num1 + num2)
elif operator == "/":
    print(num1 / num2)
elif operator == "*":
    print(num1 * num2)
else:
    print("You entered invalid operator.")
