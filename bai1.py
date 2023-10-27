import tkinter as tk
import numpy as np

def solve_equations():
    # Get values from input fields
    equations = []
    for i in range(n):
        equation = []
        for j in range(n+1):
            entry = entries[i][j].get()
            equation.append(float(entry))
        equations.append(equation)

    # Convert equations to NumPy array
    A = np.array([equation[:-1] for equation in equations])
    b = np.array([equation[-1] for equation in equations])

    # Solve the system of equations
    try:
        x = np.linalg.solve(A, b)
        result_label.config(text="Result: " + ", ".join(str(round(val, 2)) for val in x))
    except np.linalg.LinAlgError:
        result_label.config(text="The system of equations has no solution.")

# Create the Tkinter window
window = tk.Tk()
window.title("System of Equations Solver")
window.geometry("1000x500")

# Create input fields for the number of equations and unknowns
n_label = tk.Label(window, text="Number of Equations (n):")
n_label.grid(row=0, column=0, padx=5, pady=5)
n_entry = tk.Entry(window)
n_entry.grid(row=0, column=1, padx=5, pady=5)

def create_entries():
    global n, entries, result_label

    # Clear existing input fields and result label (if any)
    if 'entries' in globals():
        for row in entries:
            for entry in row:
                entry.destroy()
        result_label.destroy()

    # Create new input fields and result label
    n = int(n_entry.get())
    entries = []
    for i in range(n):
        equation = []
        for j in range(n+1):
            entry = tk.Entry(window)
            entry.grid(row=i+1, column=j, padx=5, pady=5)
            equation.append(entry)
        entries.append(equation)

    solve_button = tk.Button(window, text="Solve", command=solve_equations)
    solve_button.grid(row=n+1, column=n, padx=5, pady=10)

    result_label = tk.Label(window)
    result_label.grid(row=n+2, columnspan=n, padx=5, pady=10)

create_entries_button = tk.Button(window, text="Confirm", command=create_entries)
create_entries_button.grid(row=0, column=2, padx=5, pady=5)

window.mainloop()
