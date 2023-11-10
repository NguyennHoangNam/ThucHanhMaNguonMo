import tkinter as tk
from tkinter import filedialog
import numpy as np
import matplotlib.pyplot as plt


class SignalProcessingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Signal Processing App")

        self.signal = None

        # Create the UI elements
        self.load_button = tk.Button(root, text="Load Signal", command=self.load_signal)
        self.load_button.pack()

        self.process_button = tk.Button(root, text="Process Signal", command=self.process_signal, state=tk.DISABLED)
        self.process_button.pack()

        self.plot_button = tk.Button(root, text="Plot Signal", command=self.plot_signal, state=tk.DISABLED)
        self.plot_button.pack()

        self.root.mainloop()

    def load_signal(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            # Load the signal from file
            self.signal = np.loadtxt(file_path)
            self.process_button.config(state=tk.NORMAL)

    def process_signal(self):
        # Apply a simple signal processing operation
        self.signal = np.abs(self.signal)  # Example: taking the absolute value of the signal

        self.plot_button.config(state=tk.NORMAL)

    def plot_signal(self):
        # Plot the signal
        plt.figure()
        plt.plot(self.signal)
        plt.xlabel("Time")
        plt.ylabel("Amplitude")
        plt.title("Signal")
        plt.show()


if __name__ == "__main__":
    root = tk.Tk()
    app = SignalProcessingApp(root)
