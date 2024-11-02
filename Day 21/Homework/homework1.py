# 1. შექმენით სია, სადაც გექნებათ 4 სტრინგი, შემდეგ კი indexing-ის მეშვეობით გამოიტანეთ მეორე ელემენტი.

movies = ['Fight club','Harry Potter', 'American Psycho', 'The Truman Show']

print(movies[1])


# 2. შექმენით სია, სადაც გექნებათ 4 სტრინგი, შემდეგ კი შეცვალეთ მეორე ინდექსი სხვა მნიშვნელობით.


movies[1]= "It"

print(movies[1])


# 3. შექმენით სია, სადაც გექნებათ 5 სტრინგი, შემდეგ კი slicing-ის მეშვეობით გამოიტანეთ პირველი და მეორე ელემენტი (positive indexing).


fruits = ['apple','orange','watermelon','pineapple','banana']

print(fruits[0:2])

# 4. შექმენით სია, სადაც გექნებათ 5 სტრინგი, შემდეგ კი slicing-ის მეშვეობით გამოიტანეთ პირველი და მეორე ელემენტი (negative indexing).

print(fruits[-5:-3])


# 5. შექმენით სია, სადაც გექნებათ 6 სტრინგი,
#  შემდეგ კი slicing-ის მეშვეობით გამოიტანეთ პირველი და მეოთხე ელემენტი (negative indexing & positive indexing).

fruits = ['apple','orange','watermelon','pineapple','banana','peach']

print(fruits[0:4])

print(fruits[-6:-2])


