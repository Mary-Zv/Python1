#1)Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя
# несколько чисел и строк и сохраните в переменные, выведите на экран.

name = input('Введите Ваше имя - ')
year = int(input('Введите Ваш год рождения - '))
new_year = int(input('Введите текущий год - '))
age = new_year - year
old_age = age + 37

print(f'Вас зовут - {name}\nВаш год рождения - {year}\nВаш возраст - {age}\nЧерез 37 лет Вам будет - {old_age}')