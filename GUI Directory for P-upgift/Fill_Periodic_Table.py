import tkinter as tk
from tkinter import messagebox, ttk
import csv
import random
from functools import partial


class PeriodicTableGame:
    """
    A class representing a game to fill in the periodic table grid.
    """

    def __init__(self, app):
        """
        Initialize the game.

        Parameters:
            app (tk.Tk): The main Tkinter application.
        """
        self.app = app
        self.attempts_per_question = 3

        # Load elements from the CSV file
        self.load_elements_from_csv()

        # Shuffle the elements
        self.shuffled_elements = list(self.elements)  # Create a copy to avoid modifying the original list
        random.shuffle(self.shuffled_elements)

        # Extract unique rows and columns from the elements
        unique_rows = set(int(element['row']) - 1 for element in self.shuffled_elements)
        unique_columns = set(int(element['col']) - 1 for element in self.shuffled_elements)

        # Set the grid size based on unique rows and columns
        self.grid_size = (max(unique_rows) + 1, max(unique_columns) + 1)
        self.grid = [['' for _ in range(self.grid_size[1])] for _ in range(self.grid_size[0])]

        # Initialize current_element_index to keep track of the current element being prompted
        self.current_element_index = 0

        # Create the GUI
        self.create_widgets()
        self.prompt_element()

    def load_elements_from_csv(self):
        """
        Load elements from the CSV file.
        """
        with open('sorted_mass_with_atomic_numbers.csv', 'r') as file:
            reader = csv.DictReader(file)
            self.elements = list(reader)

    def create_widgets(self):
        """
        Create widgets for the GUI.
        """
        self.label = tk.Label(self.app, text="What is the position of {'Element'} in the periodic table?")
        self.label.grid(row=0, column=0, columnspan=self.grid_size[1], pady=10)

        # Create a grid of widgets only where rows and columns are specified
        for element in self.shuffled_elements:
            row = int(element['row']) - 1
            col = int(element['col']) - 1
            abbreviation = element['Element']
            button = ttk.Button(self.app, text="", command=partial(self.check_guess, row, col, abbreviation), width=2)
            button.grid(row=row + 1, column=col, padx=2, pady=2)

        self.textboxes = []

        self.submit_button = ttk.Button(self.app, text="Next Element", command=self.next_element)
        self.submit_button.grid(row=self.grid_size[0] + 1, column=self.grid_size[1] // 2, pady=10)

    def prompt_element(self):
        """
        Prompt the user to fill in the grid for the current element.
        """
        if self.current_element_index < len(self.shuffled_elements):
            current_element = self.shuffled_elements[self.current_element_index]
            element_name = current_element['Element']
            element_position = f"Row: {current_element['row']}, Column: {current_element['col']}"
            self.label.config(text=f"Fill the grid for the element: {element_name} ")
            messagebox.showinfo("Fill the Grid", f"Fill the grid for the element: {element_name}")
        else:
            self.label.config(text="Game Over: You have completed the game!")
            messagebox.showinfo("Game Over", "You have completed the game.")

    def check_guess(self, row, col, abbreviation):
        """
        Check if the guessed row and column are correct for the current element.

        Parameters:
            row (int): The guessed row.
            col (int): The guessed column.
            abbreviation (str): The element abbreviation.
        """
        if self.current_element_index < len(self.shuffled_elements):
            element = self.shuffled_elements[self.current_element_index]
            correct_row = int(element['row']) - 1
            correct_column = int(element['col']) - 1

            print(f"Element: {element['Element']}, Guessed row: {row}, Guessed column: {col}")

            if row == correct_row and col == correct_column:
                messagebox.showinfo("Correct!", f"The element {element['Element']} is correctly placed.")
                self.grid[correct_row][correct_column] = element['Element']
                print(f"Inserted abbreviation: {element['Element']} into grid at {correct_row}, {correct_column}")
                self.create_textbox(row, col, element['Element'])
                self.remove_button(row, col)
            else:
                messagebox.showinfo("Incorrect!",
                                    f"The correct position for {element['Element']} is {correct_row + 1}, "
                                    f"{correct_column + 1}.")

    def create_textbox(self, row, col, abbreviation):
        """
        Create a new text box at the specified row and column with the correct abbreviation.

        Parameters:
            row (int): The row for the text box.
            col (int): The column for the text box.
            abbreviation (str): The element abbreviation.
        """
        textbox = tk.Text(self.app, height=1, width=3, state=tk.NORMAL)  # Set the state to normal
        textbox.insert(tk.END, abbreviation)
        textbox.grid(row=row + 1, column=col, pady=2)
        self.textboxes.append(textbox)
        textbox.configure(state=tk.DISABLED)  # Disable the text widget after inserting the text

    def remove_button(self, row, col):
        """
        Remove the button at the specified row and column.

        Parameters:
            row (int): The row of the button.
            col (int): The column of the button.
        """
        for widget in self.app.winfo_children():
            if isinstance(widget, ttk.Button) and widget.grid_info()['row'] == row + 1 and widget.grid_info()[
                'column'] == col:
                widget.destroy()

    def next_element(self):
        """
        Move to the next element.
        """
        self.current_element_index += 1
        self.prompt_element()

    def play_again(self):
        """
        Ask the user if they want to play again.
        """
        return messagebox.askyesno("Play Again", "Do you want to play again?")


if __name__ == "__main__":
    app = tk.Tk()
    app.title("Periodic Table Game")
    game = PeriodicTableGame(app)
    app.mainloop()
