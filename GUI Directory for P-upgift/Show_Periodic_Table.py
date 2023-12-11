import tkinter as tk
import csv

class PeriodicTable(tk.Frame):
    def __init__(self, master=None, elements=None, rows=None, columns=None, **kwargs):#**kwargs collects additional keyword arguments that you can pass when creating the widget
        super().__init__(master, **kwargs)
        self.master = master
        self.title_label = tk.Label(self, text="Periodic Table")
        self.title_label.grid(row=0, column=0, columnspan=columns)
        self.elements = elements
        self.rows = rows
        self.columns = columns
        self.create_table()
        self.close_button = tk.Button(self, text="Close", command=self.close_window)
        self.close_button.grid(row=rows, columnspan=columns)


    def read_elements_from_csv(csv_file):
        elements = []
        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                if len(row) >= 5:  # Ensure there are enough columns
                    abbreviation = row[1]  # Assuming abbreviation is in column 2
                    row_num = int(row[3])  # Assuming row is in column 4
                    col_num = int(row[4])  # Assuming column is in column 5
                    elements.append((abbreviation, row_num, col_num))
        return elements

    def create_table(self):
        for element_info in self.elements:
            abbreviation, row_num, col_num = element_info
            button = tk.Button(self, text=abbreviation, width=3, height=2)
            button.grid(row=row_num, column=col_num, padx=2, pady=2)

    def close_window(self):
        self.master.destroy()

if __name__ == "__main__":
    # Specify the path to your CSV file containing element data
    csv_file_path = "sorted_mass_with_atomic_numbers.csv"

    # Read elements from the CSV file
    element_info_list = PeriodicTable.read_elements_from_csv(csv_file_path)

    # Find the maximum row and column numbers
    max_row = max(element_info[1] for element_info in element_info_list)
    max_col = max(element_info[2] for element_info in element_info_list)

    rows = max_row + 1  # Adding 1 to account for 0-based indexing
    columns = max_col + 1  # Adding 1 to account for 0-based indexing

    root = tk.Tk()
    app = PeriodicTable(root, elements=element_info_list, rows=rows, columns=columns)
    app.grid(row=0, column=0)
    root.mainloop()
