# 13. შექმენით while loop'ი რომელიც დათვლის რიცხვებს 1დან 100მდე თუმცა გამოტოვებს რიცხვებს 50დან 60მდე.


num = 1
while num <= 100:
    if num < 50 or num > 60:
        print(num)
    num += 1