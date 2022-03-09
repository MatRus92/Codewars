def str_count(strng, letter):
    all_chars = 0

    for char in strng:
        if char == letter:
            all_chars += 1
    return all_chars