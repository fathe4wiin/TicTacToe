import tkinter as tk
from tkinter import *

root = tk.Tk()
root.geometry("600x600")
root.title("TicTacToe")
root.configure(bg='#000000')
root.resizable(False, False)
root.iconbitmap("Data/logo.ico")



O= tk.PhotoImage(file="Data/oo.png")
X= tk.PhotoImage(file="Data/Xx.png")
bg=tk.PhotoImage(file="Data/sqq.png")
lie=tk.PhotoImage(file="Data/poster.png")


row1=tk.PhotoImage(file="Data/win/row1.png")
row2=tk.PhotoImage(file="Data/win/row2.png")
row3=tk.PhotoImage(file="Data/win/row3.png")
col1=tk.PhotoImage(file="Data/win/col1.png")
col2=tk.PhotoImage(file="Data/win/col2.png")
col3=tk.PhotoImage(file="Data/win/col3.png")
diag1=tk.PhotoImage(file="Data/win/diag1.png")
diag2=tk.PhotoImage(file="Data/win/diag2.png")




back=tk.Canvas(root, width=52, height=12, bg='#000000')
#back.create_image(0, 0, image=lie, anchor=NW)
#back.place(x=300, y=300)





label = tk.Label(root, text="", bg="red", width=10, height=5, relief="raised")

def draw_winning_lines(winning_pattern):

    if winning_pattern == "row1":
        label = tk.Label(root, text="",relief="raised", image=row1)
        label.place(in_=btn5, relx=0.5, rely=0.5, anchor=CENTER)

    elif winning_pattern == "row2":
        label = tk.Label(root, text="", bg="red", width=70, height=1, relief="raised")
        label.place(in_=btn5, relx=0.5, rely=0.5, anchor=CENTER)

    elif winning_pattern == "row3":
        label = tk.Label(root, text="", bg="red", width=70, height=1, relief="raised")
        label.place(in_=btn8, relx=0.5, rely=0.5, anchor=CENTER)

    elif winning_pattern == "col1":
        label = tk.Label(root, text="", bg="red", width=70, height=1, relief="raised", angle=90)
        label.place(in_=btn1, relx=0.5, rely=0.5, anchor=CENTER)


    elif winning_pattern == "col2":
        label = tk.Label(root, text="", bg="red", width=70, height=1, relief="raised", angle=90)
        label.place(in_=btn5, relx=0.5, rely=0.5, anchor=CENTER)


    elif winning_pattern == "col3":
        label = tk.Label(root, text="", bg="red", width=70, height=1, relief="raised", angle=90)
        label.place(in_=btn9, relx=0.5, rely=0.5, anchor=CENTER)


    elif winning_pattern == "diag1":
        label = tk.Label(root, text="", bg="red", width=70, height=1, relief="raised")
        label.place(in_=btn5, relx=0.5, rely=0.5, anchor=CENTER)
        label.config(angle=45)

    elif winning_pattern == "diag2":
        label = tk.Label(root, text="", bg="red", width=70, height=1, relief="raised")
        label.place(in_=btn5, relx=0.5, rely=0.5, anchor=CENTER)
        label.config(angle=45)














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
        print(turn)


    if (turn % 2) == 1:
        btn.config(image=O)
        btn.config(state=DISABLED)
        post.config(text="X's turn")
        print(turn)

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
    for btn in [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9]:
        btn.config(image=bg)


    #btn1.config(image=bg)
    #btn2.config(image=bg)
    #btn3.config(image=bg)
    #btn4.config(image=bg)
    #btn5.config(image=bg)
    #btn6.config(image=bg)
    #btn7.config(image=bg)
    #btn8.config(image=bg)
    #btn9.config(image=bg)

    for btn in [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9]:
        btn.config(state=NORMAL)

    #btn1.config(state=NORMAL)
    #btn2.config(state=NORMAL)
    #btn3.config(state=NORMAL)
    #btn4.config(state=NORMAL)
    #btn5.config(state=NORMAL)
    #btn6.config(state=NORMAL)
    #btn7.config(state=NORMAL)
    #btn8.config(state=NORMAL)
    #btn9.config(state=NORMAL)

    global turn


    turn=2

    post.config(text="It's X's turn")











canvas=tk.Frame(root, highlightthickness=0)
canvas.grid(row=1, column=0, sticky="nsew")





root.columnconfigure(0, weight=7)


root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=7)

top=tk.Canvas(root, bg="green", highlightthickness=0,)
top.create_image(0, 0, image=lie, anchor="nw")
top.place( relx=0, rely=0, x=0, y=0, height=700, width=700)




post=tk.Label(root, text="It's X's turn", font=("Arial", 35), bg="#ffe177", fg="#000000", width=16, height=1)
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
btn1.lower()


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



Clear=tk.Button(root, text="Reset", font=("Arial", 15), bg="#ffd15b", command=reset)
Clear.grid(row=0, column=0, padx=5, pady=5, sticky="e")



#can.lift()
#can.place(in_=btn2, relx=0.5, rely=0.5, anchor='center')


game.config(background="#19790F")





for btn in [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9]:
    btn.config(image=None)










root.mainloop()
