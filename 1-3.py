#3)Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

num = input('Введите число n - ')
n = int(num)
nn = int(num + num)
nnn = int(num + num + num)

print('Сумма n+nn+nnn = ', n + nn + nnn)