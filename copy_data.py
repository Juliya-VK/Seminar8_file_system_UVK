from return_data_file import data_file



def copy_file():
    data, nf = data_file()
    answer = int(input("Выберите файл, к который Вы хотите перенсти данные (от 1 до 2): "))
    while (answer < 1 or answer >2) or answer == nf:
        answer = int(input("ОШИБКА! Вы ввели некоректное значение, или выбрали тот же файл\n"
                           "Выберите файл, к который Вы хотите перенсти данные (от 1 до 2): "))
    with open(f'db/data_{answer}.txt', 'r', encoding='utf-8') as faile:
        count_row_data_and = len(file.readlines()) + 1
    data = [f'{i + count_row_data_and };{data[i].split(";")[1]};'
                f'{data[i].split(";")[2]};'
                f'{data[i].split(";")[3]};'
                f'{data[i].split(";")[4]}'
                for i in range(len(data))]
    with open(f'db/data_{answer}.txt', 'a', encoding='utf-8') as faile:
        file.writelines(data)
    print("Данные успешно скопированы!")




   

    