import turtle

t = turtle.Turtle()
t.shape("turtle")

t.speed(5)    # hız (sadece speed kullanıldı)
t.width(5)    # kenar kalınlığı 5

# kareyi (0,0) noktasından başlayarak saat yönünde çiziyoruz
t.goto(150, 0)
t.goto(150, 150)
t.goto(0, 150)
t.goto(0, 0)