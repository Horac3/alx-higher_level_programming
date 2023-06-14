#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    # Create an empty set to store the unique elements
    unique_elements_set = set()

    # Find elements present in set_1 but not in set_2
    for element in set_1:
        if element not in set_2:
            unique_elements_set.add(element)

    # Find elements present in set_2 but not in set_1
    for element in set_2:
        if element not in set_1:
            unique_elements_set.add(element)

    # Return the set of unique elements
    return unique_elements_set
