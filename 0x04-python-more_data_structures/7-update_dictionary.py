#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    # Update the value if the key already exists in the dictionary
    if key in a_dictionary:
        a_dictionary[key] = value
    else:
        # Add a new key/value pair to the dictionary
        a_dictionary[key] = value

    # Return the updated dictionary
    return a_dictionary
