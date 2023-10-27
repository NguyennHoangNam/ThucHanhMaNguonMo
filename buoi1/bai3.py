import tkinter as tk
import matplotlib.pyplot as plt
from sympy import symbols, lambdify

# Create a Tkinter window
window = tk.Tk()
window.title("Function Graph")

# Function to plot the graph
def plot_graph():
    # Get the function expression from the input
    function_expr = function_entry.get()

    # Create a symbolic variable
    x = symbols('x')

    try:
        # Convert the expression to a SymPy expression
        function = eval(function_expr)

        # Convert the SymPy expression to a callable function
        func = lambdify(x, function, modules=['numpy'])

        # Generate x values for the plot
        x_values = range(-10, 11)

        # Evaluate the function for each x value
        y_values = [func(x_val) for x_val in x_values]

        # Clear the previous plot, if any
        plt.clf()

        # Plot the graph
        plt.plot(x_values, y_values)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Function Graph')
        plt.grid(True)

        # Display the plot
        plt.show()

    except Exception as e:
        # Show an error message if the input is invalid
        error_label.config(text=str(e))

# Function input label
function_label = tk.Label(window, text="Enter a function:")
function_label.pack()

# Function input entry
function_entry = tk.Entry(window)
function_entry.pack()

# Plot button
plot_button = tk.Button(window, text="Plot", command=plot_graph)
plot_button.pack()

# Error label
error_label = tk.Label(window, fg="red")
error_label.pack()

# Run the Tkinter event loop
window.mainloop()
