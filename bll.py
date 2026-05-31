from dal import DataAccessLayer

class BusinessLogicLayer:
    def __init__(self):
        self.dal = DataAccessLayer()

    def tum_ogrencileri_getir(self):
        # İş katmanı burada gerekirse veriyi filtreleyebilir veya sıralayabilir
        return self.dal.ogrenci_listele_dal()

    def yeni_ogrenci_kaydet(self, ad, soyad, email, telefon, universite, bolum, sinif):
        # İş Kuralı Kontrolü: Boş alan var mı?
        if not ad or not soyad or not email or not universite or not bolum:
            print("BLL Uyarısı: Zorunlu alanlar boş bırakılamaz!")
            return False
        
        # İş Kuralı Kontrolü: Sınıf bilgisi mantıklı mı?
        if sinif < 1 or sinif > 4:
            print("BLL Uyarısı: Sınıf bilgisi 1 ile 4 arasında olmalıdır!")
            return False

        # Kurallar geçildiyse veritabanı katmanına gönder
        return self.dal.ogrenci_ekle_dal(ad, soyad, email, telefon, universite, bolum, sinif)
    # bll.py dosyasının EN ALTINA ekle:

    def tum_mentorleri_getir(self):
        return self.dal.mentor_listele_dal()

    def tum_randevulari_getir(self):
        return self.dal.randevu_listele_dal()

    def randevu_durumu_degistir(self, talep_id, yeni_durum):
        if not talep_id or not yeni_durum:
            return False
        return self.dal.randevu_durum_guncelle_dal(talep_id, yeni_durum)

    def tum_gorusmeleri_getir(self):
        return self.dal.gorusme_listele_dal()