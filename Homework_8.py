from function import delete, add, change, printdata, clear, loading, check_numbers, terminate, data_remake
def interface():


    print("***************************  Добро пожаловать!\t ***************************\n"
          "Выберите действие:\n"
          "___________________________\n"
          "1. Удалить запись.\n"
          "2. Добавить запись.\n"
          "3. Изменить запись.\n"
          "4. Вывести данные.\n"
          "5. Очистить файл.\n"
          "6. Перенести данные")
    answer = int(input("___________________________\nВведите номер действия: "))
    loading()
    answer = check_numbers(answer)
    while answer != 7:
        if answer == 1:
            delete()
        elif answer == 2:
            add()
        elif answer == 3:
            change()
        elif answer == 4:
            printdata()
        elif answer == 5:
            clear()
        elif answer == 6:
            transfer()
        print("Выберите действие:\n"
              "___________________________\n"
              "1. Удалить запись.\n"
              "2. Добавить запись.\n"
              "3. Изменить запись.\n"
              "4. Вывести данные.\n"
              "5. Очистить файл.\n"
              "6. Выход.")
        answer = int(input("___________________________\nВведите номер действия: "))
        answer = check_numbers(answer)

    answer = input("___________________________\n"
                   "Желаю всего доброго! Не забывай, что все данные, которые ты записал, они сохранились.\n"
                   "Удалить? (ОТВЕТЬТЕ ДА/НЕТ): ").lower()
    if answer in ['да', 'yes']:
        terminate()
        print("___________________________\n"
              "Данные успешно удалены!"
              "Всего доброго!\n")
    else:
        print("___________________________\n"
              "Всего доброго!")
    exit()

def transfer():
    printdata()
    answer = int(input('___________________________\n'
                       'Выберите файл, из которого Вы хотите перенести данные: '))
    answer2 = int(input('___________________________\n'
                       'Выберите файл, в который Вы хотите перенести данные: '))
    while answer < 1 or answer > 3:
        answer = int(input('___________________________\n'
                           'ERROR! Ошибка, скорее всего, Вы указали неправильное число.\n'
                           'Введите номер файла от 1 до 3: '))
        loading()
    with open(f'db/data{answer}.txt', 'r', encoding='utf-8') as source_file:
     with open(f'db/data{answer2}.txt', 'w', encoding='utf-8')  as target_file:
      for line in source_file:
        target_file.write(line)
    interface()    

interface()

