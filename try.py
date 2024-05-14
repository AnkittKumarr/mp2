import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate
import tkinter as tk
from tkinter import ttk

# Given data
R = 100  # Resistance (ohms)
C = 0.01  # Capacitance (farads)

# Function to calculate the emf at time t
def emf(t):
    return 400 * np.cos(2 * t)

# Function to calculate the charge using Euler's method
def euler_method(h, t_end):
    t_values = [0]
    Q_values = [0]  # Initial charge is 0
    t = 0
    Q = 0
    while t < t_end:
        dQ_dt = emf(t) - Q / (R * C)
        Q_next = Q + h * dQ_dt
        t += h
        t_values.append(t)
        Q_values.append(Q_next)
        Q = Q_next
    return t_values, Q_values

# Step size and endpoint for Euler's method
h = 0.01
t_end = 10  # Adjust as needed

# Perform Euler's method
t_values, Q_values = euler_method(h, t_end)

# Calculate current values
I_values = [(emf(t) - Q / (R * C)) / R for t, Q in zip(t_values, Q_values)]

# Create a new window
root = tk.Tk()
root.title("RC Circuit Analysis")

# Create a frame
frame = ttk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

# Create a table
table = ttk.Treeview(frame, columns=("time", "charge", "current"))
table.heading("#0", text="Index")
table.heading("time", text="Time (s)")
table.heading("charge", text="Charge (C)")
table.heading("current", text="Current (A)")

# Populate the table
for i, (t, Q, I) in enumerate(zip(t_values, Q_values, I_values)):
    table.insert("", "end", text=str(i + 1), values=(f"{t:.2f}", f"{Q:.4f}", f"{I:.4f}"))

# Add table to the frame
table.pack(fill=tk.BOTH, expand=True)

# Add a scrollbar
scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=table.yview)
table.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Run the GUI
root.mainloop()

# Plot the graph
plt.plot(t_values, Q_values, label='Charge', color='b')
plt.plot(t_values, I_values, label='Current', color='r')
plt.xlabel('Time (seconds)')
plt.ylabel('Charge (coulombs) / Current (amperes)')
plt.title('Charge and Current in RC Circuit')
plt.legend()
plt.grid(True)
plt.show()
