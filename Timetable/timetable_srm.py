from tkinter import Tk,Label,CENTER
from PIL import ImageTk, Image
#modules: tkinter, pillow

def UI():
    Timetable=Tk()
    Timetable.geometry('1920x1080')
    Timetable.state('zoomed')
    Timetable.title("TimeTable")
    Timetable['bg']='black'
    tt_layout=Image.open('CollegeTimetable.jpg')
    TTLayoutIMG=ImageTk.PhotoImage(tt_layout)
    TTLayout=Label(image=TTLayoutIMG).place(relx=0.5,rely=0.5,anchor=CENTER)
    Timetable.mainloop()

UI()

