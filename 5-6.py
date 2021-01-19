#6.Сформировать (не программно) текстовый файл.
#В нём каждая строка должна описывать учебный предмет и наличие лекционных,
# практических и лабораторных занятий по предмету. Сюда должно входить и количество занятий.
# Необязательно, чтобы для каждого предмета были все типы занятий.
#Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.
#Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
                                      #  Физика:   30(л)   —   10(лаб)
                                      #  Физкультура:   —   30(пр)   —
#Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
my_dict = {}
with open('5-6.txt', 'r', encoding='utf-8') as f:
    for line in f:
        name, status = line.split(':')
        name_sum = sum(map(int, ''.join([i for i in status if i == ' ' or (i >= '0' and i <='9')]).split()))
        my_dict[name] = name_sum
print(f'{my_dict}')