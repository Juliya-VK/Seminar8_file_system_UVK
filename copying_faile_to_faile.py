

def copy_file_contents(source_file, destination_file):
    try:
        with open(source_file, 'r', encoding='utf-8') as src:
            data = src.readlines()
        
        with open(destination_file, 'w', encoding='utf-8') as dest:
            dest.writelines(data)
        
        print(f"Данные успешно скопированы из {source_file} в {destination_file}.")
    except FileNotFoundError:
        print(f"Файл {source_file} не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

source_file = 'data_1.txt'
destination_file = 'data_2.txt'

copy_file_contents(source_file, destination_file)
