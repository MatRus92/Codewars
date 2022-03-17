def better_than_average(class_points, your_points):
    average_all = sum(i for i in class_points) / len(class_points)

    if average_all > your_points:
        return False

    return True