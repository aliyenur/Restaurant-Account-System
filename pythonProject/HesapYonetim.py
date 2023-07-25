from tkinter import *
import tkinter.messagebox
import random


root = Tk()
root.geometry("1600x800+0+0")
space = " "
#başlık tanımlama
root.title(50*space + "Restaurant Hesap Sistemi")


coverFrame = Frame(root, bd=20, pady=2, relief=SUNKEN)
coverFrame.grid()
coverMainFrame = Frame(coverFrame, bd=20, pady=2, bg='olivedrab', relief=SUNKEN)
coverMainFrame.grid()


MainFrame = Frame(coverMainFrame, bd=5, pady=2, width=1350, height=700, relief=SUNKEN)
MainFrame.grid()

Tops = Frame(MainFrame, width=1600, height=50, bg='olivedrab', bd=18, relief=SUNKEN)
Tops.grid(row=0, column=0)

Tops2 = Frame(MainFrame, width=1600, height=700, bg='olivedrab', bd=18, relief=SUNKEN)
Tops2.grid(row=1, column=0)

f1 = Frame(Tops2, width=900, height=600, bd=10, relief=SUNKEN)
f1.grid(row=0, column=0)

f1a = Frame(f1, width=900, height=600, bd=10, relief=SUNKEN)
f1a.grid(row=0, column=0)

f1b = Frame(f1, width=900, height=100, relief=SUNKEN)
f1b.grid(row=1, column=0)

lblTitle = Label(Tops, font=('arial', 50, 'bold'), text="Restaurant Hesap Sistemi", fg='lightgray', bg='olivedrab', bd=10)
lblTitle.grid(row=0, column=0, padx=270)

#string ifadeleri tkinter sınıfında kullanılabilir hala getirme
rand = StringVar()
Mantı = StringVar()
İskender = StringVar()
Kebap = StringVar()
Tavuk = StringVar()
AraToplam = StringVar()
Toplam = StringVar()
Servis_Ücreti = StringVar()
Kola = StringVar()
Ayran = StringVar()
Şalgam = StringVar()
Su = StringVar()
Çay = StringVar()
Soda = StringVar()
Vergi = StringVar()
Hesap = StringVar()

#check button
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()


Mantı.set("0")
İskender.set("0")
Kebap.set("0")
Tavuk.set("0")
Kola.set("0")
Ayran.set("0")
Şalgam.set("0")
Su.set("0")
Çay.set("0")
Soda.set("0")


#Sıfırlama işlemi
def Reset():
    Mantı.set("0")
    İskender.set("0")
    Kebap.set("0")
    Tavuk.set("0")
    Kola.set("0")
    Ayran.set("0")
    Şalgam.set("0")
    Su.set("0")
    Çay.set("0")
    Soda.set("0")
    AraToplam.set("")
    Toplam.set("")
    Servis_Ücreti.set("")
    Vergi.set("")
    Hesap.set("")


    txtMantı.configure(state=DISABLED)
    txtİskender.configure(state=DISABLED)
    txtKebap.configure(state=DISABLED)
    txtTavuk.configure(state=DISABLED)
    txtKola.configure(state=DISABLED)
    txtAyran.configure(state=DISABLED)
    txtŞalgam.configure(state=DISABLED)
    txtSu.configure(state=DISABLED)
    txtÇay.configure(state=DISABLED)
    txtSoda.configure(state=DISABLED)

#onay kutusu seçili olmama durumu
    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)


def cÇıkış():
    cÇıkış = tkinter.messagebox.askyesno("Restaurant Hesap Sistemi", "Sistemden çıkış yapmak istediğinize emin misiniz?")
    if cÇıkış > 0:
        root.destroy()
        return


