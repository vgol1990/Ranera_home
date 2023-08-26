# Задача 2.3.

# Напишите функцию, которая принимает цифры от 0 до 9 и возвращает значение прописью.
# Например,
# switch_it_up(1) -> 'One'
# switch_it_up(3) -> 'Three'
# switch_it_up(10000) -> None
# Использовать условный оператор if-elif-else нельзя!

def switch_it_up(number):
    try:
        Numbers = {1: 'один',
                   2: 'два',
                   3: 'три',
                   4: 'четыри',
                   5: 'пять',
                   6: 'шесть',
                   7: 'семь',
                   8: 'восемь',
                   9: 'девять',
                   0: 'нуль'
                    }
        return Numbers[number]
    except:
        return ('None')

Number = int(input('Введите цифру от 0 по 9 :'))
print('Вы ввели цифру:', switch_it_up(Number))