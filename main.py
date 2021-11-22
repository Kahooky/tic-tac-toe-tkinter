from tkinter import *
from tkinter import messagebox


win = Tk()
win['background'] = "#3de5ff"
win.title("tic tac toe")
win.iconbitmap("ttt.ico")
win.geometry("600x400")
win.resizable(height="false", width="false")

title = Label(win, text='TIC-TAC-TOE!!!', bg='#3de5ff')
title.pack()

oa = Frame(win, bg='#3de5ff')
oa.pack()


points = Frame(win, bg='#3de5ff')

turn = " "

p1t = Label(oa, text='p1 (X)', bg='#3de5ff')
p1t.grid(row=0, column=0)

p2t = Label(oa, text='p2 (O)', bg='#3de5ff')
p2t.grid(row=1, column=0)

p1 = Entry(oa)
p1.grid(row=0, column=1)
p1i = "pablo"

p1p = 0

p2 = Entry(oa)
p2.grid(row=1, column=1)
p2i = "name"

p2p = 0

vl1 = Frame(win, width=5, height=290, bg='black')
vl2 = Frame(win, width=5, height=290, bg='black')

hl1 = Frame(win, width=430, height=5, bg='black')
hl2 = Frame(win, width=430, height=5, bg='black')


hz = open('hs.txt', "r")
high = Label(oa, bg='#3de5ff', text="The high score is  "+hz.read())
high.grid(row=5, column=1)


b00 = Label(win, bg='#3de5ff')
b01 = Label(win, bg='#3de5ff')
b02 = Label(win, bg='#3de5ff')
b10 = Label(win, bg='#3de5ff')
b11 = Label(win, bg='#3de5ff')
b12 = Label(win, bg='#3de5ff')
b20 = Label(win, bg='#3de5ff')
b21 = Label(win, bg='#3de5ff')
b22 = Label(win, bg='#3de5ff')


def play():
    global p1i
    global p2i
    global turn
    global pop1
    global pop2
    vl1.place(relx=0.35, rely=0.10)
    vl2.place(relx=0.65, rely=0.10)
    hl1.place(relx=0.15, rely=0.30)
    hl2.place(relx=0.15, rely=0.60)
    b00.place(relx=0.15, rely=0.10, width=116, height=76)
    b01.place(relx=0.37, rely=0.10, width=163, height=76)
    b02.place(relx=0.67, rely=0.10, width=116, height=76)
    b10.place(relx=0.15, rely=0.33, width=116, height=100)
    b11.place(relx=0.37, rely=0.33, width=163, height=100)
    b12.place(relx=0.67, rely=0.33, width=116, height=100)
    b20.place(relx=0.15, rely=0.63, width=116, height=76)
    b21.place(relx=0.37, rely=0.63, width=163, height=76)
    b22.place(relx=0.67, rely=0.63, width=116, height=76)
    points.place(relx=0.10, rely=0.85)
    pop1 = Label(points, bg='#3de5ff', text=p1p)
    pop1.grid(row=0, column=0)
    pop2 = Label(points, bg='#3de5ff', text=p2p)
    pop2.grid(row=1, column=0)
    p1i = p1.get()
    p2i = p2.get()
    p1n = Label(points, bg='#3de5ff', text=p1i)
    p1n.grid(row=0, column=1)
    p2n = Label(points, bg='#3de5ff', text=p2i)
    p2n.grid(row=1, column=1)
    title.destroy()
    oa.destroy()
    turn = p1i


def w():
    if (b00['text'] == 'X' and b01['text'] == 'X' and b02['text'] == 'X') or (
            b10['text'] == 'X' and b11['text'] == 'X' and b12['text'] == 'X') or \
            (b20['text'] == 'X' and b21['text'] == 'X' and b22['text'] == 'X') or (
            b00['text'] == 'X' and b11['text'] == 'X' and b22['text'] == 'X') or \
            (b02['text'] == 'X' and b11['text'] == 'X' and b20['text'] == 'X') or (
            b00['text'] == 'X' and b10['text'] == 'X' and b20['text'] == 'X') or (
            b01['text'] == 'X' and b11['text'] == 'X' and b21['text'] == 'X') or \
            (b02['text'] == 'X' and b12['text'] == 'X' and b22['text'] == 'X') or (
            b10['text'] == 'X' and b11['text'] == 'X' and b12['text'] == 'X'):
        return True

    elif (b00['text'] == 'O' and b01['text'] == 'O' and b02['text'] == 'O') or (
            b10['text'] == 'O' and b11['text'] == 'O' and b12['text'] == 'O') or \
            (b20['text'] == 'O' and b21['text'] == 'O' and b22['text'] == 'O') or (
            b00['text'] == 'O' and b11['text'] == 'O' and b22['text'] == 'O') or \
            (b02['text'] == 'O' and b11['text'] == 'O' and b20['text'] == 'O') or (
            b00['text'] == 'O' and b10['text'] == 'O' and b20['text'] == 'O') or (
            b01['text'] == 'O' and b11['text'] == 'O' and b21['text'] == 'O') or \
            (b02['text'] == 'O' and b12['text'] == 'O' and b22['text'] == 'O') or (
            b10['text'] == 'O' and b11['text'] == 'O' and b12['text'] == 'O'):
        return True

    else:
        return False


