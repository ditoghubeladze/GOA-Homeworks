# 1. ფუნქცია უნდა პრინტავდეს დამარცვლილ სახელს, შებრუნებულად.


name = input("Enter your name:")


def speller(name):
     result = name[::-1]
     print(result)
    

speller(name)
