#первое задание я не могу проверить заданную переменную класса через функцию проверки,
# только запуском функции класса с повторным введением данных.
#это из-за того, что задан статикметод?
class Data:
    def __init__(self, string):
        self.date = string

    @classmethod
    def myf(cls, obj):
        r = obj.date.split('-')
        return int(r[0]), int(r[1]), int(r[2])
    @staticmethod
    def valid(str):
        try:
            day = int(str.split('-')[0])
            month = int(str.split('-')[1])
            year = int(str.split('-')[2])
            if day<= 31 and month <=12 and year <= 2022:
                return 'есть такая дата'
            if day > 31 or month > 12 or year > 2023:
                print('такой даты нет')
        except ValueError:
            return 'неправильный ввод данных'

a = Data('27-09-2022')
b = Data.myf(a)
print(b)
print(Data.valid('27-ii-2022'))

# второе задание
class Ex(Exception):
    def __init__(self, txt):
        self.txt = txt

d = input('введите число :')
b = input ('введите второе число : ')

try:
    d = int(d)
    b = int(b)
    c = d / b
    if b < 0 and d > 0:
        raise Ex(f'получится отрицательная дробь {c}')
    if d < 0 and b > 0:
        raise Ex(f'получится отрицательная дробь {c}')


except (ZeroDivisionError, ValueError, Ex) as error:
    print(error)
else:
    print(c)
finally:
    print('end')





# третье задание

class NotNumber(Exception):
    def __init__(self, txt):
        self.txt = txt

my_list = []
while True:
    try:
        value = input(' введите число в список:  ')
        if value.lstrip('-').isdigit():
            my_list.append(int(value))
        if value == 'stop':
            break
        if not value.lstrip('-').isdigit():
            raise NotNumber(f'это не число {value}')

    except NotNumber as err:
        print (err)
print(my_list)
# 4 задание
# вобщем , чем больше думаю, тем больше запутываюсь в решении.
# не доделано.
class Store:
    def __get__(self, instance, owner):
        self.made = []



class Orgtechnic:
    def __init__(self, year, name, price):
        self.year = year
        self.name = name
        self.price = price
        self.items = {'год выпуска': self.year, 'модель ': self.name, 'цена': self.price }
    def income(self):
        try:
            name = input(f'введите наименование ')
            price = int(input(f'введите цену за ед '))
            year = int(input('введите год выпуска  '))
            item = {'год': year, 'модель устройства': name, 'цена за ед ': price}
            self.items.update(item)
            print(self.items)
        except ValueError:
            print('неверный ввод')

class Printer(Orgtechnic):
    def __init__(self, year, name, price, any):
        super().__init__(year, name, price)


class Xerox(Orgtechnic):
    pass

p = Printer(1999, 'hp', 700, 'grey')

p.income()
x = Xerox(2000,'rt', 89)
x.income()
