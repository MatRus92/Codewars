def add_extra(list_of_numbers):
    new_list = []
    if len(list_of_numbers) == 0:
        new_list.append(1)
        return new_list

    new_list = list_of_numbers.copy()
    new_list.append(list_of_numbers[-1] + 1)
    return new_list

print(len(add_extra([1,2])))
print(len(add_extra([])))