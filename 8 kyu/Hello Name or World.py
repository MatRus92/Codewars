def hello(name = None):
    if name is None or name == "":
        return "Hello, World!"

    return "Hello, " + name[:1].upper() + name[1:].lower() + "!"

print(hello("Mateusz"))
print(hello(""))
print(hello())
print(hello("MAT"))
print(hello("john"))
print(hello("aliCE"))