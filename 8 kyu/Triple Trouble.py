def triple_trouble(one, two, three):
    allElems = ''
    for elem in list(zip(one, two, three)):
        for elemSec in elem:
            allElems += elemSec

    return allElems