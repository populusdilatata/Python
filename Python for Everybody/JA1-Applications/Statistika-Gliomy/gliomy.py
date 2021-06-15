# -*- coding: utf-8 -*-
from Tkinter import *
import Tix
import tkFileDialog
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import xlwt
import grafy
import testy
import os



class interface:
    def __init__(self, master):
        self.top=''
        self.fr = Frame(master, relief="sunken", borderwidth=2)
        self.uvodni_slovo1=Label(self.fr, text="Vítejte.", justify="left", font=20)
        self.uvodni_slovo1.pack()
        self.uvodni_slovo2=Label(self.fr, text="Tento program byl vytvořen pro lékařské účely. Statisticky zpracovává a vyhodnocuje data pacientů \ns maligními mozkovými nádory. Funkce programu se zpřístupní po načtení odpovídající databáze. \nVeškeré potřebné informace naleznete v záložce Nápověda, sekce Manuál.", justify="left")
        self.uvodni_slovo2.pack()
        self.photo = PhotoImage(file="Button/Nacist.gif")
        self.bu = Button(self.fr, image=self.photo, command=self.nacist)
        self.fr.master.title("Načtení")
        self.fr.pack()
        self.bu.pack(padx=32, pady=32, anchor=S)
########MENU########
        self.menubar = Menu(master)
        
        self.cascmenu = Menu(self.menubar, tearoff=0)
        ##    self.cascmenu.add_command(label="Volba 1", underline=6, command=self.nic) 
        ##    self.cascmenu.add_command(label="Volba 2", underline=6, state="disabled", command=self.nic) 

        self.filemenu = Menu(self.menubar, tearoff=0)
        #self.filemenu.add_cascade(label="Kaskada... ", underline=0, menu=self.cascmenu)
        self.filemenu.add_command(label="Exit", underline=0, command=master.quit)
        self.menubar.add_cascade(label="Soubor", menu=self.filemenu)

        self.editmenu = Menu(self.menubar, tearoff=0)
        self.editmenu.add_command(label=u"Explorační analýza", state="disabled", command=self.explorace)
        self.cascmenu.add_command(label=u"Oblasti MS kraje", command=self.median_MS_kraj)
        self.cascmenu.add_command(label=u"Ostrava", command=self.median_Ostrava)
        self.cascmenu.add_command(label=u"Opava", command=self.median_Opava)
        self.editmenu.add_cascade(label=u"Výběrový medián", state="disabled", menu=self.cascmenu)
        self.menubar.add_cascade(label="Statistika", menu=self.editmenu)

        self.helpmenu=Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label='Manuál', command=self.manual)
        self.helpmenu.add_separator()
        self.helpmenu.add_command(label='O programu...', command=self.oprogramu)
        self.menubar.add_cascade(label='Nápověda', menu=self.helpmenu)
        
        master.title("Gliomy")
        master.config(menu=self.menubar)

    def oprogramu(self):
        self.oprogramu_okno=Toplevel()
        self.oprogramu_okno.title("O programu")
        self.oprogramu_la= Label(self.oprogramu_okno, text=u"Autor: Žaneta Miklová \nVerze: Python v2.7 \nRok: 2012", justify=LEFT)
        self.oprogramu_la.pack(expand=1, padx=4, pady=4, fill="both")

    def median_Ostrava(self):
        self.med_zalozky=self.soubor.sheet_names()
        med_seznam_kat=[]
        sh=self.soubor.sheet_by_name(self.med_zalozky[0])
        for col in range(sh.ncols): #vytvori seznam kategorii
            med_seznam_kat.append(sh.col_values(col)[0])
        del med_seznam_kat[0:13]
        del med_seznam_kat[(len(med_seznam_kat)-1)]
        del med_seznam_kat[(len(med_seznam_kat)-1)]
        self.median_Ostrava_okno=Toplevel()
        self.median_Ostrava_okno.title("Výběrový medián MS kraje")
        self.levy_median_Ostrava_okno=LabelFrame(self.median_Ostrava_okno, text="Vyberte onemocnění")
        self.med_Ostrava_li1 = Listbox(self.levy_median_Ostrava_okno, width=30, height=10)
        self.med_Ostrava_sy1 = Scrollbar(self.levy_median_Ostrava_okno, orient="vertical", command=self.med_Ostrava_li1.yview)  
        self.med_Ostrava_la1 = Label(self.levy_median_Ostrava_okno, text=u"Není vybrana žádná kategorie", foreground="red")
        self.med_Ostrava_li1.configure(yscrollcommand=self.med_Ostrava_sy1.set)
        med_seznam_mest=[]
        for polozka in med_seznam_kat:
            self.med_Ostrava_li1.insert(END, polozka)
        
        self.med_Ostrava_li1.grid(row=0, column=0, padx=4, pady=4)
        self.med_Ostrava_sy1.grid(row=0, column=1, sticky="ns", pady=4, padx=2)
        self.med_Ostrava_la1.grid(row=1, column=0, columnspan=2)
        self.med_Ostrava_li1.bind("<Double-B1-ButtonRelease>", self.med_Ostrava_li_double)
        self.kategorie_med=''
        self.levy_median_Ostrava_okno.pack(padx=2, pady=2, expand=1, fill=BOTH, anchor=W, side="left")
        self.pravy_median_Ostrava_okno=Frame(self.median_Ostrava_okno)
        self.bu_med_Ostrava_vypis=Button(self.pravy_median_Ostrava_okno, text=u"Výpis", height=1, width=13, command=self.med_Ostrava_vypis)
        self.bu_med_Ostrava_vypis.pack(padx=2, pady=2, fill=BOTH, anchor=NE)
        self.bu_med_Ostrava_export=Button(self.pravy_median_Ostrava_okno, text=u"Export do excelu", height=1, width=13, command=self.export_Ostrava)
        self.bu_med_Ostrava_export.pack(padx=2, pady=2, fill=BOTH, anchor=SE)
        self.pravy_median_Ostrava_okno.pack(padx=4, pady=4, expand=1, fill=BOTH, anchor=E, side="right")

    def median_Opava(self):
        self.med_zalozky=self.soubor.sheet_names()
        med_seznam_kat=[]
        sh=self.soubor.sheet_by_name(self.med_zalozky[0])
        for col in range(sh.ncols): #vytvori seznam kategorii
            med_seznam_kat.append(sh.col_values(col)[0])
        del med_seznam_kat[0:13]
        del med_seznam_kat[(len(med_seznam_kat)-1)]
        del med_seznam_kat[(len(med_seznam_kat)-1)]
        self.median_Opava_okno=Toplevel()
        self.median_Opava_okno.title("Výběrový medián MS kraje")
        self.levy_median_Opava_okno=LabelFrame(self.median_Opava_okno, text="Vyberte onemocnění")
        self.med_Opava_li1 = Listbox(self.levy_median_Opava_okno, width=30, height=10)
        self.med_Opava_sy1 = Scrollbar(self.levy_median_Opava_okno, orient="vertical", command=self.med_Opava_li1.yview)  
        self.med_Opava_la1 = Label(self.levy_median_Opava_okno, text=u"Není vybrana žádná kategorie", foreground="red")
        self.med_Opava_li1.configure(yscrollcommand=self.med_Opava_sy1.set)
        med_seznam_mest=[]
        for polozka in med_seznam_kat:
            self.med_Opava_li1.insert(END, polozka)
        
        self.med_Opava_li1.grid(row=0, column=0, padx=4, pady=4)
        self.med_Opava_sy1.grid(row=0, column=1, sticky="ns", pady=4, padx=2)
        self.med_Opava_la1.grid(row=1, column=0, columnspan=2)
        self.med_Opava_li1.bind("<Double-B1-ButtonRelease>", self.med_Opava_li_double)
        self.kategorie_med=''
        self.levy_median_Opava_okno.pack(padx=2, pady=2, expand=1, fill=BOTH, anchor=W, side="left")
        self.pravy_median_Opava_okno=Frame(self.median_Opava_okno)
        self.bu_med_Opava_vypis=Button(self.pravy_median_Opava_okno, text=u"Výpis", height=1, width=13, command=self.med_Opava_vypis)
        self.bu_med_Opava_vypis.pack(padx=2, pady=2, fill=BOTH, anchor=NE)
        self.bu_med_Opava_export=Button(self.pravy_median_Opava_okno, text=u"Export do excelu", height=1, width=13, command=self.export_Opava)
        self.bu_med_Opava_export.pack(padx=2, pady=2, fill=BOTH, anchor=SE)
        self.pravy_median_Opava_okno.pack(padx=4, pady=4, expand=1, fill=BOTH, anchor=E, side="right")

    def med_Opava_vypis(self):
        self.med_vypis("Opava", "ne")

    def export_Opava(self):
        self.med_vypis("Opava", "export")


    def med_Ostrava_vypis(self):
        self.med_vypis("Ostrava", "ne")

    def export_Ostrava(self):
        self.med_vypis("Ostrava", "export")

    def export_MS(self):
        self.med_vypis("MS", "export")

    def median_MS_kraj(self):
        self.med_zalozky=self.soubor.sheet_names()
        med_seznam_kat=[]
        sh=self.soubor.sheet_by_name(self.med_zalozky[0])
        for col in range(sh.ncols): #vytvori seznam kategorii
            med_seznam_kat.append(sh.col_values(col)[0])
        del med_seznam_kat[0:13]
        del med_seznam_kat[(len(med_seznam_kat)-1)]
        del med_seznam_kat[(len(med_seznam_kat)-1)]
        self.median_okno=Toplevel()
        self.median_okno.title("Výběrový medián MS kraje")
        self.levy_median_okno=LabelFrame(self.median_okno, text="Vyberte onemocnění")
        self.med_li1 = Listbox(self.levy_median_okno, width=30, height=10)
        self.med_sy1 = Scrollbar(self.levy_median_okno, orient="vertical", command=self.med_li1.yview)  
        self.med_la1 = Label(self.levy_median_okno, text=u"Není vybrana žádná kategorie", foreground="red")
        self.med_li1.configure(yscrollcommand=self.med_sy1.set)
        med_seznam_mest=[]
        for polozka in med_seznam_kat:
            self.med_li1.insert(END, polozka)
        
        self.med_li1.grid(row=0, column=0, padx=4, pady=4)
        self.med_sy1.grid(row=0, column=1, sticky="ns", pady=4, padx=2)
        self.med_la1.grid(row=1, column=0, columnspan=2)
        self.med_li1.bind("<Double-B1-ButtonRelease>", self.med_li_double)
        self.kategorie_med=''
        self.levy_median_okno.pack(padx=2, pady=2, expand=1, fill=BOTH, anchor=W, side="left")
        self.pravy_median_okno=Frame(self.median_okno)
        self.bu_med_vypis=Button(self.pravy_median_okno, text=u"Výpis", height=1, width=13, command=self.med_vypis)
        self.bu_med_vypis.pack(padx=2, pady=2, fill=BOTH, anchor=NE)
        self.bu_med_export=Button(self.pravy_median_okno, text=u"Export do excelu", height=1, width=13, command=self.export_MS)
        self.bu_med_export.pack(padx=2, pady=2, fill=BOTH, anchor=SE)
        self.pravy_median_okno.pack(padx=4, pady=4, expand=1, fill=BOTH, anchor=E, side="right")

    def med_vypis(self, median="MS", exportuji="ne"):
        sh=self.soubor.sheet_by_name(self.med_zalozky[0])
        seznam_mest_data={}
        seznam_mest_median={}
        if self.kategorie_med=="":
            return
        else:
            data=[]
            for col in range(sh.ncols): #zjisti cislo sloupce na zaklade ziskane hodnoty jmena
                if sh.col_values(col)[0]==self.kategorie_med:
                    zalozka1=col
            if median=="MS":
                for row in range(sh.nrows):
                    if seznam_mest_data.has_key(sh.row_values(row)[6]):
                        if grafy.is_number(sh.row_values(row)[zalozka1])==True:
                            seznam_mest_data[sh.row_values(row)[6]].append(sh.row_values(row)[zalozka1])
                    else:
                        if grafy.is_number(sh.row_values(row)[zalozka1])==True:
                            seznam_mest_data[sh.row_values(row)[6]]=[sh.row_values(row)[zalozka1]]
            elif median=="Ostrava":
                for row in range(sh.nrows):
                    if sh.row_values(row)[6]=="Ostrava":
                        if seznam_mest_data.has_key(sh.row_values(row)[5]):
                            if grafy.is_number(sh.row_values(row)[zalozka1])==True:
                                seznam_mest_data[sh.row_values(row)[5]].append(sh.row_values(row)[zalozka1])
                        else:
                            if grafy.is_number(sh.row_values(row)[zalozka1])==True:
                                seznam_mest_data[sh.row_values(row)[5]]=[sh.row_values(row)[zalozka1]]
            elif median=="Opava":
                for row in range(sh.nrows):
                    if sh.row_values(row)[6]=="Opava":
                        if seznam_mest_data.has_key(sh.row_values(row)[5]):
                            if grafy.is_number(sh.row_values(row)[zalozka1])==True:
                                seznam_mest_data[sh.row_values(row)[5]].append(sh.row_values(row)[zalozka1])
                        else:
                            if grafy.is_number(sh.row_values(row)[zalozka1])==True:
                                seznam_mest_data[sh.row_values(row)[5]]=[sh.row_values(row)[zalozka1]]
            #print seznam_mest_data
            for mesto in seznam_mest_data.keys():
                if len(seznam_mest_data[mesto])>=2:
                    seznam_mest_median[mesto]=testy.median(seznam_mest_data[mesto])
            mesta=seznam_mest_median.keys()
            mesta.sort()
            if exportuji=="ne":
                self.oznameni_med_mesta=Toplevel()
                self.oznameni_med_mesta.title(u"Výběrový medián " + self.kategorie_med)
                self.txt_median_mesta=Text(self.oznameni_med_mesta, width=100, height=20)
                self.scrol_median_mesta=Scrollbar(self.oznameni_med_mesta)
                self.scrol_median_mesta.pack(side=RIGHT, fill=Y)
                self.txt_median_mesta.pack(expand=1, fill=BOTH)
                self.txt_median_mesta.focus_set()
                self.scrol_median_mesta.config(command=self.txt_median_mesta.yview)
                self.txt_median_mesta.config(yscrollcommand=self.scrol_median_mesta.set)
                self.txt_median_mesta.delete(1.0, END)
                self.txt_median_mesta.insert(END, u"Výběrové mediány:", "nadpis")
                self.txt_median_mesta.insert(END, "\n", "text")
                self.txt_median_mesta.insert(END, "\n", "text")
                for mesto in mesta:
                    self.txt_median_mesta.insert(END, mesto+": ", "text")
                    self.txt_median_mesta.insert(END, seznam_mest_median[mesto], "text")
                    self.txt_median_mesta.insert(END, "\n", "text")
                if mesta==[]:
                    self.txt_median_mesta.insert(END, u"Není splněn dostatečný rozsah výběru ani pro jednu oblast.", "text")
                self.txt_median_mesta.tag_config("podnadpis", underline=1, font="Arial 10 bold")
                self.txt_median_mesta.tag_config("nadpis", underline=1, font="Arial 13 bold")
                self.txt_median_mesta.tag_config("text", font="Arial 10")
                self.txt_median_mesta.config(state=DISABLED)
                self.txt_median_mesta.pack()
            else:
                wbk=xlwt.Workbook()
                sheet=wbk.add_sheet("sheet 1")
                sheet.write(0,0, self.kategorie_med)
                sheet.write(1,0, u"OBLAST")
                sheet.write(1,1, u"MEDIÁN [%]")
                i=2
                for mesto in mesta:
                    sheet.write(i,0, mesto)
                    sheet.write(i,1, seznam_mest_median[mesto])
                    i=i+1
                loadfile = tkFileDialog.askdirectory(initialdir="/", title=u"Zvolte cílovou složku")
                wbk.save(loadfile+"/median_"+median+".xls")
            
            
      
 
    def nic(self):
        pass

    def nacist(self):
        loadfile = tkFileDialog.askopenfilename(title='Vyberte soubor .xls', filetypes=[('Text Files','*.xls'),('Python Files','*.py'),('All Files','*')], defaultextension='.xls', initialdir='.')
        if loadfile!='':
            self.soubor=xlrd.open_workbook(loadfile)
            self.editmenu.entryconfig(0,state=NORMAL)
            self.editmenu.entryconfig(1,state=NORMAL)
            self.bu.pack_forget()
            self.testovani()

    def manual(self):
        self.manual_okno=Toplevel()
        self.manual_okno.title("Manuál")
        self.fr_tlacitka_manual=Frame(self.manual_okno)
        self.photo8 = PhotoImage(file="Button/uvod.gif")
        self.photo9 = PhotoImage(file="Button/jednovyberovy_test.gif")
        self.photo10 = PhotoImage(file="Button/dvouvyberovy_test.gif")
        self.photo11 = PhotoImage(file="Button/vicevyberovy_test.gif")
        self.photo12 = PhotoImage(file="Button/testy_normality.gif")
        self.photo13 = PhotoImage(file="Button/o_typu_roz.gif")
        self.photo14 = PhotoImage(file="Button/explorace.gif")
        self.photo15 = PhotoImage(file="Button/format.gif")
        self.bu_man8=Button(self.fr_tlacitka_manual, image=self.photo8, command=self.uvod_manual)
        self.bu_man8.pack(padx=4, pady=4, anchor=N)
        self.bu_man15=Button(self.fr_tlacitka_manual, image=self.photo15, command=self.format_dat)
        self.bu_man15.pack(padx=4, pady=4, anchor=N)
        self.bu_man9=Button(self.fr_tlacitka_manual, image=self.photo9, command=self.jednovyberove_manual)
        self.bu_man9.pack(padx=4, pady=4, anchor=N)
        self.bu_man10=Button(self.fr_tlacitka_manual, image=self.photo10, command=self.dvouvyberove_manual)
        self.bu_man10.pack(padx=4, pady=4, anchor=N)
        self.bu_man11=Button(self.fr_tlacitka_manual, image=self.photo11, command=self.vicevyberove_manual)
        self.bu_man11.pack(padx=4, pady=4, anchor=N)
        self.bu_man12=Button(self.fr_tlacitka_manual, image=self.photo12, command=self.testy_normality_manual)
        self.bu_man12.pack(padx=4, pady=4, anchor=N)
        self.bu_man13=Button(self.fr_tlacitka_manual, image=self.photo13, command=self.exponencialni_manual)
        self.bu_man13.pack(padx=4, pady=4, anchor=N)
        self.bu_man14=Button(self.fr_tlacitka_manual, image=self.photo14, command=self.exploracni_manual)
        self.bu_man14.pack(padx=4, pady=4, anchor=N)
        self.fr_tlacitka_manual.pack(fill="both", expand=1, side="left", anchor=W)
        self.fr_pravy_manual=Frame(self.manual_okno)
        self.text_manual=Text(self.fr_pravy_manual, width=150, height=40)
        self.scrol_manual=Scrollbar(self.fr_pravy_manual)
        self.scrol_manual.pack(side=RIGHT, fill=Y)
        self.text_manual.focus_set()
        self.scrol_manual.config(command=self.text_manual.yview)
        self.text_manual.config(yscrollcommand=self.scrol_manual.set)
        self.text_manual.delete(1.0, END)
        self.text_manual.insert(END, u"  ÚVOD"  , "nadpis")
        self.text_manual.insert(END, u"\n", "text")
        self.text_manual.insert(END, u"   V úvodním oknu nalezneme pod uvítacím textem tlačítko pro načtení dat ze souboru *.xls. Po načtení databáze se vám \nzpřístupní statististické metody. Protože program se hlavně zaměřuje na neparametrické testy, jako první uvidíme v hlavním okně nabídku těchto testů. Dále se nám zpřístupní explorační analýza, kterou najdeme v záložce Statistika, sekce Explorační analýza.\n\n", "text")
        self.text_manual.insert(END, u"   Jak správně zvolit alternativu Ha?", "podnadpis")
        self.text_manual.insert(END, u"\n", "text")
        self.text_manual.insert(END, u"   Na výběr máte zpravidla tři alternativy, a to dvě jednostranné (\u03BC<\u03BC0 nebo \u03BC>\u03BC0) a jednu oboustrannou (\u03BC\u2260\u03BC0). Alternativní \nhypotéza by měla být v souladu s výběrovým souborem, tzn. přizpůsobujeme  alternativní hypotézu závěrům získaným \nz výběrového souboru. Např. pokud budete chtít testovat, že medián je roven 80 a zjistíte, že výběrový medián je roven 15, pak \nbyste měli zvolit alternativu ve tvaru \u03BC<80 (tedy \u03BC<\u03BC0) nebo \u03BC\u226080 (tedy \u03BC\u2260\u03BC0).", "text")
        self.text_manual.config(state=DISABLED)
        self.text_manual.tag_config("podnadpis", underline=1, font="Arial 10 bold")
        self.text_manual.tag_config("nadpis", underline=1, font="Arial 13 bold")
        self.text_manual.tag_config("text", font="Arial 10")
        self.text_manual.pack()
        self.fr_pravy_manual.pack(fill="both", expand=1, side="right", anchor=E)

    def uvod_manual(self):
        self.text_manual.config(state=NORMAL)
        self.text_manual.delete(1.0, END)
        self.text_manual.insert(END, u"  ÚVOD"  , "nadpis")
        self.text_manual.insert(END, u"\n", "text")
        self.text_manual.insert(END, u"   V úvodním oknu nalezneme pod uvítacím textem tlačítko pro načtení dat ze souboru *.xls. Po načtení databáze se vám \nzpřístupní statististické metody. Protože program se hlavně zaměřuje na neparametrické testy, jako první uvidíme v hlavním okně nabídku těchto testů. Dále se nám zpřístupní explorační analýza, kterou najdeme v záložce Statistika, sekce Explorační analýza.\n\n", "text")
        self.text_manual.insert(END, u"   Jak správně zvolit alternativu Ha?", "podnadpis")
        self.text_manual.insert(END, u"\n", "text")
        self.text_manual.insert(END, u"   Na výběr máte zpravidla tři alternativy, a to dvě jednostranné (\u03BC<\u03BC0 nebo \u03BC>\u03BC0) a jednu oboustrannou (\u03BC\u2260\u03BC0). Alternativní \nhypotéza by měla být v souladu s výběrovým souborem, tzn. přizpůsobujeme  alternativní hypotézu závěrům získaným \nz výběrového souboru. Např. pokud budete chtít testovat, že medián je roven 80 a zjistíte, že výběrový medián je roven 15, pak \nbyste měli zvolit alternativu ve tvaru \u03BC<80 (tedy \u03BC<\u03BC0) nebo \u03BC\u226080 (tedy \u03BC\u2260\u03BC0).", "text")
        self.text_manual.tag_config("podnadpis", underline=1, font="Arial 10 bold")
        self.text_manual.tag_config("nadpis", underline=1, font="Arial 13 bold")
        self.text_manual.tag_config("text", font="Arial 10")
        self.text_manual.config(state=DISABLED)

    def format_dat(self):
        self.text_manual.config(state=NORMAL)
        self.text_manual.delete(1.0, END)
        self.text_manual.insert(END, u"  FORMÁT DAT"  , "nadpis")
        self.text_manual.insert(END, u"\n", "text")
        self.text_manual.insert(END, u"   Důležitým upozorněním je, aby data v souboru byla správná a nedocházelo k překlepům (včetně velikosti písma) nebo označení stejného prvku různýmy jmény. \n\n", "text")
        self.text_manual.insert(END, u"   Jak by měla data vypadat?\n", "podnadpis")
        self.text_manual.insert(END, u"   V souboru *.xls by měla být data uspořádána následovně (záložky a sloupce v záložkách):\n", "text")
        self.text_manual.insert(END, u"   1. Cytogenetika MS kraje\n       1. Pořadí\n       2. Příjmení a jméno\n       3. Pohlaví\n       4. Věk\n       5. Rodné číslo\n       6. Městská čtvrť\n       7. Okres\n       8. Ulice\n       9. Hlavní zaměstnání\n       10. Datum\n       11. Datum diagnózy gliomu\n       12. Datum úmrtí\n       13. Dg-cytogenetic\n       14. V dalších sloupcích jednotlivé nemoci\n       15. V předpodledním sloupci: Polyzomia\n       16. V posledním sloupci: Poznámky\n", "text")
        self.text_manual.insert(END, u"   2. Cytogenetika bez vyšetření\n       1. Pořadí\n       2. Příjmení a jméno\n       3. Pohlaví\n       4. Věk\n       5. Bydliště\n       6. Obvod\n       7. Ulice\n       8. Hlavní zaměstnání\n       9. Poznámky\n", "text")
        self.text_manual.insert(END, u"   3. Cytogenetika mimo MS kraj\n       1. Pořadí\n       2. Příjmení a jméno\n       4. Pohlaví\n       5. Věk\n       6. Bydliště\n       7. Obvod\n       8. Ulice\n       9. Číslo popisné\n       10. Hlavní zaměstnání\n       11. Dg-cytogenetic\n       12. V dalších sloupcích následují jednotlivé nemoci, Polyzomia a Poznámky\n", "text")
        self.text_manual.insert(END, u"   4. MS - regionální tabulka\n       1. Okresní oblasti MS kraje\n       2. Počet obyvatel\n       3. Počet nemocných\n       4. Absolutní počet mutací\n       5. V dalších sloupcích četnosti jednotlivých nemocí\n", "text")
        self.text_manual.insert(END, u"   5. Ostrava\n       1. Obdody\n       2. Počet obyvatel\n       3. Počet nemocných\n", "text")
        self.text_manual.insert(END, u"   5. Opava\n       1. Obdody\n       2. Počet obyvatel\n       3. Počet nemocných\n", "text")
        self.text_manual.tag_config("podnadpis", underline=1, font="Arial 10 bold")
        self.text_manual.tag_config("nadpis", underline=1, font="Arial 13 bold")
        self.text_manual.tag_config("text", font="Arial 10")
        self.text_manual.config(state=DISABLED)
        
    def jednovyberove_manual(self):
        self.text_manual.config(state=NORMAL)
        self.text_manual.delete(1.0, END)
        self.text_manual.insert(END, u"  JEDNOVÝBĚROVÉ TESTY"  , "nadpis")
        self.text_manual.insert(END, u"\n", "text")
        self.text_manual.insert(END, u"   Podle počtu šetřených výběrů rozdělujeme testy na jednovýběrové, dvouvýběrové a vícevýběrové. Jednovýběrové testy testují \npouze jeden výběr.\n\n", "text")
        self.text_manual.insert(END, u"   Znaménkový test\n", "podnadpis")
        self.text_manual.insert(END, u"   Tento test vám umožní testovat medián konkrétní nemoci. \n   1. Zvolte dvojklikem typ nemoci ze seznamu (pod seznamem se objeví váš výběr).\n   2. Zvolte hladinu významnosti \u03B1.\n   3. Zvolte testovaný medián. Vzhledem k tomu, že výběr je v %, zvolte hodnotu 0-100. \n   4. Zvolte alternativní hypotézu podle doporučení uvedeného v úvodu.\n\n", "text")
        self.text_manual.insert(END, u"   Pokud nezadáte všechny tyto potřebné údaje, test se nespustí. Pokud vše ale zadáte správně, otevře se okno s vyhodnocením \ntestu. V oknu uvidíte přehled zvolených parametrů a vypočtené hodnoty, na základě kterých se zformuluje závěr testu. Níže pak \nnásleduje slovní popis toho, zda byla hypotéza H0 zamítnuta nebo ne. Pro přehled je zde také uveden intervalový a bodový odhad mediánu, abyste se případně pak rozhodli pro správnou volbu alternativy, pokud jste tak již neučinili.\n\n", "text")
        self.text_manual.insert(END, u"   Wilcoxonův test\n", "podnadpis")
        self.text_manual.insert(END, u"   Tento test vám umožní testovat medián konkrétní nemoci. \n   1. Zvolte dvojklikem typ nemoci ze seznamu (pod seznamem se objeví váš výběr).\n   2. Zvolte hladinu významnosti \u03B1.\n   3. Zvolte testovaný medián. Vzhledem k tomu, že výběr je v %, zvolte hodnotu 0-100. \n   4. Zvolte alternativní hypotézu podle doporučení uvedeného v úvodu.\n\n", "text")
        self.text_manual.insert(END, u"   Pokud nezadáte všechny tyto potřebné údaje, test se nespustí. Pokud vše ale zadáte správně, otevře se okno s vyhodnocením \ntestu. V oknu uvidíte přehled zvolených parametrů a vypočtené hodnoty, na základě kterých se zformuluje závěr testu. Níže pak \nnásleduje slovní popis toho, zda byla hypotéza H0 zamítnuta nebo ne. Pro přehled je zde také uveden intervalový a bodový odhad mediánu, abyste se případně pak rozhodli pro správnou volbu alternativy, pokud jste tak již neučinili.\n\n", "text")
        self.text_manual.tag_config("podnadpis", underline=1, font="Arial 10 bold")
        self.text_manual.tag_config("nadpis", underline=1, font="Arial 13 bold")
        self.text_manual.tag_config("text", font="Arial 10")
        self.text_manual.config(state=DISABLED)

    def dvouvyberove_manual(self):
        self.text_manual.config(state=NORMAL)
        self.text_manual.delete(1.0, END)
        self.text_manual.insert(END, u"  DVOUVÝBĚROVÉ TESTY"  , "nadpis")
        self.text_manual.insert(END, u"\n", "text")
        self.text_manual.insert(END, u"   Podle počtu šetřených výběrů rozdělujeme testy na jednovýběrové, dvouvýběrové a vícevýběrové. Dvouvýběrové testy testují \nmezi sebou dva výběry.\n\n", "text")
        self.text_manual.insert(END, u"   Mannův-Whitneyův test\n", "podnadpis")
        self.text_manual.insert(END, u"   Tento test vám umožní testovat mediány dvou nemocí. \n   1. Zvolte dvojklikem typ nemoci z prvního seznamu (pod seznamem se objeví váš výběr).\n   2. Zvolte dvojklikem typ nemoci z druhého seznamu (pod seznamem se objeví váš výběr)\n   3. Zvolte hladinu významnosti \u03B1.\n   4. Zvolte alternativní hypotézu podle doporučení uvedeného v úvodu.\n\n", "text")
        self.text_manual.insert(END, u"   Pokud nezadáte všechny tyto potřebné údaje, test se nespustí. Test je založen na předpokladu, že rozsah prvního výběru n1 je menší nebo roven než rozsah druhého výběru n2. Pokud nebude tato podmínka splněna, budete upozorněni zprávou a následně\npak vyzváni, abyste v seznamech tyto výběry prohodili. Pokud vše již bude vpořádku, otevře se okno s vyhodnocením testu. \nV okně uvidíte přehled zvolených parametrů a vypočtené hodnoty, na základě kterých se zformuluje závěr testu. Níže pak \nnásleduje slovní popis toho, zda byla hypotéza H0 zamítnuta nebo ne. Pro přehled je zde také uveden intervalový a bodový odhad mediánu, abyste se případně pak rozhodli pro správnou volbu alternativy, pokud jste tak již neučinili.\n\n", "text")
        self.text_manual.insert(END, u"   Kolomogorovův-Smirnovův test\n", "podnadpis")
        self.text_manual.insert(END, u"   Tento test vám umožní testovat hypotézu, zda dva výběry pochází ze stejného blíže nespecifikovaného výběru. \n\n   Pokud budete mezi sebou testovat dva výběry nemocí:\n   1. Zvolte dvojklikem typ nemoci z prvního seznamu (pod seznamem se objeví váš výběr)\n   2. Vyberte dvojklikem typ nemoci z druhého seznamu (pod seznamem se objeví váš výběr)\n   3. Zvolte hladinu významnosti \u03B1.\n   4. Zvolte alternativní hypotézu podle doporučení uvedeného v úvodu.\n   Pozn. V tomto případě nemusí být vybrány obvody uvedeny v dalších seznamech.\n\n   Pokud budete mezi sebou testovat dva výběry nemocí v rámci konkrétních oblastí:\n   Postup je stejný, ale kromě typu nemoci musíte zvolit dvojklikem i obvody ze seznamu.\n\n", "text")
        self.text_manual.insert(END, u"   Pokud nezadáte všechny tyto potřebné údaje, test se nespustí. Pokud vše ale zadáte správně, otevře se okno s vyhodnocením \ntestu. V oknu uvidíte přehled zvolených parametrů a vypočtené hodnoty, na základě kterých se zformuluje závěr testu. Níže pak \nnásleduje slovní popis toho, zda byla hypotéza H0 zamítnuta nebo ne.\n\n", "text")
        self.text_manual.tag_config("podnadpis", underline=1, font="Arial 10 bold")
        self.text_manual.tag_config("nadpis", underline=1, font="Arial 13 bold")
        self.text_manual.tag_config("text", font="Arial 10")
        self.text_manual.config(state=DISABLED)

    def vicevyberove_manual(self):
        self.text_manual.config(state=NORMAL)
        self.text_manual.delete(1.0, END)
        self.text_manual.insert(END, u"  VÍCEVÝBĚROVÉ TESTY"  , "nadpis")
        self.text_manual.insert(END, u"\n", "text")
        self.text_manual.insert(END, u"   Podle počtu šetřených výběrů rozdělujeme testy na jednovýběrové, dvouvýběrové a vícevýběrové. Vícevýběrové testy testují \nmezi sebou více výběry.\n\n", "text")
        self.text_manual.insert(END, u"   Kruskalův-Wallisův test\n", "podnadpis")
        self.text_manual.insert(END, u"   Tento test vám umožní testovat mediány více výběrů mezi sebou. Jedná se o neparametrickou variantu ANOVY. \n\n", "text")
        self.text_manual.insert(END, u"   Pokud budete chtít testovat mediány v rámci konkrétních nemocí:\n", "text")
        self.text_manual.insert(END, u"       1. Přidávejte pomocí tlačítka Přidej jednotlivé výběry do seznamu. Pokud seznam nebude obsahovat alespoň 2 výběry, test \n           se nespustí a vy budete upozorněni na nedostatečný počet výběrů.\n", "text")
        self.text_manual.insert(END, u"       2. Upravujte seznam výběrů pomocí tlačítek Vymaž a Vymaž vše. \n", "text")
        self.text_manual.insert(END, u"       3. Testujte pomocí tlačítka Testovat. Pokud nebude splněna podmínka, že každý výběr musí mít rozsah alespoň 5, test se  \n           nespustí a vy budete upozorněni na nedostatečný rozsah výběrů.\n\n", "text")
        self.text_manual.insert(END, u"   Pokud budete chtít testovat mediány v různých oblastech v rámci jedné nemoci:\n", "text")
        self.text_manual.insert(END, u"       1. Vyberte nemoc ze seznamu a potvrďte ji tlačítkem se šipkami (pozn. váš výběr se zobrazí zeleně pod tlačítkem se\n           šipkami). V levém dolním seznamu se vám zaktivují možné oblasti pro testování, které již spňují podmínku o rozsahu\n           výběru. Může se stát, že seznam nebude obsahovat dostatečné množství oblastí pro zahájení testu. \n", "text")
        self.text_manual.insert(END, u"       2. viz. body 1. a 2. z předchozího postupu. \n\n", "text")
        self.text_manual.insert(END, u"   Pokud je vše zadáno správně, spustí se vám okno s vyhodnocením testu. V okně uvidíte přehled parametrů, které jste si zvolili \na hodnoty důležité pro zamítnutí nebo nezamítnutí hypotézy H0. Pokud dojde k zamítnutí hypotézy H0, bude provedena Post-hoc analýza, která bude zařazena na konec tohoto testu.", "text")
        self.text_manual.tag_config("podnadpis", underline=1, font="Arial 10 bold")
        self.text_manual.tag_config("nadpis", underline=1, font="Arial 13 bold")
        self.text_manual.tag_config("text", font="Arial 10")
        self.text_manual.config(state=DISABLED)

    def testy_normality_manual(self):
        self.text_manual.config(state=NORMAL)
        self.text_manual.delete(1.0, END)
        self.text_manual.insert(END, u"  TESTY NORMALITY"  , "nadpis")
        self.text_manual.insert(END, u"\n", "text")
        self.text_manual.insert(END, u"   Testují, zda daný výběr pochází z normálního rozdělení.\n\n", "text")
        self.text_manual.insert(END, u"   Kolmogorovův-Smirnovův test\n", "podnadpis")
        self.text_manual.insert(END, u"   Tento test nám umožňuje testovat hypotézu, že daný výběr pochází z normálního rozdělení se střední hodnotou \u03BC \na směrodatnou odchylkou..\n\n", "text")
        self.text_manual.insert(END, u"   Pokud chcete testovat rozdělení typu nemocí:\n      1. Zvolte dvojklikem typ nemoci (pod seznamem se objeví váš výběr).\n      2. Zvolte hladinu významnosti \u03B1.\n      3. Zadejte střední hodnotu \u03BC.\n      4. Zadejte směrodatnou odchylku \u03C3\n\n", "text")
        self.text_manual.insert(END, u"   Pokud chcete testovat rozdělení konkrétního typu onemocnění v konkrétní oblasti, musíte dvojklikem navíc vybrat i oblast (pod \nseznamem se objeví váš výběr).\n\n", "text")
        self.text_manual.insert(END, u"   Pokud se test nespustí, znaména to, že výběr nemá dostatečný rozsah. Jinak se otevře okno s vyhodnocením testu. V okně \nmůžete vidět přehled zvolených parametrů a hodnoty, na základě kterých se buď zamíne nebo nezamítne hypotéza H0. Níže \npotom následuje slovní popis toho, zda byla hypotéza zamítnuta nebo ne.\n\n", "text")
        self.text_manual.insert(END, u"   Test podle špičatosti-šikmosti\n", "podnadpis")
        self.text_manual.insert(END, u"   Test je založen na znalostech o špičatosti a šikmosti normálního rozdělení. Protože šikmost normálního rozdělení je rovna 0 \na špičatost normálního rozdělení je rovna 3, mělo by platit, že výběrová šikmost a výběrová špičatost daného výběru by měli být \nblízké těmto hodnotám.\n\n", "text")
        self.text_manual.insert(END, u"   Pokud chcete testovat typ rozdělení konkrétní nemoci:\n", "text")
        self.text_manual.insert(END, u"      1. Vyberte dvojklikem typ nemoci (pod seznamem se objeví váš výběr).\n", "text")
        self.text_manual.insert(END, u"      2. Vyberte hladinu významnosti \u03B1.\n\n", "text")
        self.text_manual.insert(END, u"   Pokud chcete testovat typ rozdělení konkrétní nemoci v konkrétní oblasti. Vyberte navíc dvojklikem oblast (pod seznamem se \nobjeví váš výběr).\n\n", "text")
        self.text_manual.insert(END, u"   Pokud bude výběr dostatečný, otevře se okno s vyhodnocením testu. V okně uvidíte přehled zadaných parametrů a hodnoty \ndůležité pro vyhodnocení testu. Test je rozdělen do dvou částí, v první se vyhodnocuje normalita na základě špičatosti a v druhé \nna základě šikmosti. Abychom mohli zamítnout hypotézu H0, musí obě dvě části také zamítnout hypotézu H0.", "text")
        self.text_manual.tag_config("podnadpis", underline=1, font="Arial 10 bold")
        self.text_manual.tag_config("nadpis", underline=1, font="Arial 13 bold")
        self.text_manual.tag_config("text", font="Arial 10")
        self.text_manual.config(state=DISABLED)

    def exponencialni_manual(self):
        self.text_manual.config(state=NORMAL)
        self.text_manual.delete(1.0, END)
        self.text_manual.insert(END, u"  TESTY O TYPU ROZDĚLENÍ"  , "nadpis")
        self.text_manual.insert(END, u"\n", "text")
        self.text_manual.insert(END, u"   Testují zda výběr pochází z nějakého konkrétního rozdělení. Tento program se zaměřuje na spojitá rozdělení.\n\n", "text")
        self.text_manual.insert(END, u"   Exponenciální rozdělení\n", "podnadpis")
        self.text_manual.insert(END, u"   Testuje zda daný výběr pochází z exponenciálního rozdělení.\n\n   Pokud chcte testovat hypotézu, že konkrétní nemoc pochází z exponenciálního rozdělení:\n      1. Vyberte dvojklikem typ nemoci (pod seznamem se objeví váš výběr).\n      2. Zvolte hladinu významnosti \u03B1. \n\n   Pokud chcete testovat že konkrétní nemoc v konkrétní oblasti pochází z exponenciálního rozdělení, vyberte navíc dvojklikem \npožadovanou oblast. Protože test počítá jako kritickou hodnotu kvantil chí-kvadrátu rozdělení a tento výpočet je časově náročnější, může testování trvat řádově několik sekund. Prosím vyčkejte a neukončujte program předčasně!!!\n\n", "text")
        self.text_manual.insert(END, u"   Pearsonovo rozdělení\n", "podnadpis")
        self.text_manual.insert(END, u"   Tento test testuje hypotézu, že daný výběr pochází z chí-kvadrátu rozdělení, a to pomocí Kolmogorovova-Smirnovova testu.\n\n", "text")
        self.text_manual.insert(END, u"   Pokud chcete testovat rozdělení v rámci konkrétní nemoci:\n", "text")
        self.text_manual.insert(END, u"       1. Vyberte nemoc ze seznamu (váš výběr se zobrazí pod seznamem).\n", "text")
        self.text_manual.insert(END, u"       2. Vyberte hladinu významnosti \u03B1.\n", "text")
        self.text_manual.insert(END, u"       3. Zvolte počet stupňů volnosti.\n\n", "text")
        self.text_manual.insert(END, u"   Pokud budete chtít testovat rozdělení konkrétní nemoci v konkrétní oblasti, vyberte navíc ještě dvojklikem oblast. Po spuštění \ntestu se vám zobrazí okno s přehledem parametrů, které jste zvolili a s hodnotami důležitými pro vyhodnocení testu. Následuje \npak slovní popis toho, zda byla hypotéza H0 zamítnuta či nikoliv.\n\n", "text")
        self.text_manual.tag_config("podnadpis", underline=1, font="Arial 10 bold")
        self.text_manual.tag_config("nadpis", underline=1, font="Arial 13 bold")
        self.text_manual.tag_config("text", font="Arial 10")
        self.text_manual.config(state=DISABLED)

    def exploracni_manual(self):
        self.text_manual.config(state=NORMAL)
        self.text_manual.delete(1.0, END)
        self.text_manual.insert(END, u"  EXPLORAČNÍ ANALÝZA"  , "nadpis")
        self.text_manual.insert(END, u"\n", "text")
        self.text_manual.insert(END, u"   Program graficky vyhodnocuje základní data. Jsou zde použity histogramy, koláčové grafy a pokud je to možné i krabicové \ngrafy.\n\n", "text")
        self.text_manual.insert(END, u"   Explorační analýzu naleznete v záložce Statistika sekce Explorační analýza (pokud jsou načtena data). Otevře se vám okno, \nkteré je rozděleno do záložek, tak jako tomu je v excelovském dokumentu. \n    1. Vyberte záložku\n    2. V rámečku kategorie vyberte vámi požadovaný výběr.\n    3. Vyberte typ četnosti (relativní nebo absolutní).\n    4. Vyberte typ grafu\n\n   Po stisknutí tlačítka Graf, se vám otevře okno s vygenerovaným grafem. V rámci tohoto okna jsou zde i tlačítka, které umožňují dodatečnou manipulaci s grafem a jeho uložení v podobě obrázku (doporučujeme formát *.png).\n\n", "text")
        self.text_manual.insert(END, u"   POZOR! V souboru exe tato funkce nepracuje, grafy se negenerují.\n\n", "text")
        self.text_manual.insert(END, u"  VÝBĚROVÝ MEDIÁN\n"  , "nadpis")
        self.text_manual.insert(END, u"   V záložce Statistika, sekce Výběrový medián lze vygenerovat výběrové medány pro MS kraj, Ostravu nebo Opavu a následně \ntyto data načíst do *.xls souboru.\n\n", "text")
        self.text_manual.tag_config("podnadpis", underline=1, font="Arial 10 bold")
        self.text_manual.tag_config("nadpis", underline=1, font="Arial 13 bold")
        self.text_manual.tag_config("text", font="Arial 10")
        self.text_manual.config(state=DISABLED)
        
    def testovani(self):
        self.fr_t=LabelFrame(self.fr, relief=GROOVE, borderwidth=2, text=u'Jednovýběrové testy')
        self.photo1 = PhotoImage(file="Button/Znamenkovy_test.gif")
        self.bu_zn=Button(self.fr_t, image=self.photo1, command=self.znamenkovy_test)
        self.bu_zn.pack(padx=4, pady=4, side='left')
        self.photo2 = PhotoImage(file="Button/wilcox_test.gif")
        self.bu_wi=Button(self.fr_t, image=self.photo2, command=self.wilcoxonuv_test)
        self.bu_wi.pack(padx=4, pady=4, side='left')
        self.fr_t.pack(fill = 'both',expand=1, anchor=N)
        self.fr_t_dvoj=LabelFrame(self.fr, relief=GROOVE, borderwidth=2, text=u'Dvouvýběrové testy')
        self.photo3 = PhotoImage(file="Button/Man_Whi_test.gif")
        self.bu_ma=Button(self.fr_t_dvoj, image=self.photo3, command=self.mannuv_whitneyuv_test)
        self.bu_ma.pack(padx=4, pady=4, side='left')
        self.photo4 = PhotoImage(file="Button/Kolmogo_Smir.gif")
        self.bu_KS2=Button(self.fr_t_dvoj, image=self.photo4, command=self.dvou_kolmogoruv_smirdotonuv_test)
        self.bu_KS2.pack(padx=4, pady=4, side='left')
        self.fr_t_dvoj.pack(fill = 'both',expand=1, anchor=S)
        self.fr_t_vicev=LabelFrame(self.fr, relief=GROOVE, borderwidth=2, text=u'Vícevýběrové testy')
        self.photo5 = PhotoImage(file="Button/Krus_Wal.gif")
        self.bu_krus_walis=Button(self.fr_t_vicev, image=self.photo5, command=self.kruskaluv_wallisuv_test)
        self.bu_krus_walis.pack(padx=4, pady=4, side='left')
        self.fr_t_vicev.pack(fill = 'both',expand=1, anchor=N)
        self.fr_t_norm=LabelFrame(self.fr, relief=GROOVE, borderwidth=2, text=u'Testy normality')
        self.bu_KS=Button(self.fr_t_norm, image=self.photo4, command=self.kolmogoruv_smirdotonuv_test)
        self.bu_KS.pack(padx=4, pady=4, side='left')
        self.photo6 = PhotoImage(file="Button/spicatost.gif")
        self.bu_spi=Button(self.fr_t_norm, image=self.photo6, command=self.spicatost_test)
        self.bu_spi.pack(padx=4, pady=4, side='left')
        self.fr_t_norm.pack(fill = 'both',expand=1, anchor=S)
        self.fr_t_rozdeleni=LabelFrame(self.fr, relief=GROOVE, borderwidth=2, text=u'Testy o typu rozdělení')
        self.photo7 = PhotoImage(file="Button/Exponencialni.gif")
        self.bu_expo=Button(self.fr_t_rozdeleni, image=self.photo7, command=self.test_o_exponencialnim_rozdeleni)
        self.bu_expo.pack(padx=4, pady=4, side='left')
        self.photo16 = PhotoImage(file="Button/pearson.gif")
        self.bu_pears=Button(self.fr_t_rozdeleni, image=self.photo16, command=self.pearson)
        self.bu_pears.pack(padx=4, pady=4, side='left')
        self.fr_t_rozdeleni.pack(fill = 'both',expand=1, anchor=S)

    def kruskaluv_wallisuv_test(self):
        self.kw1_hodnota_hladina=DoubleVar()
        self.kw2_hodnota_hladina=DoubleVar()
        self.kw_zalozky=self.soubor.sheet_names()
        self.kw_t=Toplevel()
        self.kw_t.title(u'Kruskalův-Wallisův test')
        self.kw_fr_horni=Frame(self.kw_t)
        self.kw_fr_horni_levy=(self.kw_fr_horni)

        self.kw_fr_horni_levy1=LabelFrame(self.kw_fr_horni_levy, relief=GROOVE, borderwidth=2, text=u'Typ')
        self.kw_li1 = Listbox(self.kw_fr_horni_levy1, width=30, height=10)
        self.kw_sy1 = Scrollbar(self.kw_fr_horni_levy1, orient="vertical", command=self.kw_li1.yview)  
        #self.kw_la1 = Label(self.kw_fr_horni_levy1, text=u"Není vybrana žádná kategorie", foreground="red")
        self.kw_li1.configure(yscrollcommand=self.kw_sy1.set)
        kw_seznam_kat=[]
        kw_seznam_mest=[]
        sh=self.soubor.sheet_by_name(self.kw_zalozky[0])
        for col in range(sh.ncols): #vytvori seznam kategorii
            kw_seznam_kat.append(sh.col_values(col)[0])
        del kw_seznam_kat[0:13]
        del kw_seznam_kat[(len(kw_seznam_kat)-1)]
        del kw_seznam_kat[(len(kw_seznam_kat)-1)]
        for polozka in kw_seznam_kat:
            self.kw_li1.insert(END, polozka)
        
        self.kw_li1.grid(row=0, column=0, padx=4, pady=4)
        self.kw_sy1.grid(row=0, column=1, sticky="ns", pady=4, padx=2)
        #self.kw_la1.grid(row=1, column=0, columnspan=2)
        self.kw_li1.bind("<B1-ButtonRelease>", self.nacti1)
        self.kategorie_kw1='' #pomocna promenna ktera se naplni v pripade zadani kategorie, jinak bude uzivatel upozornen ze nevybral promennou
        self.kw_fr_horni_levy1.pack(fill='both', expand=1, padx=2, pady=2, side='left', anchor=W)
        self.kw_fr_horni_levy.pack(fill="both", expand=1, anchor=E)
        self.kw_fr_horni_pravy=(self.kw_fr_horni)
        #horni pravy levy
        self.kw_fr_horni_pravy_levy=Frame(self.kw_fr_horni_pravy)
        self.kw_bu_horni1=Button(self.kw_fr_horni_pravy_levy, text=u"Přidej >>", height=1, width=10, command=self.pridej1)
        self.kw_bu_horni1.pack(anchor=N, padx=4, pady=8)
        self.kw_bu_horni2=Button(self.kw_fr_horni_pravy_levy, text=u"Vymaž", height=1, width=10, command=self.vymaz1)
        self.kw_bu_horni2.pack(anchor=N, padx=4)
        self.kw_bu_horni3=Button(self.kw_fr_horni_pravy_levy, text=u"Vymaž vše", height=1, width=10, command=self.vymazvse1)
        self.kw_bu_horni3.pack(anchor=N, padx=4, pady=8)
        self.kw_bu_horni4=Button(self.kw_fr_horni_pravy_levy, text=u"Testovat", height=1, width=10, command=self.testovat_kw1)
        self.kw_bu_horni4.pack(anchor=N, padx=4)
        self.fr_kw1_hladina=LabelFrame(self.kw_fr_horni_pravy_levy, relief=GROOVE, borderwidth=2, text=u'Hladina významnosti \u03B1')
        self.ra_kw1_0_01 = Radiobutton(self.fr_kw1_hladina, text=u"\u03B1 = 0.01", variable=self.kw1_hodnota_hladina, value=0.01)
        self.ra_kw1_0_01.pack(side='left', padx=4)
        self.ra_kw1_0_05 = Radiobutton(self.fr_kw1_hladina, text=u"\u03B1 = 0.05", variable=self.kw1_hodnota_hladina, value=0.05)
        self.ra_kw1_0_05.pack(side='left', padx=4)
        self.ra_kw1_0_1 = Radiobutton(self.fr_kw1_hladina, text=u"\u03B1 = 0.1", variable=self.kw1_hodnota_hladina, value=0.1)
        self.ra_kw1_0_1.pack(side='left', padx=4)
        self.fr_kw1_hladina.pack(fill = 'x',expand=1, anchor=S, pady=2)
        self.ra_kw1_0_01.select()
        self.kw_fr_horni_pravy_levy.pack(fill="both", expand=1, side="left", anchor=W)
        #horni pravy pravy
        self.kw_fr_horni_pravy_pravy=LabelFrame(self.kw_fr_horni_pravy, text="Vybrane kategorie")
        self.kw_li2 = Listbox(self.kw_fr_horni_pravy_pravy, width=30, height=10)
        self.kw_sy2 = Scrollbar(self.kw_fr_horni_pravy_pravy, orient="vertical", command=self.kw_li2.yview)
        self.kw_li2.bind("<B1-ButtonRelease>", self.nacti2)
        self.kw_li2.configure(yscrollcommand=self.kw_sy2.set)
        self.kw_li2.grid(row=0, column=2, padx=4, pady=4)
        self.kw_sy2.grid(row=0, column=3, sticky="ns", pady=4, padx=2)
        self.kategorie_kw2='' #pomocna promenna ktera se naplni v pripade zadani kategorie, jinak bude uzivatel upozornen ze nevybral promennou
        self.kw_fr_horni_pravy_pravy.pack(fill="both", expand=1, side="right", anchor=E, pady=2, padx=2)
        self.kw_fr_horni_pravy.pack(fill="both", expand=1, anchor=W)
        self.kw_fr_horni.pack(fill="both", expand=1, anchor=N)

        self.kw_fr_dolni_stred=Frame(self.kw_t, width=50, height=10)
        self.kw_bu_ze_seznamu=Button(self.kw_fr_dolni_stred, text=u"v\nv", height=2, width=2, command=self.vybrat_nemoc)
        self.kw_bu_ze_seznamu.pack(anchor=NW, padx=100)
        self.kw_la_inf=Label(self.kw_fr_dolni_stred, text="Žádná vybraná kategorie", foreground="red")
        self.kw_la_inf.pack(anchor=SW, padx=40)
        self.kw_fr_dolni_stred.pack(fill="both", expand=1, anchor=NW)

        self.kw_fr_dolni=Frame(self.kw_t)
        self.kw_fr_dolni_levy=Frame(self.kw_fr_dolni)
        
