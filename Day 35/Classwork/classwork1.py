# # 1.
# * შექმენი ფუნქცია სახელად max_of_two, რომელიც 
# არგუმენტად იღებს ორ რიცხვს. 
# * ფუნქციამ უნდა დააბრუნოს და დაპრინტოს ამ
# ორი რიცხვიდან უფრო დიდი. 

def max_of_two(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

print(max_of_two(10,11))