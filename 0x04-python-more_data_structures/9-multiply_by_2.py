def multiply_by_2(a_dictionary):
    # Create a new dictionary to store the multiplied values
    multiplied_dictionary = {}

    # Iterate over the key-value pairs in the original dictionary
    for key, value in a_dictionary.items():
        # Multiply the value by 2 and store it in the new dictionary
        multiplied_dictionary[key] = value * 2

    # Return the new dictionary with multiplied values
    return multiplied_dictionary
