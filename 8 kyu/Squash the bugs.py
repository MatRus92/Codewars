def find_longest(string):
    spl = list(string.split())
    longest = 0

    for i in spl:
        if len(i) > longest:
            longest = len(i)

    return longest