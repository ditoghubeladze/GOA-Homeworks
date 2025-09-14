products = ["ვაშლი", "ბანანი", "საზამთრო", "ფორთოხალი", "კივი"]

try:
    user_input = input("შეიყვანეთ პროდუქტის ინდექსი: ")
    index = int(user_input)  
    if index >= len(products):
        raise IndexError("ასეთი ინდექსი სიაში არ არსებობს!") 
    
    print("თქვენ აირჩიეთ:", products[index])

except ValueError:
    print("Error: გთხოვთ შეიყვანოთ მხოლოდ რიცხვი.")
finally:
    print("მადლობა პროგრამის გამოყენებისთვის!")
