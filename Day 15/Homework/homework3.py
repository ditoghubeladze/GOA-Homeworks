# 3. სთხოვეთ მომხმარებელს შემოიტანოს მისი შეფასება (0-100) და დაპრინტეთ, ჩააბარა თუ არა მოსწავლემ (>= 50) ჩააბარა, თუ(< 50) ვერ.


user_grade = int(input("Enter your grade (1-100): "))

if 100 >= user_grade >= 50:
    print("You have passed.")

elif user_grade < 50 >= 0:
    print('You failed')

else:
    print("Please enter number between 1-100!")