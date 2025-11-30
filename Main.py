import time


def dosya_okuma(dosya_adi):
    with open(dosya_adi + ".txt", "r") as f:
        icerik = f.read()
    return icerik

def dosya_kayit(dosya_adi,sureB,sureS,adimsayB,adimsayS,sonucB,sonucS):
    with open(dosya_adi + ".txt", "a",encoding="utf-8") as f:
        f.write(f"BubbleSort suresi:{sureB}\tSelectionSort süresi:{sureS}\nBubbleSort Adım Sayısı:{adimsayB}\tSelectionSort Adım Sayısı:{adimsayS}\nBubbleSort Sonuç:{sonucB}\tSelectionSort Sonuç:{sonucS}\n\n")
def bubbleSort(listeB):
    baslangic_zamani = time.perf_counter()
    a = len(listeB)
    global b 
    b = 0
    for i in range(a):
        for j in range(0, a-i-1):
            if listeB[j] > listeB[j+1]:
                listeB[j], listeB[j+1] = listeB[j+1], listeB[j]
                b += 1
    bitis_zamani = time.perf_counter()
    global gecen_zamanB
    gecen_zamanB = str(f"{bitis_zamani - baslangic_zamani:10f}")
    return listeB

def selectionSort(listeS):
    baslangic_zamani = time.perf_counter()
    a = len(listeS)
    global c 
    c = 0
    for i in range(a):
        min_idx = i
        for j in range(i+1, a):
            if listeS[j] < listeS[min_idx]:
                min_idx = j
        listeS[i], listeS[min_idx] = listeS[min_idx], listeS[i]
        c += 1
    bitis_zamani = time.perf_counter()
    global gecen_zamanS
    gecen_zamanS = str(f"{bitis_zamani - baslangic_zamani:10f}")
    return listeS

soru = input("Dosya adını giriniz (uzantısız): ")
kayit_soru = input("Kayit Dosyasi Adi ne olsun (uzantısız): ")

dosya = dosya_okuma(soru).split(",")
dosya = [int(x) for x in dosya]


bubbleSort(dosya)
selectionSort(dosya)
dosya_kayit(kayit_soru,gecen_zamanB,gecen_zamanS,b,c,bubbleSort(dosya),selectionSort(dosya))
dosya_okuma(soru)

print("işlem gerçekleştiriliyor..")