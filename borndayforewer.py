right_year = 1799
right_day = "06.06"
day = " "
year = " "
while year != right_year:
    while not year.isdigit():
        year = input("Введите год рождения А.С.Пушкина: ")
    year = int(year)
    if year != right_year:
        print("Неверный год рождения!")
        year = " "
while day != right_day:
    day = input("Введите день рождения А.С.Пушкина (чч.мм): ")
    if day != right_day:
        print("Неверный день рождения!")
print("Верно!")