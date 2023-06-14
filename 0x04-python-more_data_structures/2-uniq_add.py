def uniq_add(my_list=[]):
    # Create an empty set to store unique integers
    unique_integers = set()

    # Iterate over each element in the input list
    for element in my_list:
        # Check if the element is an integer and not already in the set
        if isinstance(element, int) and element not in unique_integers:
            # Add the unique integer to the set
            unique_integers.add(element)

    # Calculate the sum of unique integers
    sum_unique_integers = sum(unique_integers)

    # Return the sum
    return sum_unique_integers
