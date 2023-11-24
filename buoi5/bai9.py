import tkinter as tk
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk

def blur_image():
    # Open file dialog to select an image
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    
    # Read the image using OpenCV
    image = cv2.imread(file_path)
    
    # Apply blur effect using OpenCV
    blurred_image = cv2.GaussianBlur(image, (25, 25), 0)
    
    # Convert the OpenCV images to PIL format
    pil_image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    pil_blurred_image = Image.fromarray(cv2.cvtColor(blurred_image, cv2.COLOR_BGR2RGB))
    
    # Resize the images to fit in the window
    resized_image = pil_image.resize((300, 300))
    resized_blurred_image = pil_blurred_image.resize((300, 300))
    
    # Update the images on the Tkinter labels
    original_img_label.image = ImageTk.PhotoImage(resized_image)
    original_img_label.configure(image=original_img_label.image)
    
    blurred_img_label.image = ImageTk.PhotoImage(resized_blurred_image)
    blurred_img_label.configure(image=blurred_img_label.image)

# Create the Tkinter application window
window = tk.Tk()
window.title("Image Blur")

# Create a button to select and blur the image
button = tk.Button(window, text="Blur Image", command=blur_image)
button.pack(pady=10)

# Create labels to display the original image and the blurred image
original_img_label = tk.Label(window)
original_img_label.pack(side=tk.LEFT, padx=10)

blurred_img_label = tk.Label(window)
blurred_img_label.pack(side=tk.RIGHT, padx=10)

# Start the Tkinter event loop
window.mainloop()
