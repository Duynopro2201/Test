import tkinter as tk
from tkinter import messagebox, filedialog

root = tk.Tk()
root.title("Todo đơn giản")

# ===== Entry =====
entry = tk.Entry(root, width=40)
entry.pack(pady=5)

# ===== Listbox =====
listbox = tk.Listbox(root, width=50)
listbox.pack(pady=5)

# ===== Functions =====
def add_task():
    text = entry.get().strip()
    if text:
        listbox.insert(tk.END, text)
        entry.delete(0, tk.END)

def delete_task():
    if not listbox.curselection():
        return
    if messagebox.askyesno("Xác nhận", "Xóa công việc này?"):
        listbox.delete(listbox.curselection())

def mark_done():
    if not listbox.curselection():
        return
    index = listbox.curselection()[0]
    text = listbox.get(index)
    if not text.startswith("✓ "):
        listbox.delete(index)
        listbox.insert(index, "✓ " + text)

def save_tasks():
    file = filedialog.asksaveasfilename(defaultextension=".txt")
    if file:
        with open(file, "w", encoding="utf-8") as f:
            for i in range(listbox.size()):
                f.write(listbox.get(i) + "\n")

def load_tasks():
    file = filedialog.askopenfilename(filetypes=[("Text file", "*.txt")])
    if file:
        listbox.delete(0, tk.END)
        with open(file, "r", encoding="utf-8") as f:
            for line in f:
                listbox.insert(tk.END, line.strip())

# ===== Buttons =====
frame = tk.Frame(root)
frame.pack(pady=5)

tk.Button(frame, text="Thêm", command=add_task).grid(row=0, column=0, padx=5)
tk.Button(frame, text="Xóa mục chọn", command=delete_task).grid(row=0, column=1, padx=5)
tk.Button(frame, text="Hoàn thành", command=mark_done).grid(row=0, column=2, padx=5)

tk.Button(root, text="Lưu", command=save_tasks).pack(side=tk.LEFT, padx=20)
tk.Button(root, text="Tải", command=load_tasks).pack(side=tk.RIGHT, padx=20)

root.mainloop()
