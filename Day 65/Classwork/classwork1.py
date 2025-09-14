def add_numbers(num1,num2):
    return num1,num2

def full_name(firstname,lastname):
    return firstname , lastname


add_numbers_lambda = lambda num1, num2: num1 + num2

full_name_lambda = lambda firstname, lastname: firstname + " " + lastname

full_name_lambda