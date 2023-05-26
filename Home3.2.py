# #### 3.2[18]: Требуется найти в списке целых чисел самый близкий по величине элемент к заданному числу X. 
#  Пользователь вводит это число с клавиатуры, список можно считать заданным. 
# Введенное число не обязательно содержится в списке.

#     Примеры/Тесты:
#     Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 0
#     Output: 2
#     Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 9

numbers = [10, 5, 7, 3, 3, 2, 5, 7, 3, 8]
x = int(input("Введите X: "))

if x in numbers:  # если число уже есть в списке, то оно и будет ближайшим
    result = x
else: # ищем ближайшее  - closest
    closest = None
    difference = None
    for num in numbers:
        if closest == None or abs(num - x) < difference:
            closest = num
            difference = abs(num - x)
    result = closest

print(result)
