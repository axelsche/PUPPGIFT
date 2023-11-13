import random

def read_periodic_table(file_path):
    periodic_table = []
    with open('/Users/axelschelander/Desktop/KTH/DATAP/csc.kth.se_~lk_P_avikt.txt', 'r') as f:
        for line in f:
            element_info = line.strip().split()
            if len(element_info) >= 2:
                mass = float(element_info[1])
                element_data = {'element': element_info[0], 'mass': mass, 'proton_number': None}
                periodic_table.append(element_data)
            else:
                print(f"Skipping invalid line: {line.strip()}")
    return sorted(periodic_table, key=lambda x: x['mass'])

def swap_elements_by_index(table, index1, index2):
    if 0 <= index1 < len(table) and 0 <= index2 < len(table):
        table[index1], table[index2] = table[index2], table[index1]
    else:
        print(f"Invalid indices: ({index1}, {index2})")

def print_all_elements(table):
    for index, element_data in enumerate(table, start=1):
        print(f"{index}. Element: {element_data['element']}, Mass: {element_data['mass']}, Proton Number: {index}")

def test_proton_number(sorted_periodic_table):
    random_element = random.choice(sorted_periodic_table)
    element = random_element['element']
    mass = random_element['mass']
    proton_number = sorted_periodic_table.index(random_element) + 1

    attempts = 0
    while attempts < 3:
        user_input = input(f"Enter the proton number for a randomly selected element ({element}), with mass {mass}: ")
        try:
            input_value = int(user_input)
            if 1 <= input_value <= len(sorted_periodic_table):
                if input_value == proton_number:
                    print("Correct!")
                    break
                else:
                    print("Incorrect. Try again.")
                    attempts += 1
            else:
                print(f"Please enter a number between 1 and {len(sorted_periodic_table)}.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    else:
        print(f"Sorry, you've reached the maximum number of attempts. The correct answer is {proton_number}.")

def test_abbreviation(sorted_periodic_table):
    random_element = random.choice(sorted_periodic_table)
    element = random_element['element']
    proton_number = sorted_periodic_table.index(random_element) + 1

    attempts = 0
    while attempts < 3:
        user_input = input(f"Enter the abbreviation for a randomly selected element with proton number {proton_number}: ")
        if user_input.isalpha() and len(user_input) > 0:
            if user_input.lower() == element.lower():
                print("Correct!")
                break
            else:
                print("Incorrect. Try again.")
                attempts += 1
        else:
            print("Invalid input. Please enter a valid abbreviation.")

    else:
        print(f"Sorry, you've reached the maximum number of attempts. The correct answer is {element}.")

def main():
    file_path = 'periodic_table.txt'  # Update with your actual file path
    periodic_table = read_periodic_table(file_path)

    swap_elements_by_index(periodic_table, 17, 18)
    swap_elements_by_index(periodic_table, 26, 27)
    swap_elements_by_index(periodic_table, 51, 52)
    swap_elements_by_index(periodic_table, 89, 90)
    swap_elements_by_index(periodic_table, 91, 92)


    while True:
        print("\nOptions:")
        print("1. Print all elements")
        print("2. Test proton number")
        print("3. Test abbreviation")
        print("4. End")

        choice = input("Enter your choice (1, 2, 3, or 4): ")

        if choice == '1':
            print_all_elements(periodic_table)
        elif choice == '2':
            test_proton_number(periodic_table)
        elif choice == '3':
            test_abbreviation(periodic_table)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == '__main__':
    main()
