"""def longest_sequence(arr):
    n = len(arr)
    max_len = 1
    max_seq = [arr[0]]

    for i in range(n):
        current_seq_len = 1
        current_seq = [arr[i]]

        for j in range(i + 1, n):
            if arr[j] > current_seq[-1]:
                current_seq.append(arr[j])
                current_seq_len += 1
            else:
                break

        if current_seq_len > max_len:
            max_len = current_seq_len
            max_seq = current_seq

    return max_len, max_seq
import random
n = random.randint(10, 20) # случайное число от 10 до 20 включительно
arr = [random.randint(-100, 100) for i in range(n)] #генерируется массив из n чисел
max_len, max_seq = longest_sequence(arr)
print("Длина наибольшей возрастающей последовательности:", max_len)
print("Наибольшая возрастающая последовательность:", max_seq)
print("Исходный массив чисел:",arr)"""

"""def find_maximum_value(weights, values, k, m):
    n = len(weights)

    # Инициализируем двумерный массив нулями
    dp = [[0] * (k+1) for _ in range(m + 1)]

    # Заполняем матрицу с помощью динамического программирования
    for i in range(1, n + 1):
        for j in range(m, 0, -1):
            for l in range(k, 0, -1):
                # Если текущий вес экспоната меньше или равен текущему весу, и текущее количество заходов больше 0
                if weights[i-1] <= l and j > 0:
                    # Выбираем максимальную стоимость между текущей стоимостью и стоимостью, которую можно получить, если
                    # украсть данный экспонат, добавить его стоимость к максимальной стоимости, полученной для оставшегося веса,
                    # и вычесть из оставшегося количества заходов 1.
                    dp[j][l] = max(dp[j][l], dp[j-1][l-weights[i-1]] + values[i-1])

    # Извлекаем максимальную стоимость из матрицы
    max_value = dp[m][k]

    # Восстанавливаем наибольшую набранную сумму
    stolen_items = []
    j, l = m, k
    for i in range(n, 0, -1):
        if dp[j][l] != dp[j-1][l-weights[i-1]] + values[i-1]:
            continue
        stolen_items.append(i-1)
        j -= 1
        l -= weights[i-1]

    # Разворачиваем список с индексами в обратном порядке и возвращаем его вместе с максимальной стоимостью
    stolen_items.reverse()
    return max_value, stolen_items

weights = [3, 5, 2, 8, 1]
values = [7, 10, 4, 15, 2]
k = 7
m = 2

max_value, stolen_items = find_maximum_value(weights, values, k, m)

print("Максимальная стоимость:", max_value)
print("Индексы украденных экспонатов:", stolen_items)"""

# Переменная "n" обозначает количество экспонатов в музее.
#
# Переменная "k" обозначает максимальный вес, который вор может унести за один раз.
#
# Переменная "m" обозначает количество заходов, которые вор может сделать в музей.

"""def task_1():
    exhibits = {'Mona Lisa': '1 10', 'David': '20 15', 'Madonna': '1 7', 'Peacock': '10 20', 'Dance': '3 5',
                'Spring': '10 10', 'Eggs': '3 30', '1': '23 99', '2': '3 10',
                '3': '12 50', '4': '3 1', '5': '16 23', '6': '2 5'}  # exhibits: weight price
    while True:
        n = int(input(f'Input N (not more than {len(exhibits)}): '))
        if n <= len(exhibits):
            break
        else:
            print('Wrong input!')
    k = int(input('Input K: '))  # вес за один заход
    m = int(input('Input M: '))  # количество заходов
    weight = [1, 20, 1, 10, 3, 10, 3, 23, 3, 12, 3, 16, 2]
    price = [10, 15, 7, 20, 5, 10, 30, 99, 10, 50, 1, 23, 5]
    price_1kg = []
    for i in range(len(price)):
        price_1kg.append(round(price[i] / weight[i], 2))
    print(price_1kg)
    answer = []

    for i in range(m):
        print(i, 'заход')
        l = k
        weight_answer = []
        while True:
            print(l)
            max_value = max(price_1kg)  # берем максимальную стоимость 1 кг(самый ценный)
            max_index = price_1kg.index(max_value)  # определяем его индекс
            if weight[max_index] <= l:
                answer.append(price[max_index])
                l = l - weight[max_index]
                weight_answer.append(weight[max_index])
                weight.pop(max_index)
                price.pop(max_index)
                price_1kg.pop(max_index)
            else:
                break
        rasn = k - sum(weight_answer)
        print(rasn, 'разница')
        while rasn > min(weight):
            new_all = []
            for j in range(len(weight)):
                if weight[j] < rasn:
                    new_all.append(price_1kg[j])  # записываем стоимости 1 кг, которые еще можно добавить
            if new_all != '':
                answer.append(price[price_1kg.index(max(new_all))])
                weight_answer.append(weight[price_1kg.index(max(new_all))])
                rasn = rasn - weight[price_1kg.index(max(new_all))]
                weight.pop(price_1kg.index(max(new_all)))
                price.pop(price_1kg.index(max(new_all)))
                price_1kg.pop(price_1kg.index(max(new_all)))
        print(weight_answer)
    print(sum(answer), answer)
task_1()"""

def matrix(p):
    n = len(p) - 1
    our_matrix = [[float('inf') for i in range(n)] for j in range(n)]
    for i in range(n):
        our_matrix[i][i] = 0 #по диагонали ставим 0, так как матрицу на эту же матрицу умножать не нужно
    for w in range(2, n+1):
        for i in range(n-w+1):
            j = i + w - 1
            for k in range(i, j):#проходимся по всем возможным разбиениям на две подцепочки матриц
                our_matrix[i][j] = min(our_matrix[i][j], our_matrix[i][k] + our_matrix[k+1][j] + p[i]*p[k+1]*p[j+1])

    return our_matrix[0][n-1]
m = [5, 10, 15]
min_op = matrix(m)
print(min_op, 'скалярных действий')