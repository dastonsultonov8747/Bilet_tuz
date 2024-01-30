from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter import filedialog

oson_joyi = 0
qiyin_joyi = 0
nazaria_joyi = 0

oyna = Tk()
oyna.title("Bilet tuzamiz")
oyna.geometry("1200x800")
oyna.config(background="#336699")


def fakultet_select(event):
    selected_fakultet = fakultet.get()
    yonalish.configure(values=fakultetlar[selected_fakultet])


fakultetlar = {'Pedagogika': ['Psixologiya (faoliyat turlari bo‘yicha)', 'Pedagogika', 'Maktabgacha ta’lim',
                              'Boshlang‘ich ta’lim'],
               'San‘atshunoslik': ['Texnologik ta’lim',
                                   'Tasviriy san’at va muhandislik grafikasi', 'Musiqa ta’limi'],
               'Bioinjeneriya va oziq ovqat xavsizligi': ['Tuproqshunoslik',
                                                          'Sabzavotchilik, polizchilik va kartoshkachilik',
                                                          'Qishloq xo‘jalik mahsulotlarini saqlash va dastlabki ishlash texnologiyasi (mahsulotlar turlari bo‘yicha)',
                                                          'O‘simliklarni himoya qilish (ekin turlari bo‘yicha)',
                                                          'Mevachilik va uzumchilik',
                                                          'Issiqxona xo‘jaligini tashkil etish va yuritish',
                                                          'Dorivor o‘simliklarni yetishtirish va qayta ishlash texnologiyasi',
                                                          'Biotexnologiya (tarmoqlar bo‘yicha)',
                                                          'Agronomiya (sabzavotchilik va polizchilik)'],
               'Tarix': ['Tarix (mamlakatlar va yo‘nalishlar bo‘yicha)',
                         'Milliy g‘oya, ma’naviyat asoslari va huquq ta’limi', ],
               'Tabiiy Fanlar': ['Kimyo (turlari bo‘yicha)', 'Geografiya',
                                 'Geodeziya, kartografiya va kadastr (funksiyalari bo‘yicha)',
                                 'Ekologiya va atrof-muhit muhofazasi (tarmoqlar va sohalar bo‘yicha)',
                                 'Biologiya (turlari bo‘yicha)', ],
               'Filologiya': ['O‘zga tilli guruhlarda rus tili', 'O‘zbek tili va adabiyoti',
                              'Filologiya va tillarni o‘qitish: rus tili',
                              'Filologiya va tillarni o‘qitish: o‘zbek tili',
                              'Amaliy filologiya']
    , 'Xorijiy filologiya': ['Xorijiy til va adabiyoti: ingliz tili',
                             'Tarjima nazariyasi va amaliyoti (tillar bo‘yicha)',
                             'Gid hamrohligi va tarjimonlik faoliyati (tillar bo‘yicha) ',
                             'Filologiya va tillarni o‘qitish: nemis tili',
                             'Filologiya va tillarni o‘qitish: ingliz tili',
                             'Filologiya va tillarni o‘qitish: fransuz tili'],
               'Fizika-Matematika': ['KIDT', 'Matematik injenering', 'Amaliy matematika', 'Matematika', 'Fizika',
                                     'Mexanika va matematik modellashtirish'],
               'Iqtisod': ['Biznesni boshqarish', 'Turizm', 'Raqamli iqtisodiyot',
                           'Menejment: turizm biznesini boshqarish', 'Menejment: madaniy merosni boshqarish',
                           'Mehmonxona xo‘jaligini tashkil etish va boshqarish', 'Marketing', 'Iqtisodiyot',
                           'Buxgalteriya hisobi va audit', ], 'Jismoniy madaniyat': ['Sport faoliyati (kurash)',
                                                                                     'Sport faoliyati (futbol)',
                                                                                     'Sport faoliyati (xotin-qizlar sporti yo‘nalishi bo‘yicha)',
                                                                                     'Jismoniy madaniyat yo`nalishi',
                                                                                     'Tuproqshunoslik',
                                                                                     'Sabzavotchilik, polizchilik va kartoshkachilik',
                                                                                     ],
               'Kimyoviy texnologiyalar': [
                   'Yengil sanoat texnologiyalari va jihozlari (ishlab chiqarish turlari bo‘yicha)',
                   'Yengil sanoat buyumlari konstruksiyasini ishlash va texnologiyasi (ishlab chiqarish turlari bo‘yicha)',
                   'Oziq-ovqat texnologiyasi (mahsulot turlari bo‘yicha)',
                   'Kimyoviy texnologiya (ishlab chiqarish turlari bo‘yicha)'],
               'Texnika': ['Transport vositalari muhandisligi (turlari bo‘yicha)',
                           'Shahar qurilishi hamda kommunal infratuzilmani tashkil etish va boshqarish',
                           'Qurilish muhandisligi: qurilish materiallari, buyumlari va konstruksiyalarini ishlab chiqarish',
                           'Qurilish muhandisligi: bino va inshootlar qurilishi',
                           'Madaniy meros ob’yektlarini asrash',
                           'Elektr texnikasi, elektr mexanikasi va elektr texnologiyalari (tarmoqlar bo‘yicha)',
                           'Elektr energetikasi (tarmoqlar va yo‘nalishlar  bo‘yicha)',
                           'Avtomobilsozlik va traktorsozlik',
                           'Arxitektura (turlari bo‘yicha)']
               }

