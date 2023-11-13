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


def test_user(sorted_periodic_table):
    for index, element_data in enumerate(sorted_periodic_table, start=1):
        element = element_data['element']
        mass = element_data['mass']
        proton_number = index
        user_input = input(
            f"Enter the proton number for element {element} ({index}/{len(sorted_periodic_table)}), with mass {mass}: ")

        if int(user_input) == proton_number:
            print("Correct!")
        else:
            print(f"Incorrect. The proton number of {element} is {proton_number}.")


def main():
    file_path = 'periodic_table.txt'  # Update with your actual file path
    periodic_table = read_periodic_table(file_path)
    test_user(periodic_table)


if __name__ == '__main__':
    main()
