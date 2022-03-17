def hero(bullets, dragons):
    if float(bullets) < 1:
        return False

    if float(bullets) / float(dragons) >= 2:
        return True
    return False