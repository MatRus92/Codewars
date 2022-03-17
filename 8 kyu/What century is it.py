def what_century(year):
    firstPart = int(year[:-2])
    secondPart = year[-2:]
    lastDigitInFirstPart = str(firstPart)[-1]

    if secondPart == '00' and lastDigitInFirstPart != '0':
        return returnCentury(firstPart, lastDigitInFirstPart)

    if int(year) % 1000 != 0:
        firstPart += 1

    lastDigitInFirstPart = str(firstPart)[-1]
    return returnCentury(firstPart, lastDigitInFirstPart)


def returnCentury(firstPart, lastDigitInFirstPart):
    if firstPart == 11 or firstPart == 12 or firstPart == 13:
        return str(firstPart) + 'th'

    if lastDigitInFirstPart == '1':
        return str(firstPart) + 'st'
    if lastDigitInFirstPart == '2':
        return str(firstPart) + 'nd'
    if lastDigitInFirstPart == '3':
        return str(firstPart) + 'rd'

    return str(firstPart) + 'th'

print(what_century("1999"))
print(what_century("2011"))
print(what_century("2154"))
print(what_century("2259"))
print(what_century("6700"))
print(what_century("2000"))
print(what_century("987"))
