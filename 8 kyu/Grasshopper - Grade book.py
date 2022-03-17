def get_grade(s1, s2, s3):
    suma = (s1 + s2 + s3) / 3

    if suma >= 90:
        return 'A'
    if suma < 90 and suma >= 80:
        return 'B'
    if suma < 80 and suma >= 70:
        return 'C'
    if suma < 70 and suma >= 60:
        return 'D'
    return "F"