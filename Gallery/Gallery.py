from tkinter import *
from PIL import ImageTk,Image


root=Tk()
root.title("Rohit's Tkinter")
root.iconbitmap('C:/Users/Rohit/PycharmProjects/Current/images/photos.ico')


global image_list
global img_no

img_no=1

my_img1 = ImageTk.PhotoImage(Image.open("images/aspen.png"))
my_img2 = ImageTk.PhotoImage(Image.open("images/aspen2.png"))
my_img3 = ImageTk.PhotoImage(Image.open("images/me1.png"))
my_img4 = ImageTk.PhotoImage(Image.open("images/me2.png"))
my_img5 = ImageTk.PhotoImage(Image.open("images/me3.png"))

image_list = [my_img1,my_img2,my_img3,my_img4,my_img5]

status = Label(root, text="Image " + "1" +" of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)


def forward(img_no):
    global my_Label
    global button_next
    global button_back

    my_Label.grid_forget()
    my_Label = Label(image=image_list[img_no-1])
    button_next = Button(root, text=">>", command=lambda: forward(img_no+1))
    button_back = Button(root, text="<<", command=lambda: backward(img_no-1))
    status = Label(root, text="Image " + str(img_no) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)

    if(img_no == len(image_list)):
        button_next = Button(root, text=">>", state=DISABLED)

    my_Label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_next.grid(row=1, column=2)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)


def backward(img_no):
    global my_Label
    global button_next
    global button_back

    my_Label.grid_forget()
    my_Label = Label(image=image_list[img_no - 1])
    button_next = Button(root, text=">>", command=lambda: forward(img_no + 1))
    button_back = Button(root, text="<<", command=lambda: backward(img_no - 1))
    status = Label(root, text="Image " + str(img_no) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)

    if (img_no == 1):
        button_back = Button(root, text="<<", state=DISABLED)

    my_Label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_next.grid(row=1, column=2)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)


my_Label = Label(image=image_list[0])
my_Label.grid(row=0, column=0, columnspan=3)


button_back = Button(root, text="<<", command=backward(1), state=DISABLED)
button_next = Button(root, text=">>", command=lambda: forward(2))
button_quit = Button(root, text="Exit Program", command=root.quit)


button_back.grid(row=1, column=0)
button_quit.grid(row=1, column=1)
button_next.grid(row=1, column=2, pady=10)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)


root.mainloop()