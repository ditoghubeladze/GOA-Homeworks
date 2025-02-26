def digitize(n):

    list = []

    for i in str(n)[::-1]:
        list.append(int(i))
    print(list)