####dolni levy dolni####
        self.kw_fr_dolni_levy_dolni=LabelFrame(self.kw_fr_dolni_levy, text="Oblasti")
        self.kw_li3 = Listbox(self.kw_fr_dolni_levy_dolni, width=30, height=10)
        self.kw_sy3 = Scrollbar(self.kw_fr_dolni_levy_dolni, orient="vertical", command=self.kw_li3.yview)  
        #self.kw_la1 = Label(self.kw_fr_horni_levy1, text=u"Není vybrana žádná kategorie", foreground="red")
        self.kw_li3.configure(yscrollcommand=self.kw_sy3.set)
        self.kw_li3.grid(row=0, column=4, padx=4, pady=4)
        self.kw_sy3.grid(row=0, column=5, sticky="ns", pady=4, padx=2)
        self.kw_li3.bind("<B1-ButtonRelease>", self.nacti3)
        self.kategorie_kw3='' #pomocna promenna ktera se naplni v pripade zadani kategorie, jinak bude uzivatel upozornen ze nevybral promennou
        self.kw_fr_dolni_levy_dolni.pack(fill="both", expand=1, anchor=S)
        self.kw_fr_dolni_levy.pack(fill="both", expand=1, side="left", anchor=E, padx=2, pady=2)
        
        self.kw_fr_dolni_pravy=Frame(self.kw_fr_dolni)
        self.kw_fr_dolni_pravy_levy=Frame(self.kw_fr_dolni_pravy)
        self.kw2_bu_horni1=Button(self.kw_fr_dolni_pravy_levy, text=u"Přidej >>", height=1, width=10, command=self.pridej2)
        self.kw2_bu_horni1.pack(anchor=N, padx=4, pady=8)
        self.kw2_bu_horni2=Button(self.kw_fr_dolni_pravy_levy, text=u"Vymaž", height=1, width=10, command=self.vymaz2)
        self.kw2_bu_horni2.pack(anchor=N, padx=4)
        self.kw2_bu_horni3=Button(self.kw_fr_dolni_pravy_levy, text=u"Vymaž vše", height=1, width=10, command=self.vymazvse2)
        self.kw2_bu_horni3.pack(anchor=N, padx=4, pady=8)
        self.kw2_bu_horni4=Button(self.kw_fr_dolni_pravy_levy, text=u"Testovat", height=1, width=10, command=self.testovat_kw2)
        self.kw2_bu_horni4.pack(anchor=N, padx=4)
        self.fr_kw2_hladina=LabelFrame(self.kw_fr_dolni_pravy_levy, relief=GROOVE, borderwidth=2, text=u'Hladina významnosti \u03B1')
        self.ra_kw2_0_01 = Radiobutton(self.fr_kw2_hladina, text=u"\u03B1 = 0.01", variable=self.kw2_hodnota_hladina, value=0.01)
        self.ra_kw2_0_01.pack(side='left', padx=4)
        self.ra_kw2_0_05 = Radiobutton(self.fr_kw2_hladina, text=u"\u03B1 = 0.05", variable=self.kw2_hodnota_hladina, value=0.05)
        self.ra_kw2_0_05.pack(side='left', padx=4)
        self.ra_kw2_0_1 = Radiobutton(self.fr_kw2_hladina, text=u"\u03B1 = 0.1", variable=self.kw2_hodnota_hladina, value=0.1)
        self.ra_kw2_0_1.pack(side='left', padx=4)
        self.fr_kw2_hladina.pack(fill = 'x',expand=1, anchor=S, pady=2)
        self.ra_kw2_0_01.select()
        self.kw_fr_dolni_pravy_levy.pack(fill="both", expand=1, side="left", anchor=E)

        self.kw_fr_dolni_pravy_pravy=LabelFrame(self.kw_fr_dolni_pravy, text="Vybrané kategorie")
        self.kw_li4 = Listbox(self.kw_fr_dolni_pravy_pravy, width=30, height=10)
        self.kw_sy4 = Scrollbar(self.kw_fr_dolni_pravy_pravy, orient="vertical", command=self.kw_li4.yview)  
        #self.kw_la1 = Label(self.kw_fr_horni_levy1, text=u"Není vybrana žádná kategorie", foreground="red")
        self.kw_li4.configure(yscrollcommand=self.kw_sy4.set)
        self.kw_li4.grid(row=0, column=6, padx=4, pady=4)
        self.kw_sy4.grid(row=0, column=7, sticky="ns", pady=4, padx=2)
        self.kw_li4.bind("<B1-ButtonRelease>", self.nacti4)
        self.kategorie_kw4='' #pomocna promenna ktera se naplni v pripade zadani kategorie, jinak bude uzivatel upozornen ze nevybral promennou
        self.kw_fr_dolni_pravy_pravy.pack(fill="both", side="right", anchor=W, padx=2, pady=2)
        
        self.kw_fr_dolni_pravy.pack(fill="both", expand=1, side="right", anchor=W)
        self.kw_fr_dolni.pack(fill="both", expand=1, anchor=S)

    def vybrat_nemoc(self):
        if self.kategorie_kw1!="":
            self.kategorie_kw3=""
            self.kw_la_inf.configure(text=self.kw_li1.get("active"), foreground="#00B000")
            sh=self.soubor.sheet_by_name(self.kw_zalozky[0])
            self.data_nemoc={}
            for col in range(sh.ncols): #zjisti cislo sloupce na zaklade ziskane hodnoty jmena
                    if sh.col_values(col)[0]==self.kw_la_inf.cget("text"):
                        zalozka1=col
            for row in range(sh.nrows):
                if self.data_nemoc.has_key(sh.row_values(row)[6])==True:
                    #print data1[sh.row_values(row)[6]]
                    pomo=self.data_nemoc[sh.row_values(row)[6]]
                    if grafy.is_number(sh.row_values(row)[zalozka1]):
                        pomo.append(sh.row_values(row)[zalozka1])
                    self.data_nemoc[sh.row_values(row)[6]]=pomo
                else:
                    if grafy.is_number(sh.row_values(row)[zalozka1]):
                        self.data_nemoc[sh.row_values(row)[6]]=[sh.row_values(row)[zalozka1]]
            self.kw_li3.delete(0, END)
            for polozky in self.data_nemoc.keys():
                if len(self.data_nemoc[polozky])>=5:
                    self.kw_li3.insert(END, polozky)
            self.kw_li4.delete(0, END)
                

    def nacti1(self, event):
        self.kategorie_kw1="Klikli jsem na vyber, mame neco v listboxu oznacene, dava smysl to pridat"

    def nacti3(self, event):
        self.kategorie_kw3="Klikli jsem na vyber, mame neco v listboxu oznacene, dava smysl to pridat"

    def nacti2(self, event):
        self.kategorie_kw2="Klikli jsem na vyber, mame neco v listboxu oznacene, dava smysl to pridat"

    def nacti4(self, event):
        self.kategorie_kw4="Klikli jsem na vyber, mame neco v listboxu oznacene, dava smysl to pridat"

    def pridej1(self):
        if self.kategorie_kw1=='':
            return
        else:
            self.kw_li2.insert(END, self.kw_li1.get("active"))

    def pridej2(self):
        if self.kategorie_kw3=='':
            return
        else:
            self.kw_li4.insert(END, self.kw_li3.get("active"))

    def vymaz1(self):
        if len(self.kw_li2.get(0, END))==0 or self.kategorie_kw2=='':
            return
        else:
            kategorie=self.kw_li2.get("active")
            i=0
            for prvek in self.kw_li2.get(0, END):
                if prvek==kategorie:
                    self.kw_li2.delete(i)
                i=i+1

    def vymaz2(self):
        if len(self.kw_li4.get(0, END))==0 or self.kategorie_kw4=='':
            return
        else:
            kategorie=self.kw_li4.get("active")
            i=0
            for prvek in self.kw_li4.get(0, END):
                if prvek==kategorie:
                    self.kw_li4.delete(i)
                i=i+1

    def vymazvse1(self):
        if len(self.kw_li2.get(0, END))==0:
            return
        else:
            self.kw_li2.delete(0, END)

    def vymazvse2(self):
        if len(self.kw_li4.get(0, END))==0:
            return
        else:
            self.kw_li4.delete(0, END)

    def testovat_kw1(self):
        if len(self.kw_li2.get(0, END))<2:
            self.nedostatecny_rozsah()
            self.txt_maly_rozsah.delete(1.0, END)
            self.txt_maly_rozsah.insert(END, u"Nedostatečné množstvý vybraných výběrů!!!\n", "nadpis")
            self.txt_maly_rozsah.insert(END, u"Pro spuštění testu je potřeba mít v seznamu vybrané alespoň dva výběry.", "text")
        else:
            data={}
            kategorie=self.kw_li2.get(0, END)
            for polozka in kategorie:
                sh=self.soubor.sheet_by_name(self.kw_zalozky[0])
                data1=[]
                for col in range(sh.ncols): #zjisti cislo sloupce na zaklade ziskane hodnoty jmena
                    if sh.col_values(col)[0]==polozka:
                        zalozka1=col
                for row in range(sh.nrows):
                    data1.append(sh.row_values(row)[zalozka1])
                del data1[0]
                pom_data=[]
                for prvek in data1:
                    if grafy.is_number(prvek)==True:
                        pom_data.append(prvek)
                data[polozka]=pom_data
            for prvek in data.keys():
                if len(data[prvek])<5:
                    self.nedostatecny_rozsah()
                    self.txt_maly_rozsah.insert(END, u"Rozsah jednotlivých výběrů:\n", "text")
                    i=1
                    for prvek2 in data.keys():
                        self.txt_maly_rozsah.insert(END, prvek2 + u": n"+str(i)+u" = " + str(len(data[prvek2])) + u"\n", "text")
                        i=i+1
                    self.txt_maly_rozsah.insert(END, u"\nPro spuštění testu je nutné, aby rozsah každého výběru byl alespoň 5.", "text")
                    return
            vysledek_kw1=testy.kruskaluv_wallisuv_test(data, self.kw1_hodnota_hladina.get())
            self.oznameni_kw1=Toplevel()
            self.oznameni_kw1.title('Vyhodnocení Kruskalova-Wallisova testu')
            self.txt_kw1=Text(self.oznameni_kw1, width=100, height=20)
            self.scrol_kw1=Scrollbar(self.oznameni_kw1)
            self.scrol_kw1.pack(side=RIGHT, fill=Y)
            self.txt_kw1.pack(expand=1, fill=BOTH)
            self.txt_kw1.focus_set()
            self.scrol_kw1.config(command=self.txt_kw1.yview)
            self.txt_kw1.config(yscrollcommand=self.scrol_kw1.set)
            self.txt_kw1.delete(1.0, END)
            self.txt_kw1.insert(END, u"Kruskalův-Wallisův test", "nadpis")
            self.txt_kw1.insert(END, "\n", "text")
            self.txt_kw1.insert(END, "\n", "text")
            self.txt_kw1.insert(END, u"\u03B1 = "+str(self.kw1_hodnota_hladina.get()), "text")
            self.txt_kw1.insert(END, "\n", "text")
            self.txt_kw1.insert(END, u"H0: \u03BC1=\u03BC2=...=\u03BCn", "text")
            self.txt_kw1.insert(END, "\n", "text")
            self.txt_kw1.insert(END, u"Ha: \u03BC1\u2260\u03BC2\u2260...\u2260\u03BCn", "text")
            self.txt_kw1.insert(END, "\n", "text")
            self.txt_kw1.insert(END, u"p-hodnota = " + str(round(vysledek_kw1[0],5)), "text")
            self.txt_kw1.insert(END, "\n", "text")
            self.txt_kw1.insert(END, "\n", "text")
            if (vysledek_kw1[0])<=self.kw1_hodnota_hladina.get():
                self.txt_kw1.insert(END, u"Protože p-hodnota je menší nebo rovna než hladina významnosti \u03B1,", "text")
                self.txt_kw1.insert(END, "\n", "text")
                self.txt_kw1.insert(END, u"zamítáme hypotézu H0 ve prospěch alternativy.", "text")
                self.txt_kw1.insert(END, "\n", "text")
                self.txt_kw1.insert(END, "\n", "text")
                self.txt_kw1.insert(END, "Post-hoc analýza", "podnadpis")
                self.txt_kw1.insert(END, "\n", "text")
                post_h=vysledek_kw1[1]
                #print post_h
                #print post_h.values()[0][0]
                for prvek in post_h.keys():
                    udaje=post_h[prvek]
                    udaj1=udaje[0]
                    udaj2=udaje[1]
                    #print udaj1, udaj2
                    for nazev in data.keys():
                        if data[nazev]==udaj1:
                            nazev1=nazev
                        if data[nazev]==udaj2:
                            nazev2=nazev
                    if (round(prvek[0], 3))>=(round(prvek[1], 3)):
                        popis=u"Statisticky se významně LIŠÍ"
                    else:
                        popis=u"Statisticky se významně NELIŠÍ"
                    self.txt_kw1.insert(END, nazev1 + u" vs. " + nazev2 + u": " + popis, "text")
                    self.txt_kw1.insert(END, "\n", "text")
                
            else:
                self.txt_kw1.insert(END, u"Protože p-hodnota je větší než hladina významnosti \u03B1, ", "text")
                self.txt_kw1.insert(END, "\n", "text")
                self.txt_kw1.insert(END, u"nezamítáme hypotézu H0.", "text")
            self.txt_kw1.tag_config("podnadpis", underline=1, font="Arial 10")
            self.txt_kw1.tag_config("nadpis", underline=1, font="Arial 10 bold")
            self.txt_kw1.tag_config("text", font="Arial 10")
            self.txt_kw1.config(state=DISABLED)
        
    def testovat_kw2(self):
        if len(self.kw_li4.get(0, END))<2:
            self.nedostatecny_rozsah()
            self.txt_maly_rozsah.delete(1.0, END)
            self.txt_maly_rozsah.insert(END, u"Nedostatečné množstvý vybraných výběrů!!!\n", "nadpis")
            self.txt_maly_rozsah.insert(END, u"Pro spuštění testu je potřeba mít v seznamu vybrané alespoň dva výběry.", "text")
        else:
            data={}
            kategorie=self.kw_li4.get(0, END)
            for polozka in kategorie:
                data[polozka]=self.data_nemoc[polozka]
            for prvek in data.keys():
                if len(data[prvek])<5:
                    self.nedostatecny_rozsah()
                    self.txt_maly_rozsah.insert(END, u"Rozsah jednotlivých výběrů:\n", "text")
                    i=1
                    for prvek2 in data.keys():
                        self.txt_maly_rozsah.insert(END, prvek2 + u": n"+str(i)+u" = " + str(len(data[prvek2])) + u"\n", "text")
                        i=i+1
                    self.txt_maly_rozsah.insert(END, u"\nPro spuštění testu je nutné, aby rozsah každého výběru byl alespoň 5.", "text")
                    return
            vysledek_kw2=testy.kruskaluv_wallisuv_test(data, self.kw2_hodnota_hladina.get())
            self.oznameni_kw2=Toplevel()
            self.oznameni_kw2.title('Vyhodnocení Kruskalova-Wallisova testu')
            self.txt_kw2=Text(self.oznameni_kw2, width=100, height=20)
            self.scrol_kw2=Scrollbar(self.oznameni_kw2)
            self.scrol_kw2.pack(side=RIGHT, fill=Y)
            self.txt_kw2.pack(expand=1, fill=BOTH)
            self.txt_kw2.focus_set()
            self.scrol_kw2.config(command=self.txt_kw2.yview)
            self.txt_kw2.config(yscrollcommand=self.scrol_kw2.set)
            self.txt_kw2.delete(1.0, END)
            self.txt_kw2.insert(END, u"Kruskalův-Wallisův test", "nadpis")
            self.txt_kw2.insert(END, "\n", "text")
            self.txt_kw2.insert(END, "\n", "text")
            self.txt_kw2.insert(END, u"\u03B1 = "+str(self.kw2_hodnota_hladina.get()), "text")
            self.txt_kw2.insert(END, "\n", "text")
            self.txt_kw2.insert(END, u"H0: \u03BC1=\u03BC2=...=\u03BCn", "text")
            self.txt_kw2.insert(END, "\n", "text")
            self.txt_kw2.insert(END, u"Ha: \u03BC1\u2260\u03BC2\u2260...\u2260\u03BCn", "text")
            self.txt_kw2.insert(END, "\n", "text")
            self.txt_kw2.insert(END, u"p-hodnota = " + str(round(vysledek_kw2[0],5)), "text")
            self.txt_kw2.insert(END, "\n", "text")
            self.txt_kw2.insert(END, "\n", "text")
            if (vysledek_kw2[0])<=self.kw2_hodnota_hladina.get():
                self.txt_kw2.insert(END, u"Protože p-hodnota je menší nebo rovna než hladina významnosti \u03B1,", "text")
                self.txt_kw2.insert(END, "\n", "text")
                self.txt_kw2.insert(END, u"zamítáme hypotézu H0 ve prospěch alternativy.", "text")
                self.txt_kw2.insert(END, "\n", "text")
                self.txt_kw2.insert(END, "\n", "text")
                self.txt_kw2.insert(END, "Post-hoc analýza", "podnadpis")
                self.txt_kw2.insert(END, "\n", "text")
                post_h=vysledek_kw2[1]
                #print post_h
                #print post_h.values()[0][0]
                for prvek in post_h.keys():
                    udaje=post_h[prvek]
                    udaj1=udaje[0]
                    udaj2=udaje[1]
                    #print udaj1, udaj2
                    for nazev in data.keys():
                        if data[nazev]==udaj1:
                            nazev1=nazev
                        if data[nazev]==udaj2:
                            nazev2=nazev
                    if (round(prvek[0], 3))>=(round(prvek[1], 3)):
                        popis=u"Statisticky se významně LIŠÍ"
                    else:
                        popis=u"Statisticky se významně NELIŠÍ"
                    self.txt_kw2.insert(END, nazev1 + u" vs. " + nazev2 + u": " + popis, "text")
                    self.txt_kw2.insert(END, "\n", "text")
            else:
                self.txt_kw2.insert(END, u"Protože p-hodnota je větší než hladina významnosti \u03B1, ", "text")
                self.txt_kw2.insert(END, "\n", "text")
                self.txt_kw2.insert(END, u"nezamítáme hypotézu H0.", "text")
            self.txt_kw2.tag_config("podnadpis", underline=1, font="Arial 10")
            self.txt_kw2.tag_config("nadpis", underline=1, font="Arial 10 bold")
            self.txt_kw2.tag_config("text", font="Arial 10")
            self.txt_kw2.config(state=DISABLED)

    def test_o_exponencialnim_rozdeleni(self):
        self.expo_hodnota_hladina=DoubleVar()
        self.expo_zalozky=self.soubor.sheet_names()
        self.expo_t=Toplevel()
        self.expo_t.title(u'Test o exponenciálním rozdělení')
        self.fr_expo_levy=Frame(self.expo_t)
