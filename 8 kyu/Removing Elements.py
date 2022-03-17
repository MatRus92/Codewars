def remove_every_other(my_list):
    my_new_list = []
    for i in range(len(my_list)):
        if i % 2 == 0:
            my_new_list.append(my_list[i])
    return my_new_list