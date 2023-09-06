# Задача 3.1.
# Создайте класс матрицы (или таблицы).
# Требования к классу:
#   - каждая колонка является числом от 1 до n (n любое число, которые вы поставите!)
#   - в каждой ячейке содержится либо число, либо None
#   - доступы следующие методы матрицы:
#       * принимать новые значения, 
#       * заменять существующие значения, 
#       * выводить число строк и колонок.

# Пример матрицы 10 на 10 из единиц:
# [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# Примечание! 
#   - новый класс не запрещено строить на базе существующих типов данных: списков, словарей и тд.
#   - отображать в таблице/матрице название колонки не обязательно!
#   - использовать готовые классы numpy.array() и pandas.DataFrame() запрещено!
#   - проявите фантазию :)

class Matrica():

    def __init__(self) -> None:
        self.a = 0
        self.b = 0
        return

    def Input_Matrica(self):
        self.a = int(input('Число строк='))
        self.b = int(input('Число колонок='))
        self.arr = [[[] for i in range(self.b)] for j in range(self.a)]

        for i in range(self.a):
            for j in range(self.b):
                print('X(', i, ',', j, ')=', end='')
                self.arr[i][j] = input('?')
        return

    def Print_Matrica(self, Text):
        print(Text)
        for i in range(self.a):
            print(self.arr[i])
        return

    def Change_Matrica(self):
        i = int(input('Введите номер строки:'))
        j = int(input('Введите номер колонки:'))
        NewXij = input('Введите новое значение=')
        self.arr[i - 1][j - 1] = NewXij
        return

    def RowsColumns(self):
        print('Матрица содержит:')
        print('Строк:', self.a, '\nКолонок:', self.b)
        return


c = Matrica()
c.Input_Matrica()
c.Print_Matrica('Новая матрица:')
c.Change_Matrica()
c.Print_Matrica('Изменённая матрица:')
c.RowsColumns()