label = Label(oyna, text="Urganch davlat universiteti", font=14)
label.grid(row=0, column=0, sticky="w", padx=20, pady=20)

fakultet = ttk.Combobox(oyna, values=list(fakultetlar.keys()), width=25, height=2, font=14)
fakultet.set("Fakultetlar")
fakultet.bind("<<ComboboxSelected>>", fakultet_select)
fakultet.grid(row=0, column=0, sticky="w", padx=290, pady=20)

yonalish = ttk.Combobox(oyna, font=14, width=25, height=2)
yonalish.set("Yo'nalishingiz")
yonalish.grid(row=0, column=0, sticky="w", padx=650, pady=20)

tuzuvchi_lab = Label(oyna, text="Tuzuvchi", font=14, )
tuzuvchi_lab.grid(row=5, column=0, sticky="w", padx=20, pady=100)

tuzuvchi = Text(oyna, width=50, height=2, font=14)
tuzuvchi.grid(row=5, column=0, sticky="w", padx=200, pady=100)

bilet_lab = Label(oyna, text="Bilet soni ", font=14, )
bilet_lab.grid(row=7, column=0, sticky="w", pady=40, padx=20)

bilet_soni = Text(oyna, width=22, height=1, font=14)
bilet_soni.grid(row=7, column=0, sticky="w", padx=200, pady=40)

nazaria_lab = Label(oyna, text="Nazaria soni ", font=14, )
nazaria_lab.grid(row=9, column=0, sticky="w", pady=40, padx=20)

nazaria = Text(oyna, width=22, height=1, font=14)
nazaria.grid(row=9, column=0, sticky="w", padx=200, pady=40)


def nazaria_fayli_joyi():
    global nazaria_joyi
    filename_nazar = askopenfilename(filetypes=[('TextFiles', '*txt')])
    if filename_nazar:
        nazaria_joyi = filename_nazar
        nazaria_savol_fayli.config(text=filename_nazar)

    else:
        messagebox.showerror(title="Xatolik", message="Faylni ko'rsating")


nazaria_savol_fayli = Button(oyna, text="Faylni korsating", font=14, bd=7, activebackground="#00FFFF",
                             command=nazaria_fayli_joyi)
nazaria_savol_fayli.grid(row=9, column=0, sticky="w", padx=500, ipadx=35, )

qiyin_lab = Label(oyna, text="Qiyin savol soni ", font=14, )
qiyin_lab.grid(row=11, column=0, sticky="w", pady=40, padx=20)

qiyin = Text(oyna, width=22, height=1, font=14)
qiyin.grid(row=11, column=0, sticky="w", padx=200, pady=40)


def qiyin_fayl_joyi():
    global qiyin_joyi
    filename = askopenfilename(filetypes=[('TextFiles', '*txt')])
    if filename:
        qiyin_joyi = filename
        qiyin_savol_fayli.config(text=filename)

    else:
        messagebox.showerror(title="Xatolik", message="Faylni ko'rsating")


