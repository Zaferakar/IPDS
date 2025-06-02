import numpy as np

def ustel_tahmin(t1,y0,y1):
    print()
    if y0 == 0 and y1 > 0:#If the first value is zero and the last value is positive, it assumes the smallest positive value as zero to avoid errors
        y0 = 1e-10
    elif y0 == 0 and y1 < 0:#If the first value is zero and the last value is negative, it assumes the smallest negative value as zero to avoid errors
        y0 = -1e-10
    elif y0 == 0 and y1 == 0:#If both values are zero, no exponential increase is made and the gap between the two values is filled with zeros.
        sonuc = []
        for i in range(t1+1):
            sonuc.append(0)
        return sonuc
    else:
        pass

    k = np.log(y1 / y0) / t1
    def ustel_buyume(t, A, k):
        return A * np.exp(k * t)

    zaman_degerleri = np.linspace(0, t1, t1+1)
    liste_degerleri = [ustel_buyume(t, y0, k) for t in zaman_degerleri]

    sonuc = []
    for y in liste_degerleri:
        sonuc.append(y)
    return sonuc

def lineer_tahmin(t1,y0,y1):
    def lineer_degerler_olustur(baslangic, bitis, parca_sayisi):
        # Values are created at equal intervals, including the beginning and end
        adim = (bitis - baslangic) / (parca_sayisi - 1)
        return [baslangic + i * adim for i in range(parca_sayisi)]

    sonuc2 = lineer_degerler_olustur(y0, y1, t1+1)
    return sonuc2

def verileri_genislet(t1,y0,y1):
    def listeyi_doldur(liste, baslangic_degeri, bitis_degeri):
        yarisi = len(liste) // 2  # Half the length of the list
        for i in range(len(liste)):
            if i < yarisi:
                liste[i] = baslangic_degeri  # Extend the first section with the initial value
            else:
                liste[i] = bitis_degeri  # Extend the last section with the ending value
        return liste

    liste = [None] * (t1+1)
    sonuc3 = listeyi_doldur(liste, y0, y1)
    return sonuc3

def oldugu_gibi_birak(t1,y0,y1):
    bos_liste = []
    bos_liste.append(y0)
    bos_liste.extend([None] * (t1-1))
    bos_liste.append(y1)
    return bos_liste

