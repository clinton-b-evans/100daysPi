import tkinter as tk

# Create a new tkinter window
window = tk.Tk()

# Create a label widget
label = tk.Label(window, text="Enter your name:")
label.pack()

# Create an entry widget for user input
entry = tk.Entry(window)
entry.pack()

# Define a function to handle button click event
def handle_click():
    # Get the user input from the entry widget
    name = entry.get()
    
    # Update the label with the user's name
    label.config(text="Hello, " + name + "!")
    
# Create a button widget
button = tk.Button(window, text="Submit", command=handle_click)
button.pack()

# Start the tkinter event loop
window.mainloop()
