from tkinter import *

# Create the main window
window = Tk()
window.title("My First GUI Program")

# Set padding for the window
window.config(padx=10, pady=10)

# Create and place labels
miles_label = Label(text="Miles", font=("Arial", 16,))
miles_label.grid(column=4, row=0)

my_km_label = Label(text="KM", font=("Arial", 16,))
my_km_label.grid(column=4, row=1)

equal_to_label = Label(text="is equal to", font=("Arial", 16,))
equal_to_label.grid(column=2, row=1)

km_label = Label(text="", font=("Arial", 16,))
km_label.grid(column=3, row=1)

def button_clicked():
    """
    Function to convert miles to kilometers and update the km_label text.
    """
    miles = float(input.get())
    km = round(miles * 1.609,2)
    km_label.config(text=km)

# Create and place the conversion button
button = Button(text="Convert", command=button_clicked)
button.grid(column=3, row=2)

# Create and place the input entry field
input = Entry(width=10)
input.grid(column=3, row=0)

# Start the main event loop
window.mainloop()
