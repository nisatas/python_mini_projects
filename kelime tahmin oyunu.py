import random

kelime_listesi = ['slay', 'bitch', 'musa', 'sulo', 'kangal', 'ebenin', 'ami']

kelime = random.choice(kelime_listesi)

print("Kelimenin harf sayısı: ", len(kelime))

tahminler = ''
""
can = 5

while can > 0:

    hatalar = 0

    for harf in kelime:
        if harf in tahminler:
            print(harf)
        else:
            print("_")
            hatalar += 1

    if hatalar == 0:
        print("Tebrikler! Kazandın!")
        print("Kelime: ", kelime)
        break

    tahmin = input("Bir harf tahmin et: ")

    tahminler += tahmin

    if tahmin not in kelime:
        can -= 1
        print("Yanlış!")
        print("Kalan can: ", can)

        if can == 0:
            print("Kaybettin! Doğru kelime: ", kelime)