#### prvni listbox #####
        self.fr_expo_levy1=LabelFrame(self.fr_expo_levy, relief=GROOVE, borderwidth=2, text=u'Typ *(povinna)')
        self.expo_li1 = Listbox(self.fr_expo_levy1, width=30, height=10)
        self.expo_sy1 = Scrollbar(self.fr_expo_levy1, orient="vertical", command=self.expo_li1.yview)  
        self.expo_la1 = Label(self.fr_expo_levy1, text=u"Není vybrana žádná kategorie", foreground="red")
        self.expo_li1.configure(yscrollcommand=self.expo_sy1.set)
        expo_seznam_kat=[]
        expo_seznam_mest=[]
        sh=self.soubor.sheet_by_name(self.expo_zalozky[0])
        for col in range(sh.ncols): #vytvori seznam kategorii
            expo_seznam_kat.append(sh.col_values(col)[0])
        del expo_seznam_kat[0:13]
        del expo_seznam_kat[(len(expo_seznam_kat)-1)]
        del expo_seznam_kat[(len(expo_seznam_kat)-1)]
        for polozka in expo_seznam_kat:
            self.expo_li1.insert(END, polozka)
        
        self.expo_li1.grid(row=0, column=0, padx=4, pady=8)
        self.expo_sy1.grid(row=0, column=1, sticky="ns", pady=8)
        self.expo_la1.grid(row=1, column=0, columnspan=2)
        
        self.expo_li1.bind("<Double-B1-ButtonRelease>", self.expo_li1_double)
        self.kategorie_expo1='' #pomocna promenna ktera se naplni v pripade zadani kategorie, jinak bude uzivatel upozornen ze nevybral promennou
        self.fr_expo_levy1.pack(fill='both', expand=1, padx=2, pady=2, side='left', anchor=W)
##### druhy listbox ######
        expo_seznam_mest=[]
        for row in range(sh.nrows): #vytvori seznam kategorii
            if (sh.row_values(row)[6] in expo_seznam_mest) !=True:
                expo_seznam_mest.append(sh.row_values(row)[6])
        del expo_seznam_mest[0]
        self.fr_expo_levy2=LabelFrame(self.fr_expo_levy, relief=GROOVE, borderwidth=2, text=u'Oblast')
        self.expo_li2 = Listbox(self.fr_expo_levy2, width=30, height=10)
        self.expo_sy2 = Scrollbar(self.fr_expo_levy2, orient="vertical", command=self.expo_li2.yview)  
        self.expo_la2 = Label(self.fr_expo_levy2, text=u"Není vybrana žádná kategorie", foreground="red")
        self.expo_li2.configure(yscrollcommand=self.expo_sy2.set)
        mesta=expo_seznam_mest
        mesta.sort()
        for polozka in mesta:
            self.expo_li2.insert(END, polozka)
        self.expo_li2.grid(row=0, column=0, padx=4, pady=8)
        self.expo_sy2.grid(row=0, column=1, sticky="ns", pady=8)
        self.expo_la2.grid(row=1, column=0, columnspan=2)
        
        self.expo_li2.bind("<Double-B1-ButtonRelease>", self.expo_li2_double)
        self.kategorie_expo2='' #pomocna promenna ktera se naplni v pripade zadani kategorie, jinak bude uzivatel upozornen ze nevybral promennou
        self.fr_expo_levy2.pack(fill='both', expand=1, padx=2, pady=2, side='right', anchor=E)
        self.fr_expo_levy.pack(fill='both', expand=1, side='left', anchor=W)
####### prava strana s parametry #####
        self.fr_expo_pravy=Frame(self.expo_t)
        self.fr_expo_prava1=LabelFrame(self.fr_expo_pravy, relief=GROOVE, borderwidth=2, text=u'Hladina významnosti \u03B1')
        self.ra_expo0_01 = Radiobutton(self.fr_expo_prava1, text=u"\u03B1 = 0.01", variable=self.expo_hodnota_hladina, value=0.01)
        self.ra_expo0_01.pack(side='left', padx=4)
        self.ra_expo0_05 = Radiobutton(self.fr_expo_prava1, text=u"\u03B1 = 0.05", variable=self.expo_hodnota_hladina, value=0.05)
        self.ra_expo0_05.pack(side='left', padx=4)
        self.ra_expo0_1 = Radiobutton(self.fr_expo_prava1, text=u"\u03B1 = 0.1", variable=self.expo_hodnota_hladina, value=0.1)
        self.ra_expo0_1.pack(side='left', padx=4)
        self.fr_expo_prava1.pack(fill = 'x',expand=1, side="top", anchor=N)
        self.fr_expo_prava4=Frame(self.fr_expo_pravy)
        self.label_expo_prava1=Label(self.fr_expo_pravy, text="Následující testování může trvat několik sekund. \nProsím vyčkejte.", foreground="red")
        self.label_expo_prava1.pack(fill="x", expand=1, anchor=S)
        self.expo_bu_testovat1=Button(self.fr_expo_pravy, text=u"Testovat typ", command=self.exponencialni1)
        self.expo_bu_testovat1.pack(padx=4, pady=4, side='right', anchor=SE)
        self.expo_bu_testovat2=Button(self.fr_expo_pravy, text=u"Testovat podle oblasti", command=self.exponencialni2)
        self.expo_bu_testovat2.pack(padx=4, pady=4, side='right', anchor=SW)
        self.fr_expo_prava4.pack(fill = 'both',expand=1, anchor=N)
        self.fr_expo_pravy.pack(fill='both', expand=1, side='right', anchor=E, padx=4, pady=4)
        self.ra_expo0_01.select()

    def exponencialni2(self):
        self.exponencialni1("podle mest")

    def exponencialni1(self, typ="typ"):
        #print typ
        if typ=="podle mest":
            if self.kategorie_expo2=='':
                return
        if self.kategorie_expo1=='':
            return
        else:
            sh=self.soubor.sheet_by_name(self.expo_zalozky[0])
            data=[]
            for col in range(sh.ncols): #zjisti cislo sloupce na zaklade ziskane hodnoty jmena
                if sh.col_values(col)[0]==self.kategorie_expo1:
                    zalozka1=col
            if typ=="podle mest":
                for row in range(sh.nrows):
                    if sh.row_values(row)[6]==self.kategorie_expo2:
                        data.append(sh.row_values(row)[zalozka1])
            else:
                for row in range(sh.nrows):
                    data.append(sh.row_values(row)[zalozka1])
                nazev1=data[0]
                del data[0]
            pom_data1=[]
            for prvek in data:
                if grafy.is_number(prvek)==True:
                    pom_data1.append(prvek)
            if len(pom_data1)<2:
                self.nedostatecny_rozsah()
                self.txt_maly_rozsah.insert(END, u"Rozsah výběru n = " + str(len(pom_data1)) + u". Minimální rozsah výběru pro spuštění testu je 2.", "text")
            else:
                vysledek_expo=testy.exponencialni_rozdeleni(pom_data1, self.expo_hodnota_hladina.get())
                self.oznameni_expo=Toplevel()
                self.oznameni_expo.title('Vyhodnocení testu o exponenciálním rozdělení')
                self.txt_expo=Text(self.oznameni_expo, width=100, height=20)
                self.scrol_expo=Scrollbar(self.oznameni_expo)
                self.scrol_expo.pack(side=RIGHT, fill=Y)
                self.txt_expo.pack(expand=1, fill=BOTH)
                self.txt_expo.focus_set()
                self.scrol_expo.config(command=self.txt_expo.yview)
                self.txt_expo.config(yscrollcommand=self.scrol_expo.set)
                self.txt_expo.delete(1.0, END)
                self.txt_expo.insert(END, u"Test o exponenciálním rozdělení", "nadpis")
                self.txt_expo.insert(END, "\n", "text")
                self.txt_expo.insert(END, "\n", "text")
                self.txt_expo.insert(END, u"\u03B1 = "+str(self.expo_hodnota_hladina.get()), "text")
                self.txt_expo.insert(END, "\n", "text")
                self.txt_expo.insert(END, u"H0: Výběr pochází z exponenciálního rozdělení.", "text")
                self.txt_expo.insert(END, "\n", "text")
                self.txt_expo.insert(END, u"Ha: Výběr nepochází z exponenciálního rozdělení.", "text")
                self.txt_expo.insert(END, "\n", "text")
                self.txt_expo.insert(END, u"K = " + str(round(vysledek_expo[0],5)), "text")
                self.txt_expo.insert(END, "\n", "text")
                self.txt_expo.insert(END, u"Kritický obor  W = <0; " + str(round(vysledek_expo[1],5)) + u"> \u222A <" + str(round(vysledek_expo[2],5)) + u"; \u221E>", "text")
                self.txt_expo.insert(END, "\n", "text")
                self.txt_expo.insert(END, "\n", "text")
                if (vysledek_expo[0])>=vysledek_expo[2] or (vysledek_expo[0])<=vysledek_expo[1]:
                    self.txt_expo.insert(END, u"Protože K spadá do kritického oboru W, zamítáme hypotézu H0", "text")
                    self.txt_expo.insert(END, "\n", "text")
                    self.txt_expo.insert(END, u"ve prospěch alternativy na hladině významnosti \u03B1= " + str(self.expo_hodnota_hladina.get()) + u".", "text")
                else:
                    self.txt_expo.insert(END, u"Protože K nespadá do kritického oboru W, nezamítáme", "text")
                    self.txt_expo.insert(END, "\n", "text")
                    self.txt_expo.insert(END, u"hypotézu H0 na hladině významnosti \u03B1= " + str(self.expo_hodnota_hladina.get()) +u".", "text")
                self.txt_expo.tag_config("podnadpis", underline=1, font="Arial 10")
                self.txt_expo.tag_config("nadpis", underline=1, font="Arial 10 bold")
                self.txt_expo.tag_config("text", font="Arial 10")
                self.txt_expo.config(state=DISABLED)

    def dvou_kolmogoruv_smirdotonuv_test(self):
        self.kon_ks2_hodnota_hladina=DoubleVar()
        self.ks2_zalozky=self.soubor.sheet_names()
        self.ks2_t=Toplevel()
        self.ks2_t.title(u'Kolmogorovův-Smirdotonův test')
        self.fr_ks2_horni=Frame(self.ks2_t)
