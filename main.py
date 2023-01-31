from tkinter import *
from tkinter.font import BOLD, Font
from tkinter.ttk import *
#from PIL import Image, ImageTk
x=0
logs=Tk()
logs.title('Alkohola tests')
logs.geometry('640x480')
a=Canvas(logs, width=640, height=480)
a.pack()
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

dlight=1.59
dzimtas=5.79
garage=1.89
morgan=24.99
jager=24.99
jhon=2.99
lode=2.29
riga=20.99
sarema=10.99
speka16=1.99
stolis=16.99
tervete=1.59

kopa=dlight+dzimtas+garage+morgan+jager+jhon+lode+riga+sarema+speka16+stolis+tervete

lasisana1=StringVar()
lasisana2=StringVar()
lasisana3=StringVar()
lasisana4=StringVar()
lasisana5=StringVar()
lasisana6=StringVar()
lasisana7=StringVar()
lasisana8=StringVar()
lasisana9=StringVar()
lasisana10=StringVar()
lasisana11=StringVar()
lasisana12=StringVar()

sum=0



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
  dlightbilde = PhotoImage(file= "dlight.png")
  a.create_image(300, 150, image=dlightbilde)
  bilde1 = Label(image=dlightbilde)
  bilde1.image = dlightbilde
  bilde1.pack()
  ievade1=Entry(logs, width=13, textvariable=lasisana1)
  ievade1.place(x=250, y=350)
  nosaukums1=Label(logs, text='Cik maksā 0.5 litri ar Dlight enerģijas dzērienu?', font=20)
  nosaukums1.place(x=150, y=300)
  def pirmaisalkash():
    atbildelight=lasisana1.get()
    print (atbildelight)
    bilde1.place_forget()
    nosaukums1.place_forget()
    ievade1.place_forget()
    dlightbilde.__del__()
    trakaisotrais()
    nauda1.place_forget()
    global sum
    sum=sum+int(atbildelight)
  nauda1=Button(logs, text='Izvadīt rezultātu', command=pirmaisalkash)
  nauda1.place(x=250, y=400)

def trakaisotrais():
  dzimtasbilde = PhotoImage(file= "dzimtas.png")
  a.create_image(300, 150, image=dzimtasbilde)
  bilde2 = Label(image=dzimtasbilde)
  bilde2.image = dzimtasbilde
  bilde2.pack()
  ievade2=Entry(logs, width=13, textvariable=lasisana2)
  ievade2.place(x=250, y=350)
  nosaukums2=Label(logs, text='Cik maksā 0.5 litri ar Dzimtas degvīnu?', font=20)
  nosaukums2.place(x=150, y=300)
  def otraisalkash():
    atbildedzimtas=lasisana2.get()
    bilde2.place_forget()
    dzimtasbilde.__del__()
    nosaukums2.place_forget()
    ievade2.place_forget()
    trakaistrešais()
    nauda2.place_forget()
    global sum
    sum=sum+int(atbildedzimtas)
  nauda2=Button(logs, text='Izvadīt rezultātu', command=otraisalkash)
  nauda2.place(x=250, y=400)

def trakaistrešais():
  garagebilde = PhotoImage(file= "garage.png")
  a.create_image(300, 150, image=garagebilde)
  bilde3 = Label(image=garagebilde)
  bilde3.image = garagebilde
  bilde3.pack()
  ievade3=Entry(logs, width=13, textvariable=lasisana3)
  ievade3.place(x=250, y=350)
  nosaukums3=Label(logs, text='Cik maksā 0.275 litri ar Garāžu?', font=20)
  nosaukums3.place(x=150, y=300)
  def trešaisalkash():
    atbildegarage=lasisana3.get()
    bilde3.place_forget()
    garagebilde.__del__()
    nosaukums3.place_forget()
    ievade3.place_forget()
    trakaisceturtais()
    nauda3.place_forget()
    global sum
    sum=sum+int(atbildegarage)
  nauda3=Button(logs, text='Izvadīt rezultātu', command=trešaisalkash)
  nauda3.place(x=250, y=400)

def trakaisceturtais():
  jagerbilde = PhotoImage(file= "jager.png")
  a.create_image(300, 150, image=jagerbilde)
  bilde4 = Label(image=jagerbilde)
  bilde4.image = jagerbilde
  bilde4.pack()
  ievade4=Entry(logs, width=13, textvariable=lasisana4)
  ievade4.place(x=250, y=350)
  nosaukums4=Label(logs, text='Cik maksā litrs ar Jāger?', font=20)
  nosaukums4.place(x=150, y=300)
  def ceturtaisalkash():
    atbildejager=lasisana4.get()
    bilde4.place_forget()
    jagerbilde.__del__()
    nosaukums4.place_forget()
    ievade4.place_forget()
    trakaispiektais()
    nauda4.place_forget()
    global sum
    sum=sum+int(atbildejager)
  nauda4=Button(logs, text='Izvadīt rezultātu', command=ceturtaisalkash)
  nauda4.place(x=250, y=400)

