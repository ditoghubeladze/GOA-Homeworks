# # . შექმენით ფუნქცია, სადაც გექნებათ 5 ელემენტიანი სია, 
# ფუნქციაში შექმენით ცვლადი, სადაც შეინახავთ secret ინდექსის ციფრს, 
# შემდეგ კი მომხმარებელმა სიიდან უნდა აირჩიოს რომელიმე ელემენტი, თუ ელემენტის ინდექსი დაემთხვა secret_index-ს,
#  დაუბრუნეთ რომ მან მოიგო ჩელენჯი.

def function():
    names = ["Dito", "Nika", "Sandro", "Achiko", "Giorgi"]

   

    secret = 2
    print(names)
    user_guess = int(input("Choose any element (0-4): "))

    if user_guess == secret:
        print ("You chose same element as me. You won!")
    else:
        print("You didn't chose same element as me. You lost!")

function()