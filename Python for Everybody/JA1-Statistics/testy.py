# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from math import *
from scipy.stats import stats
import time

def faktorial(x):
    if x==0:
        return 1
    else:
        return x*faktorial(x-1)

def kombinace(n, k):
    citatel=1 #implementace neni podle vzorce pro kombinaci, casove velmi narocne, postup upraven nenarocnejsim zpusbem na vypocet
    if k>n/2:
        k=n-k
    for prvek in range(k):
        citatel=citatel*n
        n=n-1
    return citatel/float(faktorial(k))

def fce_signum(cislo):
    if cislo>0:
        return 1
    if cislo<0:
        return -1

def serad(prehled):
    a=[]
    for prvek in prehled:
        #print a, prvek
        a=zarad(a, prvek)
        
    return a

def zarad(a, prvek):
    #print a
    if len(a)==0:
        a.append(prvek)
        return a
    else:
        #print 'tady'
        for i in range(len(a)):
            if abs(a[i])>=abs(prvek):
                a[i:i]=[prvek]
                return a
            elif (len(a)-1)==i:
                a.append(prvek)
                return a

def prirad_poradi(serazen):
    pocet={}
    R=[]
    for prvek in serazen:
        if pocet.has_key(abs(prvek))==True:
            pocet[abs(prvek)]=pocet[abs(prvek)]+1
        else:
            pocet[abs(prvek)]=1
    i=1
    #print pocet
    for prvek in serazen:
        if pocet.has_key(abs(prvek))==True:
            if pocet[abs(prvek)]==1:
                R.append(i)
                i=i+1
            else: 
                citatel=i
                for cislo in range(pocet[abs(prvek)]-1):
                    i=i+1
                    citatel=citatel+i
                i=i+1
                prumer=citatel/float(pocet[abs(prvek)])
                for cislo in range(pocet[abs(prvek)]):
                    R.append(prumer)
                del pocet[abs(prvek)]
    return R

def prirad_poradi_bez_prumerovani(serazen):
    pocet={}
    R=[]
    for i in range(len(serazen)):
        R.append(i+1)
    return R

def dolni_kvartil(data):
    data.sort()
    zp=len(data)*0.25+0.5
    if zp%round(zp,0)==0:
        return data[int(zp)-1]
    elif zp%round(zp,0)==zp:
        return (data[int(round(zp-2,0))]+data[int(round(zp-1,0))])/float(2)
    else:
        return (data[int(round(zp,0))]+data[int(round(zp-1,0))])/float(2)

def horni_kvartil(data):
    data.sort()
    zp=len(data)*0.75+0.5
    if zp%round(zp,0)==0:
        return data[int(zp)-1]
    elif zp%round(zp,0)==zp:
        return (data[int(round(zp-2,0))]+data[int(round(zp-1,0))])/float(2)
    else:
        return (data[int(round(zp,0))]+data[int(round(zp-1,0))])/float(2)

def intervalovy_odhad_medianu(data):
    d=median(data)-1.57*((horni_kvartil(data)-dolni_kvartil(data))/float(sqrt(len(data))))
    h=median(data)+1.57*((horni_kvartil(data)-dolni_kvartil(data))/float(sqrt(len(data))))
    return round(d,3), round(h, 3)

def median(data):
    data.sort()
    #print len(data)
    zp=len(data)*0.5+0.5
    if zp%round(zp,0)==0:
        return data[int(zp)-1]
    else:
        return (data[int(zp-1.5)]+data[int(zp-0.5)])/float(2)
##    elif zp%round(zp,0)==zp:
##        return (data[int(round(zp-2,0))]+data[int(round(zp-1,0))])/float(2)
##    else:
##        return (data[int(round(zp,0))]+data[int(round(zp-1,0))])/float(2)      

def pocet_hodnot(data, hodnota):
    p=0
    for cislo in data:
       if cislo==hodnota:
           p=p+1
    return p

def chi_kvadrat_kvantil(stupne, alpha):
    Fx=0
    i=0
    pom=[]
    while (Fx<0.999):
        Fx=1-(stats.chisqprob(i,stupne))
        i=i+0.0005
        if Fx>=alpha:
            pom.append(i)
    return min(pom)