def trakaispiektais():
  jhonbilde = PhotoImage(file= "jhon.png")
  a.create_image(300, 150, image=jhonbilde)
  bilde5 = Label(image=jhonbilde)
  bilde5.image = jhonbilde
  bilde5.pack()
  ievade5=Entry(logs, width=13, textvariable=lasisana5)
  ievade5.place(x=250, y=350)
  nosaukums5=Label(logs, text='Cik maksā litrs ar Džoni?', font=20)
  nosaukums5.place(x=150, y=300)
  def piektaisalkash():
    atbildejhon=lasisana5.get()
    bilde5.place_forget()
    jhonbilde.__del__()
    nosaukums5.place_forget()
    ievade5.place_forget()
    trakaissestais()
    nauda5.place_forget()
    global sum
    sum=sum+int(atbildejhon)
  nauda5=Button(logs, text='Izvadīt rezultātu', command=piektaisalkash)
  nauda5.place(x=250, y=400)

def trakaissestais():
  kapteinisbilde = PhotoImage(file= "kapteinis.png")
  a.create_image(300, 150, image=kapteinisbilde)
  bilde6 = Label(image=kapteinisbilde)
  bilde6.image = kapteinisbilde
  bilde6.pack()
  ievade6=Entry(logs, width=13, textvariable=lasisana6)
  ievade6.place(x=250, y=350)
  nosaukums6=Label(logs, text='Cik maksā litrs ar Captain Morgan?', font=20)
  nosaukums6.place(x=150, y=300)
  def sestaisalkash():
    atbildekapteinis=lasisana6.get()
    bilde6.place_forget()
    kapteinisbilde.__del__()
    nosaukums6.place_forget()
    ievade6.place_forget()
    trakaisseptitais()
    nauda6.place_forget()
    global sum
    sum=sum+int(atbildekapteinis)
  nauda6=Button(logs, text='Izvadīt rezultātu', command=sestaisalkash)
  nauda6.place(x=250, y=400)

def trakaisseptitais():
  lodebilde = PhotoImage(file= "lode piu.png")
  a.create_image(300, 150, image=lodebilde)
  bilde7 = Label(image=lodebilde)
  bilde7.image = lodebilde
  bilde7.pack()
  ievade7=Entry(logs, width=13, textvariable=lasisana7)
  ievade7.place(x=250, y=350)
  nosaukums7=Label(logs, text='Cik maksā 0,5 litri ar Lodi?', font=20)
  nosaukums7.place(x=150, y=300)
  def septitaisalkash():
    atbildelode=lasisana7.get()
    bilde7.place_forget()
    lodebilde.__del__()
    nosaukums7.place_forget()
    ievade7.place_forget()
    trakaisastotais()
    nauda7.place_forget()
    global sum
    sum=sum+int(atbildelode)
  nauda7=Button(logs, text='Izvadīt rezultātu', command=septitaisalkash)
  nauda7.place(x=250, y=400)

def trakaisastotais():
  rigabilde = PhotoImage(file= "riigas.png")
  a.create_image(300, 150, image=rigabilde)
  bilde8 = Label(image=rigabilde)
  bilde8.image = rigabilde
  bilde8.pack()
  ievade8=Entry(logs, width=13, textvariable=lasisana8)
  ievade8.place(x=250, y=350)
  nosaukums8=Label(logs, text='Cik maksā litrs ar Rīgas melno balzāmu?', font=20)
  nosaukums8.place(x=150, y=300)
  def astotaisalkash():
    atbilderiga=lasisana8.get()
    bilde8.place_forget()
    rigabilde.__del__()
    nosaukums8.place_forget()
    ievade8.place_forget()
    trakaisdevitais()
    nauda8.place_forget()
    global sum
    sum=sum+int(atbilderiga)
  nauda8=Button(logs, text='Izvadīt rezultātu', command=astotaisalkash)
  nauda8.place(x=250, y=400)

def trakaisdevitais():
  saremabilde = PhotoImage(file= "sareema.png")
  a.create_image(300, 150, image=saremabilde)
  bilde9 = Label(image=saremabilde)
  bilde9.image = saremabilde
  bilde9.pack()
  ievade9=Entry(logs, width=13, textvariable=lasisana9)
  ievade9.place(x=250, y=350)
  nosaukums9=Label(logs, text='Cik maksā 0,5 litri ar sāremas džinu?', font=20)
  nosaukums9.place(x=150, y=300)
  def devitaisalkash():
    atbildesarema=lasisana9.get()
    bilde9.place_forget()
    saremabilde.__del__()
    nosaukums9.place_forget()
    ievade9.place_forget()
    trakaisdesmitais()
    nauda9.place_forget()
    global sum
    sum=sum+int(atbildesarema)
  nauda9=Button(logs, text='Izvadīt rezultātu', command=devitaisalkash)
  nauda9.place(x=250, y=400)

