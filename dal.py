import mysql.connector
from mysql.connector import Error

class DataAccessLayer:
    def __init__(self):
        # Veritabanı bağlantı bilgileri
        self.config = {
            'host': 'localhost',
            'database': 'KariyerMentorlukDB',
            'user': 'root',       # MySQL kullanıcı adın
            'password': 'cemay123*' # MySQL şifren
        }

    def _get_connection(self):
        return mysql.connector.connect(**self.config)

    # 1. ÖĞRENCİ LİSTELEME PROSEDÜRÜ (Select)
    def ogrenci_listele_dal(self):
        baglanti = self._get_connection()
        cursor = baglanti.cursor(dictionary=True)
        ogrenciler = []
        try:
            # Doğrudan SELECT yazmak yasak! Prosedürü çağırıyoruz.
            cursor.callproc("Sp_OgrenciListele")
            # callproc sonrasında dönen sonuç kümelerini (stored_results) alıyoruz
            for result in cursor.stored_results():
                ogrenciler = result.fetchall()
        except Error as e:
            print(f"DAL Hatası: {e}")
        finally:
            cursor.close()
            baglanti.close()
        return ogrenciler

    # 2. ÖĞRENCİ EKLEME PROSEDÜRÜ (Insert)
    def ogrenci_ekle_dal(self, ad, soyad, email, telefon, universite, bolum, sinif):
        baglanti = self._get_connection()
        cursor = baglanti.cursor()
        basarili_mi = False
        try:
            # Prosedür parametrelerini demet (tuple) olarak gönderiyoruz
            parametreler = (ad, soyad, email, telefon, universite, bolum, sinif)
            cursor.callproc("Sp_OgrenciEkle", parametreler)
            baglanti.commit() # Değişiklikleri kaydet
            basarili_mi = True
        except Error as e:
            print(f"DAL Hatası: {e}")
            baglanti.rollback() # Hata varsa geri al
        finally:
            cursor.close()
            baglanti.close()
        return basarili_mi
    # dal.py dosyasının EN ALTINA ekle:

    # 3. MENTOR LİSTELEME PROSEDÜRÜ
    def mentor_listele_dal(self):
        baglanti = self._get_connection()
        cursor = baglanti.cursor(dictionary=True)
        mentorlar = []
        try:
            cursor.callproc("Sp_MentorListele")
            for result in cursor.stored_results():
                mentorlar = result.fetchall()
        except Error as e:
            print(f"DAL Hatası: {e}")
        finally:
            cursor.close()
            baglanti.close()
        return mentorlar

    # 4. RANDEVU TALEPLERİNİ LİSTELEME PROSEDÜRÜ
    def randevu_listele_dal(self):
        baglanti = self._get_connection()
        cursor = baglanti.cursor(dictionary=True)
        talepler = []
        try:
            cursor.callproc("Sp_RandevuTalebiListele")
            for result in cursor.stored_results():
                talepler = result.fetchall()
        except Error as e:
            print(f"DAL Hatası: {e}")
        finally:
            cursor.close()
            baglanti.close()
        return talepler

    # 5. RANDEVU DURUMU GÜNCELLEME PROSEDÜRÜ (Trigger'ı tetikleyecek olan kısım)
    def randevu_durum_guncelle_dal(self, talep_id, yeni_durum):
        baglanti = self._get_connection()
        cursor = baglanti.cursor()
        basarili_mi = False
        try:
            parametreler = (talep_id, yeni_durum)
            cursor.callproc("Sp_RandevuTalebiGuncelle", parametreler)
            baglanti.commit()
            basarili_mi = True
        except Error as e:
            print(f"DAL Hatası: {e}")
            baglanti.rollback()
        finally:
            cursor.close()
            baglanti.close()
        return basarili_mi

    # 6. OTOMATİK OLUŞAN GÖRÜŞMELERİ LİSTELEME PROSEDÜRÜ
    def gorusme_listele_dal(self):
        baglanti = self._get_connection()
        cursor = baglanti.cursor(dictionary=True)
        gorusmeler = []
        try:
            cursor.callproc("Sp_GorusmeListele")
            for result in cursor.stored_results():
                gorusmeler = result.fetchall()
        except Error as e:
            print(f"DAL Hatası: {e}")
        finally:
            cursor.close()
            baglanti.close()
        return gorusmeler