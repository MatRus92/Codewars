def is_lock_ness_monster(string):
    if "three fifty" in string or "3.50" in string or "tree fiddy" in string:
        return True
    else:
        return False