#11. ცვლადში მომხმარებელს ინფუთით შემოატანინე მისი ასაკი, მეორე ცვლადში კი მამამისის ასაკი, საბოლოოდ დაუპრინტე, თუ რამდენჯერ დიდი იქნება მამამისი მასზე 15 წლის შემდეგ.

# asking user to put his age and turning it into integer
user_age = int(input("Enter your age: "))

# asking user to put his father's age and turning it into integer
father_age = int(input("Enter you Father's age: "))

#printing how much older will be father than son in 15 years
print(f"In 15 years, your Father will be {father_age+15} years old and you will be {user_age+15} years old. Your father will be {father_age-user_age} years older than you.")