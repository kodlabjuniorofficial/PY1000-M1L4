# int() fonksiyonu

yazi = "25" # Bu bir metindir (str).
print("yazi değişkeni bir metin olduğu için...")
# print(yazi + 5) 
# HATA VERİR! Çünkü metinle sayı toplanamaz, bilgisayar ne yapacağını bilemez.

# Çözüm: Metni Sayıya Çevirme
yazi = "25"
sayi = int(yazi) # Sihirli int() kutusunu kullandık, "25" → 25 oldu.
toplam = sayi + 10
print("Toplam:",toplam) # Çıktı: 35
print("--------------------")


# str() fonksiyonu

yas = 15 # Bu bir sayıdır (int).
# tanitim = "Benim yaşım " + yas
# print(tanitim) 
# HATA VERİR! Çünkü metinle sayı toplanamaz, bilgisayar ne yapacağını bilemez.

# Çözüm: Sayıyı Metne Çevirme (str() kullanımı)
yas = 15
yas = str(yas) # Sihirli str() kutusunu kullandık, 15 → "15" oldu.
tanitim = "Benim yaşım " + yas
print(tanitim)

adim_sayisi = 8000
print("Adım sayısı:", adim_sayisi) 
# Virgül (,) ile print yaptığımızda bilgisayar bizim için otomatik str() kullanır.
print("--------------------")
