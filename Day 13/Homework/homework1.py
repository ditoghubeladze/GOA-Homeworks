# 1. for loop-ის მეშვეობით გამოიტანეთ რიცხვი 10, 7-ჯერ.


for i in range(7):
    print(10)


# 2. for loop-ის მეშვეობით გამოიტანეთ 'hello' 8-ჯერ.

for i in range(8):
    print("Hello")


# 3. Input()-ის გამოყენებით მომხმარებელს შემოატანინეთ მისი სახელი,
# შემდეგ for loop-ით კი დაპრინტეთ ("hello" + მომხმარებლის სახელი) 5 ჯერ.

user_name = input("Enter your name: ")

for i in range(5):
    print(f"Hello {user_name}!")
