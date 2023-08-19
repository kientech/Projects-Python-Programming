# Coding With Kien

import datetime
import tkinter as tk

# Create a tkinter window
root = tk.Tk()
root.title("Clock")

# Create a label to display the time
time_label = tk.Label(root, font=("Arial", 80), bg="white")
time_label.pack(padx=100, pady=50)

# Function to update the time
def update_time():
    dt = datetime.datetime.now()
    time_label.config(text=dt.strftime("%H:%M:%S"))
    root.after(1000, update_time)

# Call the update_time function to start updating the time
update_time()

# Run the tkinter event loop
root.mainloop()