def test_z_chi_kvadratu(data, stupne, alpha):
    #print (1-(stats.chisqprob(x, stupne)))
    data.sort()
    R=prirad_poradi(data)
    F=[]
    Dv=[]
    Dp=[]
    pom={}
    pom2={}
    for prvek in data:
        if pom.has_key(prvek):
            pom[prvek]=pom[prvek]+1
        else:
            pom[prvek]=1
        if pom2.has_key(prvek):
            pom2[prvek]=pom2[prvek]+1
        else:
            pom2[prvek]=1
    hodnoty=pom.keys()
    kum_cet1=[]
    kum_cet2=[]
    i=0
    for prvky in data:
        if pom.has_key(prvky):
            kum_cet1.append((pom[prvky]+i)/float(len(data)))
            kum_cet2.append((pom[prvky]+i)/float(len(data)))
            i=i+pom[prvky]
            del pom[prvky]
    del kum_cet2[len(kum_cet2)-1]
    kum_cet2[0:0]=[0]
    hodnoty.sort()
    for j in range(len(kum_cet1)):
        #z0=(hodnoty[j]-stred)/float(odch)
        F.append(1-(stats.chisqprob(hodnoty[j], stupne)))
        Dv.append(abs(kum_cet1[j]-F[j]))
        Dp.append(abs(kum_cet2[j]-F[j]))
    kriticka=sqrt(1/float(2*len(data))*log(2/float(alpha)))
    pozorovana = max(max(Dv), max(Dp))
    #print Dv, Dp
    return pozorovana, kriticka

def kruskaluv_wallisuv_test(data, hladina):
    vsechny_data=[]
    T={}
    n=0
    for prvek in data.keys():
        n=n+len(data[prvek])
        for cisla in data[prvek]:
            vsechny_data.append(cisla)
    vsechny_data.sort()
    R=prirad_poradi(vsechny_data)
    pom={}
    for prvek in vsechny_data:
        if pom.has_key(prvek)==True:
            pom[prvek]=pom[prvek]+1
        else:
            pom[prvek]=1
    hodnoty=pom.keys()
    hodnoty.sort()
    i=0
    for klice in data.keys():
        T[klice]=0
    for hodnota in hodnoty:
        for prvek in data.keys():
            if (hodnota in data[prvek]) == True:
                pocet_h= pocet_hodnot(data[prvek], hodnota)
                if (pocet_h)>1:
                    for pocet in range(pocet_h):
                        T[prvek]=T[prvek]+R[i]
                        i=i+1
                else:
                    T[prvek]=T[prvek]+R[i]
                    i=i+1
    #print n, T
    t=[]
    for prvek in T.keys():
        t.append(T[prvek]/float(len(data[prvek])))
    suma=0
    for prvek in T.keys():
        suma=suma+float((T[prvek])**2)/len(data[prvek])
    xobs=(-3)*(n+1)+float(12)/(n*(n+1))*suma
    stupne=len(data.keys())-1
    #print stupne
    p_hodnota=stats.chisqprob(round(xobs, 3), stupne)#vraci 1-F(xobs) pro chi-kvadrat
    #print round(xobs, 3), p_hodnota
    return p_hodnota, post_hoc(data, hladina, t)
    
##    del (data[1])[0]
##    print data

def wilcoxonuv_test(nazev, data, hladina, median, Ha):
    Splus=0
    Sminus=0
    prehled=[]
    S=0
    for prvek in data:
        if (prvek-median)!=0:
            prehled.append(prvek-median)
    serazen=serad(prehled)
    R=prirad_poradi(serazen)
    i=0
    for prvek in serazen:
        S=S+R[i]*fce_signum(prvek)
        i=i+1
    n=i
    Splus=(float(1)/2)*S+(n*(n+1))/float(4)
    ESplus=n*(n+1)/float(4)
    varSplus=(float(1)/24)*n*(n+1)*(2*n+1)
    #print varSplus, Splus, ESplus, n
    U=float(Splus-ESplus)/(sqrt(varSplus))
    if Ha==u'\u2260':
        pulAlpha=(hladina)/float(2)
    else:
        pulAlpha=hladina
    alpha=1-pulAlpha
    pom=0
    if alpha>0.5:
        alpha=1-alpha
        pom=1
    w=sqrt(-2*log(alpha))
    a=[2.515517, 0.802853, 0.010328]
    b=[1, 1.432788, 0.189269, 0.001308]
    sumaA=0
    sumaB=0
    i=0
    for prvek in a:
        sumaA=sumaA+a[i]*(w**(i))
        i=i+1
    i=0
    for prvek in b:
        sumaB=sumaB+b[i]*(w**(i))
        i=i+1
    kriticka=-w+float(sumaA)/sumaB
    if pom==1:
        kriticka=(-1)*kriticka
    #print "vysledky"
    #print U, kriticka
    return U, kriticka

