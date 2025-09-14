# SyntaxError
# print("Hello"  

# TypeError
#result = 5 + "10"  # int + str

# ValueError
#num = int("abc")  # "abc" რიცხვი არაა

# ZeroDivisionError
#res = 10 / 0  # ნულზე გაყოფა

# IndexError
nums = [1, 2, 3]
#print(nums[5])  # არარსებული ინდექსი

# NameError
#print(xyz)  # xyz განსაზღვრული არაა

try:
    num1 = 10
    num2 = 0
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Error: ნულზე გაყოფა შეუძლებელია!")
finally:
    print("ეს ბლოკი ყოველთვის შესრულდება, იქნება თუ არა შეცდომა.")
