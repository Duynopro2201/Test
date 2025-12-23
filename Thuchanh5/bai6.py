import tkinter as tk
from tkinter import messagebox

def tinh():
    try:
        scores = [float(e.get()) for e in entries]
        if any(s < 0 or s > 10 for s in scores):
            raise ValueError

        avg = round(sum(scores) / 3, 2)

        rank = (
            "Giỏi" if avg >= 8 else
            "Khá"  if avg >= 6.5 else
            "Đạt"  if avg >= 5 else
            "Trượt"
        )

        result.set(f"Điểm TB: {avg} | Xếp loại: {rank}")

    except ValueError:
        messagebox.showerror("Lỗi", "Điểm phải là số trong [0, 10]")

# ===== GUI =====
root = tk.Tk()
root.title("Tính điểm")

entries = []
for i, mon in enumerate(("Python", "DB", "Web")):
    tk.Label(root, text=mon).grid(row=i, column=0)
    e = tk.Entry(root, width=10)
    e.grid(row=i, column=1)
    entries.append(e)

tk.Button(root, text="Tính", command=tinh).grid(
    row=3, column=0, columnspan=2, pady=5
)

result = tk.StringVar()
tk.Label(root, textvariable=result).grid(
    row=4, column=0, columnspan=2
)

root.mainloop()
