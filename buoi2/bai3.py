import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.patches import Polygon, Circle, Rectangle, Arc

def plot_point():
    x = float(point_x.get())
    y = float(point_y.get())
    ax.scatter(x, y, color='red', marker='o', s=50)
    canvas.draw()

def plot_line():
    x1 = float(line_x1.get())
    y1 = float(line_y1.get())
    x2 = float(line_x2.get())
    y2 = float(line_y2.get())
    ax.plot([x1, x2], [y1, y2], color='blue', linewidth=2)
    canvas.draw()

def plot_polygon():
    vertices_str = polygon_vertices.get()
    vertices = [list(map(float, v.split(','))) for v in vertices_str.split(';')]
    polygon = Polygon(vertices, closed=True, facecolor='yellow', edgecolor='black')
    ax.add_patch(polygon)
    canvas.draw()

def plot_circle():
    cx = float(circle_cx.get())
    cy = float(circle_cy.get())
    radius = float(circle_radius.get())
    circle = Circle((cx, cy), radius=radius, facecolor='green', edgecolor='black')
    ax.add_patch(circle)
    canvas.draw()

def plot_rectangle():
    x = float(rectangle_x.get())
    y = float(rectangle_y.get())
    width = float(rectangle_width.get())
    height = float(rectangle_height.get())
    rectangle = Rectangle((x, y), width=width, height=height, facecolor='cyan', edgecolor='black')
    ax.add_patch(rectangle)
    canvas.draw()

def plot_arc():
    cx = float(arc_cx.get())
    cy = float(arc_cy.get())
    width = float(arc_width.get())
    height = float(arc_height.get())
    theta1 = float(arc_theta1.get())
    theta2 = float(arc_theta2.get())
    arc = Arc((cx, cy), width=width, height=height, theta1=theta1, theta2=theta2, edgecolor='magenta', linewidth=2)
    ax.add_patch(arc)
    canvas.draw()

# Create the main window
root = tk.Tk()
root.title("Geometric Features")

# Create a Matplotlib figure and axes
fig = Figure(figsize=(6, 4), dpi=100)
ax = fig.add_subplot(111)

# Create a Tkinter canvas for displaying the Matplotlib figure
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().grid(row=0, column=0, columnspan=6, padx=10, pady=10)

# Create input fields for each geometric feature
point_x = tk.Entry(root)
point_x.grid(row=1, column=0, padx=5, pady=5)
point_y = tk.Entry(root)
point_y.grid(row=1, column=1, padx=5, pady=5)
point_button = tk.Button(root, text="Plot Point", command=plot_point)
point_button.grid(row=1, column=2, padx=5, pady=5)

line_x1 = tk.Entry(root)
line_x1.grid(row=2, column=0, padx=5, pady=5)
line_y1 = tk.Entry(root)
line_y1.grid(row=2, column=1, padx=5, pady=5)
line_x2 = tk.Entry(root)
line_x2.grid(row=2, column=2, padx=5, pady=5)
line_y2 = tk.Entry(root)
line_y2.grid(row=2, column=3, padx=5, pady=5)
line_button = tk.Button(root, text="Plot Line", command=plot_line)
line_button.grid(row=2, column=4, padx=5, pady=5)

polygon_vertices = tk.Entry(root)
polygon_vertices.grid(row=3, column=0, columnspan=4, padx=5, pady=5)
polygon_button = tk.Button(root, text="Plot Polygon", command=plot_polygon)
polygon_button.grid(row=3, column=4, padx=5, pady=5)

circle_cx = tk.Entry(root)
circle_cx.grid(row=4, column=0, padx=5, pady=5)
circle_cy = tk.Entry(root)
circle_cy.grid(row=4, column=1, padx=5, pady=5)
circle_radius = tk.Entry(root)
circle_radius.grid( row=4, column=2, padx=5, pady=5)
circle_button = tk.Button(root, text="Plot Circle",command=plot_circle)
circle_button.grid(row=4, column=3, padx=5, pady=5)

rectangle_x = tk.Entry(root)
rectangle_x.grid(row=5, column=0, padx=5, pady=5)
rectangle_y = tk.Entry(root)
rectangle_y.grid(row=5, column=1, padx=5, pady=5)
rectangle_width = tk.Entry(root)
rectangle_width.grid(row=5, column=2, padx=5, pady=5)
rectangle_height = tk.Entry(root)
rectangle_height.grid(row=5, column=3, padx=5, pady=5)
rectangle_button = tk.Button(root, text="Plot Rectangle", command=plot_rectangle)
rectangle_button.grid(row=5, column=4, padx=5, pady=5)

arc_cx = tk.Entry(root)
arc_cx.grid(row=6, column=0, padx=5, pady=5)
arc_cy = tk.Entry(root)
arc_cy.grid(row=6, column=1, padx=5, pady=5)
arc_width = tk.Entry(root)
arc_width.grid(row=6, column=2, padx=5, pady=5)
arc_height = tk.Entry(root)
arc_height.grid(row=6, column=3, padx=5, pady=5)
arc_theta1 = tk.Entry(root)
arc_theta1.grid(row=6, column=4, padx=5, pady=5)
arc_theta2 = tk.Entry(root)
arc_theta2.grid(row=6, column=5, padx=5, pady=5)
arc_button = tk.Button(root, text="Plot Arc", command=plot_arc)
arc_button.grid(row=6, column=6, padx=5, pady=5)

# Configure the grid to expand with the window
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Start the Tkinter event loop
root.mainloop()
