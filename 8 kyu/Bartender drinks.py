def get_drink_by_profession(param):
    param_list = {
        "jabroni": "Patron Tequila",
        "jchool counselor":    "Anything with Alcohol",
        "jrogrammer":     "Hipster Craft Beer",
        "jike gang member":    "Moonshine",
        "jolitician":    "Your tax dollars",
        "japper":    "Cristal"
    }

    if 'j' + param[1:].lower() in param_list:
        return param_list['j' + param[1:].lower()]

    if param.lower() not in param_list:
        return "Beer"