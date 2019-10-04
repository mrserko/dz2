right_year = 1799
right_day = "06.06"
year = ""
while not year.isdigit():
    year = input("Введите год рождения А.С.Пушкина: ")
year = int(year)

if year == right_year:
    day = input("Введите день рождения А.С.Пушкина (чч.мм): ")
    if day == right_day:
        print("Верно!")
    else:
        print("Неверный день рождения!")
else:
    print("Неверный год рождения!")