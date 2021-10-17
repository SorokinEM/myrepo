documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

help = """
1) p - people: команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
2) s - shelf: команда, которая спросит номер документа и выведет номер полки, на которой он находится;
3) l - list: команда, которая выведет список всех документов в формате passport 2207 876234 Василий Гупкин;
4) a - add: команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться. 
5) d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок.
6) m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую.
7) as - add_shelf: команда, которая спросит номер новой полки и добавит ее в перечень."""


# Поиск владельца документа по номеру документа
def find_by_num_doc(docs):
    print('\nМеню поиска владельца документа по номеру документа.')
    while True:
        user_input = input('\nВведите номер документа или q для выхода: ')
        if user_input == 'q':
            menu()
        for value in docs:
            if value['number'] == user_input:
                print('Владелец документа:', value['name'])


# Поиск полки по номеру документа. Проработана ситуации, когда пользователь будет вводить несуществующий документ.
def find_shelf_by_num_doc(dirs):
    print('\nМеню поиска полки по номеру документа.')
    while True:
        user_input = input('\nВведите номер документа или q для выхода: ')
        if user_input == 'q':
            menu()
        for key, value in dirs.items():
            if user_input in value:
                print(f'Документ хранится на полке: {key}')
                break
        else:
            print('Документа с таким номером не существует! Попробуй ещё раз!')


# # Выведот списка всех документов в формате passport "2207 876234" "Василий Гупкин"
def list_all_docs(docs):
    print('\nМеню списка документов.\n')
    while True:
        for value in docs:
            print(value["type"], value["number"], value["name"])
        break
    else:
        print("Нет такой команды! Попробуй ещё раз!")


# # Добавление нового документа в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться. Проработана ситуация, когда пользователь будет пытаться добавить документ на несуществующую полку.
def add_doc(docs, dirs):
    print('\nМеню добавления нового документа в каталог и в перечень полок. Для выхода введите q\n')
    while True:
        new_doc = {}
        user_input_num_doc = input('Введите номер документа: ')
        if user_input_num_doc == 'q':
            menu()
        user_input_type = input('Введите тип документа: ')
        user_input_name = input('Введите имя влыдельца документа: ')
        new_doc["type"] = user_input_type
        new_doc["number"] = user_input_num_doc
        new_doc["name"] = user_input_name
        docs.append(new_doc)
        while True:
            user_input_num_shelf = input('Введите номер полки для хранения документа: ')
            if user_input_num_shelf == 'q':
                menu()
            elif user_input_num_shelf in dirs.keys():
                dirs[user_input_num_shelf].append(new_doc["number"])
                print('Документ успешно добавлен!')
                break
            else:
                print(f'Такой полки не существует! Попробуй ещё раз')


# Запрос номера новой полки и добавление ее в перечень Предусмотрен случай, когда пользователь добавляет полку, которая уже существует.
def add_shelf(dirs):
    print('\nМеню добавления новой полки. Для выхода введите q\n')
    while True:
        user_input_new_shelf = input('Введите номер новой полки: ')
        if user_input_new_shelf == 'q':
            menu()
        elif user_input_new_shelf in dirs.keys():
            print('Такая полка уже существует, попробуй ещё раз!')
        else:
            print('Полка успешно создана!')
            dirs[user_input_new_shelf] = list()
            print
            break

        #  Удаление документа по его номеру каталога и из перечня полок.


def del_doc(docs, dirs):
    while True:
        num_doc = input('Введите номер документа для удаления или q для выхода в главное меню: ')
        if num_doc == 'q':
            menu()
        for i in range(len(docs)):
            if documents[i]["number"] == num_doc:
                del documents[i]
                print('Документ успешно удалён!')
                break
        else:
            print('Такого документа не существует! Попробуй ещё раз!')
        for value in directories.values():
            if num_doc in value:
                value.remove(num_doc)
            print(dirs)

def menu():
    while True:
        user_input = input('\nВведите комаду / help для справки: ')
        if user_input == 'people' or user_input == 'p':
            find_by_num_doc(documents)
        elif user_input == 'shelf' or user_input == 's':
            find_shelf_by_num_doc(directories)
        elif user_input == 'list' or user_input == 'l':
            list_all_docs(documents)
        elif user_input == 'add' or user_input == 'a':
            add_doc(documents, directories)
        elif user_input == 'delete' or user_input == 'd':
            del_doc(documents, directories)
        elif user_input == 'add_shelf' or user_input == 'as':
            add_shelf(directories)
        elif user_input == 'help':
            print(help)
        else:
            print('Не верная команда! Попробуй ещё раз!')


menu()

# _____________________________________________________________________________________
# def delete_by_id(doc_dir=documents, store_place=directories):
#     person_id = input_err('Введите номер документа для удаления / Quit для отмены: ', find_index)
#     if person_id is not None:
#         store_place[find_value(person_id)].remove(person_id)
#         doc_dir.pop(find_index(person_id))
#         print('Удаление совершено')


# def move_doc_to_shelf(store_place=directories):
#     print('\nВы переносите документ в новое место хранения')
#     person_id = input_err("Введите 'номер документа'  / Quit для отмены: ", find_index)
#     if person_id is not None:
#         shelf_number = input_err("Новую полку для хранения'  / Quit для отмены: ", in_key_list)
#     if shelf_number is not None:
#         store_place[find_value(person_id)].remove(person_id)
#         store_place[shelf_number].append(person_id)
#         print('Перенос успешно завершен')