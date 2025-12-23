import tkinter as tk

root = tk.Tk()
root.geometry("500x120")

frame = tk.Frame(root, bg="white")
frame.pack(fill="x", padx=10, pady=10)

# Bên trái
tk.Label(frame, text="Bên trái", bg = 'white').pack(side=tk.LEFT)

# Bên phải (Label + Button)

tk.Button(frame, text="+", bg = 'white').pack(side=tk.RIGHT)
tk.Label(frame, text="Bên phải", bg = 'white').pack(side=tk.RIGHT, padx=5)


root.mainloop()
