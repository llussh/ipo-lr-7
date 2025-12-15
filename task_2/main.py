#Телешевская Дарья
#Вариант 4
import json
print("start code …")
with open ('D:/Study/ИПО/ipo-lr-7/task_2/dump.json', 'r', encoding="utf-8") as dump:
    content = json.loads(dump.read())  
    number = input("Введите номер квалификации: ").strip()
    code = number[:12]
    find = False
    for dict in content:
        if (dict['model'] == 'data.specialty' and  dict['fields']['code'] == code):
            print("============== Найдено ===============")
            print(f"{dict['fields']['code']} >> Специальность \"{dict['fields']['title']}\"")
            find = True 
        if (dict['model'] == 'data.skill' and  dict['fields']['code'] == number):
            print(f"{dict['fields']['code']} >> Квалификация \"{dict['fields']['title']}\"")
    if find == False:
        print("=============== Не найдено ===============")
print("end code …")