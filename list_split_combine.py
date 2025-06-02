
def alt_listelere_parcala(veri):
    sonuc = []
    mevcut_alt_liste = []

    for deger in veri:
        if deger is not None:
            if mevcut_alt_liste:
                mevcut_alt_liste.append(deger)
                sonuc.append(mevcut_alt_liste)
            mevcut_alt_liste = [deger]
        else:
            mevcut_alt_liste.append(deger)

    return sonuc


def alt_listeleri_birlestir(alt_listeler):
    birlesik_liste = []  # The combo list must initially be an empty list
    for alt_liste in alt_listeler:
        if birlesik_liste and birlesik_liste[-1] == alt_liste[0]:
            birlesik_liste.extend(alt_liste[1:])  # Concatenate skipping the first element
        else:
            birlesik_liste.extend(alt_liste)  # Add all
    return birlesik_liste





