from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

ROUND_NUMBER = 5

# Задание 1
# Даны значения величины заработной платы заемщиков банка (zp) и 
# значения их поведенческого кредитного скоринга (ks):  
# zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110],  
# ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832].   
# Используя математические операции, посчитать коэффициенты линейной регрессии, 
# приняв за X заработную плату (то есть, zp - признак), 
# а за y - значения скорингового балла (то есть, ks - целевая переменная). 
# Произвести расчет как с использованием intercept, так и без.

zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

# модель линейной регрессии y = b1*x
zp_copy = zp.copy()
ks_copy = ks.copy()
zp_len = len(zp_copy)
zp_copy = zp_copy.reshape(-1,1)
ks_copy = ks_copy.reshape(-1,1)
b = np.dot(np.linalg.inv(np.dot(zp_copy.T,zp_copy)), zp_copy.T @ ks_copy)
b_not_intercept = b[0][0]
print(f'Задание 1.1, линейная регрессия без intercept:   y = x * {round(b[0][0],ROUND_NUMBER)}')
# модель линейной регрессии y = b0 + b1*x
zp_copy = np.hstack([np.ones((zp_len,1)),zp_copy])
b = np.dot(np.linalg.inv(np.dot(zp_copy.T,zp_copy)), zp_copy.T @ ks_copy)
print(f'Задание 1.2, линейная регрессия с intercept:     y = {round(b[0][0],ROUND_NUMBER)} + x * {round(b[1][0],ROUND_NUMBER)}')

# проверка
model = LinearRegression()
zp_proverka = zp.copy()
# транспонируем одномерный массив
zp_proverka=zp_proverka.reshape(-1,1)
# подбираем коэффициенты
regres = model.fit(zp_proverka,ks)
print(f'Задание 1, проверка вычислений:           intercep = {round(regres.intercept_,ROUND_NUMBER)}, b1 = {round(regres.coef_[0],ROUND_NUMBER)}')

# отрисовка графика
plt.scatter(zp,ks)
plt.plot(zp, b[0][0] + zp*b[1][0], label='y = b0 + x*b1')
plt.plot(zp, zp*b_not_intercept, label='y = x*b')
plt.title("Задание 1")
plt.xlabel('zp')
plt.ylabel('ks')
plt.legend()
plt.show()



# Задание 2
# Посчитать коэффициент линейной регрессии при заработной плате (zp), 
# используя градиентный спуск (без intercept).

def mse_(B1, x, y, n):
    return np.sum((B1*x-y)**2)/n

# расчет коэффициента методом градиентного спуска
# y = b1*x
alpha = 1e-6
b_gradient = 0.1
n = len(zp)
for i in range(2000):
    b_gradient -= alpha*(2/n)*np.sum((b_gradient*zp-ks)*zp)
    if i % 100 == 0:
        print(f'Задание 2 (y=b*x): iteration: {i}, b: {b_gradient}, mse: {mse_(b_gradient, zp, ks, len(zp))}')
# отрисовка графика
plt.scatter(zp,ks)
# plt.plot(zp, b[0][0] + zp*b[1][0], label='y = b0 + x*b1')
plt.plot(zp, zp*b_gradient, label='y = x*b')
plt.title("Задание 2")
plt.xlabel('zp')
plt.ylabel('ks')
plt.legend()
plt.show()



# Задание 3
# Произвести вычисления как в пункте 2, но с вычислением intercept. 
# Учесть, что изменение коэффициентов должно производиться на каждом шаге одновременно 
# (то есть изменение одного коэффициента не должно влиять на изменение другого во время одной итерации).
alpha = 1e-6
b_gradient = 0.01
n = len(zp)
b0 = np.mean(ks)-(np.mean(zp*ks)-np.mean(zp)*np.mean(ks))/(np.mean(zp**2)-np.mean(zp)**2)*np.mean(zp)
for i in range(2000):
    b_gradient -= alpha*np.sum((b0 + b_gradient*zp-ks)*zp)
    if i % 100 == 0:
        print(f'Задание 3 (y=b0+b1*x): iteration: {i}, b0: {b0}, b1: {b_gradient}, mse: {mse_(b_gradient, zp, ks, len(zp))}')
# отрисовка графика
plt.scatter(zp,ks)
# plt.plot(zp, b[0][0] + zp*b[1][0], label='y = b0 + x*b1')
plt.plot(zp, b0+zp*b_gradient, label='y = b0 + x*b')
plt.title("Задание 3")
plt.xlabel('zp')
plt.ylabel('ks')
plt.legend()
plt.show()

