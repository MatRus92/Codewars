def calculate(expression):
    elements = expression.split(' ')
    res = []

    signs = ['+', '-', '/', '*']
    while elements:

        el = elements.pop()
        if el not in signs:
            res.append(float(el))
        else:
            if el == '+':
                res.append(float(res.pop()) + float(res.pop()))
            if el == '-':
                res.append(float(res.pop()) - float(res.pop()))
            if el == '/':
                a = float(res.pop())
                b = float(res.pop())

                if b != 0:
                    res.append(a/b)
                else:
                    res.append(0)
                    break

            if el == '*':
                res.append(float(res.pop()) * float(res.pop()))


    return res[0]


print(calculate('+ 3 5'))
print(calculate('* + 2 2 3'))
print(calculate('/ + 3 5 * 2 2'))
print(calculate('0'))
print(calculate('123'))
print(calculate('12.456'))
print(calculate('* - 5 6 7'))