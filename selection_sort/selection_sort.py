def selection_sort(lst):
    for i in range(len(lst)):

        min_index = i

        for current_index in range(i+1, len(lst)):
            if lst[min_index] > lst[current_index]:
                min_index = current_index


