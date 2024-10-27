# . შექმენით პროგრამა, სადაც გექნებათ ცვლადი საიდუმლო პაროლით, შემდეგ მომხმარებელს გამაოცნობინეთ სიტყვა, 
# თუ მისი გამოცნობილი სიტყვა უდრის თქვენს საიდუმლო პაროლს, დაუპრინტეთ, რომ გაიმარჯვა.


secret_password = "sandro"


print("You have to guess secret password:")

user_guess = input("Password: ")
while user_guess != secret_password:
    print("Wrong password! Try again!")
    user_guess = input("Password: ")



if user_guess == secret_password:

    print("You won!")