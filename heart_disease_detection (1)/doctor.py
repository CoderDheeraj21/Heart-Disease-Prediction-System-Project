
import tkinter as tk
#from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk


##############################################+=============================================================
root = tk.Tk()
root.configure(background="brown")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Doctor Information")

# 43

# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 = Image.open('img2.jpg')
image2 = image2.resize((w, h), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)
#
label_l1 = tk.Label(root, text="__Doctor Information__",font=("Times New Roman", 30, 'bold'),
                    background="green", fg="white", width=60, height=1)
label_l1.place(x=0, y=0)


def doctor():
    label_l1 = tk.Label(root, text="__Doctor Information__\n\n\n Sr.             Name                    Phone No   \n 1.   Dr. Ranjit Patil            09011528599\n 2.   Dr. Suhas Hardas         02025520999\n 3.   Dr. Priya Palimkar      07887955500\n 4.   Dr. Ram Mangal          02067441600\n 5.   Dr. Abhijit Joshi          08048034093",font=("Times New Roman", 15, 'bold'),
                        background="grey", fg="black", width=65, height=15)
    label_l1.place(x=500, y=300)
    
    


def window():
  root.destroy()

button3 = tk.Button(root, text="doctors Information",command=doctor,width=16, height=1,font=('times', 20, ' bold '), bg="black", fg="white")
button3.place(x=600, y=100)

button3 = tk.Button(root, text="Exit",command=window,width=14, height=1,font=('times', 20, ' bold '), bg="black", fg="white")
button3.place(x=200, y=100)

root.mainloop()