def dvouvyberovy_wilcoxonuv_test(data1, data2, hladina, Ha):
    wi_seznam={}
    n1_pom=len(data1)
    n2_pom=len(data2)
    otoceni_poradi=0
    if n1_pom<=n2_pom:
        n1=n1_pom
        n2=n2_pom
        pom_data1=data1
        pom_data2=data2
    else:
        n1=n2_pom
        n2=n1_pom
        pom_data1=data2
        pom_data2=data1
        otoceni_poradi=1
    celkem_data=data1+data2
    celkem_data.sort()
    w1=0
    w2=0
    R = prirad_poradi(celkem_data)
    i=0
    pom=[]
    for prvek in celkem_data:
        if prvek in pom_data1 and prvek in pom_data2:
            w1=w1+R[i]
            i=i+1
            w2=w2+R[i]
            i=i+1
            pom_data1=vymaz_polozku(pom_data1, prvek)
            pom_data2=vymaz_polozku(pom_data2, prvek)
        elif prvek in pom_data1:
            w1=w1+R[i]
            i=i+1
            pom_data1=vymaz_polozku(pom_data1, prvek)
        elif prvek in pom_data2:
            i=i+1
            pom_data2=vymaz_polozku(pom_data2, prvek)
    w2=((n1+n2)*(n1+n2+1))/float(2)-w1
    sw1=(n1*(n1+n2+1))/float(2)
    rw1=(n1*n2*(n1+n2+1))/float(12)
    U=(w1-sw1)/float(sqrt(rw1))
    if Ha=='>':
        kriticka=test_normality(hladina)
    elif Ha=='<':
        kriticka=(-1)*test_normality(hladina)
    else:
        kriticka=test_normality(hladina/float(2))
    return U, kriticka, otoceni_poradi

######prepocet z na F(z)######
def distrib_fce_norm_roz(x):
    zn='+'
    if x<0:
        zn='-'
        x=(-1)*x
    a=[0.2316419, 0.3193815, -0.3565638, 1.781478, -1.821256, 1.330274]
    w=float(1)/(1+a[0]*x)
    suma=0
    for i in range(5):
        suma=suma+a[i+1]*w**(i+1)
    fi=float(1)/(sqrt(2*pi))*e**(((-1)*x**(2))/float(2))
    if zn=='-':
        return 1-(1-fi*suma)
    else:
        return 1-fi*suma

def exponencialni_rozdeleni(data, alpha):
    n=len(data)
    M=sum(data)/float(n)#vyberovy prumer
    suma=0
    for prvek in data:
        suma=suma+(prvek-M)**2
    S2=1/float(n-1)*suma#vyberovy rozptyl
    K=(n-1)*S2/float(M**2)
    stupne=n-1
    #print stupne
    kriticka_leva=chi_kvadrat_kvantil(stupne, alpha/float(2))
    kriticka_prava=chi_kvadrat_kvantil(stupne, 1-(alpha/float(2)))
    return K, kriticka_leva, kriticka_prava
    
    

