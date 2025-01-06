# 1. შექმენით ფუნქცია, სადაც გამოიყენებთ return-ს, შემდეგ კი შექმენით იდენტური ფუნქცია, თუმცა print-ით.


def division(a, b):
    return a - b

division(4, 2) # არ გამოაქ არაფერი
print(division(4,2)) # გამოაქ 2

def division(a,b):
    print(a-b)

division(21, 2) # გამოაქ 19

