def say_hello():
    print('hello')


def add_labell():
    label = tk.Label(win, text="new")
    label.pack()

def counter():
    global count
    count+=1
    btn4['text']=text=f' Счетчик: {count}'

count= 0

import tkinter as tk

win = tk.Tk()
wh = 500
hw = 500

win.geometry(f'{wh}x{hw}+200+200')
win.title('My second project')

btn1 = tk.Button(win, text='hello',
                 command=say_hello,
                 )

btn2 = tk.Button(win, text='add new label',
                 command=add_labell,
                 )

btn3 = tk.Button(win, text='add new label lambda',
                 command=lambda: tk.Label(win, text="new lambda").pack()
                 )

btn4 = tk.Button(win, text=f' Счетчик: {count}',
                 command=counter,
                 bg='red',
                 activebackground='blue',
                 state=tk.NORMAL
                 )


btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()
win.mainloop()