def dvouvyberovy_kolmogorovuv_smir(data1, data2, alpha):
    distribucni_fce1=prirad_distribucni_funkci(data1)
    distribucni_fce2=prirad_distribucni_funkci(data2)
    #print distribucni_fce1
    #print distribucni_fce2
    distribucni_fce1_levy=distribucni_fce1[0]
    distribucni_fce2_levy=distribucni_fce2[0]
    distribucni_fce1_pravy=distribucni_fce1[1]
    distribucni_fce2_pravy=distribucni_fce2[1]
    pom1={}
    pom2={}
    for prvek in data1:
        if pom1.has_key(prvek)==True:
            pom1[prvek]=pom1[prvek]+1
        else:
            pom1[prvek]=1
    for prvek in data2:
        if pom2.has_key(prvek)==True:
            pom2[prvek]=pom2[prvek]+1
        else:
            pom2[prvek]=1
    hodnota1=pom1.keys()
    hodnota1.sort()
    #print hodnota1
    hodnota2=pom2.keys()
    hodnota2.sort()
    #print hodnota2
    D=[]
    k=0
    for prvek in hodnota1:
        if prvek==min(hodnota1) and hodnota1[0]<hodnota2[0]:
            beta=0
        else:
            for i in range(len(hodnota2)-1):
                if prvek>=hodnota2[i] and prvek<=hodnota2[i+1]:
                    #print "jsem tu"
                    D.append(abs(distribucni_fce1_levy[k]-distribucni_fce2_levy[i]))
                    D.append(abs(distribucni_fce1_pravy[k]-distribucni_fce2_levy[i]))
                elif prvek>max(hodnota2) and i==max(range(len(hodnota2)-1)):
                    #print "jsem tu2"
                    D.append(abs(distribucni_fce1_levy[k]-1))
                    D.append(abs(distribucni_fce1_pravy[k]-1))
        k=k+1
    k=0
    for prvek in hodnota2:
        if prvek==min(hodnota2) and hodnota2[0]<hodnota1[0]:
            D.append(abs(0-distribucni_fce2_levy[0]))
        else:
            for i in range(len(hodnota1)-1):
                if prvek>=hodnota1[i] and prvek<=hodnota1[i+1]:
                    #print "jsem tu"
                    D.append(abs(distribucni_fce2_levy[k]-distribucni_fce1_levy[i]))
                    D.append(abs(distribucni_fce2_pravy[k]-distribucni_fce1_levy[i]))
                elif prvek>max(hodnota1) and i==max(range(len(hodnota1)-1)):
                    #print "jsem tu2"
                    D.append(abs(distribucni_fce2_levy[k]-1))
                    D.append(abs(distribucni_fce2_pravy[k]-1))
        k=k+1
    n1=len(data1)
    n2=len(data2)
    M=n1*n2/float(n1+n2)
    kriticka=sqrt(1/float(2*M)*log(2/float(alpha)))
    return max(D), kriticka

def prirad_distribucni_funkci(data):
    data.sort()
    pom={}
    pom2={}
    for prvek in data:
        if pom.has_key(prvek):
            pom[prvek]=pom[prvek]+1
        else:
            pom[prvek]=1
        if pom2.has_key(prvek):
            pom2[prvek]=pom2[prvek]+1
        else:
            pom2[prvek]=1
    hodnoty=pom.keys()
    kum_cet1=[]
    kum_cet2=[]
    i=0
    for prvky in data:
        if pom.has_key(prvky):
            kum_cet1.append((pom[prvky]+i)/float(len(data)))
            kum_cet2.append((pom[prvky]+i)/float(len(data)))
            i=i+pom[prvky]
            del pom[prvky]
    del kum_cet2[len(kum_cet2)-1]
    kum_cet2[0:0]=[0]
    return kum_cet1, kum_cet2

def jednov_kolm_smir_test(data, stred, odch, alpha):
    data.sort()
    R=prirad_poradi(data)
    F=[]
    Dv=[]
    Dp=[]
    pom={}
    pom2={}
    for prvek in data:
        if pom.has_key(prvek):
            pom[prvek]=pom[prvek]+1
        else:
            pom[prvek]=1
        if pom2.has_key(prvek):
            pom2[prvek]=pom2[prvek]+1
        else:
            pom2[prvek]=1
    hodnoty=pom.keys()
    kum_cet1=[]
    kum_cet2=[]
    i=0
    for prvky in data:
        if pom.has_key(prvky):
            kum_cet1.append((pom[prvky]+i)/float(len(data)))
            kum_cet2.append((pom[prvky]+i)/float(len(data)))
            i=i+pom[prvky]
            del pom[prvky]
    del kum_cet2[len(kum_cet2)-1]
    kum_cet2[0:0]=[0]
    hodnoty.sort()
    for j in range(len(kum_cet1)):
        z0=(hodnoty[j]-stred)/float(odch)
        F.append(distrib_fce_norm_roz(z0))
        Dv.append(abs(kum_cet1[j]-F[j]))
        Dp.append(abs(kum_cet2[j]-F[j]))
    kriticka=sqrt(1/float(2*len(data))*log(2/float(alpha)))
    pozorovana = max(max(Dv), max(Dp))
    return pozorovana, kriticka