def clear():
    b00['text'] = ''
    b01['text'] = ''
    b02['text'] = ''
    b10['text'] = ''
    b11['text'] = ''
    b12['text'] = ''
    b20['text'] = ''
    b21['text'] = ''
    b22['text'] = ''


def check():
    if b00['text'] != '' and b01['text'] != '' and b02['text'] != '' and b10['text'] != '' and b11['text'] != '' and b12['text'] != '' and \
            b20['text'] != '' and b21['text'] != '' and b22['text'] != '':
        return True
    else:
        return False


def a00(event):
    global turn
    global p1p
    global p2p
    global pop1
    global pop2
    if b00['text'] == '':
        if turn == p1i:
            b00.config(text="X", font=("sans", 50), fg="blue")
            turn = p2i
            if w() == True:
                clear()
                messagebox.showinfo(title="the winner is....", message=p1i+"                      ")
                p1p += 1
                pop1.config(text=p1p)
        elif turn == p2i:
            b00.config(text="O", font=("sans", 50), fg="red")
            turn = p1i
            if w() == True:
                clear()
                messagebox.showinfo(title="the winner is....", message=p2i+"                      ")
                p2p += 1
                pop2.config(text=p1p)
    if check():
        clear()
        messagebox.showinfo(title=":( saddly it is a...", message="Draw                          ")


b00.bind("<Button-1>", a00)


def a01(event):
    global turn
    global p1p
    global p2p
    global pop1
    global pop2
    if b01['text'] == '':
        if turn == p1i:
            b01.config(text="X", font=("sans", 50), fg="blue")
            turn = p2i
            if w() == True:
                clear()
                messagebox.showinfo(title="the winner is....", message=p1i+"                      ")
                p1p += 1
                pop1.config(text=p1p)
        elif turn == p2i:
            b01.config(text="O", font=("sans", 50), fg="red")
            turn = p1i
            if w() == True:
                clear()
                messagebox.showinfo(title="the winner is....", message=p2i + "                      ")
                p2p += 1
                pop2.config(text=p2p)
    if check():
        clear()
        messagebox.showinfo(title=":( saddly it is a...", message="Draw                          ")


b01.bind("<Button-1>", a01)


def a02(event):
    global turn
    global p1p
    global p2p
    global pop1
    global pop2
    if b02['text'] == '':
        if turn == p1i:
            b02.config(text="X", font=("sans", 50), fg="blue")
            turn = p2i
            if w() == True:
                clear()
                messagebox.showinfo(title="the winner is....", message=p1i + "                      ")
                p1p += 1
                pop1.config(text=p1p)
        elif turn == p2i:
            b02.config(text="O", font=("sans", 50), fg="red")
            turn = p1i
            if w() == True:
                clear()
                messagebox.showinfo(title="the winner is....", message=p2i + "                      ")
                p2p += 1
                pop2.config(text=p2p)
    if check():
        clear()
        messagebox.showinfo(title=":( saddly it is a...", message="Draw                          ")


b02.bind("<Button-1>", a02)


def a10(event):
    global turn
    global p1p
    global p2p
    global pop1
    global pop2
    if b10['text'] == '':
        if turn == p1i:
            b10.config(text="X", font=("sans", 50), fg="blue")
            turn = p2i
            if w() == True:
                clear()
                messagebox.showinfo(title="the winner is....", message=p1i + "                      ")
                p1p += 1
                pop1.config(text=p1p)
        elif turn == p2i:
            b10.config(text="O", font=("sans", 50), fg="red")
            turn = p1i
            if w() == True:
                clear()
                messagebox.showinfo(title="the winner is....", message=p2i + "                      ")
                p2p += 1
                pop2.config(text=p2p)
    if check():
        clear()
        messagebox.showinfo(title=":( saddly it is a...", message="Draw                          ")


b10.bind("<Button-1>", a10)


