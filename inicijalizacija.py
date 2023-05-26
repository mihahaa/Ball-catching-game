import numpy as np

# definisemo velicine prozora u kojem se desava interakcija

prozorD = 800
prozorV = 400

# neophodne boje neugradjene sistemski

ZUTA = (255, 255, 0)
PLAVA = (0, 255, 255)
BRAON = (102, 51, 0)

# definisanje konstantnih parametara loptica kruzica

krugR = 20
brzina_padanja = prozorV / 10

# definisanje velicina korpe (pravougaonika)

korpaL = 100
korpaG = 365
korpaD = 160
korpaV = 35

# niz sa indeksima unikatnih stanja

QIDic = {}

#Q-tabela

Q = np.zeros([5000, 3])

# klasa Krug sa X i Y koordinatama centra kao parametrima 

class Krug:

    def __init__(x, kX, kY):
        x.kX = kX
        x.kY = kY

# klasa Centar sa pravougaonikom i krugom kao parametrima

class Stanje:

    def __init__(x, pu, kg):
        x.pu = pu
        x.kg = kg
