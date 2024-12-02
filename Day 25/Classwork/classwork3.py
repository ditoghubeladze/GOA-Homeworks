# დაწერეთ while ციკლი სადაც მომხმარებელს შემოატანინებს სიტყვას მანამდე სანამ მისი სიტყვა არ დაემთხვევა password - ს


password = "goa"


guess = input("Guess password: ")

while guess != password:
    print("Try again!")
    guess = input("Guess password: ")


print("Password is corret. Congrats you won! ")