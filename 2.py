import turtle

t = turtle.Turtle()
t.shape("turtle")

t.width(5)      # çizgi kalınlığı
t.speed(3)      # hız
t.goto(100, 100)  # (100, 100) noktasına git
t.circle(40)      # 40 yarıçapında bir çember çizer
t.dot(30, "red") # belirtilen yarı çapda ve belirtilen renkte nokta oluşturur
