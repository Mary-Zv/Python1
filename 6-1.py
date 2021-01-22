#1.Создать класс TrafficLight (светофор).
#●	определить у него один атрибут color (цвет) и метод running (запуск);
#●	атрибут реализовать как приватный;
#●	в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
#●	продолжительность первого состояния (красный) составляет 7 секунд,
# второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
#●	переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
#●	проверить работу примера, создав экземпляр и вызвав описанный метод.

#Задачу можно усложнить, реализовав проверку порядка режимов.
# При его нарушении выводить соответствующее сообщение и завершать скрипт.

from time import sleep

class TrafficLight:

   __color = ['Red', 'Yellow', 'Green']

   def running(self):
       el = 0
       while el != 3:
           print(TrafficLight.__color[el])
           if el == 0:
               sleep(7)
           elif el == 1:
               sleep(2)
           elif el == 5:
               sleep(5)
           el += 1

tl = TrafficLight()
tl.running()


