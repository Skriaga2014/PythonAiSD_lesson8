'''
1. Определение количества различных подстрок с использованием хеш-функции.
Пусть дана строка S длиной N. Например, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.
Для решения задачи рекомендую воспользоваться алгоритмом sha1 из модуля hashlib или встроенную функцию hash()
'''

def rk(txt, podstr):
    len_txt = len(podstr)
    h_podstr = hash(podstr)
    count_podstr = 0
    for i in range(len(txt) - len_txt + 1):
        if h_podstr == hash(txt[i:i+len_txt]):
            count_podstr += 1
    return count_podstr

s = input('Введите строку: ')
itog = []
itog_num = 0
print(f'В строке "{s}":')
for i in range(len(s)):
    for j in range(1, len(s)):
        result = [s[i:i+j], rk(s, s[i:i+j])]
        if result not in itog:
            itog.append([s[i:i+j], rk(s, s[i:i+j])])
            itog_num += 1
            print(rk(s, s[i:i+j]), f'раз(а) встречается подстрока "{s[i:i+j]}"')


print(f'\nВариант 1: В строке "{s}" существует {itog_num} вариантов подстрок')
print(f'Вариант 2: В строке "{s}" существует {len(itog)} вариантов подстрок: {itog}')
