#это первое задание
from time import sleep
class TrafficLight:
    __attr ="color"
    def ranning(self, red, yellow, green):
        self.red = red
        self.yellow = yellow
        self.green = green
        i = 0
        while True:
            if red == 'red' and green == 'green' and yellow == 'yellow':
                print(f'{self.__attr} {self.red}')
                sleep(7)
                print(f'{self.__attr} {self.yellow}')
                sleep(2)
                print(f'{self.__attr} {self.green}')
                sleep(3)
                i = i+1
                if i == 1:
                    return ' '# иначе выводит None
            else:
                print('введите цвет в правильном порядке: red , yellow ,  green')
                break

trafficlight = TrafficLight()

print(trafficlight.ranning( 'red' , 'yellow', 'green'))

#второе задание
class Road:
    def __init__(self, length, width):
        self.mass = 25
        self.sm = 5
        self._len = length
        self._wid = width
    def info(self):
        res = self.mass * self.sm * self._len * self._wid / 1000
        print(f'расчет массы асфальта = длина * ширина * масса для покрытия 1 кв м толщиной 1 см* число см толщины полотна = {res} тонн')
road = Road(20, 5000)
road.info()


#третье задание
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.pos = position
        self._income = {"wage":int(wage), "bonus":int(bonus)}

class Position(Worker):

    def get_full_name(self):
        print(f' фамилия {self.surname},  имя {self.name} , должность {self.pos}')
    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']

w1 = Position('ALEX', 'IVANOV', 'doc', '2000', '3000')

w1.get_full_name()
print(f'доход с учетом премии = {w1.get_total_income()}')
w2 = Position('Max', 'Petrov', "lab", 3000, 4000)
w2.get_full_name()
print(w2.get_total_income())

# четвертое задание
class Car:
    def __init__(self, speed, color, name, is_police = True):
        self.speed = speed
        self.color = color
        self.name = name
        self.police = is_police


    def go(self):
        print(f'машина {self.name} поехала')

    def stop(self):
        print(f'машина {self.name} стоп')
    def turn(self, direction):
        print(f'машина {self.name} повернула {direction}')
    def show_speed(self):
        print(f'ваша скорость {self.speed}')

class TownCar(Car):
    def __init__(self,speed, color, name, is_police = True):
        super().__init__(speed, color, name, is_police)
        print(f' car is {self.speed} {self.color} {self.name} {is_police}')
    def show_speed(self):
        if self.speed > str(60):
            print('ваша скорость высокая')
        else:
            print(f' скорость {self.speed} допустима')
class Workcar(Car):
    def __init__(self,speed, color, name, is_police = True):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        if self.speed < str(40):
            print('ваша скорость низкая')
        else:
            print(f' скорость {self.speed} допустима')
class PoliceCar(Car):
    def __init__(self,speed, color, name, year, is_police = True):
        super().__init__(speed, color, name, is_police)
        self.year = year
        print(f' car is {self.speed},  {self.color}, {self.name},  {self.year}, {is_police}')
car = TownCar('70', 'red', 'Ауди', False)
car.turn('налево')
car.show_speed()
car1 = PoliceCar(60,'green', 'DAd', '1990', True,)
car1.go()



#пятое задание
class Stationery:
    def __init__(self, title):
        self.name = title

    def draw(self):
        print('запуск отрисовки')
class Pen(Stationery):
    def draw(self):
        print(f'запуск отрисовки: {self.name} ')
class Pencil(Stationery):
    def draw(self):
        print(f'запуск отрисовки: {self.name}')
class Handle(Stationery):
    def draw(self):
        print(f'рисует: {self.name}')
s = Stationery('name')
s.draw()
f = Pen("ручка")
f.draw()
s = Pencil('карандаш')
s.draw()
s = Handle('маркер')
s.draw()