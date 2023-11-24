import pandas as pd
import tkinter as tk
import tkinter.filedialog as fd
import matplotlib.pyplot as plt

def import_file():
    global df
    filetypes = (
        ('CSV Files', '*.csv'),
        ('Excel Files', ('*.xls', '*.xlsx'))
    )
    filepath = fd.askopenfilename(filetypes=filetypes)
    if filepath:
        try:
            df = pd.read_csv(filepath) if filepath.endswith('.csv') else pd.read_excel(filepath)
            display_data(df)
        except Exception as e:
            result_label.config(text=f'Error occurred while importing the file: {e}')

def display_data(df):
    for widget in data_frame.winfo_children():
        widget.destroy()

    for i, col in enumerate(df.columns):
        label = tk.Label(data_frame, text=col, relief=tk.RIDGE, width=15)
        label.grid(row=0, column=i, sticky=tk.NSEW)

    for i, row in enumerate(df.itertuples(), start=1):
        for j, value in enumerate(row[1:], start=0):
            label = tk.Label(data_frame, text=value, relief=tk.RIDGE, width=15)
            label.grid(row=i, column=j, sticky=tk.NSEW)

def find_max(df, axis):
    result = df.max(axis=axis)
    result_label.config(text=f"Maximum values:\n{result}")

def find_min(df, axis):
    result = df.min(axis=axis)
    result_label.config(text=f"Minimum values:\n{result}")

def calculate_average(df, axis):
    # Filter out non-numeric columns
    numeric_columns = df.select_dtypes(include='number')

    if numeric_columns.empty:
        result_label.config(text="No numeric columns found.")
    else:
        result = numeric_columns.mean(axis=axis)
        result_label.config(text=f"Average values:\n{result}")

def show_graph(df, column_entry):
    # Get the selected column from the entry widget
    selected_column = column_entry.get()

    # Convert values to numeric
    df = df.apply(pd.to_numeric, errors='coerce')

    # Drop any rows with missing values
    #df = df.dropna()
    if df.empty:
        result_label.config(text="No valid data to plot.")
    elif selected_column not in df.columns:
        result_label.config(text="Selected column does not exist.")
    else:
        fig, ax = plt.subplots()
        ax.plot(df.index, df[selected_column])
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_title('Graph')
        plt.show()

root = tk.Tk()
root.title('Data Analysis')

file_frame = tk.Frame(root)
file_frame.pack(pady=10)

data_frame = tk.Frame(root)
data_frame.pack(pady=10)

result_label = tk.Label(root, text='', justify=tk.LEFT)
result_label.pack(pady=10)

import_button = tk.Button(file_frame, text='Import File', command=import_file)
import_button.pack(side=tk.LEFT, padx=10)

max_button = tk.Button(root, text='Find Maximum', command=lambda: find_max(df, 0))
max_button.pack(pady=15,side=tk.LEFT)

min_button = tk.Button(root, text='Find Minimum', command=lambda: find_min(df, 0))
min_button.pack(pady=15,side=tk.LEFT)

avg_button = tk.Button(root, text='Calculate Average', command=lambda: calculate_average(df, 0))
avg_button.pack(pady=15,side=tk.LEFT)



# Create the "Show Graph" button
graph_button = tk.Button(root, text='Show Graph', command=lambda: show_graph(df, column_entry))
graph_button.pack(side=tk.LEFT)
column_entry = tk.Entry(root)
column_entry.pack(side=tk.LEFT)

root.mainloop()
