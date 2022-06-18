# Linear Search Algorithm

# def linear_search(main_list, item):
#     for i in range(len(main_list)):
#         if main_list[i] == item:
#             return i
#     return -1
#


# Linear Search Algorithm with print statements)

def linear_search(main_list, item):
    print("Starting Linear Search Algorithm")
    for i in range(len(main_list)):
        print(f"============ Iteration #{i} ============")
        print("Current list item:", main_list[i])
        print("Item searched:", item)
        print("Is the current item equal to the item searched?", main_list[i] == item)
        if main_list[i] == item:
            print(f"Item found! at index {i}")
            return i
        print("This is not the item")
    print("The item is not in the list")
    return -1


linear_search([1, 3, 2, 4, 5, 6, 7], 6)
