userChoice = 0
Numbers = [1 , 2 , 3 , 4 , 5, 6 , 7 , 8, 9 , 10 , 11 , 12, 13 , 14 , 15]

print('Меню:')
print('1. Вывести на экран все знаения')
print('2. Добавить значение')
print('3. Удалить значение')
print('4. Найти значение')
print('5. Отсортировать значения')
print('Введите опцию:')

while userChoice != 6:
        userChoice = int(input())
        if userChoice == 1:
            print(Numbers)
        elif userChoice == 2:
            print('Введите значение')
            NewValue = int(input())
            Numbers.append(NewValue)
            print(Numbers)
        elif userChoice == 3:
            if len(Numbers) !=0 :
                print('Введите число для удаления')
                searchValue = int(input())
                counter = 0
                deleted = False
                for count in range(0,len(Numbers)) :
                    if (Numbers[count] == searchValue) & (count < len(Numbers)):
                        deleted = True
                        while count+1 < len(Numbers):
                            Numbers[count] = Numbers[count+1]
                            count = count+1
                if deleted is True :
                    del Numbers[count]
                    print(Numbers)
                elif deleted is False :
                    print('Значения нет в базе данных')
            else:
                print('База пустая! Добавьте значения')
        elif userChoice == 4:
            try:
                print('Введите число для поиска его индекса:')
                index = Numbers.index(int(input()))
                print('Индекс этого числа равен')
                print(index)
            except ValueError:
                print("значение не найдено")
        elif userChoice == 5:
            print
        else:
            print('Ошибка. Выберите существующую опцию')

        print('Меню:')
        print('1. Вывести на экран все значения')
        print('2. Добавить значение')
        print('3. Удалить значение')
        print('4. Найти значение')
        print('5. Отсортировать значения')
        print('Введите опцию:')