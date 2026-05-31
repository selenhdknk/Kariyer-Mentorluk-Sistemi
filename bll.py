from dal import DataAccessLayer

class BusinessLogicLayer:
    def __init__(self):
        self.dal = DataAccessLayer()

    def tum_ogrencileri_getir(self):
        return self.dal.ogrenci_listele_dal()

    def yeni_ogrenci_kaydet(self, ad, soyad, email, telefon, universite, bolum, sinif):
        if not ad or not soyad or not email or not universite or not bolum:
            print("BLL Uyarısı: Zorunlu alanlar boş bırakılamaz!")
            return False
        
        if sinif < 1 or sinif > 4:
            print("BLL Uyarısı: Sınıf bilgisi 1 ile 4 arasında olmalıdır!")
            return False

        return self.dal.ogrenci_ekle_dal(ad, soyad, email, telefon, universite, bolum, sinif)

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
    def yeni_randevu_talebi_olustur(self, aciklama, ogrenci_id, mentor_id):
        # İş Kuralı: Açıklama boş mu veya ID'ler girilmiş mi kontrolü
        if not aciklama or not ogrenci_id or not mentor_id:
            print("BLL Uyarısı: Randevu açıklaması ve geçerli ID'ler zorunludur!")
            return False
        return self.dal.randevu_talebi_ekle_dal(aciklama, ogrenci_id, mentor_id)