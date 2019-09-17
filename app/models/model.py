def shout(string):
    return string.upper()


def ReverseStr(string):
    string = string[::-1]
    print(string)


def ReverseStr2(string):
    newstring = ""
    for n in string:
        newstring = n + newstring
    return newstring
