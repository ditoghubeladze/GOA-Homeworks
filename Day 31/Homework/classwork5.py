# 5. შექმენით ფუნქცია, რომელიც იღებს string'ს და აბრუნებს True-ს თუ ის არის Palindrome
#  (ანუ იგივენაირად იკითხება მარცნიდანაც და მარჯვნიდანაც მაგალითად: "wow") და სხვა შემთხვევაში False-ს.


def palindrome(string):
    return string == string[::-1]

result= palindrome(input("Enter any text: "))

print(result)