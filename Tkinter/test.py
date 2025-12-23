import tkinter as tk
from tkinter import messagebox

def show_name():
    name = entry.get()
    messagebox.showinfo("Xin chào", f"Chào bạn {name}")

root = tk.Tk()
root.title("Demo Tkinter")

tk.Label(root, text="Nhập tên:").pack()
entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="OK", command=show_name).pack()

root.mainloop()