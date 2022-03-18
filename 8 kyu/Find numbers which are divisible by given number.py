def divisible_by(numbers, divisor):
    returned = []

    for n in numbers:
        if n % divisor == 0:
            returned.append(n)
    return returned