qiyin_savol_fayli = Button(oyna, text="Faylni korsating", font=14, bd=7, activebackground="#00FFFF",
                           command=qiyin_fayl_joyi)
qiyin_savol_fayli.grid(row=11, column=0, sticky="w", padx=500, ipadx=35, )

oson_lab = Label(oyna, text="Oson savol soni", font=14, )
oson_lab.grid(row=13, column=0, sticky="w", pady=40, padx=20)

oson = Text(oyna, width=22, height=1, font=14)
oson.grid(row=13, column=0, sticky="w", padx=200, pady=40)


def oson_fayl_joyi():
    global oson_joyi
    filename_oson = askopenfilename(filetypes=[('TextFiles', '*txt')])
    if filename_oson:
        oson_joyi = filename_oson
        oson_soni_fayl.config(text=filename_oson)

    else:
        messagebox.showerror(title="Xatolik", message="Faylni ko'rsating")


oson_soni_fayl = Button(oyna, text="Faylni korsating", font=14, bd=7, activebackground="#00FFFF",
                        command=oson_fayl_joyi)
oson_soni_fayl.grid(row=13, column=0, sticky="w", padx=500, ipadx=35)


def bilet_tuz():
    global oson_joyi
    global qiyin_joyi
    global nazaria_joyi

    tuzuvchi_odam = tuzuvchi.get("1.0", END)
    nazaria_savol = []
    qiyin_savol = []
    oson_savol = []
    n_soni = int(nazaria.get("1.0", END))
    q_soni = int(qiyin.get("1.0", END))
    o_soni = int(oson.get("1.0", END))
    s = int(bilet_soni.get("1.0", END))
    try:
        with open(oson_joyi, "r", encoding="utf-8") as k1:
            for k in k1:
                oson_savol.append(k)
        with open(nazaria_joyi, "r", encoding="utf-8") as n:
            for j in n:
                nazaria_savol.append(j)
        with open(qiyin_joyi, "r", encoding="utf-8") as n1:
            for d in n1:
                qiyin_savol.append(d)

        file1 = filedialog.asksaveasfilename(defaultextension='.txt')
        raqami = 1
        with open(file1, "a", encoding="utf-8") as file2:
            for i in range(1, s + 1):
                file2.write(
                    f"   Urganch Davlat Universitett  {fakultet.get()}  {yonalish.get()}\n\n          {i}-bilet\n")
                # if n_soni == NONE:
                #     messagebox.showerror(title="Xatolik", message="Nazariani sonini kiritmadingiz")
                # else:
                for j in range(0, n_soni):

                    nazar = nazaria_savol
                    file2.write(f"\n       {raqami}  {nazar}\n")
                    raqami += 1



                for u in range(q_soni):
                    savolson1 = 0
                    qiyn = qiyin_savol[savolson1]
                    file2.write(f"\n       {raqami} {qiyn}\n")
                    raqami += 1
                    savolson1 += 1
                    if len(nazaria_savol) - 1 == savolson1:
                        savolson1 = 0
                for e in range(o_soni):
                    savolson2 = 0
                    osn = oson_savol[savolson2]
                    file2.write(f"\n       {raqami}  {osn}\n")
                    raqami += 1
                    savolson2 += 1
                    if len(nazaria_savol) - 1 == savolson2:
                        savolson2 = 0

                raqami = 1
                file2.write(f"\n\n      Tuzuvchi : {tuzuvchi_odam}\n")
            messagebox.showinfo(title="Yaratildi", message="Bilet muvaffaqiyatli tuzildi")
    except EXCEPTION as eror:
        print(eror)


tuzish = Button(oyna, text="Tuzish", font=14, bd=7, activebackground="#00FFFF", command=bilet_tuz)
tuzish.grid(row=13, column=0, sticky="w", padx=850, ipadx=15)


def tozala():
    mes = messagebox.askyesno(title="Exit", message="Chiqishni hohlaysizmi")
    if mes == True:
        oyna.withdraw()
        StopAsyncIteration(exit(oyna))


close = Button(oyna, text="Close", font=14, bd=7, activebackground="#00FFFF", command=tozala)
close.grid(row=11, column=0, sticky="w", padx=850, ipadx=15)

oyna.mainloop()