def trakaisdesmitais():
  tervetesbilde = PhotoImage(file= "senču.png")
  a.create_image(300, 150, image=tervetesbilde)
  bilde10 = Label(image=tervetesbilde)
  bilde10.image = tervetesbilde
  bilde10.pack()
  ievade10=Entry(logs, width=13, textvariable=lasisana10)
  ievade10.place(x=250, y=350)
  nosaukums10=Label(logs, text='Cik maksā 0,5 litri ar Tēŗvetes alu?', font=20)
  nosaukums10.place(x=150, y=300)
  def desmitaisalkash():
    atbildesencu=lasisana10.get()
    bilde10.place_forget()
    tervetesbilde.__del__()
    nosaukums10.place_forget()
    ievade10.place_forget()
    trakaisvienpadsmitais()
    nauda10.place_forget()
    global sum
    sum=sum+int(atbildesencu)
  nauda10=Button(logs, text='Izvadīt rezultātu', command=desmitaisalkash)
  nauda10.place(x=250, y=400)

def trakaisvienpadsmitais():
  cesubilde = PhotoImage(file= "speeka 16.png")
  a.create_image(300, 150, image=cesubilde)
  bilde11 = Label(image=cesubilde)
  bilde11.image = cesubilde
  bilde11.pack()
  ievade11=Entry(logs, width=13, textvariable=lasisana11)
  ievade11.place(x=250, y=350)
  nosaukums11=Label(logs, text='Cik maksā 0,28 litri ar Cēsu 14?', font=20)
  nosaukums11.place(x=150, y=300)
  def vienpadsmitaisalkash():
    atbildespeeka16=lasisana11.get()
    bilde11.place_forget()
    cesubilde.__del__()
    nosaukums11.place_forget()
    ievade11.place_forget()
    trakaisdivpadsmitais()
    nauda11.place_forget()
    global sum
    sum=sum+int(atbildespeeka16)
  nauda11=Button(logs, text='Izvadīt rezultātu', command=vienpadsmitaisalkash)
  nauda11.place(x=250, y=400)

def trakaisdivpadsmitais():
  stolisbilde = PhotoImage(file= "stolis.png")
  a.create_image(300, 150, image=stolisbilde)
  bilde12 = Label(image=stolisbilde)
  bilde12.image = stolisbilde
  bilde12.pack()
  ievade12=Entry(logs, width=13, textvariable=lasisana12)
  ievade12.place(x=250, y=350)
  nosaukums12=Label(logs, text='Cik maksā litrs ar Stolichnaya?', font=20)
  nosaukums12.place(x=150, y=300)
  def divpadsmitaisalkash():
    atbildestolis=lasisana12.get()
    bilde12.place_forget()
    stolisbilde.__del__()
    nosaukums12.place_forget()
    ievade12.place_forget()
    nauda12.place_forget()
    global sum
    sum=sum+int(atbildestolis)
    rezultats2()
  nauda12=Button(logs, text='Izvadīt rezultātu', command=divpadsmitaisalkash)
  nauda12.place(x=250, y=400)

def rezultats2():
  if sum>kopa:
    procenti=(sum/kopa)*100
    procenti=round(procenti,1)
    beiguteksts='Jūs domājāt ka alkohols ir par {0}% dārgāks nekā patiesībā!'.format(procenti)
  elif sum<kopa:
    procenti=(sum/kopa)*100
    procenti=100-procenti
    procenti=round(procenti,1)
    beiguteksts='Jūs domājāt ka alkohols ir par {0}% lētāks nekā patiesībā!'.format(procenti)
  elif sum==kopa:
    beiguteksts='Jūs precīzi uzminējāt alkoholu cenu!'
  beiguraksts=Label(text=beiguteksts, font=20)
  beiguraksts.place(x=75, y=150)
  beiguraksts2=Label(text='Neatkarīgi no rezultāta, dzert alkoholu ir naudas izmešana,', font=20)
  beiguraksts2.place(x=75, y=200)
  beiguraksts3=Label(text='Nākamajā logā redzēsiet bildi ar alkohola statistiku.', font=20)
  beiguraksts3.place(x=75, y=250)
  def izdzesana():
    beiguraksts.place_forget()
    beiguraksts2.place_forget()
    beiguraksts3.place_forget()
    pogauztabulu.place_forget()
    tabula()
  pogauztabulu=Button(logs, text='Uz tabulu!', command=izdzesana)
  pogauztabulu.place(x=250, y=300)

def tabula():
  tabulareal=PhotoImage(file= "tabula.png")
  a.create_image(350, 100, image=tabulareal)
  tabulabilde = Label(image=tabulareal)
  tabulabilde.image = tabulareal
  tabulabilde.pack()
  def maucamsakuma():
    tabulareal.__del__()
    tabulabilde.pack_forget()
    uzsakumu.place_forget()
    sākumaekrānsplace()
  uzsakumu=Button(logs, text='Uz sākumu!', command=maucamsakuma)
  uzsakumu.place(x=250, y=300)
logs.mainloop()
