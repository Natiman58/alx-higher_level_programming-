def max_integer(my_list=[]):
    if my_list == 0:
        return None
    for i in range(len(my_list)):
        if my_list[i + 1] > my_list[i]:
            return my_list[i + 1]
