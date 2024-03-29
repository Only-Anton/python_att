# 1. В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. 
#Ваша задача перевести его в one hot вид.
#-------------------------------------------------------------------------------------------------------------

import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame(lst, columns=['whoAmI']) # все что выше дано изначально, но эту строчку пришлось переделать
#data.head()
pd.get_dummies(data['whoAmI']) # Посути весь код для промежуточной аттестации

#------------------------------------------------------------------------------------------------------------

# 2. Сможете ли вы это сделать без get_dummies?

#------------------------------------------------------------------------------------------------------------

# Поидее мы можем создать двумерный массив с 0 и 1 и его преобразовать в таблицу. Выходит тоже самое

import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
mat = []      # создали массив и заполняем его
for i in range(20): 
    if lst[i] == 'human':
        row = [1,0]
    else:
        row = [0,1]
    mat.append(row)  # Добавление строки в матрицу
data = pd.DataFrame(mat, columns=['human','robot'])
data.head()

#---------------------------------------------------------------------------------------------------

# еще как вариант, создать два списка из 0 и 1 и объединить их

import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)

rob = []
hum = []
for i in range(20): 
    if lst[i] == 'human':
        rob.append(0)
        hum.append(1)
    else:
        rob.append(1)
        hum.append(0)
h = pd.DataFrame(hum, columns=['human'])
r = pd.DataFrame(rob, columns=['robot'])
data = pd.concat([h, r], axis=1)
data.head()

