# 🗓️ Randevu Sistemi

Modern, kullanıcı dostu ve tam fonksiyonel bir randevu yönetim sistemi. Müşteriler çeşitli kategorilerdeki işletmelerden randevu alabilir, işletme sahipleri ve personel randevularını yönetebilir.

![Django](https://img.shields.io/badge/Django-5.1-green)
![Python](https://img.shields.io/badge/Python-3.13-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## ✨ Özellikler

### 👤 Müşteri Özellikleri
- ✅ Kategori bazlı işletme arama
- ✅ İşletme detayları ve hizmet listesi
- ✅ Personel seçimi ile randevu oluşturma
- ✅ Randevu iptal etme
- ✅ Randevu durumu takibi
- ✅ Tamamlanan randevuları değerlendirme (1-5 yıldız + yorum)

### 🏢 İşletme Sahibi Özellikleri
- ✅ Dashboard ile istatistikler
- ✅ Randevu yönetimi (Onayla, Reddet, Tamamla)
- ✅ Haftalık trend grafiği (Chart.js)
- ✅ Hizmet popülaritesi grafiği
- ✅ Gelir takibi
- ✅ Personel yönetimi

### 👨‍💼 Personel Özellikleri ⭐ YENİ
- ✅ Personel dashboard
- ✅ Müsait saat ekleme ve yönetimi
- ✅ Atanan randevuları görüntüleme
- ✅ Randevu istatistikleri

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
- **Django 5.1**
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
git clone https://github.com/BATosi7/randevu-sistemii.git
cd randevu-sistemii
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

### 5. Sunucuyu Başlat
```bash
python manage.py runserver
```

### 6. Tarayıcıda Aç
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

### Personel Hesapları ⭐
| Kullanıcı Adı | İşletme | Uzmanlık | Şifre |
|---------------|---------|----------|-------|
| `ahmet_berber` | Ali Makas | Saç Kesimi | `pass` |
| `ayse_kuafor` | Ali Makas | Saç Boyama | `pass` |
| `mehmet_disci` | İnci Diş | Diş Temizliği | `pass` |

---

## 📊 Kategoriler

- 🦷 **Dişçi**
- ☕ **Cafe**
- 👶 **Bebek Bakımı**
- ✂️ **Kuaför**
- 🔧 **Tamirat**

---

## 🚀 Kullanım

### Müşteri Akışı
1. Kategori seç
2. İşletme seç
3. Hizmet ve personel seç
4. Tarih ve saat belirle
5. Randevu oluştur
6. Randevu tamamlandıktan sonra değerlendir

### İşletme Sahibi Akışı
1. Dashboard'a git
2. Bekleyen randevuları gör
3. Randevuları onayla/reddet
4. Tamamlanan randevuları işaretle
5. İstatistikleri incele

### Personel Akışı ⭐
1. Personel dashboard'a git
2. Müsait saatlerini ekle
3. Atanan randevuları gör
4. Randevu durumlarını takip et

---

## 🌐 Deployment

### Canlı Demo
**URL:** https://batosi.pythonanywhere.com

### Ngrok ile (Geliştirme)
```bash
# Django başlat
python manage.py runserver

# Ngrok başlat (başka terminal)
ngrok http 8000
```

---

## 📝 Veritabanı Yapısı

### Tablolar
1. **Users** - Kullanıcılar (müşteri, işletme, personel)
2. **Categories** - Kategoriler
3. **Companies** - İşletmeler
4. **Services** - Hizmetler
5. **Staff** - Personel
6. **StaffAvailability** - Personel müsait saatler ⭐
7. **Appointments** - Randevular
8. **Rating** - Değerlendirmeler

Detaylı veritabanı yapısı için `docs/veritabani_sql.md` dosyasına bakın.

---

## 🤝 Katkıda Bulunma

1. Fork yapın
2. Feature branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Commit yapın (`git commit -m 'Add amazing feature'`)
4. Push yapın (`git push origin feature/amazing-feature`)
5. Pull Request açın

---

## 📧 İletişim

Proje Linki: [https://github.com/BATosi7/randevu-sistemii](https://github.com/BATosi7/randevu-sistemii)

---

## 🙏 Teşekkürler

- [Django](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)
- [Chart.js](https://www.chartjs.org/)
- [FontAwesome](https://fontawesome.com/)
- [PythonAnywhere](https://www.pythonanywhere.com/)

---

**⭐ Projeyi beğendiyseniz yıldız vermeyi unutmayın!**
