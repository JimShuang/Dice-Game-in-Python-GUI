import tkinter as tk
from tkinter import messagebox
import os
import random as rd

window = tk.Tk()
window.title('Dice Game')
window.geometry('1800x800')

balance = 1000
b, s, o, e, w = 0, 0, 0, 0, 0

image_path = r'C:\Users\jiajunshuang\PycharmProjects\diesgame\dice_image'

canvas = tk.Canvas(window, bg='green', height=300, width=800)
canvas.pack()

def roll():
    global balance, b, s, o, e, w
    if all([b == 0, s == 0, o == 0, e == 0]):
        messagebox.showwarning("Warning", "Please make a bet.")
        return

    num1, num2, num3 = rd.randint(1, 6), rd.randint(1, 6), rd.randint(1, 6)
    dice1_name = str(num1) + '.png'
    dice2_name = str(num2) + '.png'
    dice3_name = str(num3) + '.png'
    dice1_image_path = os.path.join(image_path, dice1_name)
    dice2_image_path = os.path.join(image_path, dice2_name)
    dice3_image_path = os.path.join(image_path, dice3_name)
    dice1_image = tk.PhotoImage(file=dice1_image_path)
    dice2_image = tk.PhotoImage(file=dice2_image_path)
    dice3_image = tk.PhotoImage(file=dice3_image_path)
    canvas.image = dice1_image, dice2_image, dice3_image
    dice1 = canvas.create_image(150, 50, anchor='n', image=dice1_image)
    dice2 = canvas.create_image(400, 50, anchor='n', image=dice2_image)
    dice3 = canvas.create_image(650, 50, anchor='n', image=dice3_image)

    total = sum([num1, num2, num3])
    if total > 9:
        w += 2 * b
        big_small = 'big'
    else:
        w += 2 * s
        big_small = 'small'
    if total % 2 == 0:
        w += 2 * e
        odd_even = 'even'
    else:
        w += 2 * o
        odd_even = 'odd'

    balance += w
    b, s, o, e = 0, 0, 0, 0

    info = 'It is ' + str(total) + ', ' + big_small + ' and ' + odd_even + '.' + ' You win ' + str(w) + '!'
    messagebox.showinfo("Results", info)
    w = 0
    bal.set(str(balance))
    bigbet.set(str(b))
    smallbet.set(str(s))
    oddbet.set(str(o))
    evenbet.set(str(e))

def rebet():
    global balance, b, s, o, e
    total = sum([b, s, o, e])
    balance += total
    b, s, o, e = 0, 0, 0, 0
    bal.set(str(balance))
    bigbet.set(str(b))
    smallbet.set(str(s))
    oddbet.set(str(o))
    evenbet.set(str(e))

middle_frm = tk.Frame(window)
middle_frm.pack(side='top', pady=30)
tk.Button(middle_frm, text='Roll dice', command=roll).pack(side='left', padx=50)
tk.Button(middle_frm, text='Rebet', command=rebet).pack(side='left', padx=50)

bottom_frm = tk.Frame(window)
bottom_frm.pack(side='top', pady=30)
bet_frm = tk.Frame(bottom_frm)
bet_frm.pack()
betamount_frm = tk.Frame(window)
betamount_frm.pack()
bigamount_frm = tk.Frame(betamount_frm)
bigamount_frm.pack(side='left', padx=180)
smallamount_frm = tk.Frame(betamount_frm)
smallamount_frm.pack(side='left', padx=180)
oddamount_frm = tk.Frame(betamount_frm)
oddamount_frm.pack(side='left', padx=180)
evenamount_frm = tk.Frame(betamount_frm)
evenamount_frm.pack(side='left', padx=180)

balance_frm = tk.Frame(window)
balance_frm.pack(side='top', pady=100)
bal_frm = tk.Frame(balance_frm)
bal_frm.pack()

tk.Label(bal_frm, text='Balance', bg='pink').pack()
bal = tk.StringVar()
bal.set(str(balance))
tk.Label(bal_frm, textvariable=bal).pack()

tk.Label(bigamount_frm, text='Big Bet').pack()
bigbet = tk.StringVar()
bigbet.set(str(b))
tk.Label(bigamount_frm, textvariable=bigbet).pack()

tk.Label(smallamount_frm, text='Small Bet').pack()
smallbet = tk.StringVar()
smallbet.set(str(s))
tk.Label(smallamount_frm, textvariable=smallbet).pack()

tk.Label(oddamount_frm, text='Odd Bet').pack()
oddbet = tk.StringVar()
oddbet.set(str(o))
tk.Label(oddamount_frm, textvariable=oddbet).pack()

tk.Label(evenamount_frm, text='Even Bet').pack()
evenbet = tk.StringVar()
evenbet.set(str(e))
tk.Label(evenamount_frm, textvariable=evenbet).pack()

def make_bet(v, t):
    global balance, b, s, o, e
    balance -= v
    if t == 'b':
        b += v
    elif t == 's':
        s += v
    elif t == 'o':
        o += v
    elif t == 'e':
        e += v
    bal.set(str(balance))
    bigbet.set(str(b))
    smallbet.set(str(s))
    oddbet.set(str(o))
    evenbet.set(str(e))


bigbet_frm = tk.Frame(bet_frm, bg='blue')
bigbet_frm.pack(side='left', padx=150)
tk.Button(bigbet_frm, text='1', command=lambda *args: make_bet(1, 'b')).pack(side='left', padx=10)
tk.Button(bigbet_frm, text='5', command=lambda *args: make_bet(5, 'b')).pack(side='left', padx=10)
tk.Button(bigbet_frm, text='10', command=lambda *args: make_bet(10, 'b')).pack(side='left', padx=10)

smallbet_frm = tk.Frame(bet_frm, bg='orange')
smallbet_frm.pack(side='left', padx=150)
tk.Button(smallbet_frm, text='1', command=lambda *args: make_bet(1, 's')).pack(side='left', padx=10)
tk.Button(smallbet_frm, text='5', command=lambda *args: make_bet(5, 's')).pack(side='left', padx=10)
tk.Button(smallbet_frm, text='10', command=lambda *args: make_bet(10, 's')).pack(side='left', padx=10)

oddbet_frm = tk.Frame(bet_frm, bg='yellow')
oddbet_frm.pack(side='left', padx=150)
tk.Button(oddbet_frm, text='1', command=lambda *args: make_bet(1, 'o')).pack(side='left', padx=10)
tk.Button(oddbet_frm, text='5', command=lambda *args: make_bet(5, 'o')).pack(side='left', padx=10)
tk.Button(oddbet_frm, text='10', command=lambda *args: make_bet(10, 'o')).pack(side='left', padx=10)

evenbet_frm = tk.Frame(bet_frm, bg='purple')
evenbet_frm.pack(side='left', padx=150)
tk.Button(evenbet_frm, text='1', command=lambda *args: make_bet(1, 'e')).pack(side='left', padx=10)
tk.Button(evenbet_frm, text='5', command=lambda *args: make_bet(5, 'e')).pack(side='left', padx=10)
tk.Button(evenbet_frm, text='10', command=lambda *args: make_bet(10, 'e')).pack(side='left', padx=10)

window.mainloop()
