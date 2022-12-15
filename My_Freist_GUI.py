import tkinter as tk

win = tk.Tk()
photo = tk.PhotoImage(file="Frest_GUI.png")
win.iconphoto(False, photo)
win.config(bg="#00FFF7")
win.title("My frest project")
win.geometry("500x500+200+200")
win.minsize(200, 400)
win.maxsize(700, 800)
win.resizable(True, True)

win.mainloop()
