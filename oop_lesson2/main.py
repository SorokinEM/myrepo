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

class Character:
    def __init__(self, name, power, energy=100, hands=2):
        self.name = name
        self.power = power
        self.energy = energy
        self.__backpack = []
        self.hands = hands

    def eat(self, food):
        if self.energy < 100:
            self.energy += food
        else:
            print('Not hungry')

    def do_exercise(self, hours):
        if self.energy > 0:
            self.energy -= hours * 2
            self.power += hours * 2
        else:
            print('Too tired')
    def __change_alias(self, new_alias):
        self.alias = new_alias

    def beat_up(self, foe):
        if not isinstance(foe, Character):
            return
        if foe.power < self.power:
            foe.status = 'defeated'
            self.status = 'winner'
        else:
            print('Retreat!')
peter = Character('Peter Parker', 80)
peter.__change_alias('Spider-Man')
print(peter.alias)
print(peter.__backpack)

# Будет ошибка и её можно обойти этим дополнение команды
