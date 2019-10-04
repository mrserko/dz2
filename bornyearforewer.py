right_year = 1799
year = ""
while year != right_year:
    while not year.isdigit():
        year = input("Введите год рождения А.С.Пушкина: ")
    year = int(year)
    if year != right_year:
        print("Неверный год рождения!")
        year = " "
print("Верно!")