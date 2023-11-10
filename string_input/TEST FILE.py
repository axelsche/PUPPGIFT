import random

def pick_random_string(input_list):
    # Filter the list to include only strings
    string_list = [item for item in input_list if isinstance(item, str)]

    # Check if there are any strings in the list
    if string_list:
        # Pick a random string from the filtered list
        random_string = random.choice(string_list)
        print(random_string)
    else:
        print("No strings found in the input list.")

# Example usage:
my_list = [1, "apple", 2, "banana", 3, "orange"]
pick_random_string(my_list)
