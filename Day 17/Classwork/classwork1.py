# 1. შექმენით პროგრამა, სადა მომხმარებეს შემოატანინებთ ასაკს, თუ მისი ასაკი იქნება 18-ის ტოლი ან მეტი,
#  გამოუტანეთ რომ ის ზრდასრულია, თუ იქნება ნაკლები, გამოუტანეთ, რომ ჯერ პატარაა.


user_age = int(input("Enter your age: "))


if user_age >= 18:
    print("You are an adult")

else:
    print("You are still young")