def vymaz_polozku(data, polozka):
    for i in range(len(data)):
        if data[i]==polozka:
            del data[i]
            return data

def normalita_podle_spicatosti(data, alpha):
    prumer=0
    suma4=0
    suma3=0
    suma2=0
    n=len(data)
    for prvek in data:
        prumer=prumer+prvek
    prumer=prumer/float(len(data))
    for prvek in data:
        suma4=suma4+(prvek-prumer)**4
        suma3=suma3+(prvek-prumer)**3
        suma2=suma2+(prvek-prumer)**2
    M4=1/float(n)*suma4
    M3=1/float(n)*suma3
    M2=1/float(n)*suma2
    sikmost=float(M3)/(M2)**(3/float(2))
    spicatost=float(M4)/(M2)**2
    #print sikmost, spicatost
    Espi=3-6/float(n+1)
    varSik=6*(n-2)/float((n+1)*(n+3))
    varSpi=24*n*(n-2)*(n-3)/float(((n+1)**2)*(n+3)*(n+5))
    #print varSik, varSpi
    U=abs(sikmost)/float(varSik**(1/float(2)))
    U2=abs(spicatost-Espi)/float(varSpi**(1/float(2)))
    return U, U2, test_normality(alpha/float(2))

def test_normality(pulAlpha):#spatne pojmenovane
    pom=0
    alpha=1-pulAlpha
    if alpha>0.5:
        alpha=1-alpha
        pom=1
    w=sqrt(-2*log(alpha))
    a=[2.515517, 0.802853, 0.010328]
    b=[1, 1.432788, 0.189269, 0.001308]
    sumaA=0
    sumaB=0
    i=0
    for prvek in a:
        sumaA=sumaA+a[i]*(w**(i))
        i=i+1
    i=0
    for prvek in b:
        sumaB=sumaB+b[i]*(w**(i))
        i=i+1
    kriticka=-w+float(sumaA)/sumaB
    if pom==1:
        kriticka=abs(kriticka)
    return abs(kriticka)

def znamenkovy_test(nazev, data, hladina, median, Ha):
    rozdil=[]
    rplus=0
    rminus=0
    for prvek in data:
        rozdil.append(prvek-median)
        if (prvek-median)<0:
            rminus=rminus+1
        elif (prvek-median)>0:
            rplus=rplus+1
    if Ha=='<':
        suma=0
        for prvek in range(rplus+1):
            suma=suma+(kombinace(len(data), prvek))*((0.5)**prvek)*((0.5)**(len(data)-prvek))
        phodnota=suma
    elif Ha=='>':
        suma=0
        for prvek in range(rplus,len(data)+1):
            suma=suma+(kombinace(len(data), prvek))*((0.5)**prvek)*((0.5)**(len(data)-prvek))
        phodnota=suma
    elif Ha==u'\u2260':
        suma=0
        if rplus>(len(data)/2):
            for prvek in range(rplus,len(data)+1):
                suma=suma+(kombinace(len(data), prvek))*((0.5)**prvek)*((0.5)**(len(data)-prvek))
        else:
            for prvek in range(rplus+1):
                suma=suma+(kombinace(len(data), prvek))*((0.5)**prvek)*((0.5)**(len(data)-prvek))
        phodnota=2*suma
    return phodnota

