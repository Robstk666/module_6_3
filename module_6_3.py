class Horse:
    def __init__(self):
        self.x_distance = 0
        self.sound = 'Frrr'

    def run(self, dx):
        """Увеличивает пройденный путь по оси x."""
        self.x_distance += dx


class Eagle:
    def __init__(self):
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        """Увеличивает высоту полета по оси y."""
        self.y_distance += dy


class Pegasus(Horse, Eagle):
    def __init__(self):
        # Инициализация атрибутов классов родителей
        Horse.__init__(self)
        Eagle.__init__(self)

    def move(self, dx, dy):
        """Двигает пегаса на заданное расстояние."""
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        """Возвращает текущую позицию (x_distance, y_distance)."""
        return (self.x_distance, self.y_distance)

    def voice(self):
        """Выводит звук, который издаёт пегас."""
        print(self.sound)


# Пример работы программы
p1 = Pegasus()

# Проверяем начальное положение
print(p1.get_pos())  # Ожидается: (0, 0)

# Перемещение
p1.move(10, 15)
print(p1.get_pos())  # Ожидается: (10, 15)

# Ещё одно перемещение
p1.move(-5, 20)
print(p1.get_pos())  # Ожидается: (5, 35)

# Звук пегаса
p1.voice()  # Ожидается: "I train, eat, sleep, and repeat"