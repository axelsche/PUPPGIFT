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
        :type elements: list
        :return: A dictionary mapping the atomic number to the row and column of the element.
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