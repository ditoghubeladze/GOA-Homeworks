def fake_bin(x):
    string = ""
    for i in x:
        if int(i) < 5:
            string += "0"
        else:
            string += "1"
    return string