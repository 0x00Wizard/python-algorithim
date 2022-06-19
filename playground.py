def binary_search(data, item):
    low = 0
    high = len(data) -1

    while low <= high:
        middle = (low + high) // 2

        if data[middle] == item:
            return middle

        elif data[middle] > item:
            high = middle - 1

        else:
            low = middle + 1

    return -1


print(binary_search([1, 5, 16, 3, 7, 8, 10], 10))