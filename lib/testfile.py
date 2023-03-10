def truncate_string(string):
    newstring = string[0:1] + "..."
    if len(string) > 10:
        return newstring
    else:
        return string
    
print(truncate_string("This aint"))