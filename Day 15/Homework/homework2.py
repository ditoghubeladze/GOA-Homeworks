# 2. შექმენით პროგრამა, რომელიც ატანინებს მომხმარებლის ასაკს და განსაზღვრავს, აქვს თუ არა მას ხმის მიცემის უფლება (18 წლის და მეტი).


user_age = int(input("Enter your age: "))



if user_age >= 18:
    print("You can vote!")
else:
    print('You are under 18!')