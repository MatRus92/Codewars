def animals(heads, legs):
    if heads == 0 and legs == 0:
        return 0, 0
    if heads <= 0 or legs <= 0:
        return "No solutions"

    cows = (legs - (heads * 2)) / 2
    chickens = (legs - (cows * 4)) / 2

    if cows < 0 or chickens < 0:
        return "No solutions"
    if cows.is_integer() and chickens.is_integer():
        return chickens, cows
    else:
        return "No solutions"

print(animals(72, 200))
print(animals(116, 282))
print(animals(12, 24))
print(animals(6, 24))
print(animals(344, 872))
print(animals(158, 616))
print(animals(25, 555))
print(animals(12, 25))
print(animals(54, 956))
print(animals(0, 0))
print(animals(-370.0, 424.0))