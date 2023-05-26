# unos biblioteka, kao i dela koda sa funkcijama

import sys

from pygame.locals import *
from rad import *

# definisanje parametara okruzenja i agenta, definisanje diskretnih konstanti alfa i gama (njih postavlja korisnik prilagodjavajuci njima brzinu ucenja) itd.

FPS = 20
vremefps = pg.time.Clock()

pg.init()

prozor = pg.display.set_mode((prozorD, prozorV))
pg.display.set_caption('Skupljac loptica')

prug = pg.Rect(korpaL, korpaG, korpaD, korpaV)

skor = 0
ukupno = 0
nagrada = 0
font = pg.font.Font(None, 30)

procenat = 0

uci = .85
y = .99
i = 0
krugCentarX = int(padanjekruga(krugR))
krugCentarY = 50

# pokretanje i zaustavljanje programa

while True:
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
    prozor.fill(PLAVA)
    
#dodavanje odredjene nagrade agentu u odnosu na to da li je ili nije uhvatio lopticu, a kako smo opisali u odeljku 4.2
    
    if krugCentarY >= prozorV - korpaV - krugR:
        nagrada = racunajrezultat(prug, Krug(krugCentarX, krugCentarY))
        krugCentarX = int(padanjekruga(krugR))
        krugCentarY = 50
    else:
        nagrada = 0
        krugCentarY += int(brzina_padanja)

# promena Q-tabele 

    s = Stanje(prug, Krug(krugCentarX, krugCentarY))
    potez = besteakcija(s)
    rez = racunajrezultat(s.pu, s.kg)
    s1 = novostanjeposleakcije(s, potez)
    Q[klasifikacija(s), potez] += uci * (rez + y
            * np.max(Q[klasifikacija(s1), :]) - Q[klasifikacija(s),
            potez])
            
# promena pozicija kako pravougaonika, tako i kruga           
            
    prug = noviprugposleakcije(s.pu, potez)
    krugCentarX = int(s.kg.kX)
    krugCentarY = int(s.kg.kY)
    pg.draw.circle(prozor, ZUTA, (krugCentarX, krugCentarY), krugR, 0)
    pg.draw.rect(prozor, BRAON, prug)

# promena skora, ukupnog broja proslih loptica i procenta uspesnosi agenta

    if nagrada == 1:
        skor += nagrada
        ukupno += nagrada
        procenat = skor / ukupno * 100
    elif nagrada == -1:
        ukupno -= nagrada
        procenat = skor / ukupno * 100

# promena interfejsa

    tekst = font.render('skor: ' + str(skor), True, (10, 250, 40))
    tekst1 = font.render('ukupno loptica: ' + str(ukupno), True, (10,
                         250, 40))
    tekst2 = font.render('procenat:' + str(procenat) + '%', True, (50,
                         250, 0))
    prozor.blit(tekst, (prozorD - 600, 10))
    prozor.blit(tekst1, (prozorD - 790, 10))
    prozor.blit(tekst2, (prozorD - 450, 10))

    pg.display.update()
    
# promena epizode (otkucaj)

    vremefps.tick(FPS)
