def double_char(s):
    retStr = ""

    for i in s:
        retStr += i + i

    return retStr

print(double_char("Mateusz"))
print(double_char("String"))
print(double_char("Hello World"))
print(double_char("1234!_ "))