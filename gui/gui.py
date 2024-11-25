import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Simple GUI")

# Create a label widget
label = tk.Label(root, text="Hello, World!")
label.pack(pady=20)

# Function to update the label's text
def update_label():
    label.config(text="Button Clicked!")

# Create a button widget
button = tk.Button(root, text="Click Me", command=update_label)
button.pack(pady=10)

# Start the main event loop
root.mainloop()
