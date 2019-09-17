# function that takes a string and reverses it

def ReverseStr(string):
    string = string[::-1]
    print(string)


def ReverseStr2(string):
    newstring = ""
    for n in string:
        newstring = n + newstring
    return newstring



# function that takes a string and returns in all caps

def shout(string):
    return string.upper()
