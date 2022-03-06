def points(games):
    all_points = 0

    for match in games:
        if int(match[0]) > int(match[2]):
            all_points += 3
        elif int(match[0]) == int(match[2]):
            all_points += 1

    return all_points