def one_num():
    return Input("Please enter a number")
def two_nums():
    return Input("Please enter the first number: "), Input("Please enter the second number:")


def Input(text):
    try:
        return input(text)
    except:
        print "Nice Try! Numbers only."
        return Input(text)
