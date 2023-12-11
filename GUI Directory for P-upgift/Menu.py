import tkinter as tk
from Questions import AtomicNumberGame, ElementGame, MassGame
from Fill_Periodic_Table import PeriodicTableGame
from Show_Periodic_Table import PeriodicTable


class MenuFrame:
    """
    A class representing the main menu frame for Periodic Table learning games.

    Attributes:
        - :ivar master: The root Tkinter window.
        - :ivar frame: The main frame of the menu.
        - :ivar button1: Button to play the Atomic Number Game.
        - :ivar button2: Button to play the Element Game.
        - :ivar button3: Button to play the Mass Game.
        - :ivar button4: Button to play the Fill Periodic Table Game.
        - :ivar button5: Button to show the Periodic Table.
        - :ivar button6: Button to quit the application.
    """

    def __init__(self, master):
        """
        Initializes the MenuFrame instance.

        Parameters:
         - :param tk.Tk master: The root Tkinter window.
        """
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.pack()
        self.button1 = tk.Button(self.frame, text='Atomic Number Game', width=25, command=self.play_atomic_number_game)
        self.button1.pack()
        self.button2 = tk.Button(self.frame, text='Element Game', width=25, command=self.play_element_game)
        self.button2.pack()
        self.button3 = tk.Button(self.frame, text='Mass Game', width=25, command=self.play_mass_game)
        self.button3.pack()
        self.button4 = tk.Button(self.frame, text='Fill Periodic Table', width=25,
                                 command=self.play_periodic_table_game)
        self.button4.pack()
        self.button5 = tk.Button(self.frame, text='Show Periodic Table', width=25, command=self.show_periodic_table)
        self.button5.pack()
        self.button6 = tk.Button(self.frame, text='Quit', width=25, command=self.close_window)
        self.button6.pack()

    def play_atomic_number_game(self):
        """
        Opens a new window to play the Atomic Number Game.
        """
        self.newWindow = tk.Toplevel(self.master)
        self.app = AtomicNumberGame(self.newWindow)
        self.app.play()

    def play_element_game(self):
        """
        Opens a new window to play the Element Game.
        """
        self.newWindow = tk.Toplevel(self.master)
        self.app = ElementGame(self.newWindow)
        self.app.play()

    def play_mass_game(self):
        """
        Opens a new window to play the Mass Game.
        """
        self.newWindow = tk.Toplevel(self.master)
        self.app = MassGame(self.newWindow)
        self.app.play()

    def play_periodic_table_game(self):
        """
        Opens a new window to play the Fill Periodic Table Game.
        """
        self.newWindow = tk.Toplevel(self.master)
        self.app = PeriodicTableGame(self.newWindow)
        self.app.play()

    def show_periodic_table(self):
        """
        Shows the Periodic Table in a new window.
        """
        csv_file_path = "sorted_mass_with_atomic_numbers.csv"
        element_info_list = PeriodicTable.read_elements_from_csv(csv_file_path)
        max_row = max(element_info[1] for element_info in element_info_list)
        max_col = max(element_info[2] for element_info in element_info_list)
        rows = max_row
        columns = max_col

        self.newWindow = tk.Toplevel(self.master)
        self.app = PeriodicTable(self.newWindow, elements=element_info_list, rows=rows, columns=columns)
        self.app.pack()
        self.newWindow.mainloop()

    def close_window(self):
        self.master.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Periodic Table Learning Games")
    app = MenuFrame(root)
    root.mainloop()
