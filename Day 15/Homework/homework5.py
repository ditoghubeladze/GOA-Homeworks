# 5. დაწერეთ პროგრამა, რომელიც სთხოვს მომხმარებელს შეიყვანოს ორი რიცხვი და ამოწმებს რომელია უფრო დიდი, ან ტოლია თუ არა ისინი


num1 = int(input("Enter number: "))

num2 = int(input("Enter another number: "))

if num1 > num2:
    print(f"{num1} is higher than {num2}.")

elif num2 > num1:
    print(f"{num2} is higher than {num1}.")
else:
    print("Numbers are equal")
