#********************Import Section************************#
from tkinter import *
from sys import *
from tkinter import messagebox
#******************Making Main Windows*********************#
win = Tk()
win.title("Tic Tac Toe")
global onoff,values
onoff=[True,True,True,True,True,True,True,True,True]
values = {}
option = TRUE
def call(label,index):
    global option,flag1,onoff
    if onoff[index]==TRUE:
        if option==TRUE:
            label.configure(text="X")
            option =FALSE
            values[index]='X'
            onoff[index]=FALSE
        else:
            label.configure(text="0")
            option =TRUE
            values[index]='0'
            onoff[index]=FALSE
  
    if 0 in values and 1 in values and 2 in values and values[0]==values[1]==values[2]=='0':
        messagebox.showinfo("Congratulation","Player 2 Won")
        exit()
    elif  0 in values and 1 in values and 2 in values and values[0]==values[1]==values[2]=='X':
        messagebox.showinfo("Congratulation","Player 1 Won")
        exit()
    elif 3 in values and 4 in values and 5 in values and values[3]==values[4]==values[5]=='0':
        messagebox.showinfo("Congratulation","Player 2 Won")
        exit()
    elif  3 in values and 4 in values and 5 in values and values[3]==values[4]==values[5]=='X':
        messagebox.showinfo("Congratulation","Player 1 Won")
        exit()
    elif  6 in values and 7 in values and 8 in values and values[6]==values[7]==values[8]=='0':
        messagebox.showinfo("Congratulation","Player 2 Won")
        exit()
    elif  6 in values and 7 in values and 8 in values and values[6]==values[7]==values[8]=='X':
        messagebox.showinfo("Congratulation","Player 1 Won")
        exit()
    elif 0 in values and 3 in values and 6 in values and values[0]==values[3]==values[6]=='0':
        messagebox.showinfo("Congratulation","Player 2 Won")
        exit()
    elif  0 in values and 3 in values and 6 in values and values[0]==values[3]==values[6]=='X':
        messagebox.showinfo("Congratulation","Player 1 Won")
        exit()
    elif 1 in values and 4 in values and 7 in values and values[1]==values[4]==values[7]=='0':
        messagebox.showinfo("Congratulation","Player 2 Won")
        exit()
    elif  1 in values and 4 in values and 7 in values and values[1]==values[4]==values[7]=='X':
        messagebox.showinfo("Congratulation","Player 1 Won")
        exit()
    elif 2 in values and 5 in values and 8 in values and values[2]==values[5]==values[8]=='0':
        messagebox.showinfo("Congratulation","Player 2 Won")
        exit()
    elif  2 in values and 5 in values and 8 in values and values[2]==values[5]==values[8]=='X':
        messagebox.showinfo("Congratulation","Player 1 Won")
        exit()
    
    ##################
    elif 0 in values and 4 in values and 8 in values and values[0]==values[4]==values[8]=='0':
        messagebox.showinfo("Congratulation","Player 2 Won")
        exit()
    elif  0 in values and 4 in values and 8 in values and values[0]==values[4]==values[8]=='X':
        messagebox.showinfo("Congratulation","Player 1 Won")
        exit()
    elif 2 in values and 4 in values and 6 in values and values[2]==values[4]==values[6]=='0':
        messagebox.showinfo("Congratulation","Player 2 Won")
        exit()
    elif  2 in values and 4 in values and 6 in values and values[2]==values[4]==values[6]=='X':
        messagebox.showinfo("Congratulation","Player 1 Won")
        exit()
    elif 0 in values and 1 in values and 2 in values and 3 in values and 4 in values and 5 in values and 6 in values and 7 in values and 8 in values:
        messagebox.showinfo("Oops","It's a Draw Restart the game")
        exit()

win.geometry("305x302")
flag1 = 0
lb1 = Button(win,width="3",height=0,font=("TIMES",35),bg='white',fg='red',command=lambda:call(lb1,flag1))
lb1.grid(row=0,column=0,ipady=4,ipadx=7)
flag2 = 1
lb2 = Button(win,width="3",font=("TIMES",35),height=0,bg='white',fg='red',command=lambda:call(lb2,flag2))
lb2.grid(row=0,column=1,ipady=4,ipadx=7)
flag3 = 2
lb3 = Button(win,width=3,height=0,font=("TIMES",35),bg='white',fg='red',command=lambda:call(lb3,flag3))
lb3.grid(row=0,column=2,ipady=4,ipadx=7)

flag4 = 3
lb4 = Button(win,width=3,height=0,font=("TIMES",35),bg='white',fg='red',command=lambda:call(lb4,flag4))
lb4.grid(row=1,column=0,ipady=4,ipadx=7)
flag5 = 4
lb5 = Button(win,width=3,height=0,font=("TIMES",35),bg='white',fg='red',command=lambda:call(lb5,flag5))
lb5.grid(row=1,column=1,ipady=4,ipadx=7)
flag6 = 5
lb6 = Button(win,width=3,height=0,font=("TIMES",35),bg='white',fg='red',command=lambda:call(lb6,flag6))
lb6.grid(row=1,column=2,ipady=4,ipadx=7)

flag7 = 6
lb7 = Button(win,width=3,height=0,font=("TIMES",35),bg='white',fg='red',command=lambda:call(lb7,flag7))
lb7.grid(row=2,column=0,ipady=4,ipadx=7)
flag8 = 7
lb8 = Button(win,width=3,height=0,font=("TIMES",35),bg='white',fg='red',command=lambda:call(lb8,flag8))
lb8.grid(row=2,column=1,ipady=4,ipadx=7)
flag9 = 8
lb9 = Button(win,width=3,height=0,font=("TIMES",35),bg='white',fg='red',command=lambda:call(lb9,flag9))
lb9.grid(row=2,column=2,ipady=4,ipadx=7)
win.resizable(FALSE,FALSE)
win.mainloop()