#### prvni listbox #####
        self.fr_ks2_levy=Frame(self.fr_ks2_horni)
        self.fr_ks2_levy1=LabelFrame(self.fr_ks2_levy, relief=GROOVE, borderwidth=2, text=u'Typ *(povinna)')
        self.ks2_li1 = Listbox(self.fr_ks2_levy1, width=30, height=10)
        self.ks2_sy1 = Scrollbar(self.fr_ks2_levy1, orient="vertical", command=self.ks2_li1.yview)  
        self.ks2_la1 = Label(self.fr_ks2_levy1, text=u"Není 1 vybrana žádná kategorie", foreground="red")
        self.ks2_li1.configure(yscrollcommand=self.ks2_sy1.set)
        ks2_seznam_kat=[]
        ks2_seznam_mest=[]
        sh=self.soubor.sheet_by_name(self.ks2_zalozky[0])
        for col in range(sh.ncols): #vytvori seznam kategorii
            ks2_seznam_kat.append(sh.col_values(col)[0])
        del ks2_seznam_kat[0:13]
        del ks2_seznam_kat[(len(ks2_seznam_kat)-1)]
        del ks2_seznam_kat[(len(ks2_seznam_kat)-1)]
        for polozka in ks2_seznam_kat:
            self.ks2_li1.insert(END, polozka)
        
        self.ks2_li1.grid(row=0, column=0, padx=4, pady=8)
        self.ks2_sy1.grid(row=0, column=1, sticky="ns", pady=8)
        self.ks2_la1.grid(row=1, column=0, columnspan=2)
        
        self.ks2_li1.bind("<Double-B1-ButtonRelease>", self.ks2_li1_double)
        self.kategorie_ks21='' #pomocna promenna ktera se naplni v pripade zadani kategorie, jinak bude uzivatel upozornen ze nevybral promennou
        self.fr_ks2_levy1.pack(fill='both', expand=1, padx=2, pady=2, side='left', anchor=W)
        
##### druhy listbox ######
        ks2_seznam_mest=[]
        for row in range(sh.nrows): #vytvori seznam kategorii
            if (sh.row_values(row)[6] in ks2_seznam_mest) !=True:
                ks2_seznam_mest.append(sh.row_values(row)[6])
        del ks2_seznam_mest[0]
        self.fr_ks2_levy2=LabelFrame(self.fr_ks2_levy, relief=GROOVE, borderwidth=2, text=u'Oblast')
        self.ks2_li2 = Listbox(self.fr_ks2_levy2, width=30, height=10)
        self.ks2_sy2 = Scrollbar(self.fr_ks2_levy2, orient="vertical", command=self.ks2_li2.yview)  
        self.ks2_la2 = Label(self.fr_ks2_levy2, text=u"Není 2 vybrana žádná kategorie", foreground="red")
        self.ks2_li2.configure(yscrollcommand=self.ks2_sy2.set)
        mesta=ks2_seznam_mest
        mesta.sort()
        
        for polozka in mesta:
            self.ks2_li2.insert(END, polozka)
        self.ks2_li2.grid(row=0, column=0, padx=4, pady=8)
        self.ks2_sy2.grid(row=0, column=1, sticky="ns", pady=8)
        self.ks2_la2.grid(row=1, column=0, columnspan=2)
        
        self.ks2_li2.bind("<Double-B1-ButtonRelease>", self.ks2_li2_double)
        self.kategorie_ks22='' #pomocna promenna ktera se naplni v pripade zadani kategorie, jinak bude uzivatel upozornen ze nevybral promennou
        self.fr_ks2_levy2.pack(fill='both', expand=1, padx=2, pady=2, side='right', anchor=E)
        self.fr_ks2_levy.pack(fill='both', expand=1, anchor=W, side="left")
####### prava strana s parametry #####
        self.fr_ks2_pravy=Frame(self.fr_ks2_horni)
        self.fr_ks2_prava1=LabelFrame(self.fr_ks2_pravy, relief=GROOVE, borderwidth=2, text=u'Hladina významnosti \u03B1')
        self.ra_ks20_01 = Radiobutton(self.fr_ks2_prava1, text=u"\u03B1 = 0.01", variable=self.kon_ks2_hodnota_hladina, value=0.01)
        self.ra_ks20_01.pack(side='left', padx=4)
        self.ra_ks20_05 = Radiobutton(self.fr_ks2_prava1, text=u"\u03B1 = 0.05", variable=self.kon_ks2_hodnota_hladina, value=0.05)
        self.ra_ks20_05.pack(side='left', padx=4)
        self.ra_ks20_1 = Radiobutton(self.fr_ks2_prava1, text=u"\u03B1 = 0.1", variable=self.kon_ks2_hodnota_hladina, value=0.1)
        self.ra_ks20_1.pack(side='left', padx=4)
        self.fr_ks2_prava1.pack(fill = 'x',expand=1, side="top", anchor=S)
##        self.fr_ks2_prava4=Frame(self.fr_ks2_pravy)
##        self.ks2_bu_testovat1=Button(self.fr_ks2_pravy, text=u"Testovat typ", command=self.nic)
##        self.ks2_bu_testovat1.pack(padx=4, pady=4, side='right')
##        self.ks2_bu_testovat2=Button(self.fr_ks2_pravy, text=u"Testovat podle obvodu", command=self.nic)
##        self.ks2_bu_testovat2.pack(padx=4, pady=4, side='right')
##        self.fr_ks2_prava4.pack(fill = 'both',expand=1, anchor=N)
        self.fr_ks2_pravy.pack(fill='both', expand=1, side='right', anchor=SE, padx=2, pady=2)
        self.ra_ks20_01.select()
        self.fr_ks2_horni.pack(fill='both', expand=1, anchor=N)
        self.fr_ks2_dolni=Frame(self.ks2_t)

        #### prvni listbox #####
        self.fr_ks2_dolni_levy=Frame(self.fr_ks2_dolni)
        self.fr_ks2_dolni_levy1=LabelFrame(self.fr_ks2_dolni_levy, relief=GROOVE, borderwidth=2, text=u'Typ *(povinna)')
        self.ks2_li3 = Listbox(self.fr_ks2_dolni_levy1, width=30, height=10)
        self.ks2_sy3 = Scrollbar(self.fr_ks2_dolni_levy1, orient="vertical", command=self.ks2_li3.yview)  
        self.ks2_la3 = Label(self.fr_ks2_dolni_levy1, text=u"Není 3 vybrana žádná kategorie", foreground="red")
        self.ks2_li3.configure(yscrollcommand=self.ks2_sy3.set)
        ks2_2_seznam_kat=[]
        ks2_2_seznam_mest=[]
        sh=self.soubor.sheet_by_name(self.ks2_zalozky[0])
        for col in range(sh.ncols): #vytvori seznam kategorii
            ks2_2_seznam_kat.append(sh.col_values(col)[0])
        del ks2_2_seznam_kat[0:13]
        del ks2_2_seznam_kat[(len(ks2_2_seznam_kat)-1)]
        del ks2_2_seznam_kat[(len(ks2_2_seznam_kat)-1)]
        for polozka in ks2_2_seznam_kat:
            self.ks2_li3.insert(END, polozka)
        
        self.ks2_li3.grid(row=0, column=0, padx=4, pady=8)
        self.ks2_sy3.grid(row=0, column=1, sticky="ns", pady=8)
        self.ks2_la3.grid(row=1, column=0, columnspan=2)
        
        self.ks2_li3.bind("<Double-B1-ButtonRelease>", self.ks2_li3_double)
        self.kategorie_ks23='' #pomocna promenna ktera se naplni v pripade zadani kategorie, jinak bude uzivatel upozornen ze nevybral promennou
        self.fr_ks2_dolni_levy1.pack(fill='both', expand=1, padx=2, pady=2, side='left', anchor=W)
        
##### druhy listbox ######
        ks2_2_seznam_mest=[]
        for row in range(sh.nrows): #vytvori seznam kategorii
            if (sh.row_values(row)[6] in ks2_2_seznam_mest) !=True:
                ks2_2_seznam_mest.append(sh.row_values(row)[6])
        del ks2_2_seznam_mest[0]
        self.fr_ks2_dolni_levy2=LabelFrame(self.fr_ks2_dolni_levy, relief=GROOVE, borderwidth=2, text=u'Oblast')
        self.ks2_li4 = Listbox(self.fr_ks2_dolni_levy2, width=30, height=10)
        self.ks2_sy4 = Scrollbar(self.fr_ks2_dolni_levy2, orient="vertical", command=self.ks2_li4.yview)  
        self.ks2_la4 = Label(self.fr_ks2_dolni_levy2, text=u"Není 4 vybrana žádná kategorie", foreground="red")
        self.ks2_li4.configure(yscrollcommand=self.ks2_sy4.set)
        mesta=ks2_2_seznam_mest
        mesta.sort()
        
        for polozka in mesta:
            self.ks2_li4.insert(END, polozka)
        self.ks2_li4.grid(row=0, column=0, padx=4, pady=8)
        self.ks2_sy4.grid(row=0, column=1, sticky="ns", pady=8)
        self.ks2_la4.grid(row=1, column=0, columnspan=2)
        
        self.ks2_li4.bind("<Double-B1-ButtonRelease>", self.ks2_li4_double)
        self.kategorie_ks24='' #pomocna promenna ktera se naplni v pripade zadani kategorie, jinak bude uzivatel upozornen ze nevybral promennou
        self.fr_ks2_dolni_levy2.pack(fill='both', expand=1, padx=2, pady=2, side='right', anchor=E)
        self.fr_ks2_dolni_levy.pack(fill='both', expand=1, anchor=W, side="left")
####### prava strana s parametry #####
        self.fr_ks2_dolni_pravy=Frame(self.fr_ks2_dolni)
        
        self.fr_ks2_dolni_prava4=Frame(self.fr_ks2_dolni_pravy)
        self.ks2_bu_dolni_testovat2=Button(self.fr_ks2_dolni_prava4, text=u"Testovat podle oblasti", command=self.ks2_test_typ_2)
        self.ks2_bu_dolni_testovat2.pack(padx=4, pady=4, side='left', anchor=NW)
        self.ks2_bu_dolni_testovat1=Button(self.fr_ks2_dolni_prava4, text=u"Testovat typ", command=self.ks2_test_typ_1)
        self.ks2_bu_dolni_testovat1.pack(padx=4, pady=4, side='right', anchor=NE)
        self.fr_ks2_dolni_prava4.pack(fill = 'both',expand=1, anchor=N)
        self.fr_ks2_dolni_pravy.pack(fill='both', expand=1, side='right', anchor=E, padx=4, pady=4)
        self.ra_ks20_01.select()
        
        self.fr_ks2_dolni.pack(fill="both", anchor=S)

    def ks2_test_typ_2(self):
        self.ks2_test_typ_1("podle mest")

    def ks2_test_typ_1(self,typ="typ"):
        if self.kategorie_ks21=="" or self.kategorie_ks23=="":
            return
        elif typ=="podle mest" and(self.kategorie_ks22=="" or self.kategorie_ks24==""):
            return
        else:
            sh=self.soubor.sheet_by_name(self.ks2_zalozky[0])
            data1=[]
            data2=[]
            for col in range(sh.ncols): #zjisti cislo sloupce na zaklade ziskane hodnoty jmena
                if sh.col_values(col)[0]==self.kategorie_ks21:
                    zalozka1=col
                if sh.col_values(col)[0]==self.kategorie_ks23:
                    zalozka2=col
            if typ=="podle mest":
                for row in range(sh.nrows):
                    if sh.row_values(row)[6]==self.kategorie_ks22:
                        data1.append(sh.row_values(row)[zalozka1])
                    if sh.row_values(row)[6]==self.kategorie_ks24:
                        data2.append(sh.row_values(row)[zalozka2])
            else:
                for row in range(sh.nrows):
                    data1.append(sh.row_values(row)[zalozka1])
                    data2.append(sh.row_values(row)[zalozka2])
                del data1[0]
                del data2[0]
            pom_data1=[]
            pom_data2=[]
            for prvek in data1:
                if grafy.is_number(prvek)==True:
                    pom_data1.append(prvek)
            #print pom_data1
            for prvek in data2:
                if grafy.is_number(prvek)==True:
                    pom_data2.append(prvek)
            #print pom_data2
            if len(pom_data1)<=3 or len(pom_data2)<=3:
                self.nedostatecny_rozsah()
                self.txt_maly_rozsah.insert(END, u"Rozsah výběru n1 = " + str(len(pom_data1)) + "\n" + u"Rozsah výběru n2 = " + str(len(pom_data2)) + u"\n\n" + u"Minimální rozsah výběru pro spuštění testu je u obou výběrů 3.", "text")
                return
            else:
                #print "testuju"
                vysledek_ks2=testy.dvouvyberovy_kolmogorovuv_smir(pom_data1, pom_data2, self.kon_ks2_hodnota_hladina.get())
                self.oznameni_ks2=Toplevel()
                self.oznameni_ks2.title('Vyhodnocení dvouvýběrového Kolmogorova-Smirnovova testu')
                self.txt_ks2=Text(self.oznameni_ks2, width=100, height=20)
                self.scrol_ks2=Scrollbar(self.oznameni_ks2)
                self.scrol_ks2.pack(side=RIGHT, fill=Y)
                self.txt_ks2.pack(expand=1, fill=BOTH)
                self.txt_ks2.focus_set()
                self.scrol_ks2.config(command=self.txt_ks2.yview)
                self.txt_ks2.config(yscrollcommand=self.scrol_ks2.set)
                self.txt_ks2.delete(1.0, END)
                self.txt_ks2.insert(END, u"Dvouvýběrový Kolmogorovův-Smirnovův test", "nadpis")
                self.txt_ks2.insert(END, "\n", "text")
                self.txt_ks2.insert(END, "\n", "text")
                self.txt_ks2.insert(END, u"\u03B1 = "+str(self.kon_ks2_hodnota_hladina.get()), "text")
                self.txt_ks2.insert(END, "\n", "text")
                self.txt_ks2.insert(END, u"H0: Výběry pocházejí ze základního souboru se stejnou distribuční funkci", "text")
                self.txt_ks2.insert(END, "\n", "text")
                self.txt_ks2.insert(END, u"Ha: Výběry nepocházejí ze základního souboru se stejnou distribuční funkci", "text")
                self.txt_ks2.insert(END, "\n", "text")
                self.txt_ks2.insert(END, u"Dnm = " + str(round(vysledek_ks2[0],5)), "text")
                self.txt_ks2.insert(END, "\n", "text")
                self.txt_ks2.insert(END, u"Dnm(\u03B1) = " + str(round(vysledek_ks2[1],5)), "text")
                self.txt_ks2.insert(END, "\n", "text")
                self.txt_ks2.insert(END, "\n", "text")
                if (vysledek_ks2[0])>=vysledek_ks2[1]:
                    self.txt_ks2.insert(END, u"Protože Dnm je větší nebo rovno než kritická hodnota Dnm(\u03B1), zamítáme hypotézu H0", "text")
                    self.txt_ks2.insert(END, "\n", "text")
                    self.txt_ks2.insert(END, u"ve prospěch alternativy na hladině významnosti \u03B1= " + str(self.kon_ks2_hodnota_hladina.get()) + u".", "text")
                else:
                    self.txt_ks2.insert(END, u"Protože Dnm je menží než kritická hodnota Dnm(\u03B1), nezamítáme", "text")
                    self.txt_ks2.insert(END, "\n", "text")
                    self.txt_ks2.insert(END, u"hypotézu H0 na hladině významnosti \u03B1= " + str(self.kon_ks2_hodnota_hladina.get()) +u".", "text")
                self.txt_ks2.tag_config("nadpis", underline=1, font="Arial 10 bold")
                self.txt_ks2.tag_config("text", font="Arial 10")
                self.txt_ks2.config(state=DISABLED)
                #vysledek_sp=testy.normalita_podle_spicatosti(pom_data1, self.sp_hodnota_hladina.get())
            

    
        
    def spicatost_test(self):
        self.sp_hodnota_hladina=DoubleVar()
        self.sp_zalozky=self.soubor.sheet_names()
        self.sp_t=Toplevel()
        self.sp_t.title(u'Test normality podle špičatosti (šikmosti)')
        self.fr_sp_levy=Frame(self.sp_t)
#### prvni listbox #####
        self.fr_sp_levy1=LabelFrame(self.fr_sp_levy, relief=GROOVE, borderwidth=2, text=u'Typ *(povinna)')
        self.sp_li1 = Listbox(self.fr_sp_levy1, width=30, height=10)
        self.sp_sy1 = Scrollbar(self.fr_sp_levy1, orient="vertical", command=self.sp_li1.yview)  
        self.sp_la1 = Label(self.fr_sp_levy1, text=u"Není vybrana žádná kategorie", foreground="red")
        self.sp_li1.configure(yscrollcommand=self.sp_sy1.set)
        sp_seznam_kat=[]
        sp_seznam_mest=[]
        sh=self.soubor.sheet_by_name(self.sp_zalozky[0])
        for col in range(sh.ncols): #vytvori seznam kategorii
            sp_seznam_kat.append(sh.col_values(col)[0])
        del sp_seznam_kat[0:13]
        del sp_seznam_kat[(len(sp_seznam_kat)-1)]
        del sp_seznam_kat[(len(sp_seznam_kat)-1)]
        for polozka in sp_seznam_kat:
            self.sp_li1.insert(END, polozka)
        
        self.sp_li1.grid(row=0, column=0, padx=4, pady=8)
        self.sp_sy1.grid(row=0, column=1, sticky="ns", pady=8)
        self.sp_la1.grid(row=1, column=0, columnspan=2)
        
        self.sp_li1.bind("<Double-B1-ButtonRelease>", self.sp_li1_double)
        self.kategorie_sp1='' #pomocna promenna ktera se naplni v pripade zadani kategorie, jinak bude uzivatel upozornen ze nevybral promennou
        self.fr_sp_levy1.pack(fill='both', expand=1, padx=2, pady=2, side='left', anchor=W)
##### druhy listbox ######
        sp_seznam_mest=[]
        for row in range(sh.nrows): #vytvori seznam kategorii
            if (sh.row_values(row)[6] in sp_seznam_mest) !=True:
                sp_seznam_mest.append(sh.row_values(row)[6])
        del sp_seznam_mest[0]
        self.fr_sp_levy2=LabelFrame(self.fr_sp_levy, relief=GROOVE, borderwidth=2, text=u'Oblast')
        self.sp_li2 = Listbox(self.fr_sp_levy2, width=30, height=10)
        self.sp_sy2 = Scrollbar(self.fr_sp_levy2, orient="vertical", command=self.sp_li2.yview)  
        self.sp_la2 = Label(self.fr_sp_levy2, text=u"Není vybrana žádná kategorie", foreground="red")
        self.sp_li2.configure(yscrollcommand=self.sp_sy2.set)
        mesta=sp_seznam_mest
        mesta.sort()
        for polozka in mesta:
            self.sp_li2.insert(END, polozka)
        self.sp_li2.grid(row=0, column=0, padx=4, pady=8)
        self.sp_sy2.grid(row=0, column=1, sticky="ns", pady=8)
        self.sp_la2.grid(row=1, column=0, columnspan=2)
        
        self.sp_li2.bind("<Double-B1-ButtonRelease>", self.sp_li2_double)
        self.kategorie_sp2='' #pomocna promenna ktera se naplni v pripade zadani kategorie, jinak bude uzivatel upozornen ze nevybral promennou
        self.fr_sp_levy2.pack(fill='both', expand=1, padx=2, pady=2, side='right', anchor=E)
        self.fr_sp_levy.pack(fill='both', expand=1, side='left', anchor=W)
####### prava strana s parametry #####
        self.fr_sp_pravy=Frame(self.sp_t)
        self.fr_sp_prava1=LabelFrame(self.fr_sp_pravy, relief=GROOVE, borderwidth=2, text=u'Hladina významnosti \u03B1')
        self.ra_sp0_01 = Radiobutton(self.fr_sp_prava1, text=u"\u03B1 = 0.01", variable=self.sp_hodnota_hladina, value=0.01)
        self.ra_sp0_01.pack(side='left', padx=4)
        self.ra_sp0_05 = Radiobutton(self.fr_sp_prava1, text=u"\u03B1 = 0.05", variable=self.sp_hodnota_hladina, value=0.05)
        self.ra_sp0_05.pack(side='left', padx=4)
        self.ra_sp0_1 = Radiobutton(self.fr_sp_prava1, text=u"\u03B1 = 0.1", variable=self.sp_hodnota_hladina, value=0.1)
        self.ra_sp0_1.pack(side='left', padx=4)
        self.fr_sp_prava1.pack(fill = 'x',expand=1, side="top", anchor=N)
        self.fr_sp_prava4=Frame(self.fr_sp_pravy)
        self.sp_bu_testovat1=Button(self.fr_sp_pravy, text=u"Testovat typ", command=self.sikmost1)
        self.sp_bu_testovat1.pack(padx=4, pady=4, side='right', anchor=SE)
        self.sp_bu_testovat2=Button(self.fr_sp_pravy, text=u"Testovat podle oblasti", command=self.sikmost2)
        self.sp_bu_testovat2.pack(padx=4, pady=4, side='right', anchor=SW)
        self.fr_sp_prava4.pack(fill = 'both',expand=1, anchor=N)
        self.fr_sp_pravy.pack(fill='both', expand=1, side='right', anchor=E, padx=4, pady=4)
        self.ra_sp0_01.select()

    def sikmost2(self):
        self.sikmost1("podle mest")

    def sikmost1(self, typ="typ"):
        #print typ
        if typ=="podle mest":
            if self.kategorie_sp2=='':
                return
        if self.kategorie_sp1=='':
            return
        else:
            sh=self.soubor.sheet_by_name(self.sp_zalozky[0])
            data=[]
            for col in range(sh.ncols): #zjisti cislo sloupce na zaklade ziskane hodnoty jmena
                if sh.col_values(col)[0]==self.kategorie_sp1:
                    zalozka1=col
            if typ=="podle mest":
                for row in range(sh.nrows):
                    if sh.row_values(row)[6]==self.kategorie_sp2:
                        data.append(sh.row_values(row)[zalozka1])
            else:
                for row in range(sh.nrows):
                    data.append(sh.row_values(row)[zalozka1])
                nazev1=data[0]
                del data[0]
            pom_data1=[]
            for prvek in data:
                if grafy.is_number(prvek)==True:
                    pom_data1.append(prvek)
            #print pom_data1
            if len(pom_data1)<=3:
                self.nedostatecny_rozsah()
                self.txt_maly_rozsah.insert(END, u"Rozsah výběru n = " + str(len(pom_data1)) + u". Minimální rozsah výběru pro spuštění testu je 4.", "text")
                return
            else:
                vysledek_sp=testy.normalita_podle_spicatosti(pom_data1, self.sp_hodnota_hladina.get())
                self.oznameni_sp=Toplevel()
                self.oznameni_sp.title('Vyhodnocení testu normality podle špičatosti (šikmosti)')
                self.txt_sp=Text(self.oznameni_sp, width=100, height=20)
                self.scrol_sp=Scrollbar(self.oznameni_sp)
                self.scrol_sp.pack(side=RIGHT, fill=Y)
                self.txt_sp.pack(expand=1, fill=BOTH)
                self.txt_sp.focus_set()
                self.scrol_sp.config(command=self.txt_sp.yview)
                self.txt_sp.config(yscrollcommand=self.scrol_sp.set)
                self.txt_sp.delete(1.0, END)
                self.txt_sp.insert(END, u"Test normality podle špičatosti (šikmosti)", "nadpis")
                self.txt_sp.insert(END, "\n", "text")
                self.txt_sp.insert(END, "\n", "text")
                self.txt_sp.insert(END, u"\u03B1 = "+str(self.sp_hodnota_hladina.get()), "text")
                self.txt_sp.insert(END, "\n", "text")
                self.txt_sp.insert(END, u"H0: Výběr pochází z normálního rozdělení.", "text")
                self.txt_sp.insert(END, "\n", "text")
                self.txt_sp.insert(END, u"Ha: Výběr nepochází z normálního rozdělení.", "text")
                self.txt_sp.insert(END, "\n", "text")
                self.txt_sp.insert(END, u"|U(A3)| = " + str(round(vysledek_sp[0],5)), "text")
                self.txt_sp.insert(END, "\n", "text")
                self.txt_sp.insert(END, u"|U(A4)| = " + str(round(vysledek_sp[1],5)), "text")
                self.txt_sp.insert(END, "\n", "text")
                self.txt_sp.insert(END, u"u(\u03B1/2) = " + str(round(vysledek_sp[2],5)), "text")
                self.txt_sp.insert(END, "\n", "text")
                self.txt_sp.insert(END, "\n", "text")
                self.txt_sp.insert(END, u"Test založený na šikmosti:", "podnadpis")
                self.txt_sp.insert(END, "\n", "text")
                if (vysledek_sp[0])>=vysledek_sp[2]:
                    self.txt_sp.insert(END, u"Protože |U(A3)| je větší nebo rovno než kritická hodnota u(\u03B1/2), zamítáme hypotézu H0", "text")
                    self.txt_sp.insert(END, "\n", "text")
                    self.txt_sp.insert(END, u"ve prospěch alternativy na hladině významnosti \u03B1= " + str(self.sp_hodnota_hladina.get()) + u".", "text")
                else:
                    self.txt_sp.insert(END, u"Protože |U(A3)| je menží než kritická hodnota u(\u03B1), nezamítáme", "text")
                    self.txt_sp.insert(END, "\n", "text")
                    self.txt_sp.insert(END, u"hypotézu H0 na hladině významnosti \u03B1= " + str(self.sp_hodnota_hladina.get()) +u".", "text")
                self.txt_sp.insert(END, "\n", "text")
                self.txt_sp.insert(END, "\n", "text")
                self.txt_sp.insert(END, u"Test založený na špičatosti:", "podnadpis")
                self.txt_sp.insert(END, "\n", "text")
                if (vysledek_sp[1])>=vysledek_sp[2]:
                    self.txt_sp.insert(END, u"Protože |U(A4)| je větší nebo rovno než kritická hodnota u(\u03B1/2), zamítáme hypotézu H0", "text")
                    self.txt_sp.insert(END, "\n", "text")
                    self.txt_sp.insert(END, u"ve prospěch alternativy na hladině významnosti \u03B1= " + str(self.sp_hodnota_hladina.get()) + u".", "text")
                else:
                    self.txt_sp.insert(END, u"Protože |U(A4)| je menží než kritická hodnota u(\u03B1), nezamítáme", "text")
                    self.txt_sp.insert(END, "\n", "text")
                    self.txt_sp.insert(END, u"hypotézu H0 na hladině významnosti \u03B1= " + str(self.sp_hodnota_hladina.get()) +u".", "text")
                self.txt_sp.insert(END, "\n", "text")
                self.txt_sp.insert(END, "\n", "text")
                self.txt_sp.insert(END, u"Shrnutí:", "podnadpis")
                self.txt_sp.insert(END, "\n", "text")
                if ((vysledek_sp[0])<vysledek_sp[2]) and ((vysledek_sp[1])<vysledek_sp[2]):
                    self.txt_sp.insert(END, "Protože oba testy nezamítají hypotézu H0, celkový test také nezamítá hypotézu H0. ", "text")
                else:
                    self.txt_sp.insert(END, "Protože alespoň jeden test zamítá hypotézu H0, celkový test také zamítá\nhypotézu H0.", "text")
                self.txt_sp.tag_config("podnadpis", underline=1, font="Arial 10")
                self.txt_sp.tag_config("nadpis", underline=1, font="Arial 10 bold")
                self.txt_sp.tag_config("text", font="Arial 10")
                self.txt_sp.config(state=DISABLED)

    def pearson(self):
        self.pea_hodnota_hladina=DoubleVar()
        self.pea_zalozky=self.soubor.sheet_names()
        self.pea_t=Toplevel()
        self.pea_t.title(u'Test Pearsonova rozdělení')
        self.fr_pea_levy=Frame(self.pea_t)
