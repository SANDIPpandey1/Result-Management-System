from tkinter import *
from PIL import Image, ImageTk # pip install pillow
from tkinter import messagebox, ttk
import sqlite3
class resultClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()
        
        #=======Title=======
        
        title = Label(self.root, text="Add Student Result Details", font=("goudy old style", 20, "bold"), bg="orange", fg="#262626").place(x=50, y=15, width=1180, height=50)
        self.var_name=StringVar()
        self.var_course=StringVar()
        self.var_marks=StringVar()
        self.var_full_marks=StringVar()
        self.roll_list=[]
        
        
        
        lbl_select = Label(self.root, text="Select Student", font=("goudy old style", 20, "bold"), bg="white").place(x=50, y=100)
        lbl_Name = Label(self.root, text="Name", font=("goudy old style", 20, "bold"), bg="white").place(x=50, y=160)
        lbl_course = Label(self.root, text="Course", font=("goudy old style", 20, "bold"), bg="white").place(x=50, y=220)
        lbl_marks_ob = Label(self.root, text="Marks Obtained", font=("goudy old style", 20, "bold"), bg="white").place(x=50, y=280)
        lbl_full_marks = Label(self.root, text="Full Marks", font=("goudy old style", 20, "bold"), bg="white").place(x=50, y=340)
        
        self.txt_student = ttk.Combobox(self.root,textvariable=self.var_course,values=self.course_list,font=("goudy old style", 15, "bold"),state='readonly',justify=CENTER)
        self.txt_student.place(x=480, y=180, width=200)
        self.txt_student.set("Select")

if __name__ == "__main__":
    root = Tk()
    obj = resultClass(root)
    root.mainloop()