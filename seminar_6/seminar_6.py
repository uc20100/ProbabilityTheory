from statistics import mean
from numpy import var, std
from scipy import stats
from math import sqrt

ROUND_NUMBER = 3

# Задание 2
# В результате 10 независимых измерений некоторой величины X, 
# выполненных с одинаковой точностью, получены опытные данные:  
# 6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1  
# Предполагая, что результаты измерений подчинены нормальному закону распределения вероятностей, 
# оценить истинное значение величины X при помощи доверительного интервала, 
# покрывающего это значение с доверительной вероятностью 0,95.
x = [6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1]
t = stats.t.ppf(0.975, len(x)-1) # задаем критерий Стьюдента
x_avg = mean(x)
x_std_n = std(x, ddof=1)
point_1 = x_avg-t*(x_std_n/sqrt(len(x)))
point_2 = x_avg+t*(x_std_n/sqrt(len(x)))
print(f'Задание 2: Доверительный интервал:[{round(point_1, ROUND_NUMBER)}; {round(point_2, ROUND_NUMBER)}]')


# Задание 3
# Рост дочерей 175, 167, 154, 174, 178, 148, 160, 167, 169, 170  
# Рост матерей 178, 165, 165, 173, 168, 155, 160, 164, 178, 175  
# Используя эти данные построить 95% доверительный интервал для разности среднего роста родителей и детей.
child = [175, 167, 154, 174, 178, 148, 160, 167, 169, 170]
mother = [178, 165, 165, 173, 168, 155, 160, 164, 178, 175]
delta = mean(mother) - mean(child)
# print('Задание 3: Промежуточные вычисления')
# print(f'delta={delta}, mother_m={mean(mother)}, child_m={mean(child)}')
dispersion = (var(mother, ddof=1) + var(child, ddof=1))/2
# print(f'dispersion_all={dispersion}, mother_d={var(mother, ddof=1)}, child_d={var(child, ddof=1)} ')
se = sqrt(dispersion/len(mother)+dispersion/len(child))
# print(f'se={se}')
t = stats.t.ppf(0.975, (len(mother)+len(child)-2)) # задаем критерий Стьюдента
# print(f't = {t}')
dot_1 = delta - t*se
dot_2 = delta + t*se
print(f'Задание 3: Доверительный интервал:[{round(dot_1, ROUND_NUMBER)}; {round(dot_2, ROUND_NUMBER)}]')
