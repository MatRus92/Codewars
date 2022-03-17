def hex_to_dec(s):
    j = 0
    result = 0
    for i in s[::-1]:
        print(i)
        if i.lower() == 'a':
            i = "10"
        if i.lower() == 'b':
            i = "11"
        if i.lower() == 'c':
            i = "12"
        if i.lower() == 'd':
            i = "13"
        if i.lower() == 'e':
            i = "14"
        if i.lower() == 'f':
            i = "15"

        result += (16 ** j) * int(i)
        j += 1
    return result

#print(hex_to_dec("1"))
#print(hex_to_dec("a"))
print(hex_to_dec("10"))