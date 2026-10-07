from tkinter import * 
from tkinter.ttk import * 
import pyautogui
from tkinter import messagebox
w,h = pyautogui.size()
screen = Tk()
screen.geometry(f"{w}x{h}")
screen.config(background="darkgreen",border=10,borderwidth=10,relief="raised")
screen.title("Lets buy pizza")

Label(screen,text="Welcome to Pizza Shop",font=("Arial",30),background="darkgreen",foreground="white").grid(row=0,column=2,columnspan=3,pady=20,padx=-20)
pizzaval = StringVar()
Label(screen,text="Select your pizza",font=("Arial",20),background="darkgreen",foreground="white").grid(row=1,column=1,pady=20)
pizzacombo = Combobox(screen,textvariable=pizzaval,values =["Marg","Meateor","BBQ,","Pepperoni"] ,font=("Arial",20),state="readonly")
pizzacombo.grid(row=2,column=1,pady=20)
pizzacombo.current(0)
Label(screen,text="Select your quantity",font=("Arial",20),background="darkgreen",foreground="white").grid(row=1,column=2,pady=20,padx=20)
quantity = Spinbox(screen,from_=1,to=10,font=("Arial",20),width=5,state="readonly")
quantity.grid(row=2,column=2,pady=20)
Label(screen,text="Select the size",font=("Arial",20),background="darkgreen",foreground="white").grid(row=1,column=3,pady=20)
sizeval = StringVar(value="Medium")
Radiobutton(screen,text="Small     ",variable=sizeval,value="Small").grid(row=2,column=3,pady=20)
Radiobutton(screen,text="Medium",variable=sizeval,value="Medium").grid(row=3,column=3,pady=20)
Radiobutton(screen,text="Large     ",variable=sizeval,value="Large").grid(row=4,column=3,pady=20)
Label(screen,text="Select your toppings",font=("Arial",20),background="darkgreen",foreground="white").grid(row=1,column=0,pady=20,padx=20)
Mushroom = BooleanVar()
Olives = BooleanVar()
ExtraCheese = BooleanVar()
Jalapenos = BooleanVar()
ExtraChilli = BooleanVar()
Checkbutton(screen,text="Mushroom",variable=Mushroom).grid(row=2,column=0,pady=20)
Checkbutton(screen,text="Olives",variable=ExtraCheese).grid(row=3,column=0,pady=20)
Checkbutton(screen,text="ExtraCheese",variable=Olives).grid(row=4,column=0,pady=20)
Checkbutton(screen,text="Jalapenos",variable=Jalapenos).grid(row=5,column=0,pady=20)
Checkbutton(screen,text="ExtraChilli",variable=ExtraChilli).grid(row=6,column=0,pady=20)

def place_order():
    pizza = pizzaval.get()
    qty = quantity.get()
    size = sizeval.get()
    toppings = []
    if Mushroom.get():
        toppings.append("Mushroom")
    if Olives.get():
        toppings.append("Olives")
    if ExtraCheese.get():
        toppings.append("ExtraCheese")
    if Jalapenos.get():
        toppings.append("Jalapenos")
    if ExtraChilli.get():
        toppings.append("ExtraChilli")
    
    order_summary = f"Order Summary:\nPizza: {pizza}\nQuantity: {qty}\nSize: {size}\nToppings: {', '.join(toppings) if toppings else 'None'}"
    
    messagebox.showinfo("Order Placed", order_summary)
Button(screen,text="Place Order",command=place_order).grid(row=7,column=2,pady=20)
screen.mainloop()