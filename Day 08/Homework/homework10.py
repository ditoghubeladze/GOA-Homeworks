# 10. ცვლადში მომხარებელს ინფუთით შემოატანინე მისი ასაკი, და დაუპრინტე თუ რომელი წელი იყო მისი დაბადების დროს.

#asking user yo put his age and turning it into integer
user_age = int(input("Enter you age: "))

#printing user birth year and also printing alternative if he haven't had their birthday in this year yet
print(f"Your birth year is {2024-user_age} or {2023-user_age}")