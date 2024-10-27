# 2. შექმენი პროგრამა, სადაც მომხმარებელს შემოატანინებ მის დაბადების წელს, თუ ის იქნება 2010 წელზე მეტი,
#  დაუპრინტე, რომ gen alpha თაობის წარმომადგენელია, სხვა შემთხვევაში არაფერი არ დაუპრინტო.


user_birth_year = int(input("Enter your birth year: "))


if user_birth_year > 2010:
    print("You are member of gen alpha.")