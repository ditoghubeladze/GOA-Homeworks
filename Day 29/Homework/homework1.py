# 1. შექმენით BMI-ის გამომთვლელი ფუნქცია, რომელიც არამარტო ქულას უპრინტავს მომხმარებელს, არამედ ტექსტურად ეუბნება,
#  თუ რომელ წონით კატეგორიაში არის ის, დავალების შესასრულებლად გამოიყენეთ შემდეგი ფორმულა: BMI = Weight / Height **2


user_weight = int(input("Enter your weight (Kg): "))

user_height = float(input("Enter your height(M): "))

bmi = user_weight / user_height ** 2

print(f" Your BMI is - {bmi}")

if bmi <= 18.5:
    print("You are underweight!")
elif  18.5 < bmi <= 24.9:
    print("You are Normal weight!")
elif 25 <= bmi <= 29.9:
    print("You are Overweight!")
elif bmi < 30:
    print("You are Obeese!")






