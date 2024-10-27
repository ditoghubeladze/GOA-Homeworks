# 4. შექმენი პროგრამა, სადაც მომხმარებელს შეეკითხები რამდენი წლით უნდა დროში წინ მოგზაურობა,
#  შემდეგ შემოატანინე მისი დაბადების თარიღი, და დაუპრინტე რამდენი რომელი წელი იქნება,
#  როდესაც მომავალში მისი სასურველი წლით გადავა.



user_birth_year = int(input("Enter your birth year: "))


print("How many years do you want to travel in the future?")
time_travel_year = int(input("Enter: "))


print(f"It will be {user_birth_year+ time_travel_year} when you travel in future.")