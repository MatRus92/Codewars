def pillars(num_pill, dist, width):
    if num_pill == 1:
        return 0

    for _ in range(num_pill):
        sum_pill_dist = (num_pill - 1) * 100 * dist
        sum_pill_width = width * (num_pill  - 2)
        return sum_pill_width + sum_pill_dist

print(pillars(1, 10, 10))
print(pillars(2, 20, 25))
print(pillars(11, 15, 30))