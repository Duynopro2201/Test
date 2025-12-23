import tkinter as tk
import random

root = tk.Tk()
root.title("Tung xúc sắc")

# Load ảnh
dice_imgs = []
for i in range(1, 7):
    img = tk.PhotoImage(file=f"{i}.png")
    dice_imgs.append(img)

# Label hiển thị xúc sắc
dice_label = tk.Label(root, image=dice_imgs[0])
dice_label.pack(pady=20)

def roll(count=10):
    if count > 0:
        img = random.choice(dice_imgs)
        dice_label.config(image=img)
        dice_label.image = img
        root.after(100, roll, count - 1)
    else:
        result = random.randint(1, 6)
        dice_label.config(image=dice_imgs[result - 1])
        dice_label.image = dice_imgs[result - 1]
        print("Kết quả:", result)

# Nút tung
btn = tk.Button(root, text="Tung xúc sắc", command=roll)
btn.pack()

root.mainloop()
