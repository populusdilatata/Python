# -*- coding: utf-8 -*-
import numpy
import matplotlib.pyplot
import xlrd

def pohlavi(data, cetnost, typ):
    muzi=0
    zeny=0
    y=[]
    x=[]
    for pohlavi in data:
        if pohlavi == 'M':
            muzi = muzi+1
        if pohlavi == 'Z':
            zeny = zeny+1
    y=[muzi, zeny]
    x=[u'Muži', u'Ženy']
    cetnost_text=u'Absolutní četnost'
    if cetnost=='Relativni':
        y=[muzi/float(muzi+zeny)*100, zeny/float(muzi+zeny)*100]
        cetnost_text=u'Relativní četnost'
    if typ=='Histogram':
        width = 1.38
        ind = 2*np.arange(2)
        fig=plt.figure(u'Pohlaví', figsize=(10,5))
        plt.barh(ind, y, width, color='#92F5AF')
        plt.grid(axis='x')
        plt.xlabel(cetnost_text)
        plt.ylabel(u'Pohlaví')
        plt.ylim(-1, 2*len(x))
        plt.yticks(ind+width/2., x )
        plt.xlim(0,max(y)+1)
        plt.show(fig)
    if typ=='Kolacovy':
        fig=plt.figure(u'Pohlaví', figsize=(8,8))
        colors=('#92F5AF', '#9191FF', '#359AFF', '#FF4848', '#FFA980', 'y', 'k', 'w')
        plt.pie(y, explode=(0.025, 0.025), labels=x, colors=colors, autopct='%2.0f%%', labeldistance=1.1, shadow=False)
        plt.show(fig)

def vek(data, cetnost,typ):
    kat0=0
    kat1=0
    kat2=0
    kat3=0
    x=[]
    y=[]
    for vek in data:
        if 0<=vek<=14:
            kat0=kat0+1
        if 15<=vek<=29:
            kat1=kat1+1
        if 30<=vek<=59:
            kat2=kat2+1
        if 60<=vek:
            kat3=kat3+1
    y=[kat0, kat1, kat2, kat3]
    x=[u'0-14', u'15-29', u'30-59', u'60 a více']
    cetnost_text=u'Absolutní četnost'
    if cetnost=='Relativni':
        cetnost_text=u'Relativní četnost'
        kat=kat0 + kat1 + kat2 + kat3
        y=[kat0/float(kat)*100, kat1/float(kat)*100, kat2/float(kat)*100, kat3/float(kat)*100]
    if typ=='Histogram':
        width = 1.38
        ind = 2*np.arange(len(y))
        fig=plt.figure(u'Četnost věkových kategorií', figsize=(10, 5))
        plt.barh(ind, y, width, color='#92F5AF')
        plt.xlabel(cetnost_text)
        plt.ylabel(u'Veková kategorie')
        plt.grid(axis='x')
        plt.ylim(-0.5, 2*len(x))
        plt.yticks(ind+width/2., x )
        plt.xlim(0,max(y)+1)
        plt.show(fig)
    if typ=='Kolacovy':
        fig=plt.figure(u'Věkové kategorie', figsize=(8,8))
        colors=('#92F5AF', '#9191FF', '#359AFF', '#FF4848', '#FFA980', 'y', 'k', 'w')
        vysec=[]
        for prvek in y:
            vysec.append(0.025)
        #print vysec
        plt.pie(y, explode=vysec, labels=x, colors=colors, autopct='%1.0f%%', labeldistance=1.1, shadow=False)
        plt.show(fig)
    if typ=='Krabicovy':
        fig=plt.figure(u'Věk', figsize=(8,8))
        pom_data=[]
        for prvek in data: #zjisteni zda jsou vsechny prvky cisla a neni tam prazdny string (nevyplnene udaje) doslo by tak k chybe u krabicoveho grafu
            if is_number(prvek)==True:
                pom_data.append(prvek)
        #print pom_data
        plt.boxplot(pom_data, notch=0, sym='+', vert=1, whis=1.5, positions=None, widths=None, patch_artist=False)
        plt.ylim(min(pom_data)-5, max(pom_data)+5)
        plt.show(fig)

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def obecne(data, cetnost, typ, nazev, promenna_x=[]):
    #print promenna_x
    data_slovnik={}
    if promenna_x==[]:
        for prvek in data:
            if prvek!='':
                if data_slovnik.has_key(prvek)==True:
                    data_slovnik[prvek]=data_slovnik[prvek]+1
                else:
                    data_slovnik[prvek]=1
        celkem=sum(data_slovnik.values())
    else:
        i=0
        for mesto in promenna_x:
            data_slovnik[mesto]=data[i]
            i=i+1
    if cetnost=='Absolutni':
        cetnost_text=u'Absolutní četnost'
        if promenna_x==[]:
            x=data_slovnik.keys()
            y=data_slovnik.values()
        else:
##            knihovna={}
##            i=0
##            for prvek in data:
##                knihovna[promenna_x[i]]=data[i]
##                i=i+1
##            x=knihovna.keys()
##            x.sort()
##            y=[]
##            for prvek in x:
##                y.append(knihovna[prvek])
            y=data
            x=promenna_x
    elif cetnost=='Relativni':
        cetnost_text=u'Relativní četnost'
        if promenna_x==[]:
            for polozka in data_slovnik.keys():
                data_slovnik[polozka]=data_slovnik[polozka]/float(celkem)*100
            x=data_slovnik.keys()
            y=data_slovnik.values()
        else:
            celkem=sum(data)
            for polozka in data_slovnik:
                data_slovnik[polozka]=data_slovnik[polozka]/float(celkem)*100
            y=data_slovnik.values()
            x=data_slovnik.keys()
    if typ=='Histogram':
        width = 1.38
        ind = 2*np.arange(len(y))
        fig=plt.figure(nazev, figsize=(12, 5))
        plt.barh(ind, y, width, color='#92F5AF')
        plt.xlabel(cetnost_text)
        plt.ylabel(nazev)
        plt.grid(axis='x')
        plt.ylim(-0.5, 2*len(x))
        plt.yticks(ind+width/2., x )
        plt.xlim(0,max(y)+1)
        plt.show(fig)
    elif typ=='Kolacovy':
        vysec=[]
        for polozka in data_slovnik.keys():
            if data_slovnik[polozka]<5:
                del data_slovnik[polozka]
        x=data_slovnik.keys()
        y=data_slovnik.values()
        #print x,y
        for prvek in y:
            vysec.append(0.025)
        fig=plt.figure(nazev, figsize=(8,8))
        colors=('#92F5AF', '#9191FF', '#359AFF', '#FF4848', '#FFA980', 'y', 'r', 'w')
        plt.pie(y, explode=vysec, labels=x, colors=colors, autopct='%2.0f%%', labeldistance=1.1, shadow=False)
        plt.show(fig)

##wb=xlrd.open_workbook('Gliomy.xls')
##sh=wb.sheet_by_name(u'MS -Regionalni tabulka')
##a=[]
##b=[]
##
##for row in range(sh.nrows):
##    a.append(sh.row_values(row)[0])
##    b.append(sh.row_values(row)[4])
##
##del a[len(a)-1]
##del a[0]
##del b[0]
##del b[len(b)-1]
###print a
##print b
##
##c=[8, 10, 5, 9]
##d=[0, 1, 2, 3]
    
