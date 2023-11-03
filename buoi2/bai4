import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import pandas as pd

class ExcelClone:
    def __init__(self, root):
        self.root = root
        self.root.title("Excel Clone")
        self.current_file = None
        self.data_frame = pd.DataFrame()

        self.create_menu()
        self.create_spreadsheet()

    def create_menu(self):
        menu_bar = tk.Menu(self.root)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_file_as)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)

        edit_menu = tk.Menu(menu_bar, tearoff=0)
        edit_menu.add_command(label="Sort Column", command=self.sort_column)
        edit_menu.add_command(label="Find", command=self.find_value)

        menu_bar.add_cascade(label="File", menu=file_menu)
        menu_bar.add_cascade(label="Edit", menu=edit_menu)
        self.root.config(menu=menu_bar)

    def create_spreadsheet(self):
        self.sheet = tk.Text(self.root)
        self.sheet.pack(expand=True, fill="both")

    def new_file(self):
        self.sheet.delete("1.0", "end")
        self.current_file = None
        self.data_frame = pd.DataFrame()

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if file_path:
            self.current_file = file_path
            self.data_frame = pd.read_csv(file_path)
            self.sheet.delete("1.0", "end")
            self.sheet.insert("1.0", self.data_frame.to_string(index=False))

    def save_file(self):
        if self.current_file:
            data = self.sheet.get("1.0", "end")
            lines = data.strip().split("\n")
            rows = [line.split("\t") for line in lines]
            self.data_frame = pd.DataFrame(rows)
            self.data_frame.columns = self.data_frame.iloc[0]
            self.data_frame = self.data_frame[1:]

            try:
                self.data_frame.to_csv(self.current_file, index=False)
                self.show_message("Save", "File saved successfully.")
            except Exception as e:
                self.show_message("Error", str(e))
        else:
            self.save_file_as()

    def save_file_as(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".csv",
                                                filetypes=[("CSV Files", "*.csv")])
        if file_path:
            self.current_file = file_path
            self.save_file()

    def sort_column(self):
        column_name = self.show_input_dialog("Sort Column", "Enter column name:")
        if column_name:
            try:
                self.data_frame.sort_values(by=column_name, inplace=True)
                self.sheet.delete("1.0", "end")
                self.sheet.insert("1.0", self.data_frame.to_string(index=False))
            except KeyError:
                self.show_message("Error", "Invalid column name.")

    def find_value(self):
        value = self.show_input_dialog("Find", "Enter value:")
        if value:
            matching_rows = self.data_frame[self.data_frame.eq(value).any(1)]
            if not matching_rows.empty:
                self.sheet.delete("1.0", "end")
                self.sheet.insert("1.0", matching_rows.to_string(index=False))
            else:
                self.show_message("Find", "Value not found.")

    @staticmethod
    def show_message(title, message):
        messagebox.showinfo(title, message)

    @staticmethod
    def show_input_dialog(title, message):
        return simpledialog.askstring(title, message)

if __name__ == "__main__":
    root = tk.Tk()
    ExcelClone(root)
    root.mainloop()
