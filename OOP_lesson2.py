# class Character:
#     def __init__(self, name, power, energy=100, hands=2):
#         self.name = name
#         self.power = power
#         self.energy = energy
#         self.backpack = []
#         self.hands = hands
#
#     def eat(self, food):
#         if self.energy < 100:
#             self.energy += food
#         else:
#             print('Not hungry')
#
#     def do_exercise(self, hours):
#         if self.energy > 0:
#             self.energy -= hours * 2
#             self.power += hours * 2
#         else:
#             print('Too tired')
#     def change_alias(self, new_alias):
#         self.alias = new_alias
#
#     def beat_up(self, foe):
#         if not isinstance(foe, Character):
#             return
#         if foe.power < self.power:
#             foe.status = 'defeated'
#             self.status = 'winner'
#         else:
#             print('Retreat!')
# peter = Character('Peter Parker', 80)
# print(peter.backpack)
#
# Реализуем защищённую переменную и п
# class Character:
#     def __init__(self, name, power, energy=100, hands=2):
#         self.name = name
#         self.power = power
#         self.energy = energy
#         self._backpack = []
#         self.hands = hands
#
#     def eat(self, food):
#         if self.energy < 100:
#             self.energy += food
#         else:
#             print('Not hungry')
#
#     def do_exercise(self, hours):
#         if self.energy > 0:
#             self.energy -= hours * 2
#             self.power += hours * 2
#         else:
#             print('Too tired')
#     def _change_alias(self, new_alias):
#         self.alias = new_alias
#
#     def beat_up(self, foe):
#         if not isinstance(foe, Character):
#             return
#         if foe.power < self.power:
#             foe.status = 'defeated'
#             self.status = 'winner'
#         else:
#             print('Retreat!')
# peter = Character('Peter Parker', 80)
# peter._change_alias('Spider-Man')
# print(peter.alias)
# print(peter._backpack)
# На самом деле, технически для интерпритаора это не имеет никакого значения. Это соглашение, согласно которому,
# такие атрибуты и методы не стоит использовать за рамками класса и дочерних классов.

# Двойное подчёркивание в начале имени атрибута/метода даёт большую защиту: атрибут становится не доступным
# по этому имени вне самого класса

# Реализуем приватную переменную и метод


#__________________________
#ИНКАПСУЛЯЦИЯ:
# class Character:
#     def __init__(self, name, power, energy=100, hands=2):
#         self.name = name
#         self.power = power
#         self.energy = energy
#         self.__backpack = []
#         self.hands = hands

#     def eat(self, food):
#         if self.energy < 100:
#             self.energy += food
#         else:
#             print('Not hungry')

#     def do_exercise(self, hours):
#         if self.energy > 0:
#             self.energy -= hours * 2
#             self.power += hours * 2
#         else:
#             print('Too tired')
#     def __change_alias(self, new_alias):
#         self.alias = new_alias

#     def beat_up(self, foe):
#         if not isinstance(foe, Character):
#             return
#         if foe.power < self.power:
#             foe.status = 'defeated'
#             self.status = 'winner'
#         else:
#             print('Retreat!')
# peter = Character('Peter Parker', 80)
# peter._Character__change_alias('Spider-Man')
# print(peter.alias)
# print(peter._Character__backpack)

# Будет ошибка и её можно обойти этим дополнение команды _Caracter
# Таким образом, реализация инкапсуляции в Python носит формальный характер и работает только на уровне соглашения.

#__________________________
#НАСЛЕДОВАНИЕ:
#реализуем множественное наследование
# class Character:
#   name = ''
#   power = 0
#   energy = 100
#   hands = 2

# class Spider:
#   power = 0
#   energy = 50
#   hands = 8
#   def webshoot(self):
#     print('Pew-Pew!')

