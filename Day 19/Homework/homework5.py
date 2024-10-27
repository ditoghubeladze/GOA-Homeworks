
# BONUS

#  შექმენით ვენდინგ მანქანის თამაში პითონის მეშვეობით, როგორც გაკვეთილზე გავაკეთე,
#  უნდა გქონდეთ პროდუქტები, მომხმარებელს უნდა შეეძლოს არჩევა რიცხვის მიხედვით, 
# შემდეგ კი უნდა დაუპრინტოს ის პროდუქტი, რომელიც ამოირჩია, პროდუქტები შეინახეთ სიაში.


vending_machine = ["Coca-Cola", "Chips", "Energy Drink", "Pepsi", "Snickers", 'Bubblegum']

print('Vending Machine')

print('Product list:')

print(f'0 - {vending_machine[0]}')
print(f'1 - {vending_machine[1]}')
print(f'2 - {vending_machine[2]}')
print(f'3 - {vending_machine[3]}')
print(f'4 - {vending_machine[4]}')
print(f'5 - {vending_machine[5]}')

user_choice = int(input("Choose product: "))


print(f"You've purchased {vending_machine[user_choice]}.")