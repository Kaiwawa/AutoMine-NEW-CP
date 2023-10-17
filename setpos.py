import tkinter as tk
import pyautogui

# Function to set pointer_pos
def set_pointer_pos():
    capture_button.config(text="Click to Capture Mouse Position")
    root.bind("<Button-1>", capture_next_click)

def capture_next_click(event):
    global pointer_pos
    pointer_pos = (event.x_root, event.y_root)
    pos_label.config(text=f"Pointer Position: {pointer_pos}")
    capture_button.config(text="Capture Next Mouse Click")
    root.unbind("<Button-1>")

# Create a tkinter window
root = tk.Tk()
root.title("Capture Mouse Position")

# Create a button to initiate capturing the next click
capture_button = tk.Button(root, text="Click to Capture Mouse Position", command=set_pointer_pos)
capture_button.pack()

# Create a label to display pointer_pos
pos_label = tk.Label(root, text="Pointer Position: ")
pos_label.pack()

# Initialize pointer_pos
pointer_pos = None

# Start the tkinter main loop
root.mainloop()