# class SpiderMan(Character, Spider):
#   pass
# peter_parker = SpiderMan()
# print(peter_parker.name)
# print(peter_parker.power)
# print(peter_parker.energy)
# print(peter_parker.hands)
# peter_parker.webshoot()
#  # Линеаризация - способ представления дерева (графа, дерева) в линейную модель (плоскую структуру, список) для определения порядка наследования.
# print(SpiderMan.mro())

#Перенесём всё в init
##class Character:
##  def __init__(self, name, power, energy=100, hands=2):
##    self.name = name
##    self.power = power
##    self.energy = energy
##    self.hands = hands
##  
##class Spider:
##  def __init__(self, power, energy=50, hands=8):
##    self.power = power
##    self.energy = energy
##    self.hands = hands
##
##  def webshoot(self):
##    print('Pew-Pew')
##
##class SpiderMan(Character, Spider):
##  def turn_spider_sense(self):
##    self.energy -= 10
##    self.power += 20
##
##peter_parker = SpiderMan('Peter Parker', 80)
##print(peter_parker.energy)
##print(peter_parker.power)
##print(peter_parker.hands)
##peter_parker.turn_spider_sense()
##print('Включили паучье чутьё!')
##print(peter_parker.energy)
##print(peter_parker.power)

#Полиморфизм
#Добавим в наши родительские класы новые методы

##class Character:
##  def __init__(self, name, power, energy=100, hands=2):
##    self.name = name
##    self.power = power
##    self.energy = energy
##    self.hands = hands
##    
##  def move(self):
##    print('Changing position')
##    
##  
##class Spider:
##  def __init__(self, power, energy=50, hands=8):
##    self.power = power
##    self.energy = energy
##    self.hands = hands
##
##  def webshoot(self):
##    print('Pew-Pew')
##
##  def move(self):
##    self.webshoot()
##    print('Changing position')
##
##class SpiderMan(Character, Spider):
##  def turn_spider_sense(self):
##    self.energy -= 10
##    self.power += 20
##
##peter_parker = SpiderMan('Peter Parker', 80)
###peter_parker.webshoot()
##peter_parker.move()

##class Character:
##  def __init__(self, name, power, energy=100, hands=2):
##    self.name = name
##    self.power = power
##    self.energy = energy
##    self.hands = hands
##    
##  def move(self):
##    print('Moving on 2 squares')
##    
##  
##class Spider:
##  def __init__(self, power, energy=50, hands=8):
##    self.power = power
##    self.energy = energy
##    self.hands = hands
##
##  def webshoot(self):
##    print('Pew-Pew')
##
##  def move(self):
##    self.webshoot()
##    print('Moving on 1 squares')
##
##class SpiderMan(Character, Spider):
##  def turn_spider_sense(self):
##    self.energy -= 10
##    self.power += 20
##
##  def move(self):
##    self.webshoot()
##    print('Moving on 3 squares')
##
##peter_parker = SpiderMan('Peter Parker', 80)
####peter_parker.webshoot()
##peter_parker.move()

#Теперь создадим инвентарь нашему игровому персонажу
##class Character:
##  def __init__(self, name, power, energy=100, hands=2):
##    self.name = name
##    self.power = power
##    self.energy = energy
##    self.hands = hands
##    
##  def move(self):
##    print('Moving on 2 squares')
##    
##  
##class Spider:
##  def __init__(self, power, energy=50, hands=8):
##    self.power = power
##    self.energy = energy
##    self.hands = hands
##
##  def webshoot(self):
##    print('Pew-Pew')
##
##  def move(self):
##    self.webshoot()
##    print('Moving on 1 squares')
##
##class SpiderMan(Character, Spider):
##  #такой вариант допустимый, но зачем нам перезаписывать инициализацию,
##  #которая полностью совпадает с родителем?
##  def __init__(self, name, power, energy=100, hands=2):
##    self.name = name
##    self.power = power
##    self.energy = energy
##    self.hands = hands
##    self.backpack = []
##    
##  def turn_spider_sense(self):
##    self.energy -= 10
##    self.power += 20
##
##  def move(self):
##    self.webshoot()
##    print('Moving on 3 squares')
##
##peter_parker = SpiderMan('Peter Parker', 80)
####peter_parker.webshoot()
###peter_parker.move()
##print(peter_parker.backpack)

