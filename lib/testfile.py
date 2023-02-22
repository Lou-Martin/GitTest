def contains_hello(string):
    if string.find("hello") != -1:
        return True
    else:
        return False


print(contains_hello("HELLO world"))