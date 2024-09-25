# Множественное наследование

class Horse:                                    # класс описывающий лошадь
    def __init__(self, x_distance=0, sound='Frrr'):
        self.x_distance = x_distance
        self.sound = sound

    def run(self, dx):                          # изменение дистанции, увеличивает x_distance на dx.
        self.x_distance += dx


class Eagle:
    def __init__(self, y_distance=0, sound='I train, eat, sleep, and repeat'):
        self.y_distance = y_distance
        self.sound = sound

    def fly(self, dy):                          # изменение дистанции, увеличивает y_distance на dy
        self.y_distance += dy


class Pegasus(Horse, Eagle):                   # класс описывающий пегаса

    def __init__(self):
        Horse.__init__(self)
        Eagle.__init__(self)

    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        coordinate = (self.x_distance, self.y_distance)
        return coordinate

    def voice(self):
        print(self.sound)


# Пример работы программы:
p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()

print(Pegasus.mro()) # Для отслеживания наследования