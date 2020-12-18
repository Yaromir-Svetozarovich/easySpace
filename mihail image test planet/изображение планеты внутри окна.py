from  tkinter import *
from tkinter import messagebox

def on_closing():
    if messagebox.askokcancel("Выход из приложения", "Хотите выйти из приложения?"):
        tk.destroy()

tk = Tk()
tk.protocol("WM_DELETE_WINDOW", on_closing)
tk.title("Приложение")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=900, height=600, bd=0, highlightthickness=0)
canvas.pack()

our_image = PhotoImage(file = "Planet.png")
our_image = our_image.subsample(1, 1)
our_label = Label(tk)
our_label.image = our_image
our_label['image'] = our_label.image
our_label.place(x = 20, y = 20)

tk.mainloop()