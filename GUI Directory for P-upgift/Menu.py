import tkinter as tk
from tkinter import simpledialog, messagebox, ttk
import csv
import random
from functools import partial
from Questions import AtomicNumberGame, ElementGame, MassGame
from Fill_Periodic_Table import PeriodicTableGame
from Show_Periodic_Table import PeriodicTable

class MenuFrame:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.pack()

        self.button1 = tk.Button(self.frame, text='Atomic Number Game', width=25, command=self.play_atomic_number_game)
        self.button1.pack()
        self.button2 = tk.Button(self.frame, text='Element Game', width=25, command=self.play_element_game)
        self.button2.pack()
        self.button3 = tk.Button(self.frame, text='Mass Game', width=25, command=self.play_mass_game)
        self.button3.pack()
        self.button4 = tk.Button(self.frame, text='Fill Periodic Table', width=25, command=self.play_periodic_table_game)
        self.button4.pack()
        self.button5 = tk.Button(self.frame, text='Show Periodic Table', width=25, command=self.show_periodic_table)
        self.button5.pack()
        self.button6 = tk.Button(self.frame, text='Quit', width=25, command=self.close_window)
        self.button6.pack()

    def play_atomic_number_game(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = AtomicNumberGame(self.newWindow)
        self.app.play()

    def play_element_game(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = ElementGame(self.newWindow)
        self.app.play()

    def play_mass_game(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = MassGame(self.newWindow)
        self.app.play()

    def play_periodic_table_game(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = PeriodicTableGame(self.newWindow)
        self.app.play()

    def show_periodic_table(self):
        csv_file_path = "sorted_mass_with_atomic_numbers.csv"
        element_info_list = PeriodicTable.read_elements_from_csv(csv_file_path)
        max_row = max(element_info[1] for element_info in element_info_list)
        max_col = max(element_info[2] for element_info in element_info_list)
        rows = max_row
        columns = max_col

        self.newWindow = tk.Toplevel(self.master)
        self.app = PeriodicTable(self.newWindow, elements=element_info_list, rows=rows, columns=columns)
        self.app.pack()  # Use pack() instead of grid()
        self.newWindow.mainloop()

    def close_window(self):
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = MenuFrame(root)
    root.mainloop()
