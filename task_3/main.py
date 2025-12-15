#Телешевская Дарья 
#Вариант 4
import json
import os
print("start code …")
choice = 0
filename = 'records.json'
operations = 0
with open("D:/Study/ИПО/ipo-lr-7/task_3/records.json", 'r+', encoding="utf-8") as file:
    content = json.loads(file.read())

while choice != 5 :
    print("___________-М-Е-Н-Ю-___________")
    print("1.Вывести все записи")
    print("2.Вывести запись по полю (id)")
    print("3.Добавить запись ")
    print("4.Удалить запись по полю (id)")
    print("5.Выйти из программы")
    print("________________________________")
  
    choice = int(input("Введите номер пункта: "))

    if choice == 1:
        print("----------------ВСЕ-ЗАПИСИ----------------")
        count = 1
        for information in content:
            print(f"----------{count}-ЗАПИСЬ-------------")
            for paragraph in information:
                print(f"{paragraph} : {information[paragraph]} ")
            print()
            count += 1
        operations += 1
        print()

    elif choice == 2:
        print("--------------------------------------")
        id = input("введите поле (id): ")
        found = False
        for information in content:
            if information['id'] == id:
                found = True
                print(f"----------{id}-ЗАПИСЬ-------------")
                for paragraph in information:
                    print(f"{paragraph} : {information[paragraph]} ")
                print(f"позиция в словаре: {int(id) - 1}")  
        if found == False:
            print("Записи с таким id не найдено, попробуйте еще")
        operations += 1
        print()

    elif choice == 3:
        print("-------------ВВОД-СТРОКИ-----------")
        name = input("введите название модели: ")
        manufacturer = input("введите название производителя: ")
        is_petrol = input("введите заправляется ли машина бензином(True/False): ")
        tank_volume = input("введите объем бака(л): ")

        last_record = content[-1]

        new_record = {
           'id': str(int(last_record['id'])+1),
           'name': name,
           'manufacturer': manufacturer,
           'is_petrol': is_petrol,
           'tank_volume': tank_volume
        }
        content.append(new_record)

        with open('records.json', 'w', encoding='utf-8') as file:
            json.dump(content, file, ensure_ascii=False, indent=2)
        
        print("Запись успешно добавлена")
        operations += 1
        print()

    elif choice == 4:
        delete = input("введите id записи которыю вы хотите удалить:")
        found = False
        for information in content:
            if information['id'] == delete:
                found = True
                print(f"----------УДАЛЁННАЯ-ЗАПИСЬ-------------")
                for paragraph in information:
                    print(f"{paragraph} : {information[paragraph]} ")
                del content[int(delete) - 1]
                with open('records.json', 'w', encoding='utf-8') as file:
                    json.dump(content, file, ensure_ascii=False, indent=2)
                print("запись успешно удалена")
                break
        if found == False:
            print("Записи с таким id не найдено, попробуйте еще")
        operations += 1
        print()
    
    elif choice == 5:
        print(f"количество выполненных операций: {operations}")
        print(" ПРОГРАММА ЗАВЕРШЕНА ")
        print("end code …")
