from tkinter import * 
from tkinter.ttk import * 
import pyautogui
w,h = pyautogui.size()
screen = Tk()
screen.geometry(f"{w}x{h}")
screen.config(background="darkgreen",border=10,borderwidth=10,relief="raised")
screen.title("Coffee store")

Label(screen,text="Welcome to the Cafe",font=("Arial",30),background="blue",foreground="white").grid(row=0,column=0,columnspan=3,pady=20)
drinkval = StringVar()
Label(screen,text="Select your drink",font=("Arial",20),background="blue",foreground="white").grid(row=1,column=1,pady=20)
drinkcombo = Combobox(screen,textvariable=drinkval,values =["Cappucino","Latte","Decaf","Hot Chocolate"] ,font=("Arial",20),state="readonly")
drinkcombo.grid(row=2,column=1,pady=20)
drinkcombo.current(0)
Label(screen,text="Select your quantity",font=("Arial",20),background="darkgreen",foreground="white").grid(row=1,column=2,pady=20)
quantity = Spinbox(screen,from_=1,to=10,font=("Arial",20),width=5)
quantity.grid(row=2,column=2,pady=20)
Label(screen,text="Select the size",font=("Arial",20),background="darkgreen",foreground="white").grid(row=1,column=3,pady=20)
sizeval = StringVar(value="Grande")
Radiobutton(screen,text="Tall     ",variable=sizeval,value="Tall").grid(row=2,column=3,pady=20)
Radiobutton(screen,text="Grande",variable=sizeval,value="Grande").grid(row=3,column=3,pady=20)
Radiobutton(screen,text="Venti     ",variable=sizeval,value="Venti").grid(row=4,column=3,pady=20)

screen.mainloop()