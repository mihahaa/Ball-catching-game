# unosenje biblioteka i koda iz fajla inicijalizacija 

import random
import pygame as pg
from inicijalizacija import *

# novo stanje je samo promena pozicije korpe i loptice; u odnosu na jednu od tri pomenute akcije pravougaonik moze da se krece levo, desno ili da stoji

def novostanjeposleakcije(stanje, akcija):
    prug = None 
    # promena pozicije pravougaonika
    if akcija == 2: # 2==desno; 0==stoji; 1==levo
        if stanje.pu.right + stanje.pu.width > prozorD:
            prug = stanje.pu
        else:
            prug = pg.Rect(stanje.pu.left + stanje.pu.width,
                           stanje.pu.top, stanje.pu.width,
                           stanje.pu.height) # Rect(left, top, width, height)
    elif akcija == 1:
        if stanje.pu.left - stanje.pu.width < 0:
            prug = stanje.pu
        else:
            prug = pg.Rect(stanje.pu.left - stanje.pu.width,
                           stanje.pu.top, stanje.pu.width,
                           stanje.pu.height)
    else:
        prug = stanje.pu
        # promena pozicije kruga
    noviKrug = Krug(stanje.kg.kX, stanje.kg.kY + brzina_padanja)
    return Stanje(prug, noviKrug)
    
# ova funkcija je samo deo prosle, ali sam je napisao zbog lakseg koriscenja u daljem kodu

def noviprugposleakcije(pravougaonik, akcija):
    if akcija == 2: # 2==desno; 0==stoji; 1==levo
    # promena pozicije pravougaonika 
        if pravougaonik.right + pravougaonik.width > prozorD:
            return pravougaonik
        else:
            return pg.Rect(pravougaonik.left + pravougaonik.width,
                           pravougaonik.top, pravougaonik.width,
                           pravougaonik.height)
    elif akcija == 1:
        if pravougaonik.left - pravougaonik.width < 0:
            return pravougaonik
        else:
            return pg.Rect(pravougaonik.left - pravougaonik.width,
                           pravougaonik.top, pravougaonik.width,
                           pravougaonik.height)
    else:
        return pravougaonik

# kada u korpu upadne loptica ili ona dotakne dno, potrebno je napraviti novu i to na vrhu prozora tako sto cemo je postaviti na nasumicnoj X koordinati, a uz vec poznati poluprecnik

def padanjekruga(krugR):
    noviX = 100 - krugR
    ran = random.randint(1, 8)
    noviX *= ran
    return noviX

# racunanje rezultata se radi tako sto ce rezultat biti +1 ako smo lopticu uhvatili, a -1 ako nismo

def racunajrezultat(prug, krug):
    if prug.left <= krug.kX <= prug.right:
        return 1
    else:
        return -1

# kao sto smo vec rekli, nemoguce je uzeti indeks neke vrednosti iz Q-tabele, tako da cemo svako od unikatnih stanja preko njenog pravougaonika i kruga indeksirati u listi QIDic

def klasifikacija(stanje):
    a = stanje.pu.left
    b = int(stanje.kg.kY)
    c = int(str(a) + str(b) + str(stanje.kg.kX))
    if c in QIDic:
        return QIDic[c]
    else:
        if len(QIDic):
            maxi = max(QIDic, key=QIDic.get)
            QIDic[c] = QIDic[maxi] + 1
        else:
            QIDic[c] = 1
    return QIDic[c]
    
# u funkciji ispod biramo najbolju akciju u odnosu na trenutno stanje i to bas na nacin opisan u odeljku 3.7.2

def besteakcija(stanje):
    return np.argmax(Q[klasifikacija(stanje), :])
