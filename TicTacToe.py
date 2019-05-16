import tkinter as tk
from tkinter import messagebox
import random
from win32api import GetSystemMetrics

master = tk.Tk()
master.title("Tic Tac Toe")
master.geometry("{}x{}".format(int(GetSystemMetrics(0) / 3), int(GetSystemMetrics(1) / 2)))
turn = 'X'
win = False
turnCount = 1

def Invalid():
    messagebox.showerror(title="Invalid", message= "Invalid move!")
def turnChange():
    global buttonA1
    global buttonA2
    global buttonA3
    global buttonB1
    global buttonB2
    global buttonB3
    global buttonC1
    global buttonC2
    global buttonC3
    global turn
    global win
    global turnCount
    turnCount += 1
    if win == False:
        winMessage = turn + " has won the game!"
        if (buttonA1 == turn and buttonB1 == turn and buttonC1 == turn):
            messagebox.showinfo(title="%s won!" % turn, message=winMessage)
        elif (buttonA2 == turn and buttonB2 == turn and buttonC2 == turn):
            messagebox.showinfo(title="%s won!" % turn, message=winMessage)
        elif (buttonA3 == turn and buttonB3 == turn and buttonC3 == turn):
            messagebox.showinfo(title="%s won!" % turn, message=winMessage)
        elif (buttonA1 == turn and buttonA2 == turn and buttonA3 == turn):
            messagebox.showinfo(title="%s won!" % turn, message=winMessage)
        elif (buttonB1 == turn and buttonB2 == turn and buttonB3 == turn):
            messagebox.showinfo(title="%s won!" % turn, message=winMessage)
        elif (buttonC1 == turn and buttonC2 == turn and buttonC3 == turn):
            messagebox.showinfo(title="%s won!" % turn, message=winMessage)
        elif (buttonA3 == turn and buttonB2 == turn and buttonC1 == turn):
            messagebox.showinfo(title="%s won!" % turn, message=winMessage)
        elif (buttonA1 == turn and buttonB2 == turn and buttonC3 == turn):
            messagebox.showinfo(title="%s won!" % turn, message=winMessage)
        elif turnCount == 10:
            messagebox.showerror(title="Tie", message="It's a Tie!")
        else:
            if turn == 'X':
                turn = 'O'
                messagebox.showinfo(title="O's turn", message="O's turn")
                buttonPressed = random.choice(buttonList)
                buttonPressed.invoke()

            elif turn == 'O':
                turn = 'X'
                messagebox.showinfo(title="X's turn", message="X's turn")
    else:
        pass
def A1():
    global buttonA1
    buttonList.remove(buttonA1)
    buttonA1 = turn
    button = tk.Button(master, text=turn, width= int(GetSystemMetrics(0) / 100), height=int(GetSystemMetrics(1) / 100)
                       , command=Invalid)
    button.grid(row=1, column=1)
    turnChange()
def A2():
    global buttonA2
    buttonList.remove(buttonA2)
    buttonA2 = turn
    button = tk.Button(master, text=turn, width= int(GetSystemMetrics(0) / 100), height=int(GetSystemMetrics(1) / 100)
                       , command=Invalid)
    button.grid(row=1, column=2)
    turnChange()
def A3():
    global buttonA3
    buttonList.remove(buttonA3)
    buttonA3 = turn
    button = tk.Button(master, text=turn, width= int(GetSystemMetrics(0) / 100), height=int(GetSystemMetrics(1) / 100)
                       , command=Invalid)
    button.grid(row=1, column=3)
    turnChange()
def B1():
    global buttonB1
    buttonList.remove(buttonB1)
    buttonB1 = turn
    button = tk.Button(master, text=turn, width= int(GetSystemMetrics(0) / 100), height=int(GetSystemMetrics(1) / 100)
                       , command=Invalid)
    button.grid(row=2, column=1)
    turnChange()
def B2():
    global buttonB2
    buttonList.remove(buttonB2)
    buttonB2 = turn
    button = tk.Button(master, text=turn, width= int(GetSystemMetrics(0) / 100), height=int(GetSystemMetrics(1) / 100)
                       , command=Invalid)
    button.grid(row=2, column=2)
    turnChange()
def B3():
    global buttonB3
    buttonList.remove(buttonB3)
    buttonB3 = turn
    button = tk.Button(master, text=turn, width= int(GetSystemMetrics(0) / 100), height=int(GetSystemMetrics(1) / 100)
                       , command=Invalid)
    button.grid(row=2, column=3)
    turnChange()
def C1():
    global buttonC1
    buttonList.remove(buttonC1)
    buttonC1 = turn
    button = tk.Button(master, text=turn, width= int(GetSystemMetrics(0) / 100), height=int(GetSystemMetrics(1) / 100)
                       , command=Invalid)
    button.grid(row=3, column=1)
    turnChange()
def C2():
    global buttonC2

    buttonList.remove(buttonC2)
    buttonC2 = turn
    button = tk.Button(master, text=turn, width= int(GetSystemMetrics(0) / 100), height=int(GetSystemMetrics(1) / 100)
                       , command=Invalid)
    button.grid(row=3, column=2)
    turnChange()
def C3():
    global buttonC3
    buttonList.remove(buttonC3)
    buttonC3 = turn
    button = tk.Button(master, text=turn, width= int(GetSystemMetrics(0) / 100), height=int(GetSystemMetrics(1) / 100)
                       , command=Invalid)
    button.grid(row=3, column=3)
    turnChange()


buttonA1 = tk.Button(master, text="", width= int(GetSystemMetrics(0) / 100), height=int(GetSystemMetrics(1) / 100)
                     , command=A1)
buttonA1.grid(row=1, column=1)
buttonA2 = tk.Button(master, text="", width= int(GetSystemMetrics(0) / 100), height=int(GetSystemMetrics(1) / 100)
                     , command=A2)
buttonA2.grid(row=1, column=2)
buttonA3 = tk.Button(master, text="", width= int(GetSystemMetrics(0) / 100), height=int(GetSystemMetrics(1) / 100)
                     , command=A3)
buttonA3.grid(row=1, column=3)
buttonB1 = tk.Button(master, text="", width= int(GetSystemMetrics(0) / 100), height=int(GetSystemMetrics(1) / 100)
                     , command=B1)
buttonB1.grid(row=2, column=1)
buttonB2 = tk.Button(master, text="", width= int(GetSystemMetrics(0) / 100), height=int(GetSystemMetrics(1) / 100)
                     , command=B2)
buttonB2.grid(row=2, column=2)
buttonB3 = tk.Button(master, text="", width= int(GetSystemMetrics(0) / 100), height=int(GetSystemMetrics(1) / 100)
                     , command=B3)
buttonB3.grid(row=2, column=3)
buttonC1 = tk.Button(master, text="", width= int(GetSystemMetrics(0) / 100), height=int(GetSystemMetrics(1) / 100)
                     , command=C1)
buttonC1.grid(row=3, column=1)
buttonC2 = tk.Button(master, text="", width= int(GetSystemMetrics(0) / 100), height=int(GetSystemMetrics(1) / 100)
                     , command=C2)
buttonC2.grid(row=3, column=2)
buttonC3 = tk.Button(master, text="", width= int(GetSystemMetrics(0) / 100), height=int(GetSystemMetrics(1) / 100)
                     , command=C3)
buttonC3.grid(row=3, column=3)
buttonList = [buttonA1, buttonA2, buttonA3, buttonB1, buttonB2, buttonB3, buttonC1, buttonC2, buttonC3]

tk.mainloop()