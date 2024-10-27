# 3. შექმენი პროგრამა, სადაც მომხმარებელს შემოატანინებ მის ასაკს, თუ მისი ასაკი მეტია 10-ზე, 
# დაუპრინტე რამდენი წლის იქნება 15 წლის შემდეგ, თუ მისი ასაკი ნაკლებია 10-ზე დაუპრინტე რამდენი წლის იყო 5 წლის წინ.


user_age = int(input("Enter your age: "))


if user_age >= 15:
    print(f"In 15 years, you will be {user_age+15} years old.")
elif 0 < user_age < 10:
    print(f"5 years ago you were {user_age-5} years old.")
