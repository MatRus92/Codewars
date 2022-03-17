def guess_blue(blue_start, red_start, blue_pulled, red_pulled):
    all_blue = blue_start - blue_pulled
    all_red = red_start - red_pulled

    all = all_blue + all_red
    return all_blue / all