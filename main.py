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
def navsākumaekrāns():
  label.place_forget()
  Sākt.place_forget()
  pirmaisuzd()
  
Sākt = Button(logs, text='Sākt testu', command=navsākumaekrāns)
Sākt.place(x=300, y=300)

#Jautājumu cipari (neaiztikt)
a1=IntVar()
a2=IntVar()
a3=IntVar()
a4=IntVar()
a5=IntVar()
a6=IntVar()
a7=IntVar()
a8=IntVar()
a9=IntVar()


#Jautājumi un atbildes
def pirmaisuzd():
  J1=Label(logs, text='Cik daudz ir 1 promile?', font=15)
  R1=Checkbutton(logs, text='0,5%', variable = a1, onvalue=2, offvalue=0)
  R2=Checkbutton(logs, text='1%', variable = a1, onvalue=3, offvalue=0)
  R3=Checkbutton(logs, text='0,1%', variable = a1, onvalue=1, offvalue=0)
  J1.place(x=250, y=100)
  R1.place(x=290, y=150)
  R2.place(x=290, y=200)
  R3.place(x=290, y=250)
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
  R4.place(x=290, y=150)
  R5.place(x=290, y=200)
  R6.place(x=290, y=250)  
  def izdzestotro():
    J2.place_forget()
    R4.place_forget()
    R5.place_forget()
    R6.place_forget()
    poga2.place_forget()
    tresaisuzd()
  poga2=Button(logs, text='Nākamais Jautājums', command=izdzestotro)
  poga2.place(x=250, y=300)

def tresaisuzd():
  J3=Label(logs, text='Cik procentu jauniešu lieto alkoholu regulāri?', font=15)
  R7=Checkbutton(logs, text='15%', variable = a3, onvalue=2, offvalue=0)
  R8=Checkbutton(logs, text='35%', variable = a3, onvalue=1, offvalue=0)
  R9=Checkbutton(logs, text='55%', variable = a3, onvalue=3, offvalue=0)
  J3.place(x=150, y=100)
  R7.place(x=290, y=150)
  R8.place(x=290, y=200)
  R9.place(x=290, y=250)
  def izdzesttreso():
    J3.place_forget()
    R7.place_forget()
    R8.place_forget()
    R9.place_forget()
    poga3.place_forget()
    ceturtaisuzd()
  poga3=Button(logs, text='Nākamais Jautājums', command=izdzesttreso)
  poga3.place(x=250, y=300)

def ceturtaisuzd():
  J4=Label(logs, text='Kā alkohols ietekmē tavu draudzību?', font=15)
  R10=Checkbutton(logs, text='Lielākoties pasliktina', variable = a4, onvalue=1, offvalue=0)
  R11=Checkbutton(logs, text='Neko nemaina', variable = a4, onvalue=2, offvalue=0)
  R12=Checkbutton(logs, text='Lielākoties uzlabo', variable = a4, onvalue=3, offvalue=0)
  J4.place(x=190, y=100)
  R10.place(x=250, y=150)
  R11.place(x=250, y=200)
  R12.place(x=250, y=250)
  def izdzestceturtais():
    J4.place_forget()
    R10.place_forget()
    R11.place_forget()
    R12.place_forget()
    poga4.place_forget()
    piektaisuzd()
  poga4=Button(logs, text='Nākamais Jautājums', command=izdzestceturtais)
  poga4.place(x=250, y=300)
  
def piektaisuzd():
  J5=Label(logs, text='Cik litrus alkohola patērē latvietis gadā?', font=15)
  R13=Checkbutton(logs, text='8 litri', variable = a5, onvalue=3, offvalue=0)
  R14=Checkbutton(logs, text='11 litri', variable = a5, onvalue=2, offvalue=0)
  R15=Checkbutton(logs, text='13 litri', variable = a5, onvalue=1, offvalue=0)
  J5.place(x=190, y=100)
  R13.place(x=290, y=150)
  R14.place(x=290, y=200)
  R15.place(x=290, y=250)
  def izdzestpiekto():
    J5.place_forget()
    R13.place_forget()
    R14.place_forget()
    R15.place_forget()
    poga5.place_forget()
    sestaisuzd()
  poga5=Button(logs, text='Nākamais Jautājums', command=izdzestpiekto)
  poga5.place(x=250, y=300)


  



logs.mainloop()





