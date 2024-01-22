# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 11:37:20 2023

@author: admin
"""
import tkinter as tk
#from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk


##############################################+=============================================================
root = tk.Tk()
root.configure(background="brown")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("precautions Of Heart Disease")

# 43

# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 = Image.open('img1.jpg')
image2 = image2.resize((w, h), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)
#
label_l1 = tk.Label(root, text="__precautions Of Heart Disease__",font=("Times New Roman", 30, 'bold'),
                    background="Brown", fg="white", width=60, height=1)
label_l1.place(x=0, y=0)

def precautions():
    label_l1 = tk.Label(root, text="__precautions Of Heart Disease__ \n 1.Eat healthy. \n 2.Get active.\n 3.Stay at a healthy weight.\n 4.Quit smoking and stay away from secondhand smoke.\n 5.Control your cholesterol and blood pressure.\n 6.Drink alcohol only in moderation.\n 7.Manage stress.",font=("Times New Roman", 15, 'bold'),
                        background="white", fg="black", width=45, height=6)
    label_l1.place(x=500, y=150)

def doctor():
    from subprocess import call
    call(['python','doctor.py'])

def window():
  root.destroy()
button3 = tk.Button(root, text="precautions",command=precautions,width=14, height=1,font=('times', 20, ' bold '), bg="purple", fg="white")
button3.place(x=100, y=200)

button3 = tk.Button(root, text="doctors Information",command=doctor,width=16, height=1,font=('times', 20, ' bold '), bg="purple", fg="white")
button3.place(x=100, y=300)


button3 = tk.Button(root, text="Exit",command=window,width=14, height=1,font=('times', 20, ' bold '), bg="purple", fg="white")
button3.place(x=100, y=400)

root.mainloop()
