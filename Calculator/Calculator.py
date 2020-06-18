from tkinter import *

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def b_clear():
    e.delete(0, END)

def b_add():
    first_num:int
    first_num=e.get()
    global f_num
    global math
    math = "add"
    f_num = int(first_num)
    e.delete(0, END)

def b_sub():
    first_num: int
    first_num = e.get()
    global f_num
    global math
    math = "sub"
    f_num = int(first_num)
    e.delete(0, END)

def b_mul():
    first_num: int
    first_num = e.get()
    global f_num
    global math
    math = "mul"
    f_num = int(first_num)
    e.delete(0, END)

def b_div():
    first_num: int
    first_num = e.get()
    global f_num
    global math
    math = "div"
    f_num = int(first_num)
    e.delete(0, END)

def b_equal():
    second_num:int
    second_num=e.get()
    e.delete(0, END)
    if(math=="add"):
        e.insert(0, f_num + int(second_num))
    elif(math=="sub"):
        e.insert(0, f_num - int(second_num))
    elif (math == "mul"):
        e.insert(0, f_num * int(second_num))
    elif (math == "div"):
        e.insert(0, f_num / int(second_num))


root = Tk()
root.title("Rohit's Calculator")
root.configure(bg="#000000")
root.iconbitmap('C:/Users/Rohit/PycharmProjects/Current/Calculator/Calculator.ico')


e=Entry(root, width=35, borderwidth=5, bg="#FF6347", fg="#000000")
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1), bg="#000000", fg="red")
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2), bg="#000000", fg="red")
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3), bg="#000000", fg="red")
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4), bg="#000000", fg="red")
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5), bg="#000000", fg="red")
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6), bg="#000000", fg="red")
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7), bg="#000000", fg="red")
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8), bg="#000000", fg="red")
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9), bg="#000000", fg="red")
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0), bg="#000000", fg="red")
button_equal = Button(root, text="=", padx=91, pady=20, command=lambda: b_equal(), bg="#000000", fg="blue")
button_clear = Button(root, text="Clear", padx=79, pady=20, command=lambda: b_clear(), bg="#000000", fg="green")
button_add = Button(root, text="+", padx=39, pady=20, command=lambda: b_add(), bg="#000000", fg="yellow")
button_sub = Button(root, text="-", padx=41, pady=20, command=lambda: b_sub(), bg="#000000", fg="yellow")
button_mul = Button(root, text="x", padx=41, pady=20, command=lambda: b_mul(), bg="#000000", fg="yellow")
button_div = Button(root, text="/", padx=42, pady=20, command=lambda: b_div(), bg="#000000", fg="yellow")


button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)

button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)
button_sub.grid(row=6, column=0)
button_mul.grid(row=6, column=1)
button_div.grid(row=6, column=2)


root.mainloop()