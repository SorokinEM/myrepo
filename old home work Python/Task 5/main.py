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


# Поиск владельца документа по номеру документа
def find_by_num_doc(docs):
    num_doc = input('Введите номер документа: ')
    for value in docs:
        if value['number'] == num_doc:
            print('Владелец документа:', value['name'])


# find_by_num_doc(documents)

# Поиск полки по номеру документа
def find_shelf_by_num_doc(dirs):
    num_doc = input('Введите номер документа: ')
    for key, value in dirs.items():
        if num_doc in value:
            print(f'Номер полки с искомым документом: {key}')
            return key
    print(f'Документы без номера хранятся на полке: {key}')
    return None


# find_shelf_by_num_doc(directories)

# # Выведот списка всех документов в формате passport "2207 876234" "Василий Гупкин"
def list_all_docs(docs):
    while True:
        all_docs = input('Введите команду: ')
        if all_docs == 'list' or all_docs == 'l':
            for value in docs:
                print(value["type"], value["number"], value["name"])
            break
        else:
            print("Нет такой команды! Попробуй ещё раз!")


# list_all_docs(documents)

# # Добавление нового документа в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.
def add_doc(docs, dirs):
    new_doc = {}
    user_input_num_doc = input('Введите номер документа: ')
    user_input_type = input('Введите тип документа: ')
    user_input_name = input('Введите имя влыдельца документа: ')
    new_doc["type"] = user_input_type
    new_doc["number"] = user_input_num_doc
    new_doc["name"] = user_input_name
    docs.append(new_doc)
    while True:
        user_input_num_shelf = input('Введите номер полки для хранения документа: ')
        if user_input_num_shelf in dirs.keys():
            dirs[user_input_num_shelf].append(new_doc["number"])
            break
        else:
            print(f'Такой полки не существует! Попробуй ещё раз')
    print(docs, dirs)

#add_doc(documents, directories)


# Запрос номера новой полки и добавление ее в перечень.
def add_shelf(dirs):
    while True:
        user_input_new_shelf = input('Введите номер новой полки: ')
        if user_input_new_shelf in dirs.keys():
            print('Такая полка уже существует, попробуй ещё раз!')
        else:
            print('Полка успешно создана!')
            dirs[user_input_new_shelf] = list()
            break

# add_shelf(directories)
