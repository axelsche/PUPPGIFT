import tkinter as tk
from tkinter import messagebox, simpledialog
import csv
import random


class Game:
    """
    Base class for chemistry games.
    """

    def __init__(self, app):
        """
        Initialize the game.

        Parameters:
        - app: Tkinter application instance
        """
        self.app = app
        self.attempts_per_question = 3
        self.elements = []
        self.load_elements()
        self.create_widgets()

    def load_elements(self):
        """
        Load chemical elements from a CSV file.
        """
        with open('sorted_mass_with_atomic_numbers.csv', 'r') as file:
            reader = csv.DictReader(file)
            self.elements = list(reader)

    def play_again(self):
        """
        Ask the user if they want to play again.

        Returns:
        - bool: True if the user wants to play again, False otherwise.
        """
        return messagebox.askyesno("Play Again", "Do you want to play again?")

    def create_widgets(self):
        """
        Create widgets for the game.
        """
        self.question_text = tk.StringVar()
        self.text_box = tk.Text(self.app, height=10, width=40, wrap=tk.WORD)
        self.text_box.pack(pady=10)

    def display_question(self, question_text):
        """
        Display a question in the text box.

        Parameters:
        - question_text: Text of the question to be displayed.
        """
        self.text_box.delete("1.0", tk.END)  # Clear existing text
        self.text_box.insert(tk.END, question_text)

    def play(self):
        """
        Abstract method to be implemented in derived classes.
        """
        raise NotImplementedError("The play method must be implemented in the derived class.")


class AtomicNumberGame(Game):
    """
    Game to guess atomic numbers.
    """

    def play(self):
        """
        Play the atomic number game.
        """
        while True:
            random.shuffle(self.elements)

            for element in self.elements:
                question_text = f"Element: {element['Element']} - Mass: {element['Mass']}\n"
                self.display_question(question_text)

                attempts = 0
                while attempts < self.attempts_per_question:
                    guess = simpledialog.askinteger("Guess the Atomic Number", f"Attempt {attempts + 1}: Guess the "
                                                                               f"atomic number:")

                    if guess is None:  # User clicked Cancel
                        break

                    if guess == int(element['AtomicNumber']):
                        self.text_box.insert(tk.END, "Correct!\n")
                        break
                    else:
                        attempts += 1
                        self.text_box.insert(tk.END, f"Wrong! You have {self.attempts_per_question - attempts} "
                                                     f"attempts remaining.\n")
                        if attempts == self.attempts_per_question:
                            self.text_box.insert(tk.END, f"Out of attempts. The correct answer is:"
                                                         f" {element['AtomicNumber']}\n")
                            break

                self.text_box.insert(tk.END, "\n")

                if not self.play_again():
                    self.text_box.delete("1.0", tk.END)  # Clear text box
                    self.app.destroy()  # Close the window
                    return False


class ElementGame(Game):
    """
    Game to guess chemical elements.
    """

    def play(self):
        """
        Play the element game.
        """
        while True:
            random.shuffle(self.elements)

            for element in self.elements:
                question_text = f"Atomic number: {element['AtomicNumber']} - Mass: {element['Mass']}\n"
                self.display_question(question_text)

                attempts = 0
                while attempts < self.attempts_per_question:
                    guess = simpledialog.askstring("Guess the Element", f"Attempt {attempts + 1}: Guess the element:")

                    if guess is None:  # User clicked Cancel
                        break

                    if 0 < len(guess) <= 2 and guess.isalpha():
                        if guess.lower() == element['Element'].lower():
                            self.text_box.insert(tk.END, "Correct!\n")
                            break
                        else:
                            self.text_box.insert(tk.END, f"Wrong! \n")
                            attempts += 1
                            self.text_box.insert(tk.END,
                                                 f"You have {self.attempts_per_question - attempts} attempts "
                                                 f"remaining.\n")
                            if attempts == self.attempts_per_question:
                                self.text_box.insert(tk.END, "Out of attempts.\n")
                                break
                    else:
                        self.text_box.insert(tk.END,
                                             "Invalid input. Please enter a one or two-letter string without"
                                             " numbers.\n")

                self.text_box.insert(tk.END, "\n")

                if not self.play_again():
                    self.text_box.delete("1.0", tk.END)  # Clear text box
                    self.app.destroy()  # Close the window
                    return False


class MassGame(Game):
    """
    Game to guess element masses.
    """

    def play(self):
        """
        Play the mass game.
        """
        while True:
            random.shuffle(self.elements)

            for element in self.elements:
                masses = [float(element['Mass'])]
                for i in range(2):
                    random_element = random.choice(self.elements)
                    while random_element == element:
                        random_element = random.choice(self.elements)
                    masses.append(float(random_element['Mass']))
                random.shuffle(masses)

                question_text = f"Element: {element['Element']} - Atomic number: {element['AtomicNumber']}\nOptions:\n"
                for i, mass_option in enumerate(masses):
                    question_text += f"{chr(65 + i)}. {mass_option}\n"

                self.display_question(question_text)

                guess_index = None
                while guess_index not in range(len(masses)):
                    guess_index = simpledialog.askstring("Select the Correct Mass",
                                                         "Select the correct mass (A, B, C):").upper()
                    if guess_index.isalpha():
                        guess_index = ord(guess_index) - 65
                    else:
                        guess_index = None

                guessed_mass = masses[guess_index]

                if guessed_mass == float(element['Mass']):
                    self.text_box.insert(tk.END, "Correct!\n")
                else:
                    self.text_box.insert(tk.END, f"Wrong! The correct answer is: {element['Mass']}\n")

                self.text_box.insert(tk.END, "\n")

                if not self.play_again():
                    self.text_box.delete("1.0", tk.END)  # Clear text box
                    self.app.destroy()  # Close the window
                    return False


class GameApp(tk.Tk):
    """
    Tkinter application for chemistry games.
    """

    def __init__(self):
        """
        Initialize the game application.
        """
        super().__init__()
        self.title("Chemistry Games")
        self.geometry("600x400")

        self.label = tk.Label(self, text="Choose a Chemistry Game:")
        self.label.pack(pady=10)

        self.atomic_number_button = tk.Button(self, text="Atomic Number Game", command=self.play_atomic_number_game)
        self.atomic_number_button.pack(pady=10)

        self.element_button = tk.Button(self, text="Element Game", command=self.play_element_game)
        self.element_button.pack(pady=10)

        self.mass_button = tk.Button(self, text="Mass Game", command=self.play_mass_game)
        self.mass_button.pack(pady=10)

        self.game_text = tk.Text(self, height=10, width=40, wrap=tk.WORD)
        self.game_text.pack(pady=10)

    def play_atomic_number_game(self):
        """
        Start the atomic number game.
        """
        self.clear_text_box()
        game = AtomicNumberGame(self)
        game.play()

    def play_element_game(self):
        """
        Start the element game.
        """
        self.clear_text_box()
        game = ElementGame(self)
        game.play()

    def play_mass_game(self):
        """
        Start the mass game.
        """
        self.clear_text_box()
        game = MassGame(self)
        game.play()

    def clear_text_box(self):
        """
        Clear the text box.
        """
        self.game_text.delete("1.0", tk.END)


if __name__ == "__main__":
    app = GameApp()
    app.mainloop()
