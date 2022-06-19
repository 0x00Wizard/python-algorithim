def binary_search(data, low, high, item):
    if low <= high:
        middle = (low + high) // 2

        if data[middle] == data:
            return middle
        elif data[middle] > data:
            return binary_search(data, low, middle + 1, item)

        else:
            return binary_search(data, middle - 1, high, item)

    return -1
