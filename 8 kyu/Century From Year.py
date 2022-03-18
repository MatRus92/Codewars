import math

def century(year):
    return int(round_up(year / 100))

def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier