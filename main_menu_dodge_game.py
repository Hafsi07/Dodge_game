from tkinter import *
from PIL import ImageTk,Image

#basic window
f=Tk()
f.geometry("500x500")
f.title("main menu")

bgg=ImageTk.PhotoImage(file="E:\\hafsi al ghabiyou\\coding\\python\\Dodge game\\backgrnd.png")
c=Canvas(f,width=500,height=500).place(x=0,y=0)
Label(c,image=bgg).place(x=-2,y=0)

d=open("E:\\hafsi al ghabiyou\\coding\\python\\Dodge game\\scores.txt","r")

#the scars
def huh():
    f.destroy() 
    import games.py
    exec("games.py")
def hh(e):
    b["bg"]="black"
Label(c,text= "Highest score:"+d.read(),bd=1,bg="#9495be",font=("Arial",15),relief=RIDGE).place(x=320,y=20)
b=Button(c,text="Quit",width=7,bd=3,relief=RAISED,bg="#9495be",command=lambda: f.destroy(), font=("ARIAL",15)).place(x=300,y=300)
Button(c,text="Play",bd=3,width=7,relief=RAISED,bg="#9495be",font=("ARIAL",15),comman=huh).place(x=100,y=300)
#b.bind("<enter>",hh)
f.mainloop ()