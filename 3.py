import turtle

t = turtle.Turtle()
t.shape("turtle")
t.speed(3) # Çizimi görmek için hız

# NOT: Başlangıçta t.up() kullanmayı unutma ki çizgiler karışmasın!

#----------------------------------------------------
# 1. ÇİÇEK TASARIMI (SOLDAKİ ÇİÇEK)
#----------------------------------------------------

# Kaplumbağayı ekranın sol alt tarafına taşı
t.up()
t.goto(-150, -150)
t.down()

# GÖREV 1: Sapı Çiz
# Rengi yeşil yap.
# Kaplumbağayı yukarı baktır (90 derece).
# 50 birim ileri git (Sapı çiz).
# Kodunu buraya yaz:

# GÖREV 2: Çiçek Merkezini Çiz
# Rengi sarı yap.
# dot() komutunu kullanarak 20 birimlik bir nokta çiz.
# Kodunu buraya yaz:


# GÖREV 3: Taç Yapraklarını Çiz (3 nokta)
# Rengi magenta (pembe) yap.
# dot() komutunu kullan.
# Her nokta için t.up() ve t.goto() ile merkezin etrafındaki yeni bir noktaya gitmelisin.

# Üst yaprak kodu:
t.up()
t.goto(-150, -100) 
t.down()
t.dot(15) 

# Sol yaprak kodu:
# Kodunu buraya yaz:

# Sağ yaprak kodu:
# Kodunu buraya yaz:

