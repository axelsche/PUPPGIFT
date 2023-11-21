import random
import tkinter as tk
from tkinter import Frame

correct_answer = None
answers = None
grid_window = None
random_element = None
correct_row = None
correct_column = None
btn_fill_table = None


def read_periodic_table(file_path):
    periodic_table = []
    with open('/Users/axelschelander/Desktop/KTH/DATAP/csc.kth.se_~lk_P_avikt.txt', 'r') as f:
        for line in f:
            element_info = line.strip().split()
            if len(element_info) >= 2:
                mass = float(element_info[1])
                element_data = {'element': element_info[0], 'mass': mass, 'proton_number': None}
                periodic_table.append(element_data)

    sorted_table = sorted(periodic_table, key=lambda x: x['mass'])

    max_row, max_col = divmod(len(sorted_table), 28)

    for i, element_data in enumerate(sorted_table):
        element_data['proton_number'] = i + 1
        element_data['row'] = i // 18
        element_data['col'] = i % 18

    return sorted_table

def assign_periodic_table_positions(table):
    for i, element in enumerate(table):
        element['row'] = i // 18
        element['col'] = i % 18


def calculate_column_widths(periodic_table):
    col_widths = [0] * len(periodic_table[0])

    for row in periodic_table:
        for col, element in enumerate(row):
            element_name_len = len(f"{element['symbol']} ({element['name']})")
            col_widths[col] = max(col_widths[col], element_name_len)

    return col_widths


def swap_elements_by_index(table, index1, index2):
    if 0 <= index1 < len(table) and 0 <= index2 < len(table):
        temp_proton_number = table[index1]['proton_number']
        table[index1]['proton_number'] = table[index2]['proton_number']
        table[index2]['proton_number'] = temp_proton_number

        # Sort the table based on proton numbers
        table.sort(key=lambda x: x['proton_number'])

        # Update row and col values after sorting
        assign_periodic_table_positions(table)
    else:
        print(f"Invalid indices: ({index1}, {index2})")


