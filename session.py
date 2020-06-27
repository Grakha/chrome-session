#!/usr/bin/env python3
import tkinter as tk

# Main window
window = tk.Tk()

# Title of Frame
window.title('Files Save')

# Size of window
window.geometry("370x240")

# Body
title = tk.Label(window, text="Google Save Session")
title.pack()

# Tkinter event loop
window.mainloop()