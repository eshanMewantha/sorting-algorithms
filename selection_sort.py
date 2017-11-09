def selection_sort(items):
    """Implementation of selection sort where a given list of items are sorted in ascending order and returned"""

    for current_position in range(len(items)):
        # assume the current position as the smallest values position
        smallest_item_position = current_position

        # iterate through all elements from current position to the end including current position
        for location in range(current_position, len(items)):
            # check if an item exists which is less in value than the value in most recent smallest item
            if items[location] < items[smallest_item_position]:
                smallest_item_position = location

        # Interchange the values of current position and the smallest value found in the rest of the list
        temporary_item = items[current_position]
        items[current_position] = items[smallest_item_position]
        items[smallest_item_position] = temporary_item

    return items


print(selection_sort([9, 8, 1, 3, 4]))
