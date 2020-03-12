import tkinter as tk

root = tk.Tk()
root.withdraw()
data = root.clipboard_get()

print(data)
