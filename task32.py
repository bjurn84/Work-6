# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)


arr = [2, 5, 8, 1, 4] 
min_val = 3 
max_val = 6 
result = [] 
for i in range(len(arr)): 
    if arr[i] >= min_val and arr[i] <= max_val: 
        result.append(i) 
print(result)