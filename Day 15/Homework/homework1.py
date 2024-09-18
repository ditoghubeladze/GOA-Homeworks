# 1. დაწერეთ პროგრამა, რომელიც ამოწმებს, არის თუ არა რიცხვი დადებითი, უარყოფითი ან ნული და შესაბამისად დაპრინტეთ შეტყობინება.

num = int(input("Enter any number: "))

if num > 0:
    print("Number is positive.")

elif num == 0:
   print("Number is 0.")
   
else:
    print("Number is negative.")
