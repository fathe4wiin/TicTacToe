import tkinter as tk
from tkinter import *

root = tk.Tk()
root.geometry("600x600")
root.title("TicTacToe")
root.configure(bg='#000000')
root.resizable(False, False)

O= tk.PhotoImage(file="Data/O.png")
X= tk.PhotoImage(file="Data/X.png")
bg=tk.PhotoImage(file="Data/sq.png")


def winner():
    for btn in [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9]:
        btn.config(state="disabled")


turn=2
def turnadd():
    global turn
    turn+=1


def action(turn, btn):
    turnadd()

    if (turn % 2) == 0 :
        btn.config(image=X)
        btn.config(state=DISABLED)
        post.config(text="O's turn")


    if (turn % 2) == 1:
        btn.config(image=O)
        btn.config(state=DISABLED)
        post.config(text="X's turn")

    chk(turn)


def chk(turn):
    if btn1.cget('image') == str(X) and btn2.cget('image') == str(X) and btn3.cget('image') == str(X):
        post.config(text="X wins")
        winner()
    elif btn4.cget('image') == str(X) and btn5.cget('image') == str(X) and btn6.cget('image') == str(X):
        post.config(text="X wins")
        winner()
    elif btn7.cget('image') == str(X) and btn8.cget('image') == str(X) and btn9.cget('image') == str(X):
        post.config(text="X wins")
        winner()
    elif btn1.cget('image') == str(X) and btn4.cget('image') == str(X) and btn7.cget('image') == str(X):
        post.config(text="X wins")
        winner()
    elif btn2.cget('image') == str(X) and btn5.cget('image') == str(X) and btn8.cget('image') == str(X):
        post.config(text="X wins")
        winner()
    elif btn3.cget('image') == str(X) and btn6.cget('image') == str(X) and btn9.cget('image') == str(X):
        post.config(text="X wins")
        winner()
    elif btn1.cget('image') == str(X) and btn5.cget('image') == str(X) and btn9.cget('image') == str(X):
        post.config(text="X wins")
        winner()
    elif btn3.cget('image') == str(X) and btn5.cget('image') == str(X) and btn7.cget('image') == str(X):
        post.config(text="X wins")
        winner()


    elif btn1.cget('image') == str(O) and btn2.cget('image') == str(O) and btn3.cget('image') == str(O):
        post.config(text="O wins")
        winner()
    elif btn4.cget('image') == str(O) and btn5.cget('image') == str(O) and btn6.cget('image') == str(O):
        post.config(text="O wins")
        winner()
    elif btn7.cget('image') == str(O) and btn8.cget('image') == str(O) and btn9.cget('image') == str(O):
        post.config(text="O wins")
        winner()
    elif btn1.cget('image') == str(O) and btn4.cget('image') == str(O) and btn7.cget('image') == str(O):
        post.config(text="O wins")
        winner()
    elif btn2.cget('image') == str(O) and btn5.cget('image') == str(O) and btn8.cget('image') == str(O):
        post.config(text="O wins")
        winner()
    elif btn3.cget('image') == str(O) and btn6.cget('image') == str(O) and btn9.cget('image') == str(O):
        post.config(text="O wins")
        winner()
    elif btn1.cget('image') == str(O) and btn5.cget('image') == str(O) and btn9.cget('image') == str(O):
        post.config(text="O wins")
        winner()
    elif btn3.cget('image') == str(O) and btn5.cget('image') == str(O) and btn7.cget('image') == str(O):
        post.config(text="O wins")
        winner()


    elif turn == 10:
        post.config(text="Its a draw")
        turn = 2




def reset():
    btn1.config(image=bg)
    btn2.config(image=bg)
    btn3.config(image=bg)
    btn4.config(image=bg)
    btn5.config(image=bg)
    btn6.config(image=bg)
    btn7.config(image=bg)
    btn8.config(image=bg)
    btn9.config(image=bg)

    btn1.config(state=NORMAL)
    btn2.config(state=NORMAL)
    btn3.config(state=NORMAL)
    btn4.config(state=NORMAL)
    btn5.config(state=NORMAL)
    btn6.config(state=NORMAL)
    btn7.config(state=NORMAL)
    btn8.config(state=NORMAL)
    btn9.config(state=NORMAL)

    post.config(text="It's X's turn")














root.columnconfigure(0, weight=7)
root.columnconfigure(1, weight=3)

root.rowconfigure(0, weight=3)
root.rowconfigure(1, weight=7)


post=tk.Label(root, text="It's X's turn", font=("Arial", ), bg="#000000", fg="#FFFFFF")
post.grid(row=0, column=0)

game=tk.Frame(root, bg="#FFFFFF")
game.grid(row=1, column=0, sticky="nsew")



game.columnconfigure(0, weight=1)
game.columnconfigure(1, weight=1)
game.columnconfigure(2, weight=1)

game.rowconfigure(0, weight=1)
game.rowconfigure(1, weight=1)
game.rowconfigure(2, weight=1)


btn1=tk.Button(game, text=" ", font=("Arial", 15),image=bg, bg="#FFFFFF", fg="#000000", height=4, width=9, command=lambda: action(turn, btn1))
btn1.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

btn2=tk.Button(game, text=" ", font=("Arial", 15),image=bg, bg="#FFFFFF", fg="#000000", height=4, width=9, command=lambda: action(turn, btn2))
btn2.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

btn3=tk.Button(game, text=" ", font=("Arial", 15),image=bg, bg="#FFFFFF", fg="#000000", height=4, width=9, command=lambda: action(turn, btn3))
btn3.grid(row=0, column=2, sticky="nsew", padx=5, pady=5)

btn4=tk.Button(game, text=" ", font=("Arial", 15),image=bg, bg="#FFFFFF", fg="#000000", height=4, width=9, command=lambda: action(turn, btn4))
btn4.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

btn5=tk.Button(game, text=" ", font=("Arial", 15),image=bg, bg="#FFFFFF", fg="#000000", height=4, width=9, command=lambda: action(turn, btn5))
btn5.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)

btn6=tk.Button(game, text=" ", font=("Arial", 15),image=bg, bg="#FFFFFF", fg="#000000", height=4, width=9, command=lambda: action(turn, btn6))
btn6.grid(row=1, column=2, sticky="nsew", padx=5, pady=5)

btn7=tk.Button(game, text=" ", font=("Arial", 15),image=bg, bg="#FFFFFF", fg="#000000", height=4, width=9, command=lambda: action(turn, btn7))
btn7.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)

btn8=tk.Button(game, text=" ", font=("Arial", 15),image=bg, bg="#FFFFFF", fg="#000000", height=4, width=9, command=lambda: action(turn, btn8))
btn8.grid(row=2, column=1, sticky="nsew", padx=5, pady=5)

btn9=tk.Button(game, text=" ", font=("Arial", 15),image=bg, bg="#FFFFFF", fg="#000000", height=4, width=9, command=lambda: action(turn, btn9))
btn9.grid(row=2, column=2, sticky="nsew", padx=5, pady=5)



Clear=tk.Button(root, text="Clear", font=("Arial", 15), bg="#000000", fg="#FFFFFF", command=reset)
Clear.grid(row=1, column=1, sticky="nsew")























root.mainloop()