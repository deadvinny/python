# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3

import math
s = int(input('Введите сумму чисел x и y: '))
p = int(input('Введите произведение чисел x и y: '))

x = (s - math.sqrt(s**2-4*p))//2
y = s - x

if x > 1000 or y > 1000:
    print("Ошибка. Одно из загаданных чисел больше 1000")
else:
    print(f"Загаданные числа {int(x)}, {int(y)}")