def map_to_mendeleev_layout(periodic_table):
    mandeleev_layout = {
        1: (1, 1), 2: (1, 18),
        3: (2, 1), 4: (2, 2), 5: (2, 13), 6: (2, 14), 7: (2, 15), 8: (2, 16), 9: (2, 17), 10: (2, 18),
        11: (3, 1), 12: (3, 2), 13: (3, 13), 14: (3, 14), 15: (3, 15), 16: (3, 16), 17: (3, 17), 18: (3, 18),
        19: (4, 1), 20: (4, 2),21: (4, 3), 22: (4, 4),23: (4,5), 24: (4, 6),25: (4, 7), 26: (4, 8),27: (4, 9), 28: (4, 10),
        29: (4, 11), 30: (4, 12), 31: (4, 13), 32: (4, 14),33: (4, 15), 34: (4, 16), 35: (4, 17), 36: (4, 18),
        37: (5, 1), 38: (5, 2),39: (5, 3), 40: (5, 4),41: (5, 5), 42: (5, 6),43: (5, 7), 44: (5, 8),45: (5, 9), 46: (5, 10),
        47: (5, 11), 48: (5, 12),49: (5, 13), 50: (5, 14),51: (5, 15), 52: (5, 16), 53: (5, 17), 54: (5, 18),
        55: (6, 1), 56: (6, 2),57: (8, 3), 58: (8, 4), 59: (8, 5), 60: (8, 6), 61: (8, 7), 62: (8, 8),63: (8, 9),
        64: (8, 10), 65: (8, 11), 66: (8, 12), 67: (8, 13), 68: (8, 14),69: (8, 15), 70: (8, 16), 71: (6, 3), 72: (6, 4),
        73: (6, 5), 74: (6, 6),75: (6, 7), 76: (6, 8), 77: (6, 9), 78: (6, 10), 79: (6, 11), 80: (6, 12),81: (6, 13),
        82: (6, 14), 83: (6, 15), 84: (6, 16), 85: (6, 17), 86: (6, 18), 87: (7, 1), 88: (7, 2), 89: (9, 3), 90: (9, 4),
        91: (9, 5), 92: (9, 6),93: (9, 7), 94: (9, 8), 95: (9, 9), 96: (9, 10), 97: (9, 11), 98: (9, 12),99: (9, 13),
        100: (9, 14), 101: (9, 15), 102: (9, 16), 103: (7, 3),
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

    for element in periodic_table:
        proton_number = element['proton_number']
        if proton_number in mandeleev_layout:
            row, col = mandeleev_layout[proton_number]
            element['row'] = row
            element['col'] = col

    return periodic_table


def create_empty_grid_window():
    global grid_window

    print("Creating empty grid window")

    grid_window = tk.Toplevel(root)
    grid_frame = tk.Frame(grid_window)
    grid_frame.pack()

    for row in range(9):
        for col in range(18):
            label = tk.Label(grid_frame, text='', padx=10, pady=5, borderwidth=1, relief="solid")
            label.grid(row=row, column=col, padx=2, pady=2)

    return grid_frame


def update_grid_with_element(grid_frame, element, row, col):
    label = tk.Label(grid_frame, text=f"{element['element']}\n{element['proton_number']}", padx=10, pady=5, borderwidth=1, relief="solid")
    label.grid(row=row, column=col, padx=2, pady=2)


def setup_periodic_table_cells(frame, table, displayed):
    max_row = max(element['row'] for element in table)
    max_col = max(element['col'] for element in table)

    base_grid = [[None] * (max_col + 1) for _ in range(max_row + 1)]

    for element in table:
        row, col = element['row'], element['col']
        element_name_str = f"{element['element']}\n{element['proton_number']}"
        label_name = tk.Label(frame, text=element_name_str, padx=10, pady=5, borderwidth=1, relief="solid")
        base_grid[row][col] = label_name

    for row, labels_in_row in enumerate(base_grid):
        for col, label in enumerate(labels_in_row):
            if label:
                label.grid(row=row, column=col, padx=2, pady=2)

    displayed.set(True)


def hide_periodic_table(frame, displayed):
    for widget in frame.winfo_children():
        widget.grid_remove()

    displayed.set(False)

def open_seccondary_window():
    secondary_window = tk.Toplevel(root)
    secondary_window.title("Secondary Window")

    # Create a 9x18 grid
    for i in range(9):
        for j in range(18):
            # Add labels or any other widgets to the grid
            label = tk.Label(secondary_window, text=f"Row {i + 1}, Col {j + 1}", borderwidth=1, relief="solid",
                             width=10, height=2)
            label.grid(row=i, column=j, padx=2, pady=2)


def test_Row_Column_game(original_periodic_table_list, text_widget, entry_widget_row, entry_widget_col, attempts_label):
    global correct_answer, correct_row, correct_column, random_element

    if not original_periodic_table_list:
        text_widget.insert(tk.END, "\nGame over. You have completed the game.")
        btn_fill_table.config(state=tk.DISABLED)  # Disable the Fill Table button
        reset_game()  # Reset the game automatically
        return

    if not hasattr(test_Row_Column_game, 'current_element') or test_Row_Column_game.current_element is None:
        random_element = random.choice(original_periodic_table_list)
        test_Row_Column_game.current_element = random_element['element']
        correct_row = random_element['row']
        correct_column = random_element['col']

        text_widget.insert(tk.END, f"\nEnter the row and column for the randomly selected element ({test_Row_Column_game.current_element}): ")
        correct_answer = (correct_row, correct_column)
    else:
        user_row = entry_widget_row.get()
        user_col = entry_widget_col.get()

        if not user_row or not user_col:
            text_widget.insert(tk.END, "\nPlease enter the row and column for the next element.")
            return

        user_row = int(user_row)
        user_col = int(user_col)

        if user_row == correct_row and user_col == correct_column:
            text_widget.insert(tk.END, "\nCorrect!")

            if grid_window is None:
                create_empty_grid_window()

            update_grid_with_element(grid_window, random_element, user_row, user_col)

            original_periodic_table_list = [elem for elem in original_periodic_table_list if elem != random_element]

            test_Row_Column_game.current_element = None

            if original_periodic_table_list:
                random_element = random.choice(original_periodic_table_list)
                test_Row_Column_game.current_element = random_element['element']
                correct_row = random_element['row']
                correct_column = random_element['col']

                text_widget.insert(tk.END, f"\nEnter the row and column for the randomly selected element ({test_Row_Column_game.current_element}): ")

                correct_answer = (correct_row, correct_column)
            else:
                text_widget.insert(tk.END, "\nGame over. You have completed the game.")
                btn_fill_table.config(state=tk.DISABLED)  # Disable the Fill Table button
                test_Row_Column_game.current_element = None  # Reinitialize the game state
        else:
            attempts = int(attempts_label.cget("text").split()[-1]) + 1
            if attempts < 3:
                text_widget.insert(tk.END, f"\nIncorrect. Try again. ({attempts}/3 attempts)")
                attempts_label.config(text=f"Attempts left: {attempts}")
            else:
                text_widget.insert(tk.END, f"\nSorry, you've reached the maximum number of attempts. The correct answer is {correct_answer}.")

    entry_widget_row.delete(0, tk.END)
    entry_widget_col.delete(0, tk.END)

    btn_fill_table.config(state=tk.NORMAL)
    btn_submit_answer.config(state=tk.NORMAL)


def submit_answer(correct_row, correct_column, text_widget, entry_widget_row, entry_widget_col, attempts_label):
    global correct_answer

    # Rest of the code remains the same
    if correct_answer is not None:
        user_row = entry_widget_row.get()
        user_col = entry_widget_col.get()

        if not user_row.isdigit() or not user_col.isdigit():
            text_widget.insert(tk.END, "\nInvalid input. Please enter numeric values for row and column.")
            return

        user_row = int(user_row)
        user_col = int(user_col)

        # Extract the numeric part from the text
        current_attempts = int(attempts_label.cget("text").split()[-1])

        if (user_row, user_col) == correct_answer:
            text_widget.insert(tk.END, "\nCorrect!")
            btn_submit_answer.config(state=tk.DISABLED)  # Disable the Submit Answer button
        else:
            current_attempts += 1
            if current_attempts <= 3:  # Adjusted to include 3 attempts
                text_widget.insert(tk.END, f"\nIncorrect. Try again. ({current_attempts}/3 attempts)")
                attempts_label.config(text=f"Attempts left: {3 - current_attempts}")
                return
            else:
                text_widget.insert(tk.END, f"\nSorry, you've reached the maximum number of attempts. The correct answer is {correct_answer}.")

    entry_widget_row.delete(0, tk.END)
    entry_widget_col.delete(0, tk.END)

    btn_fill_table.config(state=tk.NORMAL)
    btn_submit_answer.config(state=tk.NORMAL)


def main():
    global root, btn_show_table, btn_test_proton, btn_test_abbreviation, btn_test_masses, btn_submit_answer, btn_hide_table, btn_fill_table, btn_answer_again, btn_exit, text_widget, entry_widget_row, entry_widget_col, attempts_label, original_periodic_table

    current_element = None
    root = tk.Tk()
    root.title("Periodic Table Game")

    displayed = tk.BooleanVar(value=False)

    original_periodic_table_list = read_periodic_table('/Users/axelschelander/Desktop/KTH/DATAP/csc.kth.se_~lk_P_avikt.txt')

    swap_elements_by_index(original_periodic_table_list, 17, 18)
    swap_elements_by_index(original_periodic_table_list, 26, 27)
    swap_elements_by_index(original_periodic_table_list, 51, 52)
    swap_elements_by_index(original_periodic_table_list, 89, 90)
    swap_elements_by_index(original_periodic_table_list, 91, 92)

    original_periodic_table = map_to_mendeleev_layout(original_periodic_table_list)

    button_frame: Frame = tk.Frame(root)
    button_frame.pack(side=tk.LEFT, padx=10)

    btn_show_table = tk.Button(button_frame, text="Show Periodic Table",
                               command=lambda: setup_periodic_table_cells(table_frame, original_periodic_table,
                                                                          displayed))
    btn_show_table.pack(pady=10, side=tk.TOP)

    btn_hide_table = tk.Button(button_frame, text="Hide Periodic Table",
                               command=lambda: hide_periodic_table(table_frame, displayed))
    btn_hide_table.pack(pady=10, side=tk.TOP)

    btn_fill_table = tk.Button(button_frame, text="Fill Table", state=tk.NORMAL,
                               command=lambda: test_Row_Column_game(original_periodic_table, text_widget,
                                                                    entry_widget_row, entry_widget_col, attempts_label))

    btn_fill_table.pack(pady=10, side=tk.TOP)

    btn_submit_answer = tk.Button(button_frame, text="Submit Answer", state=tk.NORMAL,
                                  command=lambda: submit_answer(correct_row, correct_column, text_widget,
                                                                entry_widget_row, entry_widget_col, attempts_label))


    btn_submit_answer.pack(pady=10, side=tk.TOP)

    btn_answer_again = tk.Button(button_frame, text="Answer Again", state=tk.DISABLED, command=lambda: main())
    btn_answer_again.pack(pady=10, side=tk.TOP)

    btn_exit = tk.Button(button_frame, text="Exit", command=root.destroy)
    btn_exit.pack(pady=10, side=tk.TOP)

    text_widget = tk.Text(root, height=20, width=100)  # Adjust the height as needed
    text_widget.pack(pady=10)

    table_frame = tk.Frame(root)
    table_frame.pack(pady=10)

    entry_widget = tk.Entry(root, width=30)
    entry_widget.pack(pady=10)

    attempts_label = tk.Label(root, text="Attempts left: 3")
    attempts_label.pack(pady=10)

    entry_widget_row = tk.Entry(button_frame, width=5)
    entry_widget_row.pack(pady=10, side=tk.LEFT)

    entry_widget_col = tk.Entry(button_frame, width=5)
    entry_widget_col.pack(pady=10, side=tk.LEFT)

    attempts_label = tk.Label(root, text="Attempts left: 3")
    attempts_label.pack(pady=10)

    root.mainloop()


if __name__ == '__main__':
    main()