#Функция super() можно получить доступ к унаследованным методам,
#которые были перезаписаны в дочернем классе.
##class Character:
##  def __init__(self, name, power, energy=100, hands=2):
##    self.name = name
##    self.power = power
##    self.energy = energy
##    self.hands = hands
##    
##  def move(self):
##    print('Moving on 2 squares')
##    
##  
##class Spider:
##  def __init__(self, power, energy=50, hands=8):
##    self.power = power
##    self.energy = energy
##    self.hands = hands
##
##  def webshoot(self):
##    print('Pew-Pew')
##
##  def move(self):
##    self.webshoot()
##    print('Moving on 1 squares')
##
##class SpiderMan(Character, Spider):
##  #ы полностью наследуем от родителя инициализацию и добавляем новый атрибут
##  #для экземпляра
##  def __init__(self, name, power):
##    super().__init__(name, power)
##    self.backpack = []
##    
##  def turn_spider_sense(self):
##    self.energy -= 10
##    self.power += 20
##
##  def move(self):
##    self.webshoot()
##    print('Moving on 3 squares')
##
##peter_parker = SpiderMan('Peter Parker', 80)
##print(peter_parker.backpack)
##print(peter_parker.power)
##print(peter_parker.energy)
##print(peter_parker.hands)

##class Character:
##  def __init__(self, name, power, energy=100, hands=2):
##    self.name = name
##    self.power = power
##    self.energy = energy
##    self.hands = hands
##    
##  def move(self):
##    print('Moving on 2 squares')
##    
##  
##class Spider:
##  def __init__(self, power, energy=50, hands=8):
##    self.power = power
##    self.energy = energy
##    self.hands = hands
##
##  def webshoot(self):
##    print('Pew-Pew')
##
##  def move(self):
##    self.webshoot()
##    print('Moving on 1 squares')
##
##class SpiderMan(Character, Spider):
##  def __init__(self, name, power):
##    super().__init__(name, power)
##    self.backpack = []
##    
##  def turn_spider_sense(self):
##    self.energy -= 10
##    self.power += 20
##  #Наш персонаж не может пользоваться паутиной, если её нет! попробуем исправить
##  #где ошибка?
##  def webshoot(self):
##    if 'web' in self.backpack:
###      self.webshoot() #нужно вызывать вебшут от родителя, т.е. super().webshoot()
##      super().webshoot()
##    else:
##      print('No web!')
##      
##  def move(self):
##    self.webshoot()
##    print('Moving on 3 squares')
##
##peter_parker = SpiderMan('Peter Parker', 80)
##peter_parker.webshoot()
##peter_parker.backpack.append('web')
##peter_parker.webshoot()

###Можем ли наследовать что-то не от родителя по mro, а от другог родителя?
###Добавим родительским классам атаку и проверим, как будет наследоваться
##class Character:
##  def __init__(self, name, power, energy=100, hands=2):
##    self.name = name
##    self.power = power
##    self.energy = energy
##    self.hands = hands
##    
##  def move(self):
##    print('Moving on 2 squares')
##    
##  def attak(self, foe):
##    foe.health -= 10
##        
##  
##class Spider:
##  def __init__(self, power, energy=50, hands=8):
##    self.power = power
##    self.energy = energy
##    self.hands = hands
##
##  def webshoot(self):
##    print('Pew-Pew')
##
##  def move(self):
##    self.webshoot()
##    print('Moving on 1 squares')
##
##  def attak(self, foe):
##    foe.status = 'stunned'
##
##class SpiderMan(Character, Spider):
##  def __init__(self, name, power):
##    super().__init__(name, power)
##    self.backpack = []
##    
##  def turn_spider_sense(self):
##    self.energy -= 10
##    self.power += 20
##  #Наш персонаж не может пользоваться паутиной, если её нет! попробуем исправить
##  #где ошибка?
##  def webshoot(self):
##    if 'web' in self.backpack:
###      self.webshoot() #нужно вызывать вебшут от родителя, т.е. super().webshoot()
##      super().webshoot()
##    else:
##      print('No web!')
##      
##  def move(self):
##    self.webshoot()
##    print('Moving on 3 squares')
##
##  #добавляем классу свою атаку
##  def attak(self, foe):
##    super().attak(foe)
##    Spider.attak(self, foe)
##
##    
##
##peter_parker = SpiderMan('Peter Parker', 80)
##enemy = Character('Some enemy', 10)
##enemy.health = 100
##
##peter_parker.attak(enemy)
##
##print(enemy.health)
##print(enemy.status)

