# 1. ფუნქცია უნდა პრინტავდეს დამარცვლილ სახელს, შებრუნებულად.


name = input("Enter your name:")

def spell(name):
     result = name[::-1]
     print(result)
    
spell(name)
