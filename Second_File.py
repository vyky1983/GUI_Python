import tkinter as tk

win = tk.Tk()
wh = 500
he = 600

win.title("second project")
win.geometry(f"{wh}x{he}+200+200")

lable1 = tk.Label(win, text='''Hello!''',
                  bg="#CC99CC",
                  fg="white",
                  font=("Arial", 20, "bold"),
                  # padx=20,
                  # pady=10,
                  width=10,
                  height=10,
                  anchor="nw",
                  relief=tk.RAISED,
                  bd=10,
                  justify=tk.LEFT
                  )
lable1.pack()

win.mainloop()
