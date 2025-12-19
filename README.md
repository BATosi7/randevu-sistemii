<<<<<<< HEAD
<<<<<<< HEAD
# 🗓️ Randevu Sistemi

Modern, kullanıcı dostu ve tam fonksiyonel bir randevu yönetim sistemi. Müşteriler çeşitli kategorilerdeki işletmelerden randevu alabilir, işletme sahipleri randevularını yönetebilir.

![Django](https://img.shields.io/badge/Django-6.0-green)
![Python](https://img.shields.io/badge/Python-3.13-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## ✨ Özellikler

### 👤 Müşteri Özellikleri
- ✅ Kategori bazlı işletme arama
- ✅ İşletme detayları ve hizmet listesi
- ✅ Randevu oluşturma (tarih, saat, hizmet seçimi)
- ✅ Randevu iptal etme
- ✅ Randevu durumu takibi
- ✅ Tamamlanan randevuları değerlendirme (1-5 yıldız + yorum)

### 🏢 İşletme Sahibi Özellikleri
- ✅ Dashboard ile istatistikler
- ✅ Randevu yönetimi (Onayla, Reddet, Tamamla)
- ✅ Haftalık trend grafiği (Chart.js)
- ✅ Hizmet popülaritesi grafiği
- ✅ Gelir takibi

### 🔒 Güvenlik & Validasyon
- ✅ Geçmiş tarih kontrolü
- ✅ Randevu çakışma kontrolü
- ✅ İşletme sahibi kendi işletmesine randevu alamaz
- ✅ CSRF koruması
- ✅ Form validasyonları

### 📱 Responsive Tasarım
- ✅ Mobil uyumlu (Bootstrap 5)
- ✅ Tablet ve desktop desteği
- ✅ Kart görünümü (mobil)
- ✅ Tablo görünümü (desktop)

---

## 🛠️ Teknolojiler

### Backend
- **Python 3.13**
- **Django 6.0**
- **SQLite** (Veritabanı)

### Frontend
- **HTML5** & **CSS3**
- **Bootstrap 5.3.2**
- **JavaScript** (Chart.js)
- **FontAwesome 6**

---

## 📦 Kurulum

### 1. Projeyi İndir
```bash
git clone https://github.com/USERNAME/randevu-sistemi.git
cd randevu-sistemi
```

### 2. Virtual Environment Oluştur
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac
```

### 3. Bağımlılıkları Yükle
```bash
pip install -r requirements.txt
```

### 4. Veritabanını Oluştur
```bash
python manage.py migrate
```

### 5. Demo Verileri Yükle (Opsiyonel)
```bash
python manage.py populate_data
```

### 6. Sunucuyu Başlat
```bash
python manage.py runserver
```

### 7. Tarayıcıda Aç
```
http://127.0.0.1:8000/
```

---

## 👥 Demo Hesaplar

### Müşteri Hesapları
| Kullanıcı Adı | Şifre |
|---------------|-------|
| `musteri_ali` | `pass` |
| `musteri_ayse` | `pass` |

### İşletme Sahibi Hesapları
| Kullanıcı Adı | İşletme | Şifre |
|---------------|---------|-------|
| `starbucks` | Starbucks | `pass` |
| `ali_makas` | Ali Makas | `pass` |
| `inci_dis` | İnci Diş Polikliniği | `pass` |

---

## 📊 Kategoriler

- 🦷 **Dişçi** (5 işletme)
- ☕ **Cafe** (5 işletme)
- 👶 **Bebek Bakımı** (5 işletme)
- ✂️ **Kuaför** (5 işletme)
- 🔧 **Tamirat** (5 işletme)

**Toplam:** 15 işletme, 75+ hizmet

---

## 🚀 Kullanım

### Müşteri Akışı
1. Kategori seç
2. İşletme seç
3. Hizmet seç
4. Tarih ve saat belirle
5. Randevu oluştur
6. Randevu tamamlandıktan sonra değerlendir

### İşletme Sahibi Akışı
1. Dashboard'a git
2. Bekleyen randevuları gör
3. Randevuları onayla/reddet
4. Tamamlanan randevuları işaretle
5. İstatistikleri incele

---

## 📸 Ekran Görüntüleri

### Anasayfa
![Anasayfa](screenshots/home.png)

### Dashboard
![Dashboard](screenshots/dashboard.png)

### Randevu Oluşturma
![Randevu](screenshots/appointment.png)

---

## 🌐 Deployment

### Ngrok ile (Ücretsiz)
```bash
# Django başlat
python manage.py runserver

# Ngrok başlat (başka terminal)
ngrok http 8000
```

### Production (PythonAnywhere, Heroku, vb.)
Detaylı talimatlar için `deployment_guide.md` dosyasına bakın.

---

## 📝 Lisans

MIT License - Detaylar için `LICENSE` dosyasına bakın.

---

## 🤝 Katkıda Bulunma

1. Fork yapın
2. Feature branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Commit yapın (`git commit -m 'Add amazing feature'`)
4. Push yapın (`git push origin feature/amazing-feature`)
5. Pull Request açın

---

## 📧 İletişim

Proje Sahibi - [@username](https://github.com/username)

Proje Linki: [https://github.com/username/randevu-sistemi](https://github.com/username/randevu-sistemi)

---

## 🙏 Teşekkürler

- [Django](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)
- [Chart.js](https://www.chartjs.org/)
- [FontAwesome](https://fontawesome.com/)

---

**⭐ Projeyi beğendiyseniz yıldız vermeyi unutmayın!**
=======
# randevu-sistemi
>>>>>>> 3f137e92ae3f7c6f73407a05265f72d0391002cd
=======
# randevu-sistemii
>>>>>>> 77072e658cc214bdc2ffdbed65aec9b35ccf8e79
