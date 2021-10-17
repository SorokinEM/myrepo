# class Character:
#     name = ''
#     power = 0
#     energy = 100
#     hands = 2
# # Character.__dict__
# peter = Character()
# # # print(peter.name)
# # # print(peter.power)
# # # print(peter.energy)
# # # print(peter.hands)

# # # print(peter.__dict__)

# peter.name = 'Peter Parker'
# peter.power = 70
# peter.alias = 'Spider Man'
# print(peter.name)
# print(peter.power)
# print(peter.energy)
# print(peter.hands)
# print(peter.alias)

# # print(peter.__dict__)
# # class Income:
# #   def __init__(self, id_):
# #     self.id_ = id_
# #     id_ = 100
# # income_1 = Income(1000)
# # print(income_1.id_)
# #Создаём ещё один экземпляр класса
# print('')
# bruce = Character()
# bruce.name = 'Bruce Wayne'
# bruce.power = 85
# bruce.alias = 'Batman'
# print(bruce.name)
# print(bruce.power)
# print(bruce.energy)
# print(bruce.hands)
# print(bruce.alias)
# Мы видим, что аргумент self ссылается на конкретный экземпляр класса(который ещё не создан)
# Его обязательно нужно прописывать, чтобы показать то, что все действия будут происходить именно с тем объектом, к которому мы применяем метод
# class Character:
#     name = ''
#     power = 0
#     energy = 100
#     hands = 2
#     def eat(self, food):
#       if self.energy < 100:
#         self.energy += food
#       else:
#         print('Not hungry')

#     def do_exercise(self, hours):
#       if self.energy > 0:
#         self.energy -= hours * 2
#         self.power += hours * 2
#       else:
#         print('Too tired')

#     def change_alias(self, new_alias):
#       print(self) # просто посмотрим для чего нужен self?
#       self.alias = new_alias
# #Ещё раз проинициализируем создание экземпляра
# bruce = Character()
# bruce.name = 'Bruce Wayne'
# bruce.power = 85

# #Пока нет псевдонима
# # print(bruce.alias)

# #Добавляем псевдоним
# bruce.change_alias('Batman')
# print(bruce.alias)

# #Изменим псевдоним
# bruce.change_alias('Dark Knight')
# print(bruce.alias)

# #Пусть тренируется
# bruce.do_exercise(1)
# print(bruce.power)
# print(bruce.energy)
# bruce.do_exercise(2)
# print(bruce.power)
# print(bruce.energy)
# bruce.do_exercise(2)
# print(bruce.power)
# print(bruce.energy)

# Проблема с инициализацией параметров изменяемыми типами
# class Character:
#     name = ''
#     power = 0
#     energy = 100
#     hands = 2
#     backpack = [] #добавляем атрибут с изменяемым типом - списком
#     def eat(self, food):
#       if self.ebergy < 100:
#         self.energy += food
#       else:
#         print('Not hungry')

#     def do_exercise(self, hours):
#       if self.energy > 0:
#         self.energy -= hours * 2
#         self.power += hours * 2
#       else:
#         print('Too tired')
#
# #     def change_alias(self, new_alias):
# #       self.alias = new_alias
#
# # peter = Character()
# # bruce = Character()
#
# # peter.backpack.append('web-shuters') #дадим Питеру веб-шутеры
# # #Проверяем рюкзак Питера
# # print(peter.backpack)
#
# # #проверяем рюкзак Бэтмена
# # print(bruce.backpack)
#
# # значение инициализируется при создании класса, а изменяемые типы ссылаются на один и тот же объект в памяти (поэтому рюкзак был заполнен у обоих персонажей)
# # Магический метод init позволяет задать атрибуты при инициализации экземпляра класса, а также решить проблему выше (с рюкзаками)
# class Character:
#     def __init__(self, name, power, energy=100, hands=2):
#         # параметром по-умоллчанию backpack делать не будем, чтобы он не был общим
#         self.name = name
#         self.power = power
#         self.energy = energy
#         self.backpack = []  # будем присваивать список именно для конкретного экземпляра при создании (self)
#         self.hands = hands
#
#         def eat(self, food):
#             if self.ebergy < 100:
#                 self.energy += food
#             else:
#                 print('Not hungry')
#
#         def do_exercise(self, hours):
#             if self.energy > 0:
#                 self.energy -= hours * 2
#                 self.power += hours * 2
#             else:
#                 print('Too tired')
#
#         def change_alias(self, new_alias):
#             self.alias = new_alias
# # теперь при создании экземпляра класса нам надо обязательно передать аргументы.
# # peter = Character()
# peter = Character('Peter Parker', 80)
# bruce = Character('Bruce Wayne', 85)
# print(peter.name)
# print(peter.power)
#
# # если они не заданы по умолчанию
# print(peter.hands)
#
# # при таком раскладе (init) все атрибуты сразу же попадают в словарь экземпляра (а не только изменённые)
# # print(peter.__dict__)
# peter.backpack.append('web-shuters')  # дадим Питеру веб-шутеры
# bruce.backpack.append('Poison bomb')  # дадим Брюсу ядовитую бомбу
# #Проверяем рюкзак Питера
# print(f'Содержимое рюкзака Питера: {peter.backpack}')
# # проверяем рюкзак Бэтмена
# print(f'Содержимое рюкзака Брюса: {bruce.backpack}')

# Итог: в init будем прописывать то, что хотим задавть при инициализации экземпляров классов.
# Все атрибуты сизменяемыми атрибутами по-умолчанию, которые по плану будут общие для всех экземпляров
# можно прописывать без него.

# # Взаимодействие классов, рассмотрим на примере сложения.
# num1 = 5
# num2 = 10
#
# # Числа являются экземплярами класса int
# print(type(num1))
#
# # На самом деле происходит следующее
# print(num1.__add__(num2))

# Взаимодействие классов на примере битвы))))
class Character:
    def __init__(self, name, power, energy=100, hands=2):
        # параметром по-умоллчанию backpack делать не будем, чтобы он не был общим
        self.name = name
        self.power = power
        self.energy = energy
        self.backpack = []  # будем присваивать список именно для конкретного экземпляра при создании (self)
        self.hands = hands
    def eat(self, food):
        if self.ebergy < 100:
            self.energy += food
        else:
            print('Not hungry')
    def do_exercise(self, hours):
        if self.energy > 0:
            self.energy -= hours * 2
            self.power += hours * 2
        else:
            print('Too tired')
    def change_alias(self, new_alias):
        self.alias = new_alias
# В методы мы без проблем можем передавать другие объекты и с ними взаимодействовать
    def  beat_up(self, foe):
        if not isinstance(foe, Character): #Проверка является ли объект экземпляром указаного класса
            return
        if foe.power < self.power:
            foe.status = 'defeated'
            self.status = 'winner'
        else:
            print('Retreat!')
peter = Character('Peter Parker', 80)
bruce = Character('Bruce Wayne', 85)
bruce.beat_up(peter)
# peter.beat_up(bruce)
print(peter.status)
print(bruce.status)
