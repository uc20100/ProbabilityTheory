from statistics import mean
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from math import sqrt

ROUND_NUMBER = 2

# Задание 1
# Даны значения величины заработной платы заемщиков банка (zp) и значения их поведенческого кредитного скоринга (ks):
# zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110],
# ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832].
# Найдите ковариацию этих двух величин с помощью элементарных действий, а затем с помощью функции cov из numpy
# Полученные значения должны быть равны.
# Найдите коэффициент корреляции Пирсона с помощью ковариации и среднеквадратичных отклонений двух признаков,
# а затем с использованием функций из библиотек numpy и pandas.
zp = np.asarray([35., 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.asarray([401., 574, 874, 919, 459, 739, 653, 902, 746, 832])
cov_zp_ks = mean(zp*ks)-mean(zp)*mean(ks)
print(f'Задание 1.1: Расчетная ковариация: {round(cov_zp_ks,ROUND_NUMBER)}')
print(f'Задание 1.1: numpy:                {np.cov(ks,zp, ddof=0)}')

cof_cor_pearson = cov_zp_ks/(np.std(zp, ddof=0)*np.std(ks, ddof=0))
print(f'Задание 1.2: Расчетный коэф-т корреляции Пирсона: {round(cof_cor_pearson,ROUND_NUMBER)}')
print(f'Задание 1.2: numpy:                {np.corrcoef(ks,zp)}')

df = pd.DataFrame({'zp': [35., 45, 190, 200, 40, 70, 54, 150, 120, 110],
 'ks': [401., 574, 874, 919, 459, 739, 653, 902, 746, 832]})
pandas_cof_cor_pearson = df['zp'].corr(df['ks'], method='pearson')
print(f'Задание 1.2: pandas:              {round(pandas_cof_cor_pearson, ROUND_NUMBER)}')

plt.scatter(df['zp'], df['ks'])
plt.title("Задание 1")
plt.xlabel('zp')
plt.ylabel('ks')
plt.show()



# Задание 2
# Измерены значения IQ выборки студентов,
# обучающихся в местных технических вузах:
# 131, 125, 115, 122, 131, 115, 107, 99, 125, 111.
# Известно, что в генеральной совокупности IQ распределен нормально.
# Найдите доверительный интервал для математического ожидания с надежностью 0.95.
iq = [131, 125, 115, 122, 131, 115, 107, 99, 125, 111]
iq_std = np.std(iq)
# print(f'Промежуточные данные iq_std: {round(iq_std,ROUND_NUMBER)}')
iq_mean = mean(iq)
# print(f'Промежуточные данные iq_mean: {round(iq_mean,ROUND_NUMBER)}')
t = stats.t.ppf(1-.05/2,len(iq)-1)
# print(f'Промежуточные данные t: {round(t,ROUND_NUMBER)}')
point_1 = iq_mean - t*iq_std/sqrt(len(iq))
point_2 = iq_mean + t*iq_std/sqrt(len(iq))
print(f'Задание 2: Доверительный интервал: [{round(point_1, ROUND_NUMBER)}; {round(point_2, ROUND_NUMBER)}]')



# Задание 3
# Известно, что рост футболистов в сборной распределен нормально
# с дисперсией генеральной совокупности, равной 25 кв.см. Объем выборки равен 27,
# среднее выборочное составляет 174.2. Найдите доверительный интервал для математического
# ожидания с надежностью 0.95.
lon_mean = 174.2
lon_std = sqrt(25)
lon_n = 27
z = stats.norm.ppf(1-.05/2)
# print(f'Промежуточные данные z: {round(z,ROUND_NUMBER)}')
dot_1 = lon_mean - z*lon_std/sqrt(lon_n)
dot_2 = lon_mean + z*lon_std/sqrt(lon_n)
print(f'Задание 3: Доверительный интервал: [{round(dot_1, ROUND_NUMBER)}; {round(dot_2, ROUND_NUMBER)}]')


