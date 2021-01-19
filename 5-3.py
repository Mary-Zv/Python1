#3.Создать текстовый файл (не программно). Построчно записать фамилии сотрудников
# и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тысяч,
# вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода сотрудников.
#Пример файла:
#Иванов 23543.12
#Петров 13749.32

# мой вариант. почему-то ругается на 12 строку. не понимаю причину. Обьясните пожалуйста)
#with open('5-3.txt', 'r', encoding='utf-8') as f:
    #sal = []
    #poor = []
    #new_list = f.read().split('\n')
    #for el in new_list:
        #el = el.split()
        #if int(el[1]) < 20000:
            #poor.append(el[0])
        #sal.append(el[1])
#print(f'Оклад меньше 20000 {poor}\nсредний оклад {sum(map(int, sal)) / len(sal)}')


# вариант из разбора дз
with open('5-3.txt','r', encoding='utf=8') as f:
    my_dict = {line.split()[0]: float(line.split()[1]) for line in f}
    print(f'Average salary = {round(sum(my_dict.values()) / len(my_dict), 3)}\n'
          f'Employees with salary less than 20k {[e[0] for e in my_dict.items() if e[1] < 20000]}')