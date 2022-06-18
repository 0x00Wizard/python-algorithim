def linear_search(main_list, item):
    for i in range(len(main_list)):
        if main_list[i] == item:
            return i
        else:
            return -1


