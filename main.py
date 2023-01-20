from tkinter import *
from tkinter.font import BOLD, Font
from tkinter.ttk import *
from PIL import Image,ImageTk
x=0
logs=Tk()
logs.title('Alkohola tests')
logs.geometry('640x480')
a=Canvas(logs, width=640, height=480)
a.place(x=0, y=0)
#Sākuma ekrāns
  
def navsākumaekrāns():
  label.place_forget()
  Sākt.place_forget()
  minēšana.place_forget()
  pirmaisuzd()

def minēšana():
  label.place_forget()
  Sākt.place_forget()
  minēšana.place_forget()
  trakaispirmais()
  
def sākumaekrānsplace():
  label.place(x=250, y=100, height=20, width=150)
  Sākt.place(x=280, y=200)
  minēšana.place(x=280, y=300)

label = Label(logs, text="Tests par alkoholu",font=25)
label.place(x=250, y=100, height=20, width=150)
Sākt = Button(logs, text='Sākt testu', command=navsākumaekrāns)
Sākt.place(x=280, y=200)
minēšana = Button(logs, text='Minēšana', command=minēšana)
minēšana.place(x=280, y=300)

  
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
a10=IntVar()


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

def sestaisuzd():
  J6=Label(logs, text='Cik iztērē vidēji Latvijā priekš alkohola gada laikā?', font=15)
  R16=Checkbutton(logs, text='80 eiro', variable = a6, onvalue=1, offvalue=0)
  R17=Checkbutton(logs, text='100 eiro', variable = a6, onvalue=2, offvalue=0)
  R18=Checkbutton(logs, text='120 eiro', variable = a6, onvalue=3, offvalue=0)
  J6.place(x=110, y=100)
  R16.place(x=270, y=150)
  R17.place(x=270, y=200)
  R18.place(x=270, y=250)
  def izdzestsesto():
    J6.place_forget()
    R16.place_forget()
    R17.place_forget()
    R18.place_forget()
    poga6.place_forget()
    septitaisuzd()
  poga6=Button(logs, text='Nākamais Jautājums', command=izdzestsesto)
  poga6.place(x=250, y=300)
  
def septitaisuzd():
  J7=Label(logs, text='Cik procenti vīriešu paliek vairāk agresīvi alkohola reibumā?', font=15)
  R19=Checkbutton(logs, text='20%', variable = a7, onvalue=3, offvalue=0)
  R20=Checkbutton(logs, text='35%', variable = a7, onvalue=2, offvalue=0)
  R21=Checkbutton(logs, text='50%', variable = a7, onvalue=1, offvalue=0)
  J7.place(x=110, y=100)
  R19.place(x=270, y=150)
  R20.place(x=270, y=200)
  R21.place(x=270, y=250)
  def izdzestseptito():
    J7.place_forget()
    R19.place_forget()
    R20.place_forget()
    R21.place_forget()
    poga7.place_forget()
    astotaisuzd()
  poga7=Button(logs, text='Nākamais Jautājums', command=izdzestseptito)
  poga7.place(x=250, y=300)

def astotaisuzd():
  J8=Label(logs, text='Vai alkohols skaitās kā narkotikas?', font=15)
  R22=Checkbutton(logs, text='Jā', variable = a8, onvalue=1, offvalue=0)
  R23=Checkbutton(logs, text='Nē', variable = a8, onvalue=2, offvalue=0)
  R24=Checkbutton(logs, text='Atšķirībā kāds veids', variable = a8, onvalue=3, offvalue=0)
  J8.place(x=110, y=100)
  R22.place(x=270, y=150)
  R23.place(x=270, y=200)
  R24.place(x=270, y=250)
  def izdzestastoto():
    J8.place_forget()
    R22.place_forget()
    R23.place_forget()
    R24.place_forget()
    poga8.place_forget()
    devitaisuzd()
  poga8=Button(logs, text='Nākamais Jautājums', command=izdzestastoto)
  poga8.place(x=250, y=300)

def devitaisuzd():
  J9=Label(logs, text='Cik cilvēki Latvijā pieķerti alkohola reibumā pie stūres 2020. gadā?', font=15)
  R25=Checkbutton(logs, text='2469 cilvēki', variable = a9, onvalue=3, offvalue=0)
  R26=Checkbutton(logs, text='2894 cilvēki', variable = a9, onvalue=2, offvalue=0)
  R27=Checkbutton(logs, text='3275 cilvēki', variable = a9, onvalue=1, offvalue=0)
  J9.place(x=100, y=100)
  R25.place(x=270, y=150)
  R26.place(x=270, y=200)
  R27.place(x=270, y=250)
  def izdzestdevito():
    J9.place_forget()
    R25.place_forget()
    R26.place_forget()
    R27.place_forget()
    poga9.place_forget()
    desmitaisuzd()
  poga9=Button(logs, text='Nākamais Jautājums', command=izdzestdevito)
  poga9.place(x=250, y=300)

def desmitaisuzd():
  J10=Label(logs, text='Cik cilvēki 2017. gadā nomira no alkohola saindēšanās Latvijā?', font=15)
  R28=Checkbutton(logs, text='117 cilvēki', variable = a10, onvalue=1, offvalue=0)
  R29=Checkbutton(logs, text='186 cilvēki', variable = a10, onvalue=2, offvalue=0)
  R30=Checkbutton(logs, text='294 cilvēki', variable = a10, onvalue=3, offvalue=0)
  J10.place(x=100, y=100)
  R28.place(x=270, y=150)
  R29.place(x=270, y=200)
  R30.place(x=270, y=250)
  def izdzestdesmito():
    J10.place_forget()
    R28.place_forget()
    R29.place_forget()
    R30.place_forget()
    poga10.place_forget()
    rezultats1()
  poga10=Button(logs, text='Pabeigt', command=izdzestdesmito)
  poga10.place(x=250, y=300)

def rezultats1():
    sum=0
    if a1.get()==1:
      sum=sum+1
    if a2.get()==1:
      sum=sum+1
    if a3.get()==1:
      sum=sum+1
    if a4.get()==1:
      sum=sum+1
    if a5.get()==1:
      sum=sum+1
    if a6.get()==1:
      sum=sum+1
    if a7.get()==1:
      sum=sum+1
    if a8.get()==1:
      sum=sum+1
    if a9.get()==1:
      sum=sum+1
    if a10.get()==1:
      sum=sum+1
    izvade1=Label(logs, text='No 10 jautājumiem, jums pareizas ir '+str(sum)+'.', font=20)
    izvade1.place(x=180, y=100)
    def rezultats1dzesana():
      izvade1.place_forget()
      nojauna.place_forget()
      sākumaekrānsplace()
      a1=0
      a2=0
      a3=0
      a4=0
      a5=0
      a6=0
      a7=0
      a8=0
      a9=0
      a10=0
    nojauna=Button(logs, text='Iet uz galveno izvelni', command=rezultats1dzesana)
    nojauna.place(x=250, y=300)

def trakaispirmais():
  image=Image.open('image.png')
  img=image.resize((450, 350))
  jager1=ImageTk.PhotoImage(img)
  a.create_image(400, 250,image=jager1)
  

logs.mainloop()
