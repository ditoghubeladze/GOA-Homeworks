# 1) შექმენით 5 ელემენტიანი სია და ამოაგდეთ მე-0-ე და მე-4-ე ინდექსზე მდგომი ელემენტები


names = ["dito", "achiko", "sandro", "dachi", "ilia"]

names.pop(0)
names.pop(3)


# 2) შექმენით 5 ელემენტიანი სია და მე-2-ე და მე-3-ე ინდეხებზე დაამატეთ 2 ელემენტი

names = ["dito", "achiko", "sandro", "dachi", "ilia"]

names.insert(2, 'giorgi')
names.insert(3, 'goa')


# 3) შექმენით 5 ელემენტიანი სია და მის ბოლოში დაამატეთ 3 ელემენტი. inspect-ი არ გამოიყენოთ

names = ["dito", "achiko", "sandro", "dachi", "ilia"]

names.append('lasha')
names.append('gio')
names.append('nika')


# 4) შექმენით დიდი სია და დაითვალეთ მასში რამდენი ელემენტია


names = ["dito", "achiko", "sandro", "dachi", "ilia","gio",'lasha','irakli','aleqsi','levani','giorgi']

print(len(names))
