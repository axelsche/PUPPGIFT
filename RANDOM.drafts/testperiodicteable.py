import tkinter as tk
from Show_Periodic_Table import PeriodicTable

if __name__ == "__main__":
    csv_file_path = "sorted_mass_with_atomic_numbers.csv"
    element_info_list = PeriodicTable.read_elements_from_csv(csv_file_path)

    max_row = max(element_info[1] for element_info in element_info_list)
    max_col = max(element_info[2] for element_info in element_info_list)

    rows = max_row + 1
    columns = max_col + 1

    root = tk.Tk()
    app = PeriodicTable(root, elements=element_info_list, rows=rows, columns=columns)
    app.grid(row=0, column=0)
    root.mainloop()