def ToplamHesap():
    x = random.randint(823, 358823)
    randomRef= str(x)
    rand.set(randomRef)


    HeMantı = float(Mantı.get())
    Heİskender = float(İskender.get())
    HeKebap = float(Kebap.get())
    HeTavuk = float(Tavuk.get())
    HeKola = float(Kola.get())
    HeAyran = float(Ayran.get())
    HeŞalgam = float(Şalgam.get())
    HeSu = float(Su.get())
    HeÇay = float(Çay.get())
    HeSoda = float(Çay.get())

    MantıHesabı = HeMantı*110
    İskenderHesabı = Heİskender*230
    KebapHesabı = HeKebap*200
    TavukHesabı = HeTavuk * 160
    KolaHesabı = HeKola * 25
    AyranHesabı = HeAyran * 20
    ŞalgamHesabı = HeŞalgam * 23
    SuHesabı = HeSu * 10
    ÇayHesabı = HeÇay * 110
    SodaHesabı = HeSoda * 8

    YemekHesabı = str('₺%.2f' % (MantıHesabı + İskenderHesabı + KebapHesabı + TavukHesabı + KolaHesabı + AyranHesabı +ŞalgamHesabı +SuHesabı + ÇayHesabı+ SodaHesabı))
    VergiÜcreti = ((MantıHesabı + İskenderHesabı + KebapHesabı + TavukHesabı + KolaHesabı + AyranHesabı + ŞalgamHesabı + SuHesabı + ÇayHesabı + SodaHesabı) * 0.1)
    ServisÜcreti =str('₺%.2f' %((MantıHesabı + İskenderHesabı + KebapHesabı + TavukHesabı + KolaHesabı + AyranHesabı +ŞalgamHesabı +SuHesabı + ÇayHesabı+ SodaHesabı) / 99))
    AToplam = str('₺%.2f' % (MantıHesabı + İskenderHesabı + KebapHesabı + TavukHesabı + KolaHesabı + AyranHesabı +ŞalgamHesabı +SuHesabı + ÇayHesabı+ SodaHesabı))
    ToplamVeri = (MantıHesabı + İskenderHesabı + KebapHesabı + TavukHesabı + KolaHesabı + AyranHesabı +ŞalgamHesabı +SuHesabı + ÇayHesabı+ SodaHesabı)
    Servis_Ücreti.set(ServisÜcreti)
    Hesap.set(YemekHesabı)
    AraToplam.set(AToplam)
    Vergi.set(str('₺%.2f' % (VergiÜcreti)))
    ToplamHesap =str('₺%.2f' % (VergiÜcreti + ToplamVeri))
    Toplam.set(ToplamHesap)


#

def hesapMantı():
    if(var1.get()==1):
        txtMantı.configure(state=NORMAL)
        txtMantı.focus()
        txtMantı.delete('0', END)
        Mantı.set("")
    elif(var1.get()==0):
        txtMantı.configure(state=DISABLED)
        Mantı.set("0")

def hesapİskender():
    if(var2.get()==1):
        txtİskender.configure(state=NORMAL)
        txtİskender.focus()
        txtİskender.delete('0', END)
        İskender.set("")
    elif(var2.get()==0):
        txtİskender.configure(state=DISABLED)
        İskender.set("0")

def hesapTavuk():
    if(var4.get()==1):
        txtTavuk.configure(state=NORMAL)
        txtTavuk.focus()
        txtTavuk.delete('0', END)
        Tavuk.set("")
    elif(var4.get()==0):
        txtTavuk.configure(state=DISABLED)
        Tavuk.set("0")


def hesapKola():
    if (var5.get() == 1):
        txtKola.configure(state=NORMAL)
        txtKola.focus()
        txtKola.delete('0', END)
        Kola.set("")
    elif (var5.get() == 0):
        txtKola.configure(state=DISABLED)
        Kola.set("0")

def hesapKebap():
    if (var3.get() == 1):
        txtKebap.configure(state=NORMAL)
        txtKebap.focus()
        txtKebap.delete('0', END)
        Kebap.set("")
    elif (var3.get() == 0):
        txtKebap.configure(state=DISABLED)
        Kebap.set("0")


def hesapAyran():
    if (var6.get() == 1):
        txtAyran.configure(state=NORMAL)
        txtAyran.focus()
        txtAyran.delete('0', END)
        Ayran.set("")
    elif (var6.get() == 0):
        txtAyran.configure(state=DISABLED)
        Ayran.set("0")

def hesapŞalgam():
    if (var7.get() == 1):
        txtŞalgam.configure(state=NORMAL)
        txtŞalgam.focus()
        txtŞalgam.delete('0', END)
        Şalgam.set("")
    elif (var7.get() == 0):
        txtŞalgam.configure(state=DISABLED)
        Şalgam.set("0")


def hesapSu():
    if (var8.get() == 1):
        txtSu.configure(state=NORMAL)
        txtSu.focus()
        txtSu.delete('0', END)
        Su.set("")
    elif (var8.get() == 0):
        txtSu.configure(state=DISABLED)
        Su.set("0")


