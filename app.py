import streamlit as st
from bll import BusinessLogicLayer

bll = BusinessLogicLayer()

st.set_page_config(page_title="Kariyer Mentorluk Sistemi", layout="wide")
st.title("🎓 Kariyer Mentorluk ve CV Takip Sistemi")
st.subheader("Yönetim Paneli")
st.markdown("---")

# Yan Menü Navigasyonu (Tüm sekmeler aktif edildi)
menu = st.sidebar.selectbox(
    "Menü Seçimi",
    ["Öğrenci Listesi", "Yeni Öğrenci Ekle", "Mentor Listesi", "Randevu Talepleri", "Planlanan Görüşmeler"]
)

# 1. ÖĞRENCİ LİSTELEME
# app.py içindeki "Öğrenci Listesi" bölümünü bul ve bu şekilde güncelle:
if menu == "Öğrenci Listesi":
    st.header("📋 Kayıtlı Öğrenciler")
    
    ogrenciler = bll.tum_ogrencileri_getir()
    
    if ogrenciler:
        # 1. Veriyi Pandas DataFrame yapısına dönüştürüyoruz
        import pandas as pd
        df = pd.DataFrame(ogrenciler)
        
        # 2. Teknik kolon isimlerini arayüzde görünecek şık isimlerle eşliyoruz
        df = df.rename(columns={
            'ogrenci_id': 'Öğrenci ID',
            'ad': 'Ad',
            'soyad': 'Soyad',
            'email': 'E-Posta Adresi',
            'telefon': 'Telefon Numarası',
            'universite': 'Üniversite',
            'bolum': 'Bölüm',
            'sinif': 'Sınıf',
            'kayit_tarihi': 'Sisteme Kayıt Tarihi'
        })
        
        # 3. Yeniden adlandırılmış şık tabloyu ekrana basıyoruz
        st.dataframe(df, use_container_width=True, hide_index=True)
    else:
        st.info("Sistemde henüz kayıtlı öğrenci bulunmamaktadır.")

# 2. YENİ ÖĞRENCİ EKLEME
elif menu == "Yeni Öğrenci Ekle":
    st.header("👤 Yeni Öğrenci Kayıt Formu")
    with st.form("ogrenci_formu", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            ad = st.text_input("Ad")
            email = st.text_input("E-posta")
            universite = st.text_input("Üniversite", value="Bartın Üniversitesi")
            sinif = st.number_input("Sınıf", min_value=1, max_value=4, step=1)
        with col2:
            soyad = st.text_input("Soyad")
            telefon = st.text_input("Telefon Numarası")
            bolum = st.text_input("Bölüm")
            
        submit_button = st.form_submit_button(label="Öğrenciyi Kaydet")
        if submit_button:
            sonuc = bll.yeni_ogrenci_kaydet(ad, soyad, email, telefon, universite, bolum, sinif)
            if sonuc:
                st.success(f"✔️ {ad} {soyad} başarıyla sisteme eklendi!")
            else:
                st.error("❌ Kayıt işlemi başarısız.")

# 3. MENTOR LİSTELEME
elif menu == "Mentor Listesi":
    st.header("👨‍🏫 Mentor Kadromuz")
    mentorlar = bll.tum_mentorleri_getir()
    if mentorlar:
        st.dataframe(mentorlar, use_container_width=True)
    else:
        st.info("Sistemde henüz kayıtlı mentor bulunmamaktadır.")

# 4. RANDEVU TALEPLERİ VE ONAYLAMA SÜRECİ
elif menu == "Randevu Talepleri":
    st.header("📨 Öğrencilerden Gelen Görüşme Talepleri")
    
    
    talepler = bll.tum_randevulari_getir()
    if talepler:
        st.dataframe(talepler, use_container_width=True)
        
        st.markdown("### ⚙️ Talep Yönetim Aksiyonu")
        col1, col2 = st.columns(2)
        with col1:
            talep_id = st.number_input("İşlem Yapılacak Talep ID:", min_value=1, step=1)
        with col2:
            islem = st.selectbox("Kararınız:", ["Onaylandi", "Reddedildi"])
            
        if st.button("Kararı Uygula"):
            sonuc = bll.randevu_durumu_degistir(talep_id, islem)
            if sonuc:
                st.success(f"✔️ {talep_id} numaralı talep durumu '{islem}' olarak güncellendi!")
                st.rerun()
            else:
                st.error("İşlem sırasında bir hata oluştu.")
    else:
        st.info("Bekleyen randevu talebi bulunmuyor.")

# 5. PLANLANAN GÖRÜŞMELER (TRIGGER TAKİP ALANI)
elif menu == "Planlanan Görüşmeler":
    st.header("📅 Takvim ve Kesinleşen Online Görüşmeler")
   
    
    gorusmeler = bll.tum_gorusmeleri_getir()
    if gorusmeler:
        st.dataframe(gorusmeler, use_container_width=True)
    else:
        st.info("Henüz kesinleşmiş bir görüşme takvimi yok.")