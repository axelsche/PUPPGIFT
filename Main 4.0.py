import csv
import random


class ElementSorter:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        self.sorted_elements = None

    def read_elements(self):
        """
    :func:`read_elements` reads the elements from the input file.
    :return: A list of elements.
    :rtype: list
    """
        with open(self.input_file, 'r') as file:
            lines = file.readlines()
        return [line.strip() for line in lines]

    def sort_elements_by_mass(self, elements):
        """:func:`sort_elements_by_mass` sorts the elements by mass.
        :param elements: A list of elements.
        :type elements: list
        """
        parsed_elements = [{'Element': element.split()[0], 'Mass': float(element.split()[1])} for element in elements]
        sorted_elements = sorted(parsed_elements, key=lambda x: x['Mass'])

        # Assign atomic numbers based on sorting order
        for i, element in enumerate(sorted_elements):
            element['AtomicNumber'] = i + 1

        self.sorted_elements = sorted_elements
        return sorted_elements


    def swap_elements_by_index(self, index1, index2):
        ''':func:`swap_elements_by_index` swaps the positions of two elements based on their indices.
        :param index1: The index of the first element.
        :type index1: int'''
        if 0 <= index1 < len(self.sorted_elements) and 0 <= index2 < len(self.sorted_elements):
            # Swap the positions of two elements based on their indices
            temp_element = self.sorted_elements[index1]
            self.sorted_elements[index1] = self.sorted_elements[index2]
            self.sorted_elements[index2] = temp_element

    def reassign_indices(self):
        for i, element in enumerate(self.sorted_elements):
            element['AtomicNumber'] = i + 1

    def map_to_mendeleev_layout(self): #make this CSV MAYBE to look nicer
        ''' :func:`map_to_mendeleev_layout` maps the elements to the Mendeleev layout.
        :type elements: list
        :return: A dictionary mapping the atomic number to the row and column of the element.
        '''
        mandeleev_layout = {
            1: (1, 1), 2: (1, 18),
            3: (2, 1), 4: (2, 2), 5: (2, 13), 6: (2, 14), 7: (2, 15), 8: (2, 16), 9: (2, 17), 10: (2, 18),
            11: (3, 1), 12: (3, 2), 13: (3, 13), 14: (3, 14), 15: (3, 15), 16: (3, 16), 17: (3, 17), 18: (3, 18),
            19: (4, 1), 20: (4, 2), 21: (4, 3), 22: (4, 4), 23: (4, 5), 24: (4, 6), 25: (4, 7), 26: (4, 8), 27: (4, 9),
            28: (4, 10), 29: (4, 11), 30: (4, 12), 31: (4, 13), 32: (4, 14), 33: (4, 15), 34: (4, 16), 35: (4, 17),
            36: (4, 18),
            37: (5, 1), 38: (5, 2), 39: (5, 3), 40: (5, 4), 41: (5, 5), 42: (5, 6), 43: (5, 7), 44: (5, 8), 45: (5, 9),
            46: (5, 10), 47: (5, 11), 48: (5, 12), 49: (5, 13), 50: (5, 14), 51: (5, 15), 52: (5, 16), 53: (5, 17),
            54: (5, 18),
            55: (6, 1), 56: (6, 2), 57: (8, 3), 58: (8, 4), 59: (8, 5), 60: (8, 6), 61: (8, 7), 62: (8, 8), 63: (8, 9),
            64: (8, 10), 65: (8, 11), 66: (8, 12), 67: (8, 13), 68: (8, 14), 69: (8, 15), 70: (8, 16), 71: (6, 3),
            72: (6, 4), 73: (6, 5), 74: (6, 6), 75: (6, 7), 76: (6, 8), 77: (6, 9), 78: (6, 10), 79: (6, 11),
            80: (6, 12), 81: (6, 13), 82: (6, 14), 83: (6, 15), 84: (6, 16), 85: (6, 17), 86: (6, 18),
            87: (7, 1), 88: (7, 2), 89: (9, 3), 90: (9, 4), 91: (9, 5), 92: (9, 6), 93: (9, 7), 94: (9, 8), 95: (9, 9),
            96: (9, 10), 97: (9, 11), 98: (9, 12), 99: (9, 13), 100: (9, 14), 101: (9, 15), 102: (9, 16), 103: (7, 3),
        }

        empty_cells = [(1, 3), (1, 4), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8),
                   (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8),
                   (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8),
                   (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8),
                   (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8),
                   (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8),
                   (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8),
                   (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8),
                   (10, 3), (10, 4), (10, 5), (10, 6), (10, 7), (10, 8)]


        for cell in empty_cells:
            mandeleev_layout[cell] = None

        for element in self.sorted_elements:
            proton_number = element['AtomicNumber']
            if proton_number in mandeleev_layout:
                row, col = mandeleev_layout[proton_number]
                element['row'] = row
                element['col'] = col

    def write_sorted_elements_to_csv(self):
        ''':func:`write_sorted_elements_to_csv` writes the sorted elements to a CSV file.
        :param elements: A list of elements.
        '''

        with open(self.output_file, 'w', newline='') as csvfile:
            fieldnames = ['AtomicNumber', 'Element', 'Mass', 'row', 'col']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for row in self.sorted_elements:
                writer.writerow(row)

    def process_elements(self, swaps=[]):
        ''' :func:`process_elements` processes the elements.
        :param elements: A list of elements.
        :param swaps: A list of tuples containing the indices of the elements to swap.'''
        elements = self.read_elements()
        self.sort_elements_by_mass(elements)

        # Perform specific swaps
        for swap in swaps:
            self.swap_elements_by_index(*swap)

        # Reassign indices after swaps
        self.reassign_indices()

        # Apply Mendeleev layout
        self.map_to_mendeleev_layout()

        # Write to CSV
        self.write_sorted_elements_to_csv()


