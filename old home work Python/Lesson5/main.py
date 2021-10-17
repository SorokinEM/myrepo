# def square(number):
#   """Это моя первая функция!"""
#   result = number ** 2
#   return result

# print(square(5))

# res = square(5)

# print(res)

# def square():
#   user_number = int(input('Введите число: '))
#   result = user_number ** 2
#   return result
# print(square())

# def power(number_1, number_2=2):
#   result = number_1 ** number_2
#   return result

# print(power(number_2=2, number_1=8))

# def power(number_1, number_2=2):
#   result = number_1 ** number_2
#   return result

# # res = power(5, 4)

# # print(res)
# print(power(5, 4))

# my_list = [5, 1, 2, 3, 4]
# res = my_list.sort()
# # print(my_list)

# salary = 1500
# bonus = 500

# def info():
#   print(salary + bonus)

# # info()
# def info_2():
#   bonus = 50
#   print(salary + bonus)

# # info_2()

# def info_3():
#   salary = 1000
#   bonus = 50
#   print(salary + bonus)

# # info_3()

# def info_4():
#   salary = 1000
#   bonus = 50

#   some_number = 1
#   print(salary + bonus)

# name = 'James'

# def say_hi():
#   name = 'Oleg'
#   print('Hello' , name)
# say_hi()

# name = 'James'

# def say_hi():
#   global name
#   name = 'Oleg'
#   print('Hello' , name)

# print(name)
# say_hi()
# print(name)

# name = 'James'

# def say_hi():
#   global name
#   global some_number
#   some_number = 1
#   name = 'Oleg'
#   print('Hello' , name)

# print(name)
# say_hi()
# print(name)

# print(some_number)

# name = 'James'

# def say_hi():
#   global name
#   global some_number
#   some_number = 1
#   name = 'Oleg'
#   print('Hello' , name)

# print(name)
# say_hi()
# print(name)

# print(some_number)

# def say_hi():
#   name = 'Oleg'
#   def get_name():
#     # nonlocal name
#     name ='James'
#     return name
#   get_name()
#   print('Hello', name)
# say_hi()

# res = lambda x,y: x+y
# print(res(5, 4))

# map()

# filter()

# reduce()

students_list = [
    {"name": "Василий", "surename": "Теркин", "gender": "м",
     "program_exp": True, "grade": [8, 8, 9, 10, 9], "exam": 8},
    {"name": "Мария", "surename": "Павлова", "gender": "ж",
     "program_exp": True, "grade": [7, 8, 9], "exam": 9},
    {"name": "Ирина", "surename": "Андреевна", "gender": "ж",
     "program_exp": False, "grade": [10, 9, 8, 10, 10], "exam": 7},
    {"name": "Татьяна", "surename": "Сидорова", "gender": "ж",
     "program_exp": False, "grade": [7, 8, 8, 9], "exam": 10},
    {"name": "Иван", "surename": "Васильев", "gender": "м",
     "program_exp": True, "grade": [9, 8, 9, 6], "exam": 5},
    {"name": "Роман", "surename": "Золотарев", "gender": "м",
     "program_exp": False, "grade": [8, 9, 9, 6, 9], "exam": 6}
]


# ____________________________________________________________________________________________________________________
# #функция подсчётасреднего бала за экзамен у всех студентов
# def get_avg_ex_grade(students):
#   sum_ex = 0
#   for student in students:
#     sum_ex = sum_ex + student['exam']
#   return round(sum_ex / len(student), 2)
# print(get_avg_ex_grade(students_list))

# ____________________________________________________________________________________________________________________
# #функция подсчётасреднего средней оценки за дом. задание у всех студентов
# def get_avg_hw_grade(students):
#   sum_hw = 0
#   for student in students:
#     sum_hw = sum_hw + (sum(student['grade']) / len(student['grade']))
#   return round(sum_hw / len(student), 2)
# print(get_avg_hw_grade(students_list))

# ____________________________________________________________________________________________________________________
# # #функция подсчётасреднего средней оценки за дом. задание у всех студентов с опытом и без
# def get_avg_hw_grade(students, exp):
#   sum_hw = 0 #счётчик для сумирования всех оценок
#   counter = 0 # счётчик для сумирования под определённое условие true/false
#   for student in students:
#     if student['program_exp'] == exp:
#       sum_hw = sum_hw + (sum(student['grade']) / len(student['grade']))
#       counter += 1
#   return round(sum_hw / counter, 2)
# print(get_avg_hw_grade(students_list, True))
# print(get_avg_hw_grade(students_list, False))

# ____________________________________________________________________________________________________________________
# # #функция подсчётасреднего средней оценки за дом. задание у всех студентов с опытом и без
# def get_avg_hw_grade(students, exp=None):
#   sum_hw = 0 #счётчик для сумирования всех оценок
#   counter = 0 # счётчик для сумирования под определённое условие true/false
#   for student in students:
#     if student['program_exp'] == exp or exp is None:
#       sum_hw = sum_hw + (sum(student['grade']) / len(student['grade']))
#       counter += 1
#   return round(sum_hw / counter, 2)

# print(f'Средняя оценка за ДЗ для всех студентов: {get_avg_hw_grade(students_list)}')
# print(f'Средняя оценка за ДЗ для студентов с опытом програмирования: {get_avg_hw_grade(students_list, True)}')
# print(f'Средняя оценка за ДЗ для студентов без опыта программирования: {get_avg_hw_grade(students_list, False)}')

# ____________________________________________________________________________________________________________________
# #функция подсчётасреднего средней оценки за дом. задание у всех студентов с опытом и без:
def get_avg_hw_grade(students, exp=None):
    sum_hw = 0  # счётчик для сумирования всех оценок
    counter = 0  # счётчик для сумирования под определённое условие true/false
    for student in students:
        if student['program_exp'] == exp or exp is None:
            sum_hw = sum_hw + (sum(student['grade']) / len(student['grade']))
            counter += 1
    return round(sum_hw / counter, 2)


# #функция вывода информации по пользовательскому запросу:
def main(students):
    while True:
        user_input = input('Введите комманду: ')
        if user_input == '1':
            print(f'Средняя оценка за ДЗ для всех студентов: {get_avg_hw_grade(students)}')
        elif user_input == '2':
            print(f'Средняя оценка за ДЗ для студентов с опытом програмирования: {get_avg_hw_grade(students, True)}')
        elif user_input == '3':
            print(f'Средняя оценка за ДЗ для студентов без опыта программирования: {get_avg_hw_grade(students, False)}')
        elif user_input == 'q':
            print(f'Пока!')
            break
        else:
            print(f'Такой команды нет! Пока!')
            break


main(students_list)