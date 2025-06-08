import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageEnhance, ImageTk

def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png;*.jpeg")])
    if file_path:
        global img, img_display
        img = Image.open(file_path)
        img_display = img.resize((250, 250))
        img_tk = ImageTk.PhotoImage(img_display)
        panel.config(image=img_tk)
        panel.image = img_tk

def edit_and_save():
    if img:
        img_resized = img.resize((400, 400))
        enhancer = ImageEnhance.Brightness(img_resized)
        img_bright = enhancer.enhance(1.5)
        save_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG", "*.jpg")])
        if save_path:
            img_bright.save(save_path)
            messagebox.showinfo("Success", f"Image saved as {save_path}")

root = tk.Tk()
root.title("Simple Image Editor")

img = None
img_display = None

btn_open = tk.Button(root, text="Open Image", command=open_image)
btn_open.pack()

panel = tk.Label(root)
panel.pack()

btn_save = tk.Button(root, text="Edit & Save", command=edit_and_save)
btn_save.pack()

root.mainloop()