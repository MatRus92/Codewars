def difference_in_ages(ages):
    min_age = min(ages)
    max_age = max(ages)

    if min_age == max_age:
        return (min_age, max_age, 0)

    return (min_age, max_age, max_age - min_age)