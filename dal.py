import mysql.connector
from mysql.connector import Error

class DataAccessLayer:
    def __init__(self):
        self.config = {
            'host': 'localhost',
            'database': 'KariyerMentorlukDB',
            'user': 'root',       
            'password': 'cemay123*'
        }

    def _get_connection(self):
        return mysql.connector.connect(**self.config)

    def ogrenci_listele_dal(self):
        baglanti = self._get_connection()
        cursor = baglanti.cursor(dictionary=True)
        ogrenciler = []
        try:
            cursor.callproc("Sp_OgrenciListele")
            for result in cursor.stored_results():
                ogrenciler = result.fetchall()
        except Error as e:
            print(f"DAL Hatası: {e}")
        finally:
            cursor.close()
            baglanti.close()
        return ogrenciler

    def ogrenci_ekle_dal(self, ad, soyad, email, telefon, universite, bolum, sinif):
        baglanti = self._get_connection()
        cursor = baglanti.cursor()
        basarili_mi = False
        try:
            parametreler = (ad, soyad, email, telefon, universite, bolum, sinif)
            cursor.callproc("Sp_OgrenciEkle", parametreler)
            baglanti.commit() 
            basarili_mi = True
        except Error as e:
            print(f"DAL Hatası: {e}")
            baglanti.rollback() 
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
    
    def randevu_talebi_ekle_dal(self, aciklama, ogrenci_id, mentor_id):
        baglanti = self._get_connection()
        cursor = baglanti.cursor()
        basarili_mi = False
        try:
            parametreler = (aciklama, ogrenci_id, mentor_id)
            cursor.callproc("Sp_RandevuTalebiEkle", parametreler)
            baglanti.commit()
            basarili_mi = True
        except Error as e:
            print(f"DAL Hatası: {e}")
            baglanti.rollback()
        finally:
            cursor.close()
            baglanti.close()
        return basarili_mi