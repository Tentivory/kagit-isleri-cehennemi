#!/usr/bin/env python3
# Kağıt İşleri Cehennemi v1.0 - Resmi Sürüm
# Çalıştırmak için: python cehennem.py
# Uyarı: Bir kez başladınız mı, çıkış yoktur (Ctrl+C teknik olarak mümkün ama sistem şüpheyle bakar).
# Gizli not: YnVyb2tyYXNpIGNlaGVubmVtaQ== (kimse decode etmez zaten)

import time
import random

adimlar = [
    "Evrakın fotokopisini çekin, sonra aslını kaybedin.",
    "Üst kata çıkın, orada 'aşağı kata inin' densin.",
    "Damga için sıraya girin, damgacı molada.",
    "Formu doldurun, formu reddedilsin, yeni form isteyin.",
    "İmza için müdürü bekleyin, müdür toplantıda.",
    "Dosyayı başka birime yönlendirin, o birim de size yönlendirsin.",
    "Kağıtları zımbalayın, zımba bittiğini fark edin.",
    "Randevu alın, randevu saatinde 'sistem çöktü' densin.",
    "Kimlik fotokopisi isteyin, sonra 'eski kimlik geçersiz' densin.",
    "Tüm evrakları tarayın, tarayıcı kağıt sıkıştırsın.",
    "İtiraz dilekçesi yazın, dilekçe 'eksik evrak' diye reddedilsin.",
    "Yeni bir sıra numarası alın, sıra numaraları bitti densin."
]

print("=== KAĞIT İŞLERİ CEHENNEMİNE HOŞGELDİNİZ ===")
print("Süreç resmen başlatıldı. Lütfen sabırlı olun (olmayacaksınız).")
print("Çıkmak için Ctrl+C basabilirsiniz (ama onay bekleyebilir).\n")

adim = 1
while True:
    secilen = random.choice(adimlar)
    print(f"Adım {adim}: {secilen}")
    print(f"   (Tahmini süre: {random.randint(5, 45)} dakika, gerçek süre: sonsuz)")
    time.sleep(random.uniform(0.8, 2.5))
    adim += 1
    if adim % 8 == 0:
        print("   >>> ÖNEMLİ BİLDİRİM: Tüm süreç baştan başladı. Tebrikler, ilerleme kaydettiniz. <<<\n")
