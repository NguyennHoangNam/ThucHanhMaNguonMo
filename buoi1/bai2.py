import tkinter as tk
from sympy import symbols, diff, integrate, simplify
import matplotlib.pyplot as plt
import numpy as np

def differentiate():
    # Get the user input
    expression = input_entry.get()

    # Create a SymPy symbol for the variable
    x = symbols('x')

    try:
        # Differentiate the expression
        derivative = diff(expression, x)

        # Simplify the derivative expression
        derivative = simplify(derivative)

        # Display the result
        result_label.config(text="Derivative: " + str(derivative))
    except:
        result_label.config(text="Invalid input")

def integrate_func():
    # Get the user input
    expression = input_entry.get()

    # Create a SymPy symbol for the variable
    x = symbols('x')

    try:
        # Integrate the expression
        integral = integrate(expression, x)

        # Display the result
        result_label.config(text="Integral: " + str(integral))
    except:
        result_label.config(text="Invalid input")

def plot_func():
    # Get the user input
    expression = input_entry.get()

    # Create a SymPy symbol for the variable
    x = symbols('x')

    try:
        # Create a SymPy expression from the input
        expr = sympify(expression)

        # Create a lambda function from the expression
        f = lambdify(x, expr)

        # Generate x values for the plot
        x_vals = np.linspace(-10, 10, 400)

        # Evaluate the function for the x values
        y_vals = f(x_vals)

        # Plot the function
        plt.figure()
        plt.plot(x_vals, y_vals)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Function Plot')
        plt.grid(True)
        plt.show()
    except:
        result_label.config(text="Invalid input")

# Create the Tkinter window
window = tk.Tk()
window.title("Calculus Learning Tool")

# Create input field for the expression
input_label = tk.Label(window, text="Enter an expression:")
input_label.pack()
input_entry = tk.Entry(window)
input_entry.pack()

# Create button to differentiate the expression
differentiate_button = tk.Button(window, text="Differentiate", command=differentiate)
differentiate_button.pack()

# Create button to integrate the expression
integrate_button = tk.Button(window, text="Integrate", command=integrate_func)
integrate_button.pack()

# Create button to plot the expression
plot_button = tk.Button(window, text="Plot", command=plot_func)
plot_button.pack()

# Create label to display the result
result_label = tk.Label(window)
result_label.pack()

window.mainloop()