#Перегрузка и переопределение методов
#Можем ли наследовать что-то не от родителя по mro, а от другог родителя?
#Добавим родительским классам атаку и проверим, как будет наследоваться
##class Character:
##  def __init__(self, name, power, energy=100, hands=2):
##    self.name = name
##    self.power = power
##    self.energy = energy
##    self.hands = hands
##    
##  def move(self):
##    print('Moving on 2 squares')
##    
##  def attak(self, foe):
##    foe.health -= 10
##        
##  
##class Spider:
##  def __init__(self, power, energy=50, hands=8):
##    self.power = power
##    self.energy = energy
##    self.hands = hands
##
##  def webshoot(self):
##    print('Pew-Pew')
##
##  def move(self):
##    self.webshoot()
##    print('Moving on 1 squares')
##
##  def attak(self, foe):
##    foe.status = 'stunned'
##
##class SpiderMan(Character, Spider):
##  def __init__(self, name, power):
##    super().__init__(name, power)
##    self.backpack = []
##    
##  def turn_spider_sense(self):
##    self.energy -= 10
##    self.power += 20
##  #Наш персонаж не может пользоваться паутиной, если её нет! попробуем исправить
##  #где ошибка?
##  def webshoot(self):
##    if 'web' in self.backpack:
###      self.webshoot() #нужно вызывать вебшут от родителя, т.е. super().webshoot()
##      super().webshoot()
##    else:
##      print('No web!')
##      
##  def move(self):
##    self.webshoot()
##    print('Moving on 3 squares')
##
##  #добавляем классу свою атаку
##  def attak(self, foe):
##    super().attak(foe)
##    Spider.attak(self, foe)
##
##  #Добавим возможность сравнения персонажей
##  def __lt__(self, other):
##    if not isinstance(other, Character):
##      print('Not a Character!')
##      return
##    return self.power < other.power
##
##  def __str__(self): #Переопределили как будет работать метод print()
##    res = f'Сила персонажа = {self.power}'
##    return res
##  
##peter_parker = SpiderMan('Peter Parker', 80)
##miles_morales = SpiderMan('Miles Morales', 85)
####print(peter_parker < miles_morales)
####print(peter_parker > miles_morales)
##peter_parker.__lt__(miles_morales)
##print(peter_parker)
####print(peter_parker)
####print(miles_morales)
##enemy = Character('Some enemy', 10)
##enemy.health = 100
##
##peter_parker.attak(enemy)
##
##print(enemy.health)
##print(enemy.status)


#Наводки к ДЗ!!!!!!!!!


1)  создаём класс lector от mentor pass, класс rewiever от lector pass
2)  Вся инициализация будет реализовывоться от дочерних классов
3)  Смотрим чем дочерние классы будут отличаться от родительских:
    - просто вырезаем def rate_hw из класса менторов и вставляем его в класс rewiever
    - добавляем похожий код def rate_hw студентам что они могли ставить оценки лекторам (также у лекторов делаем словарь как и устудентов для олценок)(код как пример ниже)
    - для подсчёта средней оценки за лекцию у лекторов написать отдельный метод


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
 
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
 
cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
 
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
 
print(best_student.grades)