#### prvni listbox #####
        self.fr_pea_levy1=LabelFrame(self.fr_pea_levy, relief=GROOVE, borderwidth=2, text=u'Typ *(povinna)')
        self.pea_li1 = Listbox(self.fr_pea_levy1, width=30, height=10)
        self.pea_sy1 = Scrollbar(self.fr_pea_levy1, orient="vertical", command=self.pea_li1.yview)  
        self.pea_la1 = Label(self.fr_pea_levy1, text=u"Není vybrana žádná kategorie", foreground="red")
        self.pea_li1.configure(yscrollcommand=self.pea_sy1.set)
        pea_seznam_kat=[]
        pea_seznam_mest=[]
        sh=self.soubor.sheet_by_name(self.pea_zalozky[0])
        for col in range(sh.ncols): #vytvori seznam kategorii
            pea_seznam_kat.append(sh.col_values(col)[0])
        del pea_seznam_kat[0:13]
        del pea_seznam_kat[(len(pea_seznam_kat)-1)]
        del pea_seznam_kat[(len(pea_seznam_kat)-1)]
        for polozka in pea_seznam_kat:
            self.pea_li1.insert(END, polozka)
        
        self.pea_li1.grid(row=0, column=0, padx=4, pady=8)
        self.pea_sy1.grid(row=0, column=1, sticky="ns", pady=8)
        self.pea_la1.grid(row=1, column=0, columnspan=2)
        
        self.pea_li1.bind("<Double-B1-ButtonRelease>", self.pea_li1_double)
        self.kategorie_pea1='' #pomocna promenna ktera se naplni v pripade zadani kategorie, jinak bude uzivatel upozornen ze nevybral promennou
        self.fr_pea_levy1.pack(fill='both', expand=1, padx=2, pady=2, side='left', anchor=W)
##### druhy listbox ######
        pea_seznam_mest=[]
        for row in range(sh.nrows): #vytvori seznam kategorii
            if (sh.row_values(row)[6] in pea_seznam_mest) !=True:
                pea_seznam_mest.append(sh.row_values(row)[6])
        del pea_seznam_mest[0]
        self.fr_pea_levy2=LabelFrame(self.fr_pea_levy, relief=GROOVE, borderwidth=2, text=u'Oblast')
        self.pea_li2 = Listbox(self.fr_pea_levy2, width=30, height=10)
        self.pea_sy2 = Scrollbar(self.fr_pea_levy2, orient="vertical", command=self.pea_li2.yview)  
        self.pea_la2 = Label(self.fr_pea_levy2, text=u"Není vybrana žádná kategorie", foreground="red")
        self.pea_li2.configure(yscrollcommand=self.pea_sy2.set)
        mesta=pea_seznam_mest
        mesta.sort()
        for polozka in mesta:
            self.pea_li2.insert(END, polozka)
        self.pea_li2.grid(row=0, column=0, padx=4, pady=8)
        self.pea_sy2.grid(row=0, column=1, sticky="ns", pady=8)
        self.pea_la2.grid(row=1, column=0, columnspan=2)
        
        self.pea_li2.bind("<Double-B1-ButtonRelease>", self.pea_li2_double)
        self.kategorie_pea2='' #pomocna promenna ktera se naplni v pripade zadani kategorie, jinak bude uzivatel upozornen ze nevybral promennou
        self.fr_pea_levy2.pack(fill='both', expand=1, padx=2, pady=2, side='right', anchor=E)
        self.fr_pea_levy.pack(fill='both', expand=1, side='left', anchor=W)
####### prava strana s parametry #####
        self.fr_pea_pravy=Frame(self.pea_t)
        self.fr_pea_prava1=LabelFrame(self.fr_pea_pravy, relief=GROOVE, borderwidth=2, text=u'Hladina významnosti \u03B1')
        self.ra_pea0_01 = Radiobutton(self.fr_pea_prava1, text=u"\u03B1 = 0.01", variable=self.pea_hodnota_hladina, value=0.01)
        self.ra_pea0_01.pack(side='left', padx=4)
        self.ra_pea0_05 = Radiobutton(self.fr_pea_prava1, text=u"\u03B1 = 0.05", variable=self.pea_hodnota_hladina, value=0.05)
        self.ra_pea0_05.pack(side='left', padx=4)
        self.ra_pea0_1 = Radiobutton(self.fr_pea_prava1, text=u"\u03B1 = 0.1", variable=self.pea_hodnota_hladina, value=0.1)
        self.ra_pea0_1.pack(side='left', padx=4)
        self.fr_pea_prava1.pack(fill = 'x',expand=1, side="top", anchor=N)
        self.fr_pea_prava2=LabelFrame(self.fr_pea_pravy, relief=GROOVE, borderwidth=2, text=u'Počet stupňů volnosti')
        self.en_pea_t = Entry(self.fr_pea_prava2)
        self.en_pea_t.pack(side="top", padx=4, pady=4, fill="x")
        self.fr_pea_prava2.pack(fill = 'x',expand=1, anchor=N)
        self.fr_pea_prava5=Frame(self.fr_pea_pravy)
        self.fr_pea_la3=Label(self.fr_pea_prava5, text=u"Vyberte parametry", foreground="#00B000")
        self.fr_pea_la3.pack(fill="both", expand=1, anchor=N)
        self.fr_pea_prava5.pack(fill = 'both',expand=1, anchor=N)
        self.fr_pea_prava4=Frame(self.fr_pea_pravy)
        self.pea_bu_testovat1=Button(self.fr_pea_pravy, text=u"Testovat typ", command=self.pearson1)
        self.pea_bu_testovat1.pack(padx=4, pady=4, side='right')
        self.pea_bu_testovat2=Button(self.fr_pea_pravy, text=u"Testovat podle oblasti", command=self.pearson2)
        self.pea_bu_testovat2.pack(padx=4, pady=4, side='right')
        self.fr_pea_prava4.pack(fill = 'both',expand=1, anchor=N)
        self.fr_pea_pravy.pack(fill='both', expand=1, side='right', anchor=E, padx=4, pady=4)
        self.ra_pea0_01.select()

    def pearson2(self):
        self.pearson1("podle mest")

    def pearson1(self, typ="typ"):
        #print typ
        if typ=="podle mest":
            if self.kategorie_pea2=='':
                return
        if self.kategorie_pea1=='':
            return
        elif self.en_pea_t.get()=="":
            self.fr_pea_la3.configure(text="Nezadali jste počet stupňů volnosti", foreground="red")
        else:
            sh=self.soubor.sheet_by_name(self.pea_zalozky[0])
            data=[]
            for col in range(sh.ncols): #zjisti cislo sloupce na zaklade ziskane hodnoty jmena
                if sh.col_values(col)[0]==self.kategorie_pea1:
                    zalozka1=col
            if typ=="podle mest":
                for row in range(sh.nrows):
                    if sh.row_values(row)[6]==self.kategorie_pea2:
                        data.append(sh.row_values(row)[zalozka1])
            else:
                for row in range(sh.nrows):
                    data.append(sh.row_values(row)[zalozka1])
                nazev1=data[0]
                del data[0]
            pom_data1=[]
            for prvek in data:
                if grafy.is_number(prvek)==True:
                    pom_data1.append(prvek)
            if len(pom_data1)<=3:
                self.nedostatecny_rozsah()
                self.txt_maly_rozsah.insert(END, u"Rozsah výběru n = " + str(len(pom_data1)) + u". Minimální rozsah výběru pro spuštění testu je 4.", "text")
            else:
                self.fr_pea_la3.configure(text="OK", foreground="#00B000")
                vysledek_pea=testy.test_z_chi_kvadratu(pom_data1, int(self.en_pea_t.get()),self.pea_hodnota_hladina.get())
                self.oznameni_pea=Toplevel()
                self.oznameni_pea.title('Vyhodnocení testu o Pearsonově rozdělení')
                self.txt_pea=Text(self.oznameni_pea, width=100, height=20)
                self.scrol_pea=Scrollbar(self.oznameni_pea)
                self.scrol_pea.pack(side=RIGHT, fill=Y)
                self.txt_pea.pack(expand=1, fill=BOTH)
                self.txt_pea.focus_set()
                self.scrol_pea.config(command=self.txt_pea.yview)
                self.txt_pea.config(yscrollcommand=self.scrol_pea.set)
                self.txt_pea.delete(1.0, END)
                self.txt_pea.insert(END, u"Test Pearsonova rozdělení", "nadpis")
                self.txt_pea.insert(END, "\n", "text")
                self.txt_pea.insert(END, "\n", "text")
                self.txt_pea.insert(END, u"\u03B1 = "+str(self.pea_hodnota_hladina.get()), "text")
                self.txt_pea.insert(END, "\n", "text")
                self.txt_pea.insert(END, u"H0: Výběr pochází z Pearsonova rozdělení s "+self.en_pea_t.get()+u" stupňů volnosti.", "text")
                self.txt_pea.insert(END, "\n", "text")
                self.txt_pea.insert(END, u"Ha: Výběr nepochází z Pearsonova rozdělení s "+self.en_pea_t.get()+u" stupňů volnosti.", "text")
                self.txt_pea.insert(END, "\n", "text")
                self.txt_pea.insert(END, u"Dn = " + str(round(vysledek_pea[0],5)), "text")
                self.txt_pea.insert(END, "\n", "text")
                self.txt_pea.insert(END, u"Dn(\u03B1) = " + str(round(vysledek_pea[1],5)), "text")
                self.txt_pea.insert(END, "\n", "text")
                self.txt_pea.insert(END, "\n", "text")
                if (vysledek_pea[0])>=vysledek_pea[1]:
                    self.txt_pea.insert(END, u"Protože Dn je větší nebo rovno než kritická hodnota Dn(\u03B1), zamítáme hypotézu H0", "text")
                    self.txt_pea.insert(END, "\n", "text")
                    self.txt_pea.insert(END, u"ve prospěch alternativy na hladině významnosti \u03B1= " + str(self.pea_hodnota_hladina.get()) + u".", "text")
                else:
                    self.txt_pea.insert(END, u"Protože Dn je menží než kritická hodnota Dn(\u03B1), nezamítáme", "text")
                    self.txt_pea.insert(END, "\n", "text")
                    self.txt_pea.insert(END, u"hypotézu H0 na hladině významnosti \u03B1= " + str(self.pea_hodnota_hladina.get()) +u".", "text")
                self.txt_pea.insert(END, "\n", "text")
                self.txt_pea.insert(END, "\n", "text")
                self.txt_pea.tag_config("podnadpis", underline=1, font="Arial 10")
                self.txt_pea.tag_config("nadpis", underline=1, font="Arial 10 bold")
                self.txt_pea.tag_config("text", font="Arial 10")
                self.txt_pea.config(state=DISABLED)

    def kolmogoruv_smirdotonuv_test(self):#vyuzivan i k testu normality podle spicatosti a sikmosti
        self.ks_hodnota_hladina=DoubleVar()
        self.ks_zalozky=self.soubor.sheet_names()
        self.ks_t=Toplevel()
        self.ks_t.title(u'Kolmogorův-Smirdotonův test')
        self.fr_ks_levy=Frame(self.ks_t)
#### prvni listbox #####
        self.fr_ks_levy1=LabelFrame(self.fr_ks_levy, relief=GROOVE, borderwidth=2, text=u'Typ *(povinna)')
        self.ks_li1 = Listbox(self.fr_ks_levy1, width=30, height=10)
        self.ks_sy1 = Scrollbar(self.fr_ks_levy1, orient="vertical", command=self.ks_li1.yview)  
        self.ks_la1 = Label(self.fr_ks_levy1, text=u"Není vybrana žádná kategorie", foreground="red")
        self.ks_li1.configure(yscrollcommand=self.ks_sy1.set)
        ks_seznam_kat=[]
        ks_seznam_mest=[]
        sh=self.soubor.sheet_by_name(self.ks_zalozky[0])
        for col in range(sh.ncols): #vytvori seznam kategorii
            ks_seznam_kat.append(sh.col_values(col)[0])
        del ks_seznam_kat[0:13]
        del ks_seznam_kat[(len(ks_seznam_kat)-1)]
        del ks_seznam_kat[(len(ks_seznam_kat)-1)]
        for polozka in ks_seznam_kat:
            self.ks_li1.insert(END, polozka)
        
        self.ks_li1.grid(row=0, column=0, padx=4, pady=8)
        self.ks_sy1.grid(row=0, column=1, sticky="ns", pady=8)
        self.ks_la1.grid(row=1, column=0, columnspan=2)
        
        self.ks_li1.bind("<Double-B1-ButtonRelease>", self.ks_li1_double)
        self.kategorie_ks1='' #pomocna promenna ktera se naplni v pripade zadani kategorie, jinak bude uzivatel upozornen ze nevybral promennou
        self.fr_ks_levy1.pack(fill='both', expand=1, padx=2, pady=2, side='left', anchor=W)
##### druhy listbox ######
        ks_seznam_mest=[]
        for row in range(sh.nrows): #vytvori seznam kategorii
            if (sh.row_values(row)[6] in ks_seznam_mest) !=True:
                ks_seznam_mest.append(sh.row_values(row)[6])
        del ks_seznam_mest[0]
        self.fr_ks_levy2=LabelFrame(self.fr_ks_levy, relief=GROOVE, borderwidth=2, text=u'Oblast')
        self.ks_li2 = Listbox(self.fr_ks_levy2, width=30, height=10)
        self.ks_sy2 = Scrollbar(self.fr_ks_levy2, orient="vertical", command=self.ks_li2.yview)  
        self.ks_la2 = Label(self.fr_ks_levy2, text=u"Není vybrana žádná kategorie", foreground="red")
        self.ks_li2.configure(yscrollcommand=self.ks_sy2.set)
        mesta=ks_seznam_mest
        mesta.sort()
        for polozka in mesta:
            self.ks_li2.insert(END, polozka)
        self.ks_li2.grid(row=0, column=0, padx=4, pady=8)
        self.ks_sy2.grid(row=0, column=1, sticky="ns", pady=8)
        self.ks_la2.grid(row=1, column=0, columnspan=2)
        
        self.ks_li2.bind("<Double-B1-ButtonRelease>", self.ks_li2_double)
        self.kategorie_ks2='' #pomocna promenna ktera se naplni v pripade zadani kategorie, jinak bude uzivatel upozornen ze nevybral promennou
        self.fr_ks_levy2.pack(fill='both', expand=1, padx=2, pady=2, side='right', anchor=E)
        self.fr_ks_levy.pack(fill='both', expand=1, side='left', anchor=W)
####### prava strana s parametry #####
        self.fr_ks_pravy=Frame(self.ks_t)
        self.fr_ks_prava1=LabelFrame(self.fr_ks_pravy, relief=GROOVE, borderwidth=2, text=u'Hladina významnosti \u03B1')
        self.ra_ks0_01 = Radiobutton(self.fr_ks_prava1, text=u"\u03B1 = 0.01", variable=self.ks_hodnota_hladina, value=0.01)
        self.ra_ks0_01.pack(side='left', padx=4)
        self.ra_ks0_05 = Radiobutton(self.fr_ks_prava1, text=u"\u03B1 = 0.05", variable=self.ks_hodnota_hladina, value=0.05)
        self.ra_ks0_05.pack(side='left', padx=4)
        self.ra_ks0_1 = Radiobutton(self.fr_ks_prava1, text=u"\u03B1 = 0.1", variable=self.ks_hodnota_hladina, value=0.1)
        self.ra_ks0_1.pack(side='left', padx=4)
        self.fr_ks_prava1.pack(fill = 'x',expand=1, side="top", anchor=N)
        self.fr_ks_prava2=LabelFrame(self.fr_ks_pravy, relief=GROOVE, borderwidth=2, text=u'Střední hodnota \u03BC')
        self.en_ks_t = Entry(self.fr_ks_prava2)
        self.en_ks_t.pack(side="top", padx=4, pady=4, fill="x")
        self.fr_ks_prava2.pack(fill = 'x',expand=1, anchor=N)
        self.fr_ks_prava3=LabelFrame(self.fr_ks_pravy, relief=GROOVE, borderwidth=2, text=u'Směrodatná odchylka \u03C3')
        self.en_ks_t2 = Entry(self.fr_ks_prava3)
        self.en_ks_t2.pack(side="top", padx=4, pady=4, fill="x")
        self.fr_ks_prava3.pack(fill = 'x',expand=1, anchor=N)
        self.fr_ks_prava5=Frame(self.fr_ks_pravy)
        self.fr_ks_la3=Label(self.fr_ks_prava5, text=u"Vyberte parametry", foreground="#00B000")
        self.fr_ks_la3.pack(fill="both", expand=1, anchor=N)
        self.fr_ks_prava5.pack(fill = 'both',expand=1, anchor=N)
        self.fr_ks_prava4=Frame(self.fr_ks_pravy)
        self.ks_bu_testovat1=Button(self.fr_ks_pravy, text=u"Testovat typ", command=self.kol_smir_test)
        self.ks_bu_testovat1.pack(padx=4, pady=4, side='right')
        self.ks_bu_testovat2=Button(self.fr_ks_pravy, text=u"Testovat podle oblasti", command=self.kol_smir_test1)
        self.ks_bu_testovat2.pack(padx=4, pady=4, side='right')
        self.fr_ks_prava4.pack(fill = 'both',expand=1, anchor=N)
        self.fr_ks_pravy.pack(fill='both', expand=1, side='right', anchor=E, padx=4, pady=4)
        self.ra_ks0_01.select()

    def kol_smir_test(self):
        if self.kategorie_ks1=='':
            return
        elif self.en_ks_t.get()=="":
            self.fr_ks_la3.configure(text=u"Nezadali jste střední hodnotu", foreground="red")
            return
        elif self.en_ks_t2.get()=="":
            self.fr_ks_la3.configure(text=u"Nezadali jste směrodatnou odchylku", foreground="red")
            return
        else:
            self.fr_ks_la3.configure(text=u"OK", foreground="#00B000")
            sh=self.soubor.sheet_by_name(self.ks_zalozky[0])
            data=[]
            for col in range(sh.ncols): #zjisti cislo sloupce na zaklade ziskane hodnoty jmena
                if sh.col_values(col)[0]==self.kategorie_ks1:
                    zalozka1=col
            for row in range(sh.nrows):
                data.append(sh.row_values(row)[zalozka1])
            nazev1=data[0]
            del data[0]
            pom_data1=[]
            for prvek in data:
                if grafy.is_number(prvek)==True:
                    pom_data1.append(prvek)
            if len(pom_data1)==0:
                self.nedostatecny_rozsah()
                self.txt_maly_rozsah.insert(END, u"Rozsah výběru n = " + str(len(pom_data1)) + u". Minimální rozsah výběru pro spuštění testu je 1.", "text")
                return
            vysledek_ks=testy.jednov_kolm_smir_test(pom_data1, float(self.en_ks_t.get()), float(self.en_ks_t2.get()), self.ks_hodnota_hladina.get())
            self.oznameni_ks=Toplevel()
            self.oznameni_ks.title('Vyhodnocení Kolmogorova-Smirnovova testu')
            self.txt_ks=Text(self.oznameni_ks, width=100, height=20)
            self.scrol_ks=Scrollbar(self.oznameni_ks)
            self.scrol_ks.pack(side=RIGHT, fill=Y)
            self.txt_ks.pack(expand=1, fill=BOTH)
            self.txt_ks.focus_set()
            self.scrol_ks.config(command=self.txt_ks.yview)
            self.txt_ks.config(yscrollcommand=self.scrol_ks.set)
            self.txt_ks.delete(1.0, END)
            self.txt_ks.insert(END, u"Kolmogorovův-Smirnovův test (test normality)", "nadpis")
            self.txt_ks.insert(END, "\n", "text")
            self.txt_ks.insert(END, "\n", "text")
            self.txt_ks.insert(END, u"\u03B1 = "+str(self.ks_hodnota_hladina.get()), "text")
            self.txt_ks.insert(END, "\n", "text")
            self.txt_ks.insert(END, u"H0: Výběr pochází z normálního rozdělení N("+self.en_ks_t.get()+"; "+self.en_ks_t2.get()+")", "text")
            self.txt_ks.insert(END, "\n", "text")
            self.txt_ks.insert(END, u"Ha: Výběr nepochází z normálního rozdělení N("+self.en_ks_t.get()+"; "+self.en_ks_t2.get()+")", "text")
            self.txt_ks.insert(END, "\n", "text")
            self.txt_ks.insert(END, u"Dn = " + str(round(vysledek_ks[0],5)), "text")
            self.txt_ks.insert(END, "\n", "text")
            self.txt_ks.insert(END, u"Dn(\u03B1) = " + str(round(vysledek_ks[1],5)), "text")
            self.txt_ks.insert(END, "\n", "text")
            self.txt_ks.insert(END, "\n", "text")
            if (vysledek_ks[0])>=vysledek_ks[1]:
                self.txt_ks.insert(END, u"Protože Dn je větší nebo rovno než kritická hodnota Dn(\u03B1), zamítáme hypotézu H0", "text")
                self.txt_ks.insert(END, "\n", "text")
                self.txt_ks.insert(END, u"ve prospěch alternativy na hladině významnosti \u03B1= " + str(self.ks_hodnota_hladina.get()) + u".", "text")
            else:
                self.txt_ks.insert(END, u"Protože Dn je menží než kritická hodnota Dn(\u03B1), nezamítáme", "text")
                self.txt_ks.insert(END, "\n", "text")
                self.txt_ks.insert(END, u"hypotézu H0 na hladině významnosti \u03B1= " + str(self.ks_hodnota_hladina.get()) +u".", "text")
            self.txt_ks.tag_config("nadpis", underline=1, font="Arial 10 bold")
            self.txt_ks.tag_config("text", font="Arial 10")
            self.txt_ks.config(state=DISABLED)

    def kol_smir_test1(self):
        if self.kategorie_ks1=='':
            return
        if self.kategorie_ks2=='':
            return
        elif self.en_ks_t.get()=="":
            self.fr_ks_la3.configure(text=u"Nezadali jste střední hodnotu", foreground="red")
            return
        elif self.en_ks_t2.get()=="":
            self.fr_ks_la3.configure(text=u"Nezadali jste směrodatnou odchylku", foreground="red")
            return
        else:
            self.fr_ks_la3.configure(text=u"OK", foreground="#00B000")
            sh=self.soubor.sheet_by_name(self.ks_zalozky[0])
            data=[]
            for col in range(sh.ncols): #zjisti cislo sloupce na zaklade ziskane hodnoty jmena
                if sh.col_values(col)[0]==self.kategorie_ks1:
                    zalozka1=col
            for row in range(sh.nrows):
                if sh.row_values(row)[6]==self.kategorie_ks2:
                    data.append(sh.row_values(row)[zalozka1])
            nazev1=zalozka1
            pom_data1=[]
            for prvek in data:
                if grafy.is_number(prvek)==True:
                    pom_data1.append(prvek)
            if len(pom_data1)==0:
                self.nedostatecny_rozsah()
                self.txt_maly_rozsah.insert(END, u"Rozsah výběru n = " + str(len(pom_data1)) + u". Minimální rozsah výběru pro spuštění testu je 1.", "text")
                return
            else:
                vysledek_ks=testy.jednov_kolm_smir_test(pom_data1, float(self.en_ks_t.get()), float(self.en_ks_t2.get()), self.ks_hodnota_hladina.get())
                self.oznameni_ks=Toplevel()
                self.oznameni_ks.title('Vyhodnocení Kolmogorova-Smirnovova testu')
                self.txt_ks=Text(self.oznameni_ks, width=100, height=20)
                self.scrol_ks=Scrollbar(self.oznameni_ks)
                self.scrol_ks.pack(side=RIGHT, fill=Y)
                self.txt_ks.pack(expand=1, fill=BOTH)
                self.txt_ks.focus_set()
                self.scrol_ks.config(command=self.txt_ks.yview)
                self.txt_ks.config(yscrollcommand=self.scrol_ks.set)
                self.txt_ks.delete(1.0, END)
                self.txt_ks.insert(END, u"Kolmogorovův-Smirnovův test (test normality)", "nadpis")
                self.txt_ks.insert(END, "\n", "text")
                self.txt_ks.insert(END, "\n", "text")
                self.txt_ks.insert(END, u"\u03B1 = "+str(self.ks_hodnota_hladina.get()), "text")
                self.txt_ks.insert(END, "\n", "text")
                self.txt_ks.insert(END, u"H0: Výběr pochází z normálního rozdělení N("+self.en_ks_t.get()+"; "+self.en_ks_t2.get()+")", "text")
                self.txt_ks.insert(END, "\n", "text")
                self.txt_ks.insert(END, u"Ha: Výběr nepochází z normálního rozdělení N("+self.en_ks_t.get()+"; "+self.en_ks_t2.get()+")", "text")
                self.txt_ks.insert(END, "\n", "text")
                self.txt_ks.insert(END, u"Dn = " + str(round(vysledek_ks[0],5)), "text")
                self.txt_ks.insert(END, "\n", "text")
                self.txt_ks.insert(END, u"Dn(\u03B1) = " + str(round(vysledek_ks[1],5)), "text")
                self.txt_ks.insert(END, "\n", "text")
                self.txt_ks.insert(END, "\n", "text")
                if (vysledek_ks[0])>=vysledek_ks[1]:
                    self.txt_ks.insert(END, u"Protože Dn je větší nebo rovno než kritická hodnota Dn(\u03B1), zamítáme hypotézu H0", "text")
                    self.txt_ks.insert(END, "\n", "text")
                    self.txt_ks.insert(END, u"ve prospěch alternativy na hladině významnosti \u03B1= " + str(self.ks_hodnota_hladina.get()) + u".", "text")
                else:
                    self.txt_ks.insert(END, u"Protože Dn je menží než kritická hodnota Dn(\u03B1), nezamítáme", "text")
                    self.txt_ks.insert(END, "\n", "text")
                    self.txt_ks.insert(END, u"hypotézu H0 na hladině významnosti \u03B1= " + str(self.ks_hodnota_hladina.get()) +u".", "text")
                self.txt_ks.tag_config("nadpis", underline=1, font="Arial 10 bold")
                self.txt_ks.tag_config("text", font="Arial 10")
                self.txt_ks.config(state=DISABLED)
            
    def mannuv_whitneyuv_test(self):
        self.ma_hodnota_hladina=DoubleVar()
        self.ma_hodnota_Ha=StringVar()
        self.ma_zalozky=self.soubor.sheet_names()
        self.ma_t=Toplevel()
        self.ma_t.title(u'Mannův-Whitneyův test')

        self.fr_ma_levy=Frame(self.ma_t)
