import tkinter as tk
import random
from tkinter import messagebox

# --- Hàm xử lý ---
def nap_tien():
    global taikhoan
    try:
        so_tien = int(entry_nap.get())
        if so_tien <= 0:
            messagebox.showwarning("Lỗi", "Số tiền phải lớn hơn 0!")
        else:
            taikhoan += so_tien
            label_sodu.config(text=f"Số dư: {taikhoan}")
            entry_nap.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ!")

def choi():
    global taikhoan
    try:
        cuoc = int(entry_cuoc.get())
        if cuoc > taikhoan:
            messagebox.showwarning("Thiếu tiền", "Số dư không đủ!")
            return
        if cuoc <= 0:
            messagebox.showwarning("Lỗi", "Tiền cược phải > 0!")
            return
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ!")
        return

    chon = var_chon.get()
    A, B, C = random.randint(1,6), random.randint(1,6), random.randint(1,6)
    tong = A + B + C

    label_kq_xucxac.config(text=f"🎲 {A} - {B} - {C} (Tổng = {tong})")

    # Xác định thắng thua
    if 3 <= tong <= 10:
        kq = "xỉu"
    else:
        kq = "tài"

    if chon == kq:
        taikhoan += cuoc
        messagebox.showinfo("Kết quả", f"Bạn chọn {chon.upper()} và đã THẮNG! +{cuoc}đ")
    else:
        taikhoan -= cuoc
        messagebox.showinfo("Kết quả", f"Bạn chọn {chon.upper()} và đã THUA! -{cuoc}đ")

    label_sodu.config(text=f"Số dư: {taikhoan}")

    if taikhoan <= 0:
        messagebox.showinfo("Hết tiền", "Bạn đã hết tiền! Hãy nạp thêm để chơi tiếp!")

# --- Giao diện chính ---
root = tk.Tk()
root.title("🎲 Game Tài Xỉu")
root.geometry("350x380")
root.resizable(False, False)

taikhoan = 0

# --- Khung nạp tiền ---
frame_nap = tk.LabelFrame(root, text="💰 Nạp tiền", padx=10, pady=10)
frame_nap.pack(padx=10, pady=10, fill="x")

tk.Label(frame_nap, text="Số tiền:").pack(side="left")
entry_nap = tk.Entry(frame_nap, width=10)
entry_nap.pack(side="left", padx=5)
tk.Button(frame_nap, text="Nạp", command=nap_tien).pack(side="left")

label_sodu = tk.Label(frame_nap, text=f"Số dư: {taikhoan}")
label_sodu.pack(side="right")

# --- Khung chơi ---
frame_game = tk.LabelFrame(root, text="🎮 Chơi tài xỉu", padx=10, pady=10)
frame_game.pack(padx=10, pady=10, fill="x")

var_chon = tk.StringVar(value="tài")
tk.Radiobutton(frame_game, text="Tài (11-18)", variable=var_chon, value="tài").pack(anchor="w")
tk.Radiobutton(frame_game, text="Xỉu (3-10)", variable=var_chon, value="xỉu").pack(anchor="w")

tk.Label(frame_game, text="Tiền cược:").pack()
entry_cuoc = tk.Entry(frame_game, width=10)
entry_cuoc.pack()

tk.Button(frame_game, text="🎲 Quay xúc xắc", command=choi, bg="lightgreen").pack(pady=10)

label_kq_xucxac = tk.Label(frame_game, text="🎲 Chưa quay")
label_kq_xucxac.pack()

# --- Chạy chương trình ---
root.mainloop()
