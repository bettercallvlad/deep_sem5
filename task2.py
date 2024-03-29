# Самостоятельно сохраните в переменной строку текста.
# Создайте из строки словарь, где ключ - буква,
# а значение - код буквы. Напишите преобразование в одну строку.

text = 'Самостоятельно сохраните'
res = {}
for i in text:
    res[i] = ord(i)
print(res)
# решение в одну строку
res_new = {i: ord(i) for i in text}
print(res_new)

# Продолжаем развивать задачу 2.
# Возьмите словарь, который вы получили.
# Сохраните его итераторатор. Далее выведите первые 5
# пар ключ-значение, обращаясь к итератору, а не к словарю.

dict_iter = iter(res.items())
for _ in range(5):
    print(next(dict_iter))
