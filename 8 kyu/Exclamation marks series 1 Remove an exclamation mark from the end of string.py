def remove(s):
    if len(s) == 0 or len(s) == 1:
        return s

    if s[-1] == "!":
        return s[:-1]
    else:
        return s