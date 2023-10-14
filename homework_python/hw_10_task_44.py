# Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца.
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?
#
# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst})
# data.head()


import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
lst_robot, lst_human = [],[]
random.shuffle(lst)
print(lst)
lst_robot = [1 if el == 'robot' else 0 for el in lst ]
lst_human = [1 if el == 'human' else 0 for el in lst ]
print(pd.DataFrame({'robot': lst_robot, 'human': lst_human}))