#### prvni listbox #####
        self.fr_ma_levy1=Frame(self.fr_ma_levy)
        self.ma_li1 = Listbox(self.fr_ma_levy1, width=30, height=10)
        self.ma_sy1 = Scrollbar(self.fr_ma_levy1, orient="vertical", command=self.ma_li1.yview)  
        self.ma_la1 = Label(self.fr_ma_levy1, text=u"Není vybrana žádná kategorie", foreground="red")
        self.ma_li1.configure(yscrollcommand=self.ma_sy1.set)
        ma_seznam_kat=[]
        sh=self.soubor.sheet_by_name(self.ma_zalozky[0])
        for col in range(sh.ncols): #vytvori seznam kategorii
                ma_seznam_kat.append(sh.col_values(col)[0])
        del ma_seznam_kat[0:13]
        del ma_seznam_kat[(len(ma_seznam_kat)-1)]
        del ma_seznam_kat[(len(ma_seznam_kat)-1)]
        for polozka in ma_seznam_kat:
            self.ma_li1.insert(END, polozka)
        
        self.ma_li1.grid(row=0, column=0, padx=4, pady=8)
        self.ma_sy1.grid(row=0, column=1, sticky="ns", pady=8)
        self.ma_la1.grid(row=1, column=0, columnspan=2)
        
        self.ma_li1.bind("<Double-B1-ButtonRelease>", self.ma_li1_double)
        self.kategorie_ma1='' #pomocna promenna ktera se naplni v pripade zadani kategorie, jinak bude uzivatel upozornen ze nevybral promennou
        self.fr_ma_levy1.pack(fill='both', expand=1, padx=2, pady=2, side='left', anchor=W)
##### druhy listbox ######
        self.fr_ma_levy2=Frame(self.fr_ma_levy)
        self.ma_li2 = Listbox(self.fr_ma_levy2, width=30, height=10)
        self.ma_sy2 = Scrollbar(self.fr_ma_levy2, orient="vertical", command=self.ma_li2.yview)  
        self.ma_la2 = Label(self.fr_ma_levy2, text=u"Není vybrana žádná kategorie", foreground="red")
        self.ma_li2.configure(yscrollcommand=self.ma_sy2.set)
        
        for polozka in ma_seznam_kat:
            self.ma_li2.insert(END, polozka)
        
        self.ma_li2.grid(row=0, column=0, padx=4, pady=8)
        self.ma_sy2.grid(row=0, column=1, sticky="ns", pady=8)
        self.ma_la2.grid(row=1, column=0, columnspan=2)
        
        self.ma_li2.bind("<Double-B1-ButtonRelease>", self.ma_li2_double)
        self.kategorie_ma2='' #pomocna promenna ktera se naplni v pripade zadani kategorie, jinak bude uzivatel upozornen ze nevybral promennou
        self.fr_ma_levy2.pack(fill='both', expand=1, padx=2, pady=2, side='right', anchor=E)
        self.fr_ma_levy.pack(fill='both', expand=1, side='left', anchor=W)
##### prava strana s parametry #####
        self.fr_ma_pravy=Frame(self.ma_t)

        self.fr_ma_prava1=LabelFrame(self.fr_ma_pravy, relief=GROOVE, borderwidth=2, text=u'Hladina významnosti \u03B1')
        self.ra_ma0_01 = Radiobutton(self.fr_ma_prava1, text=u"\u03B1 = 0.01", variable=self.ma_hodnota_hladina, value=0.01)
        self.ra_ma0_01.pack(side='left', padx=4)
        self.ra_ma0_05 = Radiobutton(self.fr_ma_prava1, text=u"\u03B1 = 0.05", variable=self.ma_hodnota_hladina, value=0.05)
        self.ra_ma0_05.pack(side='left', padx=4)
        self.ra_ma0_1 = Radiobutton(self.fr_ma_prava1, text=u"\u03B1 = 0.1", variable=self.ma_hodnota_hladina, value=0.1)
        self.ra_ma0_1.pack(side='left', padx=4)
        self.fr_ma_prava1.pack(fill = 'x', side="top", anchor=N)
        
##        self.la_ma_med = Label(self.fr_ma_prava2, text=u"Zadejte hodnotu 0-100 [%]", foreground="#00B000")
##        self.la_ma_med.pack(fill="both", padx=4, pady=4, anchor=S)
        
        self.fr_ma_prava3=LabelFrame(self.fr_ma_pravy, relief=GROOVE, borderwidth=2, text=u'Zvolte Ha')
        self.ra_ma_mensi = Radiobutton(self.fr_ma_prava3, text=u"\u03BC1 < \u03BC2", variable=self.ma_hodnota_Ha, value='<')
        self.ra_ma_mensi.pack(padx=4, side='left')
        self.ra_ma_vetsi = Radiobutton(self.fr_ma_prava3, text=u"\u03BC1 > \u03BC2", variable=self.ma_hodnota_Ha, value='>')
        self.ra_ma_vetsi.pack(padx=4, side='left')
        self.ra_ma_ruzne = Radiobutton(self.fr_ma_prava3, text=u"\u03BC1 \u2260 \u03BC2", variable=self.ma_hodnota_Ha, value=u'\u2260')
        self.ra_ma_ruzne.pack(padx=4, side='left') 
        self.fr_ma_prava3.pack(fill = 'x', anchor=N, side="top")
        #self.fr_ma_prava4=Frame(self.fr_ma_pravy)
        
        self.ma_bu_testovat=Button(self.fr_ma_pravy, text=u"Testovat", command=self.test_ma)
        self.ma_bu_testovat.pack(padx=4, pady=4, side='right', anchor=SE)
        
        #self.fr_ma_prava4.pack(fill = 'both',expand=1)
        self.ra_ma0_01.select()
        self.ra_ma_mensi.select()
        
        self.fr_ma_pravy.pack(fill='both', expand=1, side='right', anchor=E, padx=4, pady=4)
        
    def wilcoxonuv_test(self):
        self.wi_hodnota_hladina=DoubleVar()
        self.wi_hodnota_Ha=StringVar()
        self.wi_zalozky=self.soubor.sheet_names()
        self.wi_t=Toplevel()
        self.wi_t.title(u'Wilcoxonův test')
        self.fr_wi_t=Frame(self.wi_t)
#### listbox vlevo #####
        self.fr_wi_t_leva=Frame(self.fr_wi_t)
        self.wi_li = Listbox(self.fr_wi_t_leva, width=30, height=10)
        self.wi_sy = Scrollbar(self.fr_wi_t_leva, orient="vertical", command=self.wi_li.yview)  
        self.wi_la = Label(self.fr_wi_t_leva, text=u"Není vybrana žádná kategorie", foreground="red")
        self.wi_li.configure(yscrollcommand=self.wi_sy.set)
        wi_seznam_kat=[]
        sh=self.soubor.sheet_by_name(self.wi_zalozky[0])
        for col in range(sh.ncols): #vytvori seznam kategorii
                wi_seznam_kat.append(sh.col_values(col)[0])
        del wi_seznam_kat[0:13]
        del wi_seznam_kat[(len(wi_seznam_kat)-1)]
        del wi_seznam_kat[(len(wi_seznam_kat)-1)]
        for polozka in wi_seznam_kat:
            self.wi_li.insert(END, polozka)
        
        self.wi_li.grid(row=0, column=0, padx=4, pady=8)
        self.wi_sy.grid(row=0, column=1, sticky="ns", pady=8)
        self.wi_la.grid(row=1, column=0, columnspan=2)
        
        self.wi_li.bind("<Double-B1-ButtonRelease>", self.wi_li_double)
        self.kategorie_wi='' #pomocna promenna ktera se naplni v pripade zadani kategorie, jinak bude uzivatel upozornen ze nevybral promennou
        self.fr_wi_t_leva.pack(fill = 'both',expand=1, side="left", anchor=W)
##### frame s parametry vpravo #####
        self.fr_wi_t_prava=Frame(self.fr_wi_t)
        self.fr_wi_t_prava1=LabelFrame(self.fr_wi_t_prava, relief=GROOVE, borderwidth=2, text=u'Hladina významnosti \u03B1')
        self.ra_wi0_01 = Radiobutton(self.fr_wi_t_prava1, text=u"\u03B1 = 0.01", variable=self.wi_hodnota_hladina, value=0.01)
        self.ra_wi0_01.pack(side='left', padx=4)
        self.ra_wi0_05 = Radiobutton(self.fr_wi_t_prava1, text=u"\u03B1 = 0.05", variable=self.wi_hodnota_hladina, value=0.05)
        self.ra_wi0_05.pack(side='left', padx=4)
        self.ra_wi0_1 = Radiobutton(self.fr_wi_t_prava1, text=u"\u03B1 = 0.1", variable=self.wi_hodnota_hladina, value=0.1)
        self.ra_wi0_1.pack(side='left', padx=4)
        self.fr_wi_t_prava1.pack(fill = 'both',expand=1, side="top", anchor=N)
        self.fr_wi_t_prava2=LabelFrame(self.fr_wi_t_prava, relief=GROOVE, borderwidth=2, text=u'Zvolte medián [%]')
        self.en_wi_t = Entry(self.fr_wi_t_prava2)
        self.en_wi_t.pack(side="top", padx=4, pady=4, fill="x")
        self.la_wi_med = Label(self.fr_wi_t_prava2, text=u"Zadejte hodnotu 0-100 [%]", foreground="#00B000")
        self.la_wi_med.pack(fill="both", padx=4, pady=4, anchor=S)
        self.fr_wi_t_prava2.pack(fill = 'both',expand=1, anchor=S)
        self.fr_wi_t_prava3=LabelFrame(self.fr_wi_t_prava, relief=GROOVE, borderwidth=2, text=u'Zvolte Ha')
        self.ra_wi_mensi = Radiobutton(self.fr_wi_t_prava3, text=u"\u03BC < \u03BC0", variable=self.wi_hodnota_Ha, value='<')
        self.ra_wi_mensi.pack(padx=4, side='left')
        self.ra_wi_vetsi = Radiobutton(self.fr_wi_t_prava3, text=u"\u03BC > \u03BC0", variable=self.wi_hodnota_Ha, value='>')
        self.ra_wi_vetsi.pack(padx=4, side='left')
        self.ra_wi_ruzne = Radiobutton(self.fr_wi_t_prava3, text=u"\u03BC \u2260 \u03BC0", variable=self.wi_hodnota_Ha, value=u'\u2260')
        self.ra_wi_ruzne.pack(padx=4, side='left') 
        self.fr_wi_t_prava3.pack(fill = 'both',expand=1, anchor=S)
        self.fr_wi_t_prava.pack(padx=4, pady=4, fill = 'both',expand=1, side="right", anchor=E)
        self.fr_wi_t.pack(fill = 'both',expand=1)
        self.fr_wi_t2=Frame(self.wi_t)
        
        
        self.wi_bu_testovat=Button(self.fr_wi_t2, text=u"Testovat", command=self.test_wi)
        self.wi_bu_testovat.pack(padx=4, pady=4, side='right')
        
        self.fr_wi_t2.pack(fill = 'both',expand=1)
        self.ra_wi0_01.select()
        self.ra_wi_mensi.select()

    def test_ma(self):
        data1=[]
        data2=[]
        ma_spust_test=''
        sh=self.soubor.sheet_by_name(self.ma_zalozky[0])
        if True==True:
            ma_spust_test="ok"
            
#### naplneni dat1 podle vybrane kategorie z listboxu 1 ######
        if self.kategorie_ma1!='':
            for col in range(sh.ncols): #zjisti cislo sloupce na zaklade ziskane hodnoty jmena
                if sh.col_values(col)[0]==self.kategorie_ma1:
                    zalozka1=col
            for row in range(sh.nrows):
                data1.append(sh.row_values(row)[zalozka1])
            nazev1=data1[0]
            del data1[0]
            pom_data1=[]
            for prvek in data1:
                if grafy.is_number(prvek)==True:
                    pom_data1.append(prvek)