def hesapÇay():
    if (var9.get() == 1):
        txtÇay.configure(state=NORMAL)
        txtÇay.focus()
        txtÇay.delete('0', END)
        Çay.set("")
    elif (var9.get() == 0):
        txtÇay.configure(state=DISABLED)
        Çay.set("0")


def hesapSoda():
    if (var10.get() == 1):
        txtSoda.configure(state=NORMAL)
        txtSoda.focus()
        txtSoda.delete('0', END)
        Soda.set("")
    elif (var10.get() == 0):
        txtSoda.configure(state=DISABLED)
        Soda.set("0")


lblRef = Label(f1a, font=('arial', 16, 'bold'), text="Sipariş No", fg='olivedrab', bd=10)
lblRef.grid(row=0, column=0, sticky=W)
txtRefence = Entry(f1a, font=('arial', 16, 'bold'), textvariable=rand, bd=10, justify='right', bg='lightgray')
txtRefence.grid(row=0, column=1)

chkMantı =Checkbutton(f1a, text="Mantı", variable=var1, onvalue=1, offvalue=0,
                       font=('arial', 16, 'bold'),command=hesapMantı ).grid(row=1, column=0, sticky=W)

txtMantı = Entry(f1a, font=('arial', 16, 'bold'), textvariable=Mantı, insertwidth=4, bd=10, justify='right',
                 bg='gray', state=DISABLED)
txtMantı.grid(row=1, column=1)

chkİskender =Checkbutton(f1a, text="İskender", variable=var2, onvalue=1, offvalue=0,
                       font=('arial', 16, 'bold'), command=hesapİskender).grid(row=2, column=0, sticky=W)

txtİskender = Entry(f1a, font=('arial', 16, 'bold'), textvariable=İskender, insertwidth=4, bd=10, justify='right',
                 bg='gray', state=DISABLED)
txtİskender.grid(row=2, column=1)

chkKebap =Checkbutton(f1a, text="Kebap", variable=var3, onvalue=1, offvalue=0,
                       font=('arial', 16, 'bold'), command=hesapKebap).grid(row=3, column=0, sticky=W)

txtKebap = Entry(f1a, font=('arial', 16, 'bold'), textvariable=Kebap, insertwidth=4, bd=10, justify='right',
                 bg='gray', state=DISABLED)
txtKebap.grid(row=3, column=1)

chkTavuk =Checkbutton(f1a, text="Tavuk", variable=var4, onvalue=1, offvalue=0,
                       font=('arial', 16, 'bold'), command=hesapTavuk).grid(row=4, column=0, sticky=W)

txtTavuk = Entry(f1a, font=('arial', 16, 'bold'), textvariable=Tavuk, insertwidth=4, bd=10, justify='right',
                 bg='gray', state=DISABLED)
txtTavuk.grid(row=4, column=1)

chkKola =Checkbutton(f1a, text="Kola", variable=var5, onvalue=1, offvalue=0,
                       font=('arial', 16, 'bold'), command=hesapKola).grid(row=5, column=0, sticky=W)

txtKola = Entry(f1a, font=('arial', 16, 'bold'), textvariable=Kola, insertwidth=4, bd=10, justify='right',
                 bg='gray', state=DISABLED)
txtKola.grid(row=5, column=1)

chkAyran =Checkbutton(f1a, text="Ayran", variable=var6, onvalue=1, offvalue=0,
                       font=('arial', 16, 'bold'),command=hesapAyran).grid(row=6, column=0, sticky=W)

txtAyran = Entry(f1a, font=('arial', 16, 'bold'), textvariable=Ayran, insertwidth=4, bd=10, justify='right',
                 bg='gray', state=DISABLED)
txtAyran.grid(row=6, column=1)

chkŞalgam =Checkbutton(f1a, text="Şalgam", variable=var7, onvalue=1, offvalue=0,
                       font=('arial', 16, 'bold'),command=hesapŞalgam).grid(row=7, column=0, sticky=W)

txtŞalgam = Entry(f1a, font=('arial', 16, 'bold'), textvariable=Şalgam, insertwidth=4, bd=10, justify='right',
                 bg='gray', state=DISABLED)
txtŞalgam.grid(row=7, column=1)

