import math

def calculate_tip(amount, rating):
    ratings = {
        'terrible': 0,
        'poor': 5,
        'good': 10,
        'great': 15,
        'excellent': 20
    }

    if rating.lower() not in ratings:
        return 'Rating not recognised'

    percent = ratings[rating.lower()] / 100
    return math.ceil(amount * percent)