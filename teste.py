
import tkinter as tk


root = tk.Tk()  # Create the main window (root)
root.title("Hello, Tkinter!")  # Set the window title
root.geometry("300x200")  # Set window size (width x height)

label = tk.Label(root, text="Welcome to Tkinter!")  # Create a label widget
label.pack()  # Add the label to the window

root.mainloop()  # Start the main event loop


def on_button_click():
    label.config(text="Button Clicked!")

button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack()