chkSu =Checkbutton(f1a, text="Su", variable=var8, onvalue=1, offvalue=0,
                       font=('arial', 16, 'bold'),command=hesapSu).grid(row=1, column=2, sticky=W)

txtSu = Entry(f1a, font=('arial', 16, 'bold'), textvariable=Su, insertwidth=4, bd=10, justify='right',
                 bg='gray', state=DISABLED)
txtSu.grid(row=1, column=3, pady=5)

chkÇay =Checkbutton(f1a, text="Çay", variable=var9, onvalue=1, offvalue=0,
                       font=('arial', 16, 'bold'),command=hesapÇay).grid(row=2, column=2, sticky=W, pady=5)

txtÇay = Entry(f1a, font=('arial', 16, 'bold'), textvariable=Çay, insertwidth=4, bd=10, justify='right',
                 bg='gray', state=DISABLED)
txtÇay.grid(row=2, column=3,pady=5)

chkSoda =Checkbutton(f1a, text="Soda", variable=var10, onvalue=1, offvalue=0,
                       font=('arial', 16, 'bold'),command=hesapSoda).grid(row=0, column=2, sticky=W, pady=5)

txtSoda = Entry(f1a, font=('arial', 16, 'bold'), textvariable=Soda, insertwidth=4, bd=10, justify='right',
                 bg='gray', state=DISABLED)
txtSoda.grid(row=0, column=3,pady=5)


lblHesap = Label(f1a, font=('arial', 16, 'bold'), text="Yemek Ücreti", bd=2, anchor='w')
lblHesap.grid(row=3, column=2, sticky=W, pady=5)
txtHesap = Entry(f1a, font=('arial', 16, 'bold'), textvariable=Hesap, bd=10, insertwidth=4,
                 justify='right')
txtHesap.grid(row=3, column=3, pady=5)

lblServis = Label(f1a, font=('arial', 16, 'bold'), text="Servis Ücreti", bd=2, anchor='w')
lblServis.grid(row=4, column=2, sticky=W, pady=5)
txtServis = Entry(f1a, font=('arial', 16, 'bold'), textvariable=Servis_Ücreti, bd=10, insertwidth=4,
                 justify='right')
txtServis.grid(row=4, column=3, pady=5)

lblVergi = Label(f1a, font=('arial', 16, 'bold'), text="Vergi Ücreti", bd=2, anchor='w')
lblVergi.grid(row=5, column=2, sticky=W, pady=5)
txtVergi = Entry(f1a, font=('arial', 16, 'bold'), textvariable=Vergi, bd=10, insertwidth=4,
                 justify='right')
txtVergi.grid(row=5, column=3, pady=5)


lblAraToplam = Label(f1a, font=('arial', 16, 'bold'), text="Ara Toplam", bd=2, anchor='w')
lblAraToplam.grid(row=6, column=2, sticky=W, pady=5)
txtAraToplam = Entry(f1a, font=('arial', 16, 'bold'), textvariable=AraToplam, bd=10, insertwidth=4,
                 justify='right')
txtAraToplam.grid(row=6, column=3, pady=5)


lblToplam = Label(f1a, font=('arial', 16, 'bold'), text="Toplam", bd=2, anchor='w')
lblToplam.grid(row=7, column=2, sticky=W, pady=5)
txtToplam = Entry(f1a, font=('arial', 16, 'bold'), textvariable=Toplam, bd=10, insertwidth=4,
                 justify='right')
txtToplam.grid(row=7, column=3, pady=5)


btnToplam = Button(f1b, padx=16, pady=8, bd=2, fg="lightgray", font=('arial', 17, 'bold'), width=17, text="Toplam",
                   bg='olivedrab', command=ToplamHesap ).grid(row=0, column=0, pady=5, padx=5)

btnReset = Button(f1b, padx=16, pady=8, bd=2, fg="lightgray", font=('arial', 17, 'bold'), width=17, text="Reset",
                   bg='olivedrab',command=Reset).grid(row=0, column=1, pady=5, padx=5)

btnÇıkış = Button(f1b, padx=16, pady=8, bd=2, fg="lightgray", font=('arial', 17, 'bold'), width=17, text="Çıkış",
                   bg='olivedrab',command=cÇıkış).grid(row=0, column=2, pady=5, padx=5)

root.mainloop()

