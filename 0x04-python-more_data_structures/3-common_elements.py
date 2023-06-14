def common_elements(set_1, set_2):
    # Create an empty set to store the common elements
    common_elements_set = set()

    # Iterate over each element in set_1
    for element in set_1:
        # Check if the element is present in set_2
        if element in set_2:
            # Add the common element to the set
            common_elements_set.add(element)

    # Return the set of common elements
    return common_elements_set
