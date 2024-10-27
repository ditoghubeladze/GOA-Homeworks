# 1. შექმენი პროგრამა, სადაც მომხმარებელს შემოატანინებ თავის, შემდეგ კი მეგობრის  ასაკს,
#  თუ მეგობრის ასაკი მეტია მის ასაკზე, დაუპრინტე რომ პატარაა, თუ მისი ასაკი მეტია მეგობრის ასაკზე, დაუპრინტე რომ დიდია.




user_age = int(input("Enter you age: "))


user_friend_age = int(input("Enter your friend's age: "))


if user_age > user_friend_age:
    print("You are older than your friend.")
elif user_age < user_friend_age:
    print("Your friend is older than you.")
else:
    print("You and your friend are same age.")