#### naplneni dat2 podle vybrane kategorie z listboxu 2 ######
        if self.kategorie_ma2!='' and self.kategorie_ma1!='':
            for col in range(sh.ncols): #zjisti cislo sloupce na zaklade ziskane hodnoty jmena
                if sh.col_values(col)[0]==self.kategorie_ma2:
                    zalozka2=col
            for row in range(sh.nrows):
                data2.append(sh.row_values(row)[zalozka2])
            nazev2=data2[0]
            del data2[0]
            pom_data2=[]
            for prvek in data2:
                if grafy.is_number(prvek)==True:
                    pom_data2.append(prvek)
            if len(pom_data1)<2 or len(pom_data2)<2:
                self.nedostatecny_rozsah()
                self.txt_maly_rozsah.insert(END, u"Rozsah prvního výběru n1 = " + str(len(pom_data1)) + u". Rozsah druhého výběru n2 = " + str(len(pom_data2)) + u". \nMinimální rozsah každého výběru pro spuštění testu je 2.", "text")
            if ma_spust_test=="ok" and len(pom_data1)>=2 and len(pom_data2)>=2:
                intervalovy_odhad1=testy.intervalovy_odhad_medianu(pom_data1)
                intervalovy_odhad2=testy.intervalovy_odhad_medianu(pom_data2)
                median1=testy.median(pom_data1)
                median2=testy.median(pom_data2)
                vysledek_ma=testy.dvouvyberovy_wilcoxonuv_test(pom_data1, pom_data2, float(self.ma_hodnota_hladina.get()), self.ma_hodnota_Ha.get())
                self.oznameni_ma=Toplevel()
                self.oznameni_ma.title('Vyhodnocení Mannova-Whitneyova testu')
                self.txt_ma=Text(self.oznameni_ma, width=100, height=20)
                self.scrol_ma=Scrollbar(self.oznameni_ma)
                self.scrol_ma.pack(side=RIGHT, fill=Y)
                self.txt_ma.pack(expand=1, fill=BOTH)
                self.txt_ma.focus_set()
                self.scrol_ma.config(command=self.txt_ma.yview)
                self.txt_ma.config(yscrollcommand=self.scrol_ma.set)
                self.txt_ma.delete(1.0, END)    
                self.txt_ma.insert(END, u"Mannův-Whitneyův test", "nadpis")
                self.txt_ma.insert(END, "\n", "text")
                self.txt_ma.insert(END, "\n", "text")
                if vysledek_ma[2]==1:
                    self.txt_ma.insert(END, u"Protože n1 > n2, což nevyhovuje podmínkám testu, prosím prohoďte v seznamech tyto\nvýběry, aby bylo splněno, že n1 \u2264 n2.", "text")
                else:
                    self.txt_ma.insert(END, u"\u03B1 = "+str(self.ma_hodnota_hladina.get()), "text")
                    self.txt_ma.insert(END, "\n", "text")
                    self.txt_ma.insert(END, u"H0: \u03BC1 = \u03BC2", "text")
                    self.txt_ma.insert(END, "\n", "text")
                    self.txt_ma.insert(END, u"Ha: \u03BC1 " + self.ma_hodnota_Ha.get() + u" \u03BC2", "text")
                    self.txt_ma.insert(END, "\n", "text")
                    self.txt_ma.insert(END, u"U = " + str(round(vysledek_ma[0],5)), "text")
                    self.txt_ma.insert(END, "\n", "text")
                    if self.ma_hodnota_Ha.get()==u"\u2260":
                        self.txt_ma.insert(END, u"u(\u03B1/2) = " + str(round(vysledek_ma[1],5)), "text")
                    elif self.ma_hodnota_Ha.get()=="<":
                        self.txt_ma.insert(END, u"-u(\u03B1) = " + str(round(vysledek_ma[1],5)), "text")
                    elif self.ma_hodnota_Ha.get()==">":
                        self.txt_ma.insert(END, u"u(\u03B1) = " + str(round(vysledek_ma[1],5)), "text")
                    self.txt_ma.insert(END, "\n", "text")
                    self.txt_ma.insert(END, "\n", "text")
                    if self.ma_hodnota_Ha.get()==u"\u2260":
                        if abs(vysledek_ma[0])>=vysledek_ma[1]:
                            self.txt_ma.insert(END, u"Protože |U| je větší nebo rovno než kritická hodnota u(\u03B1/2), zamítáme hypotézu H0", "text")
                            self.txt_ma.insert(END, "\n", "text")
                            self.txt_ma.insert(END, u"na hladině \u03B1.", "text")
                        else:
                            self.txt_ma.insert(END, u"Protože |U| je menží než kritická hodnota u(\u03B1/2), nezamítáme", "text")
                            self.txt_ma.insert(END, "\n", "text")
                            self.txt_ma.insert(END, u"hypotézu H0.", "text")
                    elif self.ma_hodnota_Ha.get()=="<":
                        if (vysledek_ma[0])<vysledek_ma[1]:
                            self.txt_ma.insert(END, u"Protože U je menší než kritická hodnota -u(\u03B1), zamítáme hypotézu H0", "text")
                            self.txt_ma.insert(END, "\n", "text")
                            self.txt_ma.insert(END, u"na hladině \u03B1.", "text")
                        else:
                            self.txt_ma.insert(END, u"Protože U je větší nebo rovno než kritická hodnota -u(\u03B1), nezamítáme", "text")
                            self.txt_ma.insert(END, "\n", "text")
                            self.txt_ma.insert(END, u"hypotézu H0.", "text")
                    elif self.ma_hodnota_Ha.get()==">":
                        if (vysledek_ma[0])>vysledek_ma[1]:
                            self.txt_ma.insert(END, u"Protože U je větší než kritická hodnota u(\u03B1), zamítáme hypotézu H0", "text")
                            self.txt_ma.insert(END, "\n", "text")
                            self.txt_ma.insert(END, u"na hladině \u03B1.", "text")
                        else:
                            self.txt_ma.insert(END, u"Protože U je menší nebo rovno než kritická hodnota u(\u03B1), nezamítáme", "text")
                            self.txt_ma.insert(END, "\n", "text")
                            self.txt_ma.insert(END, u"hypotézu H0.", "text")
                    self.txt_ma.insert(END, "\n", "text")
                    self.txt_ma.insert(END, "\n", "text")
                    self.txt_ma.insert(END, "Intervalový odhad mediánu prvního výběru je <"+str(intervalovy_odhad1[0])+"; "+str(intervalovy_odhad1[1])+"> s 95% spolehlivostí.", "text")
                    self.txt_ma.insert(END, "\n", "text")
                    self.txt_ma.insert(END, "Bodový odhad mediánu prvního výběru, který odpovídá výběrovému mediánu,  je " + str(median1), "text")
                    self.txt_ma.insert(END, "\n", "text")
                    self.txt_ma.insert(END, "\n", "text")
                    self.txt_ma.insert(END, "Intervalový odhad mediánu druhého výběru je <"+str(intervalovy_odhad2[0])+"; "+str(intervalovy_odhad2[1])+"> s 95% spolehlivostí.", "text")
                    self.txt_ma.insert(END, "\n", "text")
                    self.txt_ma.insert(END, "Bodový odhad mediánu druhého výběru, který odpovídá výběrovému mediánu,  je " + str(median2), "text")
                self.txt_ma.tag_config("nadpis", underline=1, font="Arial 10 bold")
                self.txt_ma.tag_config("text", font="Arial 10")
                self.txt_ma.config(state=DISABLED)
        elif self.kategorie_ma1=='' and self.kategorie_ma2=="":
            self.ma_la1.configure(text='Nevybrali jste kategorii', foreground="red")
            self.ma_la2.configure(text='Nevybrali jste kategorii', foreground="red")
        elif self.kategorie_ma1=='':
            self.ma_la1.configure(text='Nevybrali jste kategorii', foreground="red")
        elif self.kategorie_ma2=='':
            self.ma_la2.configure(text='Nevybrali jste kategorii', foreground="red")


    def test_wi(self):
        data=[]
        wi_spust_test=''
        sh=self.soubor.sheet_by_name(self.wi_zalozky[0])
        if (self.en_wi_t.get())=="":#pretypovani na float jinak vstup bere jako string a ne cislo
            self.la_wi_med.configure(text=u"Nezadali jste medián", foreground="red")
        elif float(self.en_wi_t.get())<0:
            self.la_wi_med.configure(text=u"Nezadali jste 0-100 [%]", foreground="red")
        elif float(self.en_wi_t.get())>100:
            self.la_wi_med.configure(text=u"Nezadali jste 0-100 [%]", foreground="red")
        else:
            wi_spust_test="ok"
            self.la_wi_med.configure(text=u"OK", foreground="#00B000")
        if self.kategorie_wi!='':
            for col in range(sh.ncols): #zjisti cislo sloupce na zaklade ziskane hodnoty jmena
                if sh.col_values(col)[0]==self.kategorie_wi:
                    zalozka=col
            for row in range(sh.nrows):
                data.append(sh.row_values(row)[zalozka])
            nazev=data[0]
            del data[0]
            pom_data=[]
            for prvek in data:
                if grafy.is_number(prvek)==True:
                    pom_data.append(prvek)
            if len(pom_data)<2:
                self.nedostatecny_rozsah()
                self.txt_maly_rozsah.insert(END, u"Rozsah výběru n = " + str(len(pom_data)) + u". Minimální rozsah výběru pro spuštění testu je 2.", "text")
            if wi_spust_test=="ok" and len(pom_data)>=2:
                vysledek=testy.wilcoxonuv_test(nazev, pom_data, float(self.wi_hodnota_hladina.get()), float(self.en_wi_t.get()), self.wi_hodnota_Ha.get())
                intervalovy_odhad=testy.intervalovy_odhad_medianu(pom_data)
                self.oznameni_wi=Toplevel()
                self.oznameni_wi.title('Vyhodnocení Wilcoxonova testu')
                self.txt_wi=Text(self.oznameni_wi, width=100, height=20)
                self.scrol_wi=Scrollbar(self.oznameni_wi)
                self.scrol_wi.pack(side=RIGHT, fill=Y)
                self.txt_wi.pack(expand=1, fill=BOTH)
                self.txt_wi.focus_set()
                self.scrol_wi.config(command=self.txt_wi.yview)
                self.txt_wi.config(yscrollcommand=self.scrol_wi.set)
                self.txt_wi.delete(1.0, END)
                self.txt_wi.insert(END, u"Wilcoxonův test", "nadpis")
                self.txt_wi.insert(END, "\n", "text")
                self.txt_wi.insert(END, "\n", "text")
                self.txt_wi.insert(END, u"\u03B1 = "+str(self.wi_hodnota_hladina.get()), "text")
                self.txt_wi.insert(END, "\n", "text")
                self.txt_wi.insert(END, u"\u03BC = " + str(self.en_wi_t.get()) + " %", "text")
                self.txt_wi.insert(END, "\n", "text")
                self.txt_wi.insert(END, u"H0: \u03BC = \u03BC0", "text")
                self.txt_wi.insert(END, "\n", "text")
                self.txt_wi.insert(END, u"Ha: \u03BC " + self.wi_hodnota_Ha.get() + u" \u03BC0", "text")
                self.txt_wi.insert(END, "\n", "text")
                self.txt_wi.insert(END, u"U = " + str(round(vysledek[0],5)), "text")
                self.txt_wi.insert(END, "\n", "text")
                if self.wi_hodnota_Ha.get()==u"\u2260":
                    self.txt_wi.insert(END, u"u(\u03B1/2) = " + str(round(vysledek[1],5)), "text")
                elif self.wi_hodnota_Ha.get()=="<":
                    self.txt_wi.insert(END, u"-u(\u03B1) = " + str((-1)*round(vysledek[1],5)), "text")
                elif self.wi_hodnota_Ha.get()==">":
                    self.txt_wi.insert(END, u"u(\u03B1) = " + str(round(vysledek[1],5)), "text")
                self.txt_wi.insert(END, "\n", "text")
                self.txt_wi.insert(END, "\n", "text")
                if self.wi_hodnota_Ha.get()==u"\u2260":
                    if abs(vysledek[0])>=vysledek[1]:
                        self.txt_wi.insert(END, u"Protože |U| je větší nebo rovno než kritická hodnota u(\u03B1/2), zamítáme hypotézu H0", "text")
                        self.txt_wi.insert(END, "\n", "text")
                        self.txt_wi.insert(END, u"na hladině \u03B1.", "text")
                    else:
                        self.txt_wi.insert(END, u"Protože |U| je menží než kritická hodnota u(\u03B1/2), nezamítáme", "text")
                        self.txt_wi.insert(END, "\n", "text")
                        self.txt_wi.insert(END, u"hypotézu H0.", "text")
                elif self.wi_hodnota_Ha.get()=="<":
                    if (vysledek[0])<vysledek[1]:
                        self.txt_wi.insert(END, u"Protože U je menší než kritická hodnota -u(\u03B1), zamítáme hypotézu H0", "text")
                        self.txt_wi.insert(END, "\n", "text")
                        self.txt_wi.insert(END, u"na hladině \u03B1.", "text")
                    else:
                        self.txt_wi.insert(END, u"Protože U je větší nebo rovno než kritická hodnota -u(\u03B1), nezamítáme", "text")
                        self.txt_wi.insert(END, "\n", "text")
                        self.txt_wi.insert(END, u"hypotézu H0.", "text")
                elif self.wi_hodnota_Ha.get()==">":
                    if (vysledek[0])>vysledek[1]:
                        self.txt_wi.insert(END, u"Protože U je větší než kritická hodnota u(\u03B1), zamítáme hypotézu H0", "text")
                        self.txt_wi.insert(END, "\n", "text")
                        self.txt_wi.insert(END, u"na hladin \u03B1.", "text")
                    else:
                        self.txt_wi.insert(END, u"Protože U je menší nebo rovno než kritická hodnota u(\u03B1), nezamítáme", "text")
                        self.txt_wi.insert(END, "\n", "text")
                        self.txt_wi.insert(END, u"hypotézu H0.", "text")
                self.txt_wi.insert(END, "\n", "text")
                self.txt_wi.insert(END, "\n", "text")
                self.txt_wi.insert(END, "Intervalový odhad mediánu je <"+str(intervalovy_odhad[0])+"; "+str(intervalovy_odhad[1])+"> s 95% spolehlivostí.", "text")
                self.txt_wi.insert(END, "\n", "text")
                self.txt_wi.insert(END, "Bodový odhad mediánu, který odpovídá výběrovému mediánu, je " + str(testy.median(pom_data)), "text")
                self.txt_wi.tag_config("nadpis", underline=1, font="Arial 10 bold")
                self.txt_wi.tag_config("text", font="Arial 10")
                self.txt_wi.config(state=DISABLED)
        else:
            self.wi_la.configure(text='Nevybrali jste kategorii', foreground="red")

    def med_li_double(self, event):#po dvojkliku v seznamu kategorii
        self.med_la1.configure(text=self.med_li1.get("active"), foreground="#00B000")
        self.kategorie_med=self.med_li1.get("active")#zjisti aktivovanou kategorii v seznamu

    def med_Ostrava_li_double(self, event):#po dvojkliku v seznamu kategorii
        self.med_Ostrava_la1.configure(text=self.med_Ostrava_li1.get("active"), foreground="#00B000")
        self.kategorie_med=self.med_Ostrava_li1.get("active")#zjisti aktivovanou kategorii v seznamu

    def med_Opava_li_double(self, event):#po dvojkliku v seznamu kategorii
        self.med_Opava_la1.configure(text=self.med_Opava_li1.get("active"), foreground="#00B000")
        self.kategorie_med=self.med_Opava_li1.get("active")#zjisti aktivovanou kategorii v seznamu

    def pea_li1_double(self, event):#po dvojkliku v seznamu kategorii
        self.pea_la1.configure(text=self.pea_li1.get("active"), foreground="#00B000")
        self.kategorie_pea1=self.pea_li1.get("active")#zjisti aktivovanou kategorii v seznamu

    def pea_li2_double(self, event):#po dvojkliku v seznamu kategorii
        self.pea_la2.configure(text=self.pea_li2.get("active"), foreground="#00B000")
        self.kategorie_pea2=self.pea_li2.get("active")#zjisti aktivovanou kategorii v seznamu

    def expo_li1_double(self, event):#po dvojkliku v seznamu kategorii
        self.expo_la1.configure(text=self.expo_li1.get("active"), foreground="#00B000")
        self.kategorie_expo1=self.expo_li1.get("active")#zjisti aktivovanou kategorii v seznamu

    def expo_li2_double(self, event):#po dvojkliku v seznamu kategorii
        self.expo_la2.configure(text=self.expo_li2.get("active"), foreground="#00B000")
        self.kategorie_expo2=self.expo_li2.get("active")#zjisti aktivovanou kategorii v seznamu

    def ks2_li1_double(self, event):#po dvojkliku v seznamu kategorii
        self.ks2_la1.configure(text=self.ks2_li1.get("active"), foreground="#00B000")
        self.kategorie_ks21=self.ks2_li1.get("active")#zjisti aktivovanou kategorii v seznamu

    def ks2_li2_double(self, event):#po dvojkliku v seznamu kategorii
        self.ks2_la2.configure(text=self.ks2_li2.get("active"), foreground="#00B000")
        self.kategorie_ks22=self.ks2_li2.get("active")#zjisti aktivovanou kategorii v seznamu

    def ks2_li3_double(self, event):#po dvojkliku v seznamu kategorii
        self.ks2_la3.configure(text=self.ks2_li3.get("active"), foreground="#00B000")
        self.kategorie_ks23=self.ks2_li3.get("active")#zjisti aktivovanou kategorii v seznamu

    def ks2_li4_double(self, event):#po dvojkliku v seznamu kategorii
        self.ks2_la4.configure(text=self.ks2_li4.get("active"), foreground="#00B000")
        self.kategorie_ks24=self.ks2_li4.get("active")#zjisti aktivovanou kategorii v seznamu

    def sp_li1_double(self, event):#po dvojkliku v seznamu kategorii
        self.sp_la1.configure(text=self.sp_li1.get("active"), foreground="#00B000")
        self.kategorie_sp1=self.sp_li1.get("active")#zjisti aktivovanou kategorii v seznamu

    def sp_li2_double(self, event):#po dvojkliku v seznamu kategorii
        self.sp_la2.configure(text=self.sp_li2.get("active"), foreground="#00B000")
        self.kategorie_sp2=self.sp_li2.get("active")#zjisti aktivovanou kategorii v seznamu
           
    def ks_li1_double(self, event):#po dvojkliku v seznamu kategorii
        self.ks_la1.configure(text=self.ks_li1.get("active"), foreground="#00B000")
        self.kategorie_ks1=self.ks_li1.get("active")#zjisti aktivovanou kategorii v seznamu

    def ks_li2_double(self, event):#po dvojkliku v seznamu kategorii
        self.ks_la2.configure(text=self.ks_li2.get("active"), foreground="#00B000")
        self.kategorie_ks2=self.ks_li2.get("active")#zjisti aktivovanou kategorii v seznamu
        
    def wi_li_double(self, event):#po dvojkliku v seznamu kategorii
        self.wi_la.configure(text=self.wi_li.get("active"), foreground="#00B000")
        self.kategorie_wi=self.wi_li.get("active")#zjisti aktivovanou kategorii v seznamu

    def ma_li1_double(self, event):#po dvojkliku v seznamu kategorii
        self.ma_la1.configure(text=self.ma_li1.get("active"), foreground="#00B000")
        self.kategorie_ma1=self.ma_li1.get("active")#zjisti aktivovanou kategorii v seznamu

    def ma_li2_double(self, event):#po dvojkliku v seznamu kategorii
        self.ma_la2.configure(text=self.ma_li2.get("active"), foreground="#00B000")
        self.kategorie_ma2=self.ma_li2.get("active")#zjisti aktivovanou kategorii v seznamu

    def znamenkovy_test(self):
        self.hodnota_hladina=DoubleVar()
        self.hodnota_Ha=StringVar()
        self.zalozky=self.soubor.sheet_names()
        self.zn_t=Toplevel()
        self.zn_t.title('Znaménkový test')
        self.fr_zn_t=Frame(self.zn_t)
        self.fr_zn_t_leva=Frame(self.fr_zn_t)
        self.zn_li = Listbox(self.fr_zn_t_leva, width=30, height=10)
        self.zn_sy = Scrollbar(self.fr_zn_t_leva, orient="vertical", command=self.zn_li.yview)  
        self.zn_la = Label(self.fr_zn_t_leva, text=u"Není vybrana žádná kategorie", foreground="red")
        self.zn_li.configure(yscrollcommand=self.zn_sy.set)
        seznam_kat=[]
        sh=self.soubor.sheet_by_name(self.zalozky[0])
        for col in range(sh.ncols): #vytvori seznam kategorii
                seznam_kat.append(sh.col_values(col)[0])
        del seznam_kat[0:13]
        del seznam_kat[(len(seznam_kat)-1)]
        del seznam_kat[(len(seznam_kat)-1)]
        for polozka in seznam_kat:
            self.zn_li.insert(END, polozka)
        
        self.zn_li.grid(row=0, column=0, padx=4, pady=8)
        self.zn_sy.grid(row=0, column=1, sticky="ns", pady=8)
        self.zn_la.grid(row=1, column=0, columnspan=2)
        
        self.zn_li.bind("<Double-B1-ButtonRelease>", self.zn_li_double)
        self.kategorie_zn='' #pomocna promenna ktera se naplni v pripade zadani kategorie, jinak bude uzivatel upozornen ze nevybral promennou
        self.fr_zn_t_leva.pack(fill = 'both',expand=1, side="left", anchor=W)
        self.fr_zn_t_prava=Frame(self.fr_zn_t)
        self.fr_zn_t_prava1=LabelFrame(self.fr_zn_t_prava, relief=GROOVE, borderwidth=2, text=u'Hladina významnosti \u03B1')
        self.ra_zn0_01 = Radiobutton(self.fr_zn_t_prava1, text=u"\u03B1 = 0.01", variable=self.hodnota_hladina, value=0.01)
        self.ra_zn0_01.pack(side='left', padx=4)
        self.ra_zn0_05 = Radiobutton(self.fr_zn_t_prava1, text=u"\u03B1 = 0.05", variable=self.hodnota_hladina, value=0.05)
        self.ra_zn0_05.pack(side='left', padx=4)
        self.ra_zn0_1 = Radiobutton(self.fr_zn_t_prava1, text=u"\u03B1 = 0.1", variable=self.hodnota_hladina, value=0.1)
        self.ra_zn0_1.pack(side='left', padx=4)
        self.fr_zn_t_prava1.pack(fill = 'both',expand=1, side="top", anchor=N)
        self.fr_zn_t_prava2=LabelFrame(self.fr_zn_t_prava, relief=GROOVE, borderwidth=2, text=u'Zvolte medián [%]')
        self.en_zn_t = Entry(self.fr_zn_t_prava2)
        self.en_zn_t.pack(side="top", padx=4, pady=4, fill="x")
        self.la_zn_med = Label(self.fr_zn_t_prava2, text=u"Zadejte hodnotu 0-100 [%]", foreground="#00B000")
        self.la_zn_med.pack(fill="both", padx=4, pady=4, anchor=S)
        self.fr_zn_t_prava2.pack(fill = 'both',expand=1, anchor=S)
        self.fr_zn_t_prava3=LabelFrame(self.fr_zn_t_prava, relief=GROOVE, borderwidth=2, text=u'Zvolte Ha')
        self.ra_zn_mensi = Radiobutton(self.fr_zn_t_prava3, text=u"\u03BC < \u03BC0", variable=self.hodnota_Ha, value='<')
        self.ra_zn_mensi.pack(padx=4, side='left')
        self.ra_zn_vetsi = Radiobutton(self.fr_zn_t_prava3, text=u"\u03BC > \u03BC0", variable=self.hodnota_Ha, value='>')
        self.ra_zn_vetsi.pack(padx=4, side='left')
        self.ra_zn_ruzne = Radiobutton(self.fr_zn_t_prava3, text=u"\u03BC \u2260 \u03BC0", variable=self.hodnota_Ha, value=u'\u2260')
        self.ra_zn_ruzne.pack(padx=4, side='left') 
        self.fr_zn_t_prava3.pack(fill = 'both',expand=1, anchor=S)
        self.fr_zn_t_prava.pack(padx=4, pady=4, fill = 'both',expand=1, side="right", anchor=E)
        self.fr_zn_t.pack(fill = 'both',expand=1)
        self.fr_zn_t2=Frame(self.zn_t)
        
        
        self.bu_testovat=Button(self.fr_zn_t2, text=u"Testovat", command=self.test_zn)
        self.bu_testovat.pack(padx=4, pady=4, side='right')
        
        self.fr_zn_t2.pack(fill = 'both',expand=1)
        self.ra_zn0_01.select()
        self.ra_zn_mensi.select()

    def test_zn(self):
        data=[]
        spust_test=''
        sh=self.soubor.sheet_by_name(self.zalozky[0])
        if (self.en_zn_t.get())=="":#pretypovani na float jinak vstup bere jako string a ne cislo
            #print '1'
            self.la_zn_med.configure(text=u"Nezadali jste medián", foreground="red")
        elif float(self.en_zn_t.get())<0:
            self.la_zn_med.configure(text=u"Nezadali jste 0-100 [%]", foreground="red")
        elif float(self.en_zn_t.get())>100:
            self.la_zn_med.configure(text=u"Nezadali jste 0-100 [%]", foreground="red")
        else:
            spust_test="ok"
            self.la_zn_med.configure(text=u"OK", foreground="#00B000")
        if self.kategorie_zn!='':
            for col in range(sh.ncols): #zjisti cislo sloupce na zaklade ziskane hodnoty jmena
                if sh.col_values(col)[0]==self.kategorie_zn:
                    zalozka=col
            for row in range(sh.nrows):
                data.append(sh.row_values(row)[zalozka])
            nazev=data[0]
            del data[0]
            pom_data=[]
            for prvek in data:
                if grafy.is_number(prvek)==True:
                    pom_data.append(prvek)
            if len(pom_data)<2:
                self.nedostatecny_rozsah()
                self.txt_maly_rozsah.insert(END, u"Rozsah výběru n = " + str(len(pom_data)) + u". Minimální rozsah výběru pro spuštění testu je 2.", "text")
                #self.txt_maly_rozsah.insert(END, u"\n", "text")
            if spust_test=="ok" and len(pom_data)>=2:
                vysledek=testy.znamenkovy_test(nazev, pom_data, float(self.hodnota_hladina.get()), float(self.en_zn_t.get()), self.hodnota_Ha.get())
                intervalovy_odhad=testy.intervalovy_odhad_medianu(pom_data)
                self.oznameni_zn=Toplevel()
                self.oznameni_zn.title('Vyhodnocení znaménkového testu')
                self.txt_zn=Text(self.oznameni_zn, width=100, height=20)
                self.scrol_zn=Scrollbar(self.oznameni_zn)
                self.scrol_zn.pack(side=RIGHT, fill=Y)
                self.txt_zn.pack(expand=1, fill=BOTH)
                self.txt_zn.focus_set()
                self.scrol_zn.config(command=self.txt_zn.yview)
                self.txt_zn.config(yscrollcommand=self.scrol_zn.set)
                self.txt_zn.delete(1.0, END)
                self.txt_zn.insert(END, u"Znaménkový test", "nadpis")
                self.txt_zn.insert(END, "\n", "text")
                self.txt_zn.insert(END, "\n", "text")
                self.txt_zn.insert(END, u"\u03B1 = "+str(self.hodnota_hladina.get()), "text")
                self.txt_zn.insert(END, "\n", "text")
                self.txt_zn.insert(END, u"\u03BC = " + str(self.en_zn_t.get()) + " %", "text")
                self.txt_zn.insert(END, "\n", "text")
                self.txt_zn.insert(END, u"H0: \u03BC = \u03BC0", "text")
                self.txt_zn.insert(END, "\n", "text")
                self.txt_zn.insert(END, u"Ha: \u03BC " + self.hodnota_Ha.get() + u" \u03BC0", "text")
                self.txt_zn.insert(END, "\n", "text")
                self.txt_zn.insert(END, u"p-hodnota = " + str(round(vysledek,5)), "text")
                self.txt_zn.insert(END, "\n", "text")
                self.txt_zn.insert(END, "\n", "text")
                if vysledek<self.hodnota_hladina.get():
                    self.txt_zn.insert(END, u"Protože p-hodnota je menší než hladina významnosti \u03B1, zamítáme hypotézu H0", "text")
                    self.txt_zn.insert(END, "\n", "text")
                    self.txt_zn.insert(END, u"ve prospěch alternativy.", "text")
                else:
                    self.txt_zn.insert(END, u"Protože p-hodnota je větší nebo rovna než hladina významnosti \u03B1, nezamítáme \nhypotézu H0.", "text")
                self.txt_zn.tag_config("nadpis", underline=1, font="Arial 10 bold")
                self.txt_zn.insert(END, "\n", "text")
                self.txt_zn.insert(END, "\n", "text")
                self.txt_zn.insert(END, "Intervalový odhad mediánu je <"+str(intervalovy_odhad[0])+"; "+str(intervalovy_odhad[1])+"> s 95% spolehlivostí.", "text")
                self.txt_zn.insert(END, "\n", "text")
                self.txt_zn.insert(END, "Bodový odhad mediánu, který odpovídá výběrovému mediánu,  je " + str(testy.median(pom_data)), "text")
                self.txt_zn.tag_config("text", font="Arial 10")
                self.txt_zn.config(state=DISABLED)
        else:
            self.zn_la.configure(text='Nevybrali jste kategorii', foreground="red")
            
        
    def zn_li_double(self, event):#po dvojkliku v seznamu kategorii
        self.zn_la.configure(text=self.zn_li.get("active"), foreground="#00B000")
        self.kategorie_zn=self.zn_li.get("active")#zjisti aktivovanou kategorii v seznamu

    def nedostatecny_rozsah(self):
        self.maly_rozsah=Toplevel()
        self.maly_rozsah.title('Nedostatečný rozsah výběru')
        self.txt_maly_rozsah=Text(self.maly_rozsah, width=100, height=20)
        self.scrol_maly_rozsah=Scrollbar(self.maly_rozsah)
        self.scrol_maly_rozsah.pack(side=RIGHT, fill=Y)
        self.txt_maly_rozsah.pack(expand=1, fill=BOTH)
        self.txt_maly_rozsah.focus_set()
        self.scrol_maly_rozsah.config(command=self.txt_maly_rozsah.yview)
        self.txt_maly_rozsah.config(yscrollcommand=self.scrol_maly_rozsah.set)
        self.txt_maly_rozsah.delete(1.0, END)
        self.txt_maly_rozsah.insert(END, u"Nedostatečný rozsah výběru !!!\n", "nadpis")
        self.txt_maly_rozsah.tag_config("nadpis", underline=1, font="Arial 12 bold", foreground="red")
        self.txt_maly_rozsah.tag_config("text", font="Arial 10")

    def explorace(self):
        self.zalozky=self.soubor.sheet_names()
        self.top=Toplevel()
        self.nb = Tix.NoteBook(self.top)
        self.nb.add("page1", label=self.zalozky[0])
        self.nb.add("page2", label=self.zalozky[1])
        self.nb.add("page3", label=self.zalozky[2])
        self.nb.add("page4", label=self.zalozky[3])
        self.nb.add("page5", label=self.zalozky[4])
        self.nb.add("page6", label=self.zalozky[5])
        self.p1 = self.nb.subwidget_list["page1"]
        self.p2 = self.nb.subwidget_list["page2"]
        self.p3 = self.nb.subwidget_list["page3"]
        self.p4 = self.nb.subwidget_list["page4"]
        self.p5 = self.nb.subwidget_list["page5"]
        self.p6 = self.nb.subwidget_list["page6"]

####### ZALOZKA6 #######
        self.z6_hodnota = StringVar()  #kategorie, kvuli zachovani abstraktnosti a dynamickeho pristupu ke sloupum v excelu hodnota odpovida cislu sloupce s pozadovanumi daty
        self.z6_hodnota2 = StringVar() #cetnost
        self.z6_hodnota3 = StringVar() #typ grafu
        self.z6_exp_nad = Frame(self.p6, relief="sunken", borderwidth=2)
    ####### Nadpis #######
        self.z6_f3 = Frame(self.z6_exp_nad, borderwidth=2)
        self.z6_la = Label(self.z6_f3, text="Vyberte jednu z kategorií pro explorační analýzu", anchor='center')
        self.z6_la.pack(side='top', fill='x')
        self.z6_f3.pack(fill='both', expand=1)        
    ####### Leva tabulka #######
        self.z6_hlavni = Frame(self.z6_exp_nad, borderwidth=2)
        self.z6_horni = LabelFrame(self.z6_hlavni, relief=GROOVE, borderwidth=2, text='Kategorie')
        
        self.z6_b4 = Radiobutton(self.z6_horni, text=u"Počet nemocných v částech Opavy", variable=self.z6_hodnota, value='Ostrava', command=self.nastaveniopv6)
        self.z6_b4.pack(anchor=W, padx=4)
        self.z6_b1 = Radiobutton(self.z6_horni, text=u"Nemocní ku počtu obyvatel v Opavě", variable=self.z6_hodnota, value='Pomer', command=self.nastavenipom6)
        self.z6_b1.pack(anchor=W, padx=4)
        self.z6_horni.pack(fill = 'both', anchor=N, expand=1)
        self.z6_dolni = Frame(self.z6_hlavni)
        self.z6_bu = Button(self.z6_dolni, text="Graf", width=10, height=2, command=self.graf_zalozka5)
        self.z6_bu.pack(padx=2, pady=2, fill= 'y', anchor=SE)
        self.z6_dolni.pack(fill = 'both', anchor=S, expand=1)
        self.z6_hlavni.pack(fill = 'both', padx=2, pady=2, anchor=W, side='left', expand=1)
    ####### Prava tabulka #######       
        self.z6_f2 = Frame(self.z6_exp_nad, borderwidth=2)
        self.z6_fr1=LabelFrame(self.z6_f2, relief=GROOVE, borderwidth=2, text='Četnost')
        self.z6_b5 = Radiobutton(self.z6_fr1, text="Absolutní", variable=self.z6_hodnota2, value="Absolutni")
        self.z6_b5.pack(anchor=W,  padx=4)
        self.z6_bcr = Radiobutton(self.z6_fr1, text="Relativní", variable=self.z6_hodnota2, value="Relativni")
        self.z6_bcr.pack(anchor=W,  padx=4)
        self.z6_fr1.pack(fill = 'both', anchor=N, expand=1)
        self.z6_fr2=LabelFrame(self.z6_f2, relief=GROOVE, borderwidth=2, text='Typ grafu')
        self.z6_b6 = Radiobutton(self.z6_fr2, text="Histogram", variable=self.z6_hodnota3, value="Histogram", command=self.nastavenihis6)
        self.z6_b6.pack(anchor=W,  padx=4)
        self.z6_btk = Radiobutton(self.z6_fr2, text="Koláčový", variable=self.z6_hodnota3, value="Kolacovy", command=self.nastavenikol6)
        self.z6_btk.pack(anchor=W,  padx=4)
        self.z6_fr2.pack(fill = 'both', anchor=S, expand=1)
        self.z6_f2.pack(fill = 'both', padx=2, pady=2, anchor=E, side='right', expand=1)

        
        self.z6_exp_nad.pack(fill = 'both')
        
        
        self.z6_b4.select() # vybere jeden radiobutton jinak by byli zaskrtle vsechny (pohlvai)
        self.z6_b6.select() # absolutni cetnost
        self.z6_b5.select() # histogram

####### ZALOZKA5 #######
        self.z5_hodnota = StringVar()  #kategorie, kvuli zachovani abstraktnosti a dynamickeho pristupu ke sloupum v excelu hodnota odpovida cislu sloupce s pozadovanumi daty
        self.z5_hodnota2 = StringVar() #cetnost
        self.z5_hodnota3 = StringVar() #typ grafu
        self.z5_exp_nad = Frame(self.p5, relief="sunken", borderwidth=2)
    ####### Nadpis #######
        self.z5_f3 = Frame(self.z5_exp_nad, borderwidth=2)
        self.z5_la = Label(self.z5_f3, text="Vyberte jednu z kategorií pro explorační analýzu", anchor='center')
        self.z5_la.pack(side='top', fill='x')
        self.z5_f3.pack(fill='both', expand=1)        
    ####### Leva tabulka #######
        self.z5_hlavni = Frame(self.z5_exp_nad, borderwidth=2)
        self.z5_horni = LabelFrame(self.z5_hlavni, relief=GROOVE, borderwidth=2, text='Kategorie')
        
        self.z5_b4 = Radiobutton(self.z5_horni, text=u"Počet nemocných v částech Ostravy", variable=self.z5_hodnota, value='Ostrava', command=self.nastaveniost5)
        self.z5_b4.pack(anchor=W, padx=4)
        self.z5_b1 = Radiobutton(self.z5_horni, text=u"Nemocní ku počtu obyvatel v Ostravě", variable=self.z5_hodnota, value='Pomer', command=self.nastavenipom5)
        self.z5_b1.pack(anchor=W, padx=4)
        self.z5_horni.pack(fill = 'both', anchor=N, expand=1)
        self.z5_dolni = Frame(self.z5_hlavni)
        self.z5_bu = Button(self.z5_dolni, text="Graf", width=10, height=2, command=self.graf_zalozka4)
        self.z5_bu.pack(padx=2, pady=2, fill= 'y', anchor=SE)
        self.z5_dolni.pack(fill = 'both', anchor=S, expand=1)
        self.z5_hlavni.pack(fill = 'both', padx=2, pady=2, anchor=W, side='left', expand=1)
    ####### Prava tabulka #######       
        self.z5_f2 = Frame(self.z5_exp_nad, borderwidth=2)
        self.z5_fr1=LabelFrame(self.z5_f2, relief=GROOVE, borderwidth=2, text='Četnost')
        self.z5_b5 = Radiobutton(self.z5_fr1, text="Absolutní", variable=self.z5_hodnota2, value="Absolutni")
        self.z5_b5.pack(anchor=W,  padx=4)
        self.z5_bcr = Radiobutton(self.z5_fr1, text="Relativní", variable=self.z5_hodnota2, value="Relativni")
        self.z5_bcr.pack(anchor=W,  padx=4)
        self.z5_fr1.pack(fill = 'both', anchor=N, expand=1)
        self.z5_fr2=LabelFrame(self.z5_f2, relief=GROOVE, borderwidth=2, text='Typ grafu')
        self.z5_b6 = Radiobutton(self.z5_fr2, text="Histogram", variable=self.z5_hodnota3, value="Histogram", command=self.nastavenihis5)
        self.z5_b6.pack(anchor=W,  padx=4)
        self.z5_btk = Radiobutton(self.z5_fr2, text="Koláčový", variable=self.z5_hodnota3, value="Kolacovy", command=self.nastavenikol5)
        self.z5_btk.pack(anchor=W,  padx=4)
        self.z5_fr2.pack(fill = 'both', anchor=S, expand=1)
        self.z5_f2.pack(fill = 'both', padx=2, pady=2, anchor=E, side='right', expand=1)

        
        self.z5_exp_nad.pack(fill = 'both')
        
        
        self.z5_b4.select() # vybere jeden radiobutton jinak by byli zaskrtle vsechny (pohlvai)
        self.z5_b6.select() # absolutni cetnost
        self.z5_b5.select() # histogram

