from bll import BusinessLogicLayer

def ana_menu():
    bll = BusinessLogicLayer()
    
    while True:
        print("\n--- KARİYER MENTORLUK SİSTEMİ ---")
        print("1. Öğrencileri Listele")
        print("2. Yeni Öğrenci Ekle")
        print("3. Çıkış")
        secim = input("Seçiminiz: ")

        if secim == "1":
            ogrenciler = bll.tum_ogrencileri_getir()
            print("\n--- ÖĞRENCİ LİSTESİ ---")
            for ogr in ogrenciler:
                print(f"ID: {ogr['ogrenci_id']} | {ogr['ad']} {ogr['soyad']} - {ogr['universite']} ({ogr['bolum']} - {ogr['sinif']}. Sınıf)")
        
        elif secim == "2":
            print("\n--- YENİ ÖĞRENCİ KAYDI ---")
            ad = input("Ad: ")
            soyad = input("Soyad: ")
            email = input("E-posta: ")
            telefon = input("Telefon: ")
            uni = input("Üniversite: ")
            bolum = input("Bölüm: ")
            sinif = int(input("Sınıf (1-4): "))

            sonuc = bll.yeni_ogrenci_kaydet(ad, soyad, email, telefon, uni, bolum, sinif)
            if sonuc:
                print("✔️ Öğrenci başarıyla kaydedildi!")
            else:
                print("❌ Kayıt işlemi başarısız oldu.")
        
        elif secim == "3":
            print("Sistemden çıkılıyor...")
            break
        else:
            print("Geçersiz seçim!")

if __name__ == "__main__":
    ana_menu()