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


def plot_person_card(doc_dir=documents):
    print('\nСодержимое документов:')
    for card_index in range(len(doc_dir)):
        result = ", ".join(f'{value}' for value in doc_dir[card_index].values())
        print(f'Карточка {card_index + 1}: {result}')


def plot_store_dir(storage_place=directories):
    print('\nСодержимое полок:')
    for store, item_store in storage_place.items():
        item_store_str = ", ".join(f"'{word}'" for word in item_store)
        if item_store_str == "":
            item_store_str = "'Пусто'"
        print(f'Содержимое полки №{store} : {item_store_str}')


def find_person_by_id(doc_dir=documents):
    person_id = input_err('Введите номер документа для поиска владельца: ', find_index)
    if person_id is not None:
        print(f'Владелец документа {doc_dir[find_index(person_id)]["name"]}\n')


def find_store_place_by_id(store_place=directories):
    person_id = input_err('Введите номер документа для поиска полки: / Quit для отмены: ', find_value)
    if person_id is not None:
        print(f'Номер полки запрошенного документа: {find_value(person_id)}\n')


def add_new_doc(doc_dir=documents, store_place=directories):
    print('\nВы создаете новую запись')
    new_storage = input_err('Введите номер полки для хранения документов / cancel если передумали: ', in_key_list,
                            'cancel')
    if new_storage is not None:
        new_line = dict()
        for key in doc_dir[0]:
            new_line[key] = input(f"Введите данные для поля '{key}': ")
        doc_dir.append(new_line)
        store_place[new_storage].append(new_line["number"])


def quit_command(text_inp, stop_word):
    if text_inp.lower() == stop_word:
        command_error()
        return True
    return False


def input_err(st_text, func, stop_word='quit'):
    while True:
        text_inp = input('\n' + st_text)
        if quit_command(text_inp, stop_word):
            return None
        res = func(text_inp)
        if res is None:
            command_error()
            continue
        return text_inp


def find_index(person_id, doc_dir=documents):
    for index in range(len(doc_dir)):
        if doc_dir[index]['number'] == person_id:
            return index
    return None


def find_value(person_id, store_place=directories):
    for store, item_store in store_place.items():
        if person_id in item_store:
            return store
    return None


def find_key(person_id, store_place=directories):
    if person_id in store_place.keys():
        return None
    return person_id


def in_key_list(person_id, store_place=directories):
    if person_id in store_place.keys():
        return person_id
    return None


def delete_by_id(doc_dir=documents, store_place=directories):
    person_id = input_err('Введите номер документа для удаления / Quit для отмены: ', find_index)
    if person_id is not None:
        store_place[find_value(person_id)].remove(person_id)
        doc_dir.pop(find_index(person_id))
        print('Удаление совершено')


def add_new_shelf(store_place=directories):
    print('\nВы добавляете новую полку')
    shelf_name = input_err('Введите порядковый номер полки / Quit для выхода: ', find_key)
    if shelf_name is not None and find_key(shelf_name) is not None:
        store_place[shelf_name] = list()
        print('Добавление успешно')


def move_doc_to_shelf(store_place=directories):
    print('\nВы переносите документ в новое место хранения')
    person_id = input_err("Введите 'номер документа'  / Quit для отмены: ", find_index)
    if person_id is not None:
        shelf_number = input_err("Новую полку для хранения'  / Quit для отмены: ", in_key_list)
    if shelf_number is not None:
        store_place[find_value(person_id)].remove(person_id)
        store_place[shelf_number].append(person_id)
        print('Перенос успешно завершен')


def my_quit():
    print('Завершение работы')
    exit(0)


def command_error():
    print('Ошибка ввода данных')


def main_prog():
    while True:
        print('\nВведите команду запроса / Help для справки: ')
        command = input()
        command_dict.get(command.lower(), command_error)()
    return None


help_menu = ("""
    'plot_shelf' : вывод на экран содержимого полок,
    'add_shelf'  : добавление новой полки хранения,
    'get_shelf'  : поиск полки хранения по номеру документа,
    'plot_ID'    : вывод на экран содержимого списка документов ,
    'get_name'   : поиск имени человека по номеру документа, 
    'move_ID'    : перенести документы в другую папку,    
    'add_ID'     : создание нового документа,       
    'delete_ID'  : удаление спика документов из базы по номеру,
    'Help'       : вызов меню помощи,
    'Quit'       : завершение работы""")

command_dict = {
    'plot_shelf': plot_store_dir,
    'plot_id': plot_person_card,
    'move_id': move_doc_to_shelf,
    'add_shelf': add_new_shelf,
    'add_id': add_new_doc,
    'get_name': find_person_by_id,
    'get_shelf': find_store_place_by_id,
    'delete_id': delete_by_id,
    'help': lambda: print(help_menu),
    'quit': my_quit
}

if __name__ == '__main__':
    main_prog()