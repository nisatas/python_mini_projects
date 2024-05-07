# Yapılacaklar Listesi Uygulaması

yapilacaklar_listesi = []

while True:
    # Menüyü yazdır
    print("1- Yapilacaklar Listesini Göster")
    print("2- Yapilacaklar Listesine Ekle")
    print("3- Yapilacaklar Listesinden Sil")
    print("4- Çikiş")
  
    # Kullanıcıdan seçim yapmasını iste
    secim = input("Seçiminiz: ")
    
    # Yapılacaklar listesini göster
    if secim == "1":
        print("Yapilacaklar Listesi:")
        for i in yapilacaklar_listesi:
           print("-", i)
    
    # Yapılacaklar listesine ekle
    elif secim == "2":
        yapilacak = input("Yapilacak işi girin: ")
        yapilacaklar_listesi.append(yapilacak)
        print(yapilacak, "listeye eklendi.")
    
    # Yapılacaklar listesinden sil
    elif secim == "3":
        silinecek = input("Silinecek işi girin: ")
        if silinecek in yapilacaklar_listesi:
            yapilacaklar_listesi.remove(silinecek)
            print(silinecek, "listedeki işler arasından silindi.")
        else:
            print(silinecek, "listede bulunamadı.")
    
    # Programdan çıkış yap
    elif secim == "4":
        print("Program sonlandiriliyor...")
        break
    
    # Geçersiz seçim durumunda kullanıcıyı uyar
    else:
        print("Geçersiz seçim. Tekrar deneyin.")









