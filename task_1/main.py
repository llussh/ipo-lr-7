
#Вариант 4
print("start code …")

books = [{"title":"Heaven Official's Blessing", "author" : "Mo Xiang Tong Xiu", "year" : "2020"},
 {"title": "Десять негритят" , "author": "Агата Кристи" , "year": "1939"},
 {"title": "Славгород" , "author":"Софа Вернер" , "year":"2023"},
 {"title": "Портрет Дориана Грея", "author": "Оскар Уайльд", "year":"1890"},
 {"title": "Если все кошки в мире исчезнут", "author": "Гэнки Кавамура", "year":"2012"}]

i = 1
for book in books:
    print(f" ---------------------- Книга {i} -----------------------")
    print(f"Название: {book['title']}, Автор: {book['author']}")
    print(f" ---------------------- {book['year']} ----------------------")
    print()
    i+=1


print("end code …")

