# 3. შექმენით ფუნქცია რომელიც არგუმენტად აიღებს თქვენს შექმნილ სიას, რომელშიც იქნება მინიმუმ 5 რიცხვი და დაპრინტავს ამ სიისის მაქსიმალურ რიცხვს, მინიმალურ რიცხვს, რიცხვების ჯამს და სიის სიგრძეს.

numbers = [12, 8342, 578000, 119, 138]


def list(numbers):
    
    ma = max(numbers)
    mi = min(numbers)
    summ = sum(numbers)
    le = len(numbers)

    print("მაქსი", ma)
    print("მინი:", mi)
    print(" ჯამი:", summ)
    print(" სიგრძე:", le)



list(numbers)