class Game:
    def __init__(self):
        self.element_sorter = ElementSorter(input_file='/Users/axelschelander/Desktop/KTH/DATAP/csc.kth.se_~lk_P_avikt.txt',
                                           output_file='sorted_mass_with_atomic_numbers.csv')

    def play_atomic_number_game(self):
        self.atomic_number_game()
        return self.play_again()

    def play_element_game(self):
        self.element_game()
        return self.play_again()

    def play_mass_game(self):
        self.mass_game()
        return self.play_again()

    def play_Row_column_game(self):
        self.Row_column_game()
        return self.play_again()

    def play_again(self):
        play_again_input = input("Do you want to play again? (yes/no): ").lower()
        return play_again_input == 'yes'

    def play_game(self):
        while True:
            game_type = input("Enter your choice (1-6): ").strip()
            if game_type.isdigit() and 1 <= int(game_type) <= 6:
                break
            print("Invalid choice. Please enter a number between 1 and 6.")

        game_type = int(game_type)

        if game_type == 1:
            return self.play_atomic_number_game()
        elif game_type == 2:
            return self.play_element_game()
        elif game_type == 3:
            return self.play_mass_game()
        elif game_type == 4:
            return self.play_Row_column_game()
        elif game_type == 5:
            self.print_periodic_table()
            return True
        elif game_type == 6:
            print("Exiting the program. Goodbye!")
            return False

    def main_menu(self):
        ''' :func:`main_menu` displays the main menu and handles the user's choice.
        :return: True if the user wants to play again, False otherwise.
        :rtype: bool
        '''
        while True:
            print("Main Menu:")
            print("1. Atomic Number Game")
            print("2. Element Name Game")
            print("3. Mass Game")
            print("4. Row and Column Game")
            print("5. Print Periodic Table")
            print("6. Exit")

            # Corrected line
            user_choice = input("Enter your choice (1-6): ").strip()

            if user_choice.isdigit() and 1 <= int(user_choice) <= 6:
                user_choice = int(user_choice)
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")
                continue

            if user_choice == 6:
                print("Exiting the program. Goodbye!")
                return

            self.play_selected_game(user_choice)

    def play_selected_game(self, game_type):
        if game_type == 1:
            self.play_atomic_number_game()
        elif game_type == 2:
            self.play_element_game()
        elif game_type == 3:
            self.play_mass_game()
        elif game_type == 4:
            self.play_Row_column_game()
        elif game_type == 5:
            self.print_periodic_table()

    def print_periodic_table(self):
        ''':func:`print_periodic_table` prints the periodic table.
        :param elements: A list of elements.
        :type elements: list
        '''

        with open('sorted_mass_with_atomic_numbers.csv', 'r') as file:
            reader = csv.DictReader(file)
            elements = list(reader)

        # Create a 2D list of elements
        table = [['' for _ in range(18)] for _ in range(10)]
        for element in elements:
            row = int(element['row'])
            col = int(element['col'])
            table[row - 1][col - 1] = element['Element']

        # Print the table
        for row in table:
            print(' '.join([f"{element:<2}" for element in row]))

    def play_atomic_number_game(self):
        ''':func:`play_atomic_number_game` plays the atomic number game.
        :return: True if the user wants to play again, False otherwise.
        :rtype: bool
        '''

        attempts_per_question = 3

        while True:
            self.element_sorter.process_elements(swaps=[
                (17, 18),
                (26, 27),
                (51, 52),
                (89, 90),
                (91, 92)
            ])

            with open('sorted_mass_with_atomic_numbers.csv', 'r') as file:
                reader = csv.DictReader(file)
                elements = list(reader)

            random.shuffle(elements)

            for element in elements:
                print(f"Element: {element['Element']} - Mass: {element['Mass']}")

                attempts = 0
                while attempts < attempts_per_question:
                    guess = input(f"Attempt {attempts + 1}: Guess the atomic number: ")

                    try:
                        guess = int(guess)
                    except ValueError:
                        print(f"Invalid input. Please enter a number.")
                        continue

                    if guess == int(element['AtomicNumber']):
                        print("Correct!")
                        break
                    else:
                        attempts += 1
                        print("Wrong!")
                        print(f"You have {attempts_per_question - attempts} attempts remaining.")
                        if attempts == attempts_per_question:
                            print("Out of attempts. The correct answer is:", element['AtomicNumber'])
                            break

                print("")

                if not self.play_again():
                    return False
        # Exit the function and return to the main menu

    def play_element_game(self):
        attempts_per_question = 3

        while True:
            self.element_sorter.process_elements(swaps=[
                (17, 18),
                (26, 27),
                (51, 52),
                (89, 90),
                (91, 92)
            ])

            with open('sorted_mass_with_atomic_numbers.csv', 'r') as file:
                reader = csv.DictReader(file)
                elements = list(reader)

            random.shuffle(elements)

            for element in elements:
                print(f"Atomic number: {element['AtomicNumber']} - Mass: {element['Mass']}")

                attempts = 0
                while attempts < attempts_per_question:
                    guess = input(f"Attempt {attempts + 1}: Guess the element: ")

                    if (len(guess) == 1 or len(guess) == 2) and guess.isalpha():
                        if guess.lower() == element['Element'].lower():
                            print("Correct!")
                            break
                        else:
                            print("Wrong!")
                            print(f"The correct answer is: {element['Element']}")
                            attempts += 1
                            print(f"You have {attempts_per_question - attempts} attempts remaining.")
                            if attempts == attempts_per_question:
                                print("Out of attempts.")
                                break
                    else:
                        print("Invalid input. Please enter a one or two-letter string without numbers.")

                print("")

                if not self.play_again():
                    return False

    def get_random_incorrect_mass(self, correct_mass):
        # Generate 3 random incorrect masses
        incorrect_masses = [correct_mass]
        while len(incorrect_masses) < 3:
            random_mass = round(random.uniform(0.1, 300), 1)
            if random_mass not in incorrect_masses:
                incorrect_masses.append(random_mass)

        random.shuffle(incorrect_masses)
        return incorrect_masses

    def play_mass_game(self):
        while True:
            self.element_sorter.process_elements(swaps=[
                (17, 18),
                (26, 27),
                (51, 52),
                (89, 90),
                (91, 92)
            ])

            with open('sorted_mass_with_atomic_numbers.csv', 'r') as file:
                reader = csv.DictReader(file)
                elements = list(reader)

            random.shuffle(elements)

            for element in elements:
                masses = [float(element['Mass'])]
                for i in range(2):
                    random_element = random.choice(elements)
                    while random_element == element:
                        random_element = random.choice(elements)
                    masses.append(float(random_element['Mass']))
                random.shuffle(masses)

                print(f"Element: {element['Element']} - Atomic number: {element['AtomicNumber']}")
                print("Options:")
                for i, mass_option in enumerate(masses):
                    print(f"{chr(65 + i)}. {mass_option}")

                guess_index = None
                while guess_index not in range(len(masses)):
                    guess_index = input("Select the correct mass (A, B, C): ").upper()
                    if guess_index.isalpha():
                        guess_index = ord(guess_index) - 65
                    else:
                        guess_index = None

                guessed_mass = masses[guess_index]

                if guessed_mass == float(element['Mass']):
                    print("Correct!")
                else:
                    print("Wrong!")
                    print(f"The correct answer is: {element['Mass']}")

                print("")

                if not self.play_again():
                    return False

    def play_Row_column_game(self):
        attempts_per_question = 3

        while True:
            self.element_sorter.process_elements(swaps=[
                (17, 18),
                (26, 27),
                (51, 52),
                (89, 90),
                (91, 92)
            ])

            with open('sorted_mass_with_atomic_numbers.csv', 'r') as file:
                reader = csv.DictReader(file)
                elements = list(reader)

            random.shuffle(elements)

            for element in elements:
                correct_row = int(element['row'])
                correct_column = int(element['col'])

                attempts = 0
                while attempts < attempts_per_question:
                    guess = input(
                        f"Attempt {attempts + 1}: Guess the correct row and column for element {element['Element']} (row, col): ")

                    try:
                        guessed_row, guessed_column = map(int, guess.split(','))

                        if not (1 <= guessed_row <= 10 and 1 <= guessed_column <= 18):
                            raise ValueError("Invalid input. Please enter valid row and column numbers.")

                        if guessed_row == correct_row and guessed_column == correct_column:
                            print("Correct!")
                            break
                        else:
                            attempts += 1
                            print(f"Wrong! You have {attempts_per_question - attempts} attempts remaining.")
                            if attempts == attempts_per_question:
                                print(f"Out of attempts. The correct answer is: {correct_row}, {correct_column}")
                                break

                    except ValueError as e:
                        print(e)

                print("")

                if not self.play_again():
                    return False

    def play_again(self):
        play_again_input = input("Do you want to play again? (y/n): ").lower()
        if play_again_input == 'y':
            return True  # play the game again
        elif play_again_input == 'n':
            self.main_menu()
            print("Returning to the main menu.")
            return False  # return to main_menu function
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
            return self.play_again()



# Example usage
game_instance = Game()
game_instance.main_menu()# Example usage