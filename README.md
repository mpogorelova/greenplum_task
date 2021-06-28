# Дружим GREENPLUM DB с SQLAlchemy
Это заняло у меня достаточно много времени, поэтому имеет
смысл описать всё по шагам.

#In a nutshell
1. Выполнила необходимые предустановки: установила VirtualBox и
Ubuntu 18.04
   
2. Установила Greenplum по инструкции с официального сайта
3. Настроила файл gpinitsystem_singlenode (в официальном гайде пропущен шаг, поэтому пришлось догадываться о создании файла 
   hostname_singlenode)
4. Стартанула кластер и создала стендовую БД (demo)
5. Установила PyCharm Pro (про версия это важно, только в ней есть поддержка Databases)
6. Поставила SQLAlchemy
7. Собственно написала сам скрипт в репозитории, который создаёт стендовый двухстраничный web, 
куда пользователь вводит данные "Клиент-Соглашение", которые далее заливаются в БД
   
8. Дальше - самое интересное. Установка модуля psycopg2, который ни в какую не хотел ставиться

:palm_tree: **ONE ETERNITY LATER...** :palm_tree:

В итоге после `pip install psycopg2` и всевозможных попыток понять, почему команда `pip` ВДРУГ перестала выполняться, получилось
успешно поставить модуль с уточнением версии)) `pip install psycorp2==2.4.5`


ТА-ДААМ!

Всё заработало, данные в web-приложении на localhost перестали исчезать
после рестарта

