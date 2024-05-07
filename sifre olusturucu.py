import random

harfler = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
sayilar = "0123456789"
karakterler = "!@#$%^&*()_+-={}|[]:;<>,.?/"

uzunluk = int(input("Şifre uzunluğunu girin: "))
if uzunluk < 8:
    print("Şifre uzunluğu en az 8 karakter olmalıdır.")
else:
    harf_sayisi = int(input("Kaç harf istersiniz?: "))
    sayi_sayisi = int(input("Kaç sayi istersiniz?: "))
    karakter_sayisi = uzunluk - harf_sayisi - sayi_sayisi

    sifre = ""

    for i in range(harf_sayisi):
        sifre += random.choice(harfler)

    for i in range(sayi_sayisi):
        sifre += random.choice(sayilar)

    for i in range(karakter_sayisi):
        sifre += random.choice(karakterler)

    sifre_listesi = list(sifre)
    random.shuffle(sifre_listesi)
    sifre = "".join(sifre_listesi)

    print("Oluşturulan Şifre: ", sifre)
