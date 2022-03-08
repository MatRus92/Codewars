def to_alternating_case(string):
    ret = ""
    for character in string:
        if character.isupper():
            ret += character.lower()
        else:
            ret += character.upper()

    return ret