def post_hoc(data, alpha,t):
    n=0
    for prvek in data.keys():
        n=n+len(data[prvek])
    hladina=1-alpha/float(kombinace(len(data.keys()),2))
    z=test_normality(hladina)
    koef=sqrt(1/float(12)*n*(n+1)*z)
    i=0
    vysledek={}
    pom_data=[]
    for prvek in data.keys():
        pom_data.append(data[prvek])
    for prvek in data.keys():
        k=i+1
        if i<=(len(data.keys())-2):
            for prvek1 in range(len(data.keys())):
                if prvek1>=k:
                    n1=len(pom_data[i])
                    n2=len(pom_data[prvek1])
                    prehled=(pom_data[i], pom_data[prvek1])
                    vysledek[abs(t[i]-t[prvek1]),koef*sqrt(1/float(n1)+1/float(n2))]=prehled
        i=i+1
    return vysledek #klic: prvni pozorovana hodnota, druhy kriticka, value data
##x=[]
##y=[]
##i=1
##while i<=120:
##    t1=time.clock()
##    chi_kvadrat_kvantil(i, 0.99)
##    t2=time.clock()
##    x.append(i)
##    y.append(round(t2-t1))
##    i=i+1
##print x
##print y
##print median([22, 82, 27, 43, 19, 47,41,34,34,42,35])
##print test_normality(0.025)
##print intervalovy_odhad_medianu([22, 82, 27, 43, 19, 47,41,34,34,42,35])
##print prirad_distribucni_funkci([22, 82, 27, 43, 19, 19,41,34,34,82])
##data={}
##data[1]=[55, 54, 58, 61, 52, 60, 53, 65]
##data[2]=[52, 50, 51, 51, 49]
##data[3]=[47, 53, 49, 50, 46, 48, 50]
##t=[16.25, 8.4, 5.43]
##post_hoc(data, 0.05,t)
##print kruskaluv_wallisuv_test(data, 0.05)
#test_z_chi_kvadratu(25, 10)
##print test_normality(0.05)
##print test_z_chi_kvadratu([5, 6, 7, 8, 9, 11, 12, 14, 16, 35], 10, 0.05)
##t=stats.distributions.t_gen(name="t", longname="Student T", shapes="df", extradoc="")
##print t
##print stats.distributions.t.pdf(3, 10)
##print dvouvyberovy_kolmogorovuv_smir([1.5,2,3,4,5,6,7,8,9, 10], [1.5, 3.5, 5.5, 7.5, 9.5], 0.05)
##print dvouvyberovy_kolmogorovuv_smir([5.7, 5.5, 4.3, 5.9, 5.2, 5.6, 5.8, 5.1], [5, 4.5, 4.2, 5.4, 4.4], 0.05)
##print prirad_poradi_bez_prumerovani([1, 4, 6, 8, 8, 9])
##print prirad_poradi([0,0,1,2,3,3,3,4])
##data1=[0,1,2,3,3,5]
##data2=[0, 3, 4, 4]
##print distrib_fce_norm_roz(1.046)
#data1=[3238, 3195, 3246, 3190, 3204, 3254, 3229, 3225, 3217, 3241]
##data=[19.73213, 19.10783, 19.23429, 19.03771, 19.26952, 19.10462, 19.47332, 17.65991, 20.21917, 18.72712]
##data2=[20.21, 18.08, 18.96, 11.29, 20.62, 14.25, 17.84, 16.97, 13.97, 13.97, 15.92, 12.45]
##normalita_podle_spicatosti(data2)
##print jednov_kolm_smir_test(data2, 17, 3.2, 0.01)
#data2=[3261, 3187, 3209, 3212, 3258, 3248, 3215, 3226, 3240, 3234]
#data=[24, 25, 29, 20, 21, 22, 26, 23, 27, 28, 100, 98, 80, 150, 88, 40, 35, 50, 70, 68]
#dvouvyberovy_wilcoxonuv_test(data1, data2, 0.05, '<')
#print vymaz_polozku([2,3,5,5,6], 5)
#data=[2158.7, 1678.15, 2316, 2061, 2207, 1708, 2575, 2357, 2256, 2165, 2399, 1779, 2336, 1765, 2053, 2414, 2200, 2654, 1753, 1784]
#se=[7, 10, 2, -7, -5, 4]
#print test_normality(0.025)
#print prirad_poradi(serad(se))
#print wilcoxonuv_test('wil', data, 0.05, 30, 'Ha')
#znamenkovy_test('a', data, 0.01, 2000, 'ruzne')
##p=kombinace(8,3)*((0.49)**3)*((0.51)**5)
##print p
#print kombinace(5, 0)
