# 2. შექმენით ფუნქცია, რომელსაც გადაეცემა 5 არგუმენტი, 5 ინფუთით მომხარებელს აარჩევინეთ ნებისმიერი რიცხვი, ბოლოს კი დაუპრინტეთ ამ რიცხვებისაგან შემდგარი სია.


def function(num1 ,num2 ,num3 ,num4 , num5):
    
    numbers = [num1 ,num2 ,num3,num4 , num5]
    print("number list:", numbers)


num1 = int(input(" first : "))
num2 = int(input("second : "))
num3 = int(input(" third : "))
num4 = int(input(" fourth : "))
num5 = int(input(" fifth : "))

function(num1 ,num2 ,num3 ,num4 , num5)