# Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции sorted, max и min использовать нельзя!

def minimum(arr):
    min_numb = arr[0]
    for numb in arr:
        if numb < min_numb:
            min_numb = numb
    return min_numb

def maximum(arr):
    max_numb = arr[0]
    for numb in arr:
        if numb > max_numb:
            max_numb = numb
    return max_numb

arr = [4,6,2,1,9,63,-134,566]
print(f"max = {maximum(arr)}, min = {minimum(arr)}")

arr = [-52, 56, 30, 29, -54, 0, -110]
print(f"max = {maximum(arr)}, min = {minimum(arr)}")

arr = [42, 54, 65, 87, 0]
print(f"max = {maximum(arr)}, min = {minimum(arr)}")

arr = [5]
print(f"max = {maximum(arr)}, min = {minimum(arr)}")