def a11(event):
    global turn
    global p1p
    global p2p
    global pop1
    global pop2
    if b11['text'] == '':
        if turn == p1i:
            b11.config(text="X", font=("sans", 50), fg="blue")
            turn = p2i
            if w() == True:
                clear()
                messagebox.showinfo(title="the winner is....", message=p1i + "                      ")
                p1p += 1
                pop1.config(text=p1p)
        elif turn == p2i:
            b11.config(text="O", font=("sans", 50), fg="red")
            turn = p1i
            if w() == True:
                clear()
                messagebox.showinfo(title="the winner is....", message=p2i + "                      ")
                p2p += 1
                pop2.config(text=p2p)
    if check():
        clear()
        messagebox.showinfo(title=":( saddly it is a...", message="Draw                          ")


b11.bind("<Button-1>", a11)


def a12(event):
    global turn
    global p1p
    global p2p
    global pop1
    global pop2
    if b12['text'] == '':
        if turn == p1i:
            b12.config(text="X", font=("sans", 50), fg="blue")
            turn = p2i
            if w() == True:
                clear()
                messagebox.showinfo(title="the winner is....", message=p1i + "                      ")
                p1p += 1
                pop1.config(text=p1p)
        elif turn == p2i:
            b12.config(text="O", font=("sans", 50), fg="red")
            turn = p1i
            if w() == True:
                clear()
                messagebox.showinfo(title="the winner is....", message=p2i + "                      ")
                p2p += 1
                pop2.config(text=p2p)
    if check():
        clear()
        messagebox.showinfo(title=":( saddly it is a...", message="Draw                          ")


b12.bind("<Button-1>", a12)


def a20(event):
    global turn
    global p1p
    global p2p
    global pop1
    global pop2
    if b20['text'] == '':
        if turn == p1i:
            b20.config(text="X", font=("sans", 50), fg="blue")
            turn = p2i
            if w() == True:
                clear()
                messagebox.showinfo(title="the winner is....", message=p1i + "                      ")
                p1p += 1
                pop1.config(text=p1p)
        elif turn == p2i:
            b20.config(text="O", font=("sans", 50), fg="red")
            turn = p1i
            if w() == True:
                clear()
                messagebox.showinfo(title="the winner is....", message=p2i + "                      ")
                p2p += 1
                pop2.config(text=p2p)
    if check():
        clear()
        messagebox.showinfo(title=":( saddly it is a...", message="Draw                          ")


b20.bind("<Button-1>", a20)


def a21(event):
    global turn
    global p1p
    global p2p
    global pop1
    global pop2
    if b21['text'] == '':
        if turn == p1i:
            b21.config(text="X", font=("sans", 50), fg="blue")
            turn = p2i
            if w() == True:
                clear()
                messagebox.showinfo(title="the winner is....", message=p1i + "                      ")
                p1p += 1
                pop1.config(text=p1p)
        elif turn == p2i:
            b21.config(text="O", font=("sans", 50), fg="red")
            turn = p1i
            if w() == True:
                clear()
                messagebox.showinfo(title="the winner is....", message=p2i + "                      ")
                p2p += 1
                pop2.config(text=p2p)
    if check():
        clear()
        messagebox.showinfo(title=":( saddly it is a...", message="Draw                          ")


b21.bind("<Button-1>", a21)


def a22(event):
    global turn
    global p1p
    global p2p
    global pop1
    global pop2
    if b22['text'] == '':
        if turn == p1i:
            b22.config(text="X", font=("sans", 50), fg="blue")
            turn = p2i
            if w() == True:
                clear()
                messagebox.showinfo(title="the winner is....", message=p1i + "                      ")
                p1p += 1
                pop1.config(text=p1p)
        elif turn == p2i:
            b22.config(text="O", font=("sans", 50), fg="red")
            turn = p1i
            if w() == True:
                clear()
                messagebox.showinfo(title="the winner is....", message=p2i + "                      ")
                p2p += 1
                pop2.config(text=p2p)
    if check():
        clear()
        messagebox.showinfo(title=":( saddly it is a...", message="Draw                          ")


b22.bind("<Button-1>", a22)

play = Button(oa, text='play', command=play)
play.grid(row=3, column=1)


def hs():
    global p1p
    global p2p
    hz = open('hs.txt', "r")
    x = p1p
    o = p2p
    po = hz.read()
    r = open('hs.txt', "w")
    print(po,len(po))
    if (x > int(po)) or (o > int(po)):
        if x > o:
            r.write(str(x))
        else:
            r.write(str(o))
    win.destroy()


win.protocol("WM_DELETE_WINDOW", hs)


win.mainloop()
