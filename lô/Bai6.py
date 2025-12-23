import tkinter as tk
from tkinter import messagebox
def calculate_grade():
    try:
        p_score = scale_python.get()
        d_score = scale_db.get()
        w_score = scale_web.get()
        average = (p_score + d_score + w_score) / 3
        if average >= 8.0:
            rank = "Giỏi"
            color = "#2ecc71"
        elif average >= 6.5:
            rank = "Khá"
            color = "#3498db"
        elif average >= 5.0:
            rank = "Đạt"
            color = "#f39c12"
        else:
            rank = "Trượt"
            color = "#e74c3c"
        lbl_tb_val.config(text=f"{average:.2f}", fg=color)
        lbl_rank_val.config(text=rank, fg=color)
    except Exception as e:
        messagebox.showerror("Lỗi hệ thống", f"Đã xảy ra lỗi: {e}")
root = tk.Tk()
root.title("Máy tính điểm chuẩn")
root.geometry("450x400")
root.configure(padx=20, pady=20)

def create_score_scale(label_text, row_idx):
    tk.Label(root, text=label_text, font=("Arial", 10, "bold")).grid(row=row_idx, column=0, sticky="w", pady=5)
    s = tk.Scale(root, from_=0, to=10, resolution=0.1, orient="horizontal", length=250, 
                tickinterval=2, bg="#f0f0f0")
    s.grid(row=row_idx, column=1, padx=10)
    return s
scale_python = create_score_scale("Python:", 0)
scale_db     = create_score_scale("Database:", 1)
scale_web    = create_score_scale("Web Design:", 2)
btn_calc = tk.Button(root, text="TÍNH KẾT QUẢ", font=("Arial", 11, "bold"),
                    bg="#2c3e50", fg="white", command=calculate_grade, height=2)
btn_calc.grid(row=3, column=0, columnspan=2, sticky="we", pady=25)
tk.Label(root, text="Điểm Trung Bình:", font=("Arial", 11)).grid(row=4, column=0, sticky="e")
lbl_tb_val = tk.Label(root, text="0.0", font=("Arial", 11, "bold"))
lbl_tb_val.grid(row=4, column=1, sticky="w", padx=10)
tk.Label(root, text="Xếp Loại:", font=("Arial", 11)).grid(row=5, column=0, sticky="e")
lbl_rank_val = tk.Label(root, text="---", font=("Arial", 11, "bold"))
lbl_rank_val.grid(row=5, column=1, sticky="w", padx=10)
root.mainloop()