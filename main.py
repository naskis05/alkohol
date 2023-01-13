from tkinter import *
from tkinter.font import BOLD, Font
from tkinter.ttk import *
x=0
logs=Tk()
logs.title('Alkohola tests')
logs.geometry('640x480')
a=Canvas(logs, width=640, height=480)
a.place(x=0, y=0)
#Sākuma ekrāns
label = Label(logs, text="Tests par alkoholu",font=25)
label.place(x=250, y=100, height=20, width=150)

a1=IntVar()
a2=IntVar()



def pirmaisuzd():
  J1=Label(logs, text='Cik daudz ir 1 promile?', font=15)
  R1=Checkbutton(logs, text='0,5%', variable = a1, onvalue=2, offvalue=0)
  R2=Checkbutton(logs, text='1%', variable = a1, onvalue=3, offvalue=0)
  R3=Checkbutton(logs, text='0,1%', variable = a1, onvalue=1, offvalue=0)
  J1.place(x=250, y=100)
  R1.place(x=250, y=150)
  R2.place(x=250, y=200)
  R3.place(x=250, y=250)
  def izdzestpirmo():
    J1.place_forget()
    R1.place_forget()
    R2.place_forget()
    R3.place_forget()
    poga1.place_forget()
    otraisuzd()
  poga1=Button(logs, text='Nākamais jautājums', command=izdzestpirmo)
  poga1.place(x=250, y=300)


def otraisuzd():
  J2=Label(logs, text='Kurā vietā Latvija ir alkoholisma ziņā Eiropas Savienībā?', font=15)
  R4=Checkbutton(logs, text='1. vieta', variable = a2, onvalue=2, offvalue=0)
  R5=Checkbutton(logs, text='2. vieta', variable = a2, onvalue=1, offvalue=0)
  R6=Checkbutton(logs, text='3. vieta', variable = a2, onvalue=3, offvalue=0)
  J2.place(x=100, y=100)
  R4.place(x=250, y=150)
  R5.place(x=250, y=200)
  R6.place(x=250, y=250)  

def navsākumaekrāns():
  label.place_forget()
  Sākt.place_forget()
  pirmaisuzd()
  
Sākt = Button(logs, text='Sākt testu', command=navsākumaekrāns)
Sākt.place(x=300, y=300)

  




logs.mainloop()