####### ZALOZKA4 #######
        self.z3_hodnota = StringVar()  #kategorie, kvuli zachovani abstraktnosti a dynamickeho pristupu ke sloupum v excelu hodnota odpovida cislu sloupce s pozadovanumi daty
        self.z3_hodnota2 = StringVar() #cetnost
        self.z3_hodnota3 = StringVar() #typ grafu
        self.z3_exp_nad = Frame(self.p4, relief="sunken", borderwidth=2)
    ####### Nadpis #######
        self.z3_f3 = Frame(self.z3_exp_nad)
        self.z3_la = Label(self.z3_f3, text="Vyberte jednu z kategorií pro explorační analýzu", anchor='center')
        self.z3_la.pack(side='top', fill='x')
        self.z3_f3.pack(fill='both', expand=1)
    ####### Leva tabulka #######
        self.z3_hlavni = Frame(self.z3_exp_nad, borderwidth=2)
        self.z3_horni = LabelFrame(self.z3_hlavni, relief=GROOVE, borderwidth=2, text='Dvojklikem vyberte kategorii')
        
        self.z3_li = Listbox(self.z3_horni, width=30, height=10)
        self.z3_sy = Scrollbar(self.z3_horni, orient="vertical", command=self.z3_li.yview)  
        self.z3_la = Label(self.z3_horni, text=u"Není vybrana žádná kategorie", foreground="red")
        self.z3_li.configure(yscrollcommand=self.z3_sy.set)
        seznam_kat=[]
        sh=self.soubor.sheet_by_name(self.zalozky[3])
        for col in range(sh.ncols): #vytvori seznam kategorii
                seznam_kat.append(sh.col_values(col)[0])
        del seznam_kat[0:3]
        del seznam_kat[len(seznam_kat)-1]
        for polozka in seznam_kat:
            self.z3_li.insert(END, polozka)
        
        self.z3_hlavni.pack()
        self.z3_li.grid(row=0, column=0, padx=4, pady=4)
        self.z3_sy.grid(row=0, column=1, sticky="ns", pady=4)
        self.z3_la.grid(row=1, column=0, columnspan=2)
        
        self.z3_li.bind("<Double-B1-ButtonRelease>", self.liTakeOver)
        self.kategorie_seznam='' #pomocna promenna ktera se naplni v pripade zadani kategorie, jinak bude uzivatel upozornen ze nevybral promennou
    
        self.z3_horni.pack(fill = 'both', anchor=N, expand=1)
        self.z3_dolni = Frame(self.z3_hlavni)
        self.z3_bu = Button(self.z3_dolni, text="Graf", width=10, height=2, command=self.graf_zalozka3)
        self.z3_bu.pack(padx=2, pady=2, fill= 'y', anchor=SE)
        self.z3_dolni.pack(fill = 'both', anchor=S, expand=1)
        self.z3_hlavni.pack(fill = 'both', padx=2, pady=2, anchor=W, side='left', expand=1)
    ####### Prava tabulka #######       
        self.z3_f2 = Frame(self.z3_exp_nad, borderwidth=2)
        self.z3_fr1=LabelFrame(self.z3_f2, relief=GROOVE, borderwidth=2, text='Četnost')
        self.z3_b5 = Radiobutton(self.z3_fr1, text="Absolutní", variable=self.z3_hodnota2, value="Absolutni")
        self.z3_b5.pack(anchor=W,  padx=4)
        self.z3_bcr = Radiobutton(self.z3_fr1, text="Relativní", variable=self.z3_hodnota2, value="Relativni")
        self.z3_bcr.pack(anchor=W,  padx=4)
        self.z3_fr1.pack(fill = 'both', anchor=N, expand=1)
        self.z3_fr2=LabelFrame(self.z3_f2, relief=GROOVE, borderwidth=2, text='Typ grafu')
        self.z3_b6 = Radiobutton(self.z3_fr2, text="Histogram", variable=self.z3_hodnota3, value="Histogram", command=self.nastavenihis4)
        self.z3_b6.pack(anchor=W,  padx=4)
        self.z3_btk = Radiobutton(self.z3_fr2, text="Koláčový", variable=self.z3_hodnota3, value="Kolacovy", command=self.nastavenikol4)
        self.z3_btk.pack(anchor=W,  padx=4)
        self.z3_fr2.pack(fill = 'both', anchor=S, expand=1)
        self.z3_f2.pack(fill = 'both', padx=2, pady=2, anchor=E, side='right', expand=1)
        
        self.z3_b6.select() # absolutni cetnost
        self.z3_b5.select() # histogram
        
        self.z3_exp_nad.pack(fill = 'both')

####### ZALOZKA3 #######
        self.z4_hodnota = StringVar()  #kategorie, kvuli zachovani abstraktnosti a dynamickeho pristupu ke sloupum v excelu hodnota odpovida cislu sloupce s pozadovanumi daty
        self.z4_hodnota2 = StringVar() #cetnost
        self.z4_hodnota3 = StringVar() #typ grafu
        self.z4_exp_nad = Frame(self.p3, relief="sunken", borderwidth=2)
    ####### Nadpis #######
        self.z4_f3 = Frame(self.z4_exp_nad)
        self.z4_la = Label(self.z4_f3, text="Vyberte jednu z kategorií pro explorační analýzu", anchor='center')
        self.z4_la.pack(side='top', fill='x')
        self.z4_f3.pack(fill='both', expand=1)
    ####### Leva tabulka #######
        self.z4_hlavni = Frame(self.z4_exp_nad, borderwidth=2)
        self.z4_horni = LabelFrame(self.z4_hlavni, relief=GROOVE, borderwidth=2, text='Kategorie')
        self.z4_b4 = Radiobutton(self.z4_horni, text="Pohlaví", variable=self.z4_hodnota, value='Pohlavi', command=self.nastavenipoh3)
        self.z4_b4.pack(anchor=W, padx=4)
        self.z4_b1 = Radiobutton(self.z4_horni, text="Věk", variable=self.z4_hodnota, value='Vek', command=self.nastavenivek3)
        self.z4_b1.pack(anchor=W, padx=4)
        self.z4_b2 = Radiobutton(self.z4_horni, text="Dg-cytogenetic", variable=self.z4_hodnota, value='Dg-cytogenetic', command=self.nastavenidgc3)
        self.z4_b2.pack(anchor=W, padx=4)
        self.z4_horni.pack(fill = 'both', anchor=N, expand=1)
        self.z4_dolni = Frame(self.z4_hlavni)
        self.z4_bu = Button(self.z4_dolni, text="Graf", width=10, height=2, command=self.graf_zalozka2)
        self.z4_bu.pack(padx=2, pady=2, fill= 'y', anchor=SE)
        self.z4_dolni.pack(fill = 'both', anchor=S, expand=1)
        self.z4_hlavni.pack(fill = 'both', padx=2, pady=2, anchor=W, side='left', expand=1)
    ####### Prava tabulka #######       
        self.z4_f2 = Frame(self.z4_exp_nad, borderwidth=2)
        self.z4_fr1=LabelFrame(self.z4_f2, relief=GROOVE, borderwidth=2, text='Četnost')
        self.z4_b5 = Radiobutton(self.z4_fr1, text="Absolutní", variable=self.z4_hodnota2, value="Absolutni")
        self.z4_b5.pack(anchor=W,  padx=4)
        self.z4_bcr = Radiobutton(self.z4_fr1, text="Relativní", variable=self.z4_hodnota2, value="Relativni")
        self.z4_bcr.pack(anchor=W,  padx=4)
        self.z4_fr1.pack(fill = 'both', anchor=N, expand=1)
        self.z4_fr2=LabelFrame(self.z4_f2, relief=GROOVE, borderwidth=2, text='Typ grafu')
        self.z4_b6 = Radiobutton(self.z4_fr2, text="Histogram", variable=self.z4_hodnota3, value="Histogram", command=self.nastavenihis3)
        self.z4_b6.pack(anchor=W,  padx=4)
        self.z4_btk = Radiobutton(self.z4_fr2, text="Koláčový", variable=self.z4_hodnota3, value="Kolacovy", command=self.nastavenikol3)
        self.z4_btk.pack(anchor=W,  padx=4)
        self.z4_btkr = Radiobutton(self.z4_fr2, text="Krabicový", state='disabled', variable=self.z4_hodnota3, value="Krabicovy", command=self.nastavenikra3)
        self.z4_btkr.pack(anchor=W,  padx=4)
        self.z4_fr2.pack(fill = 'both', anchor=S, expand=1)
        self.z4_f2.pack(fill = 'both', padx=2, pady=2, anchor=E, side='right', expand=1)

##        self.z2_f3 = Frame(self.z2_exp_nad)
##        self.z2_bu = Button(self.z2_f3, text="Graf", width=10, height=2, command=self.graf_zalozka1)
##        self.z2_bu.pack(padx=2, pady=2, anchor=S)
##        self.z2_f3.pack(fill = 'both', padx=2, pady=2, expand=1)

        self.z4_b4.select() # vybere jeden radiobutton jinak by byli zaskrtle vsechny (pohlvai)
        self.z4_b6.select() # absolutni cetnost
        self.z4_b5.select() # histogram
        
        self.z4_exp_nad.pack(fill = 'both')

####### ZALOZKA2 #######
        self.z2_hodnota = StringVar()  #kategorie, kvuli zachovani abstraktnosti a dynamickeho pristupu ke sloupum v excelu hodnota odpovida cislu sloupce s pozadovanumi daty
        self.z2_hodnota2 = StringVar() #cetnost
        self.z2_hodnota3 = StringVar() #typ grafu
        self.z2_exp_nad = Frame(self.p2, relief="sunken", borderwidth=2)
    ####### Nadpis #######
        self.z2_f3 = Frame(self.z2_exp_nad)
        self.z2_la = Label(self.z2_f3, text="Vyberte jednu z kategorií pro explorační analýzu", anchor='center')
        self.z2_la.pack(side='top', fill='x')
        self.z2_f3.pack(fill='both', expand=1)
    ####### Leva tabulka #######
        self.z2_hlavni = Frame(self.z2_exp_nad, borderwidth=2)
        self.z2_horni = LabelFrame(self.z2_hlavni, relief=GROOVE, borderwidth=2, text='Kategorie')
        self.z2_b4 = Radiobutton(self.z2_horni, text="Pohlaví", variable=self.z2_hodnota, value='Pohlavi', command=self.nastavenipoh2)
        self.z2_b4.pack(anchor=W, padx=4)
        self.z2_b1 = Radiobutton(self.z2_horni, text="Věk", variable=self.z2_hodnota, value='Vek', command=self.nastavenivek2)
        self.z2_b1.pack(anchor=W, padx=4)
        self.z2_b2 = Radiobutton(self.z2_horni, text="Oblast", variable=self.z2_hodnota, value='Obvod', command=self.nastaveniobv2)
        self.z2_b2.pack(anchor=W, padx=4)
        self.z2_horni.pack(fill = 'both', anchor=N, expand=1)
        self.z2_dolni = Frame(self.z2_hlavni)
        self.z2_bu = Button(self.z2_dolni, text="Graf", width=10, height=2, command=self.graf_zalozka1)
        self.z2_bu.pack(padx=2, pady=2, fill= 'y', anchor=SE)
        self.z2_dolni.pack(fill = 'both', anchor=S, expand=1)
        self.z2_hlavni.pack(fill = 'both', padx=2, pady=2, anchor=W, side='left', expand=1)
    ####### Prava tabulka #######       
        self.z2_f2 = Frame(self.z2_exp_nad, borderwidth=2)
        self.z2_fr1=LabelFrame(self.z2_f2, relief=GROOVE, borderwidth=2, text='Četnost')
        self.z2_b5 = Radiobutton(self.z2_fr1, text="Absolutní", variable=self.z2_hodnota2, value="Absolutni")
        self.z2_b5.pack(anchor=W,  padx=4)
        self.z2_bcr = Radiobutton(self.z2_fr1, text="Relativní", variable=self.z2_hodnota2, value="Relativni")
        self.z2_bcr.pack(anchor=W,  padx=4)
        self.z2_fr1.pack(fill = 'both', anchor=N, expand=1)
        self.z2_fr2=LabelFrame(self.z2_f2, relief=GROOVE, borderwidth=2, text='Typ grafu')
        self.z2_b6 = Radiobutton(self.z2_fr2, text="Histogram", variable=self.z2_hodnota3, value="Histogram", command=self.nastavenihis2)
        self.z2_b6.pack(anchor=W,  padx=4)
        self.z2_btk = Radiobutton(self.z2_fr2, text="Koláčový", variable=self.z2_hodnota3, value="Kolacovy", command=self.nastavenikol2)
        self.z2_btk.pack(anchor=W,  padx=4)
        self.z2_btkr = Radiobutton(self.z2_fr2, text="Krabicový", state='disabled', variable=self.z2_hodnota3, value="Krabicovy", command=self.nastavenikra2)
        self.z2_btkr.pack(anchor=W,  padx=4)
        self.z2_fr2.pack(fill = 'both', anchor=S, expand=1)
        self.z2_f2.pack(fill = 'both', padx=2, pady=2, anchor=E, side='right', expand=1)

        self.z2_b4.select() # vybere jeden radiobutton jinak by byli zaskrtle vsechny (pohlvai)
        self.z2_b6.select() # absolutni cetnost
        self.z2_b5.select() # histogram
        
        self.z2_exp_nad.pack(fill = 'both')

####### ZALOZKA1 #######
        self.hodnota = StringVar()  #kategorie, kvuli zachovani abstraktnosti a dynamickeho pristupu ke sloupum v excelu hodnota odpovida cislu sloupce s pozadovanumi daty
        self.hodnota2 = StringVar() #cetnost
        self.hodnota3 = StringVar() #typ grafu
        self.exp_nad = Frame(self.p1, relief="sunken", borderwidth=2)
    ####### Nadpis #######
        self.f3 = Frame(self.exp_nad, borderwidth=2)
        self.la = Label(self.f3, text="Vyberte jednu z kategorií pro explorační analýzu", anchor='center')
        self.la.pack(side='top', fill='x')
        self.f3.pack(fill='both', expand=1)        
    ####### Leva tabulka #######
        self.hlavni = Frame(self.exp_nad, borderwidth=2)
        self.horni = LabelFrame(self.hlavni, relief=GROOVE, borderwidth=2, text='Kategorie')
        #self.f1 = LabelFrame(self.exp_nad, relief=GROOVE, borderwidth=2, text='Kategorie', height= 100, width = 100)
        
        self.b4 = Radiobutton(self.horni, text="Pohlaví", variable=self.hodnota, value='Pohlavi', command=self.nastavenipoh)
        self.b4.pack(anchor=W, padx=4)
        self.b1 = Radiobutton(self.horni, text="Věk", variable=self.hodnota, value='Vek', command=self.nastavenivek)
        self.b1.pack(anchor=W, padx=4)
        self.b2 = Radiobutton(self.horni, text="Oblast", variable=self.hodnota, value='Okres', command=self.nastaveniokr)
        self.b2.pack(anchor=W, padx=4)
        self.b3 = Radiobutton(self.horni, text="Dg-cytogenetic", variable=self.hodnota, value='Dg-cytogenetic', command=self.nastavenidgc)
        self.b3.pack(anchor=W,  padx=4)
        self.horni.pack(fill = 'both', anchor=N, expand=1)
        self.dolni = Frame(self.hlavni)
        self.bu = Button(self.dolni, text="Graf", width=10, height=2, command=self.graf_zalozka0)
        self.bu.pack(padx=2, pady=2, fill= 'y', anchor=SE)
        self.dolni.pack(fill = 'both', anchor=S, expand=1)
        self.hlavni.pack(fill = 'both', padx=2, pady=2, anchor=W, side='left', expand=1)
    ####### Prava tabulka #######       
        self.f2 = Frame(self.exp_nad, borderwidth=2)
        self.fr1=LabelFrame(self.f2, relief=GROOVE, borderwidth=2, text='Četnost')
        self.b5 = Radiobutton(self.fr1, text="Absolutní", variable=self.hodnota2, value="Absolutni")
        self.b5.pack(anchor=W,  padx=4)
        self.bcr = Radiobutton(self.fr1, text="Relativní", variable=self.hodnota2, value="Relativni")
        self.bcr.pack(anchor=W,  padx=4)
        self.fr1.pack(fill = 'both', anchor=N, expand=1)
        self.fr2=LabelFrame(self.f2, relief=GROOVE, borderwidth=2, text='Typ grafu')
        self.b6 = Radiobutton(self.fr2, text="Histogram", variable=self.hodnota3, value="Histogram", command=self.nastavenihis)
        self.b6.pack(anchor=W,  padx=4)
        self.btk = Radiobutton(self.fr2, text="Koláčový", variable=self.hodnota3, value="Kolacovy", command=self.nastavenikol)
        self.btk.pack(anchor=W,  padx=4)
        self.btkr = Radiobutton(self.fr2, text="Krabicový", state='disabled', variable=self.hodnota3, value="Krabicovy", command=self.nastavenikra)
        self.btkr.pack(anchor=W,  padx=4)
        self.fr2.pack(fill = 'both', anchor=S, expand=1)
        self.f2.pack(fill = 'both', padx=2, pady=2, anchor=E, side='right', expand=1)

        
        self.exp_nad.pack(fill = 'both')
        
        
        self.b4.select() # vybere jeden radiobutton jinak by byli zaskrtle vsechny (pohlvai)
        self.b6.select() # absolutni cetnost
        self.b5.select() # histogram
        self.nb.pack(expand=1, fill=BOTH,padx=10,pady=5)
        self.top.title('Explorační analýza')

    def liTakeOver(self, event):
        self.z3_la.configure(text=self.z3_li.get("active"), foreground="#00B000")
        self.kategorie_seznam=self.z3_li.get("active")#zjisti aktivovanoz kategorii v seznamu

##pomocne funkce ktere identifikuji zalozku excelu pred vygenerovanim grafu
    def graf_zalozka0(self):
        cetnost=self.hodnota2.get()
        typ=self.hodnota3.get()
        kategorie=self.hodnota.get()
        self.graf(0, cetnost, typ, kategorie)

    def graf_zalozka1(self):
        cetnost=self.z2_hodnota2.get()
        typ=self.z2_hodnota3.get()
        kategorie=self.z2_hodnota.get()
        self.graf(1, cetnost, typ, kategorie)

    def graf_zalozka2(self):
        cetnost=self.z4_hodnota2.get()
        typ=self.z4_hodnota3.get()
        kategorie=self.z4_hodnota.get()
        self.graf(2, cetnost, typ, kategorie)

    def graf_zalozka3(self):
        cetnost=self.z3_hodnota2.get()
        typ=self.z3_hodnota3.get()
        kategorie=self.kategorie_seznam            
        if kategorie=='':
            self.z3_la.configure(text=u'NEZVOLILI JSTE KATEGORII !!!', foreground="red")
        else:
            self.graf(3, cetnost, typ, kategorie, 2)

    def graf_zalozka4(self):
        cetnost=self.z5_hodnota2.get()
        typ=self.z5_hodnota3.get()
        kategorie=u'POČET NEMOCNÝCH'
        self.graf(4, cetnost, typ, kategorie, 2)

    def graf_zalozka5(self):
        cetnost=self.z6_hodnota2.get()
        typ=self.z6_hodnota3.get()
        kategorie=u'POCET NEMOCNYCH'
        self.graf(5, cetnost, typ, kategorie, 2)

## vygenerovani grafu po stisknuti tlacitka graf v exploracni analyze
    def graf(self, zalozka, cetnost, typ, kategorie, varianta=1):
        sh=self.soubor.sheet_by_name(self.zalozky[zalozka])
        data=[]
        if kategorie=='Pohlavi':
            for row in range(sh.nrows):
                data.append(sh.row_values(row)[2])
            del data[0]
            #print 'prvni'
            grafy.pohlavi(data, cetnost,typ)
        elif kategorie=='Vek':
            for row in range(sh.nrows):
                data.append(sh.row_values(row)[3])
            del data[0]
            #print 'druhy'
            grafy.vek(data, cetnost,typ)
        elif varianta==1:#podminak resi problem kdy ve sloupcich se nenachcazi jednotlive hodnoty kategorie(př. muž, muž, žena) ale přímo jeji absolutni četnost
            #print "prvni varianta"
            for col in range(sh.ncols): #zjisti cislo sloupce na zaklade ziskane hodnoty jmena
                if sh.col_values(col)[0]==kategorie:
                    zalozka=col
            for row in range(sh.nrows):
                data.append(sh.row_values(row)[zalozka])
            
            nazev=data[0]
            del data[0]
            
            
            #print 'treti'
            #print data
            i=0
            for prvek in data:
                data[i]=prvek.replace(u"ř","r")
                data[i]=data[i].replace(u"ě","e")
                i=i+1
            grafy.obecne(data, cetnost,typ, nazev)
        elif varianta==2:#podminak resi problem kdy ve sloupcich se nenachcazi jednotlive hodnoty kategorie(př. muž, muž, žena) ale přímo jeji absolutni četnost
            #print "druha varianta"
            promenna_x=[]
            for col in range(sh.ncols): #zjisti cislo sloupce na zaklade ziskane hodnoty jmena
                if sh.col_values(col)[0]==kategorie:
                    zalozka=col
            for row in range(sh.nrows):
                data.append(sh.row_values(row)[zalozka])
                promenna_x.append(sh.row_values(row)[0])
            if self.z5_hodnota.get()=="Pomer":#pocet nemocnych vuci poctu obyvatel v oblasti
                podil=[]
                for row in range(sh.nrows):
                    podil.append(sh.row_values(row)[1]) #celkovy pocet obyvatel v oblasti
                del podil[0]
                del podil[len(podil)-1]
                #print podil
            nazev=data[0]
            del data[0]
            del promenna_x[0]
            del data[len(data)-1]
            del promenna_x[len(promenna_x)-1]
            if self.z5_hodnota.get()=="Pomer":
                i=0
                #print data, podil
                for hodnoty in data:
                    if data[i]!=0:
                        data[i]=float(data[i])/podil[i]
                    i=i+1
                    
            #print 'treti'
            i=0
            for prvek in promenna_x:
                promenna_x[i]=promenna_x[i].replace(u"ř","r")
                promenna_x[i]=promenna_x[i].replace(u"ě","e")
                promenna_x[i]=promenna_x[i].replace(u"ť","t")
                i=i+1
            grafy.obecne(data, cetnost,typ, nazev, promenna_x)

#####nastaveni radiobuttonu (RB), povoleni nebo zamezeni pristupu na prvni zalozce#####
## pri kliknuti na RB kolacovy
    def nastavenikol(self):
        self.bcr.select()
        self.b5.configure(state='disabled')
        self.bcr.configure(state=NORMAL)
## na RB histogram
    def nastavenihis(self):
        self.b5.configure(state=NORMAL)
        self.bcr.configure(state=NORMAL)
        self.b5.configure(state=NORMAL)
## na RB krabicovy
    def nastavenikra(self):
        self.bcr.configure(state='disabled')
        self.b5.configure(state='disabled')
## na RB pohlavi
    def nastavenipoh(self):
        self.b6.select()
        self.btkr.configure(state='disabled')
        self.bcr.configure(state=NORMAL)
        self.b5.configure(state=NORMAL)
## na RB vek
    def nastavenivek(self):
        self.btkr.configure(state=NORMAL)
## na RB okres
    def nastaveniokr(self):
        self.btkr.configure(state='disabled')
## na RB dg-cytogenetic
    def nastavenidgc(self):
        self.btkr.configure(state='disabled')

#####nastaveni radiobuttonu (RB), povoleni nebo zamezeni pristupu na druhe zalozce#####
## pri kliknuti na RB kolacovy
    def nastavenikol2(self):
        self.z2_bcr.select()
        self.z2_b5.configure(state='disabled')
        self.z2_bcr.configure(state=NORMAL)
## na RB histogram
    def nastavenihis2(self):
        self.z2_b5.configure(state=NORMAL)
        self.z2_bcr.configure(state=NORMAL)
        self.z2_b5.configure(state=NORMAL)
## na RB krabicovy
    def nastavenikra2(self):
        self.z2_bcr.configure(state='disabled')
        self.z2_b5.configure(state='disabled')
## na RB pohlavi
    def nastavenipoh2(self):
        self.z2_b6.select()
        self.z2_btkr.configure(state='disabled')
        self.z2_bcr.configure(state=NORMAL)
        self.z2_b5.configure(state=NORMAL)
## na RB vek
    def nastavenivek2(self):
        self.z2_btkr.configure(state=NORMAL)
## na RB obvod
    def nastaveniobv2(self):
        self.z2_b5.configure(state=NORMAL)
        self.z2_bcr.configure(state=NORMAL)
        self.z2_b6.select()
        self.z2_btkr.configure(state='disabled')

#####nastaveni radiobuttonu (RB), povoleni nebo zamezeni pristupu na treti zalozce#####
## pri kliknuti na RB kolacovy
    def nastavenikol3(self):
        self.z4_bcr.select()
        self.z4_b5.configure(state='disabled')
        self.z4_bcr.configure(state=NORMAL)
## na RB histogram
    def nastavenihis3(self):
        self.z4_b5.configure(state=NORMAL)
        self.z4_bcr.configure(state=NORMAL)
        self.z4_b5.configure(state=NORMAL)
## na RB krabicovy
    def nastavenikra3(self):
        self.z4_bcr.configure(state='disabled')
        self.z4_b5.configure(state='disabled')
## na RB pohlavi
    def nastavenipoh3(self):
        self.z4_b6.select()
        self.z4_btkr.configure(state='disabled')
        self.z4_bcr.configure(state=NORMAL)
        self.z4_b5.configure(state=NORMAL)
## na RB vek
    def nastavenivek3(self):
        self.z4_btkr.configure(state=NORMAL)
## na RB dg-cytogenetic
    def nastavenidgc3(self):
        self.z4_b5.configure(state=NORMAL)
        self.z4_bcr.configure(state=NORMAL)
        self.z4_b6.select()
        self.z4_btkr.configure(state='disabled')

#####nastaveni radiobuttonu (RB), povoleni nebo zamezeni pristupu na ctvrte zalozce#####
## pri kliknuti na RB kolacovy
    def nastavenikol4(self):
        self.z3_bcr.select()
        self.z3_b5.configure(state='disabled')
        self.z3_bcr.configure(state=NORMAL)
## na RB histogram
    def nastavenihis4(self):
        self.z3_b5.configure(state=NORMAL)
        self.z3_bcr.configure(state=NORMAL)
        self.z3_b5.configure(state=NORMAL)

#####nastaveni radiobuttonu (RB), povoleni nebo zamezeni pristupu na pate zalozce#####
## pri kliknuti na RB kolacovy
    def nastavenikol5(self):
        self.z5_bcr.select()
        self.z5_b5.configure(state='disabled')
        self.z5_bcr.configure(state=NORMAL)
## na RB histogram
    def nastavenihis5(self):
        self.z5_b5.configure(state=NORMAL)
        self.z5_bcr.configure(state=NORMAL)
        self.z5_b5.configure(state=NORMAL)
        if self.z5_hodnota.get()=='Pomer':
            self.z5_bcr.select()
            self.z5_b5.configure(state='disabled')
## na RB pocet nemocnych v castech ostravy
    def nastaveniost5(self):
        self.z5_b5.configure(state=NORMAL)
        self.z5_bcr.configure(state=NORMAL)
        pass
## na RB nemocni ku poctu obyvatel
    def nastavenipom5(self):
        self.z5_bcr.select()
        self.z5_b5.configure(state='disabled')
        pass

#####nastaveni radiobuttonu (RB), povoleni nebo zamezeni pristupu na seste zalozce#####
## pri kliknuti na RB kolacovy
    def nastavenikol6(self):
        self.z6_bcr.select()
        self.z6_b5.configure(state='disabled')
        self.z6_bcr.configure(state=NORMAL)
## na RB histogram
    def nastavenihis6(self):
        self.z6_b5.configure(state=NORMAL)
        self.z6_bcr.configure(state=NORMAL)
        self.z6_b5.configure(state=NORMAL)
        if self.z6_hodnota.get()=='Pomer':
            self.z6_bcr.select()
            self.z6_b5.configure(state='disabled')
## na RB pocet nemocnych v castech ostravy
    def nastaveniopv6(self):
        self.z6_b5.configure(state=NORMAL)
        self.z6_bcr.configure(state=NORMAL)
        pass
## na RB nemocni ku poctu obyvatel
    def nastavenipom6(self):
        self.z6_bcr.select()
        self.z6_b5.configure(state='disabled')
        pass

root = Tix.Tk()
app = interface(root)
root.mainloop()
