from math import factorial, e

def combinations(n, k): 
    """
    Функция выполняет подсчет сочетаний
    :param n: n различных элементов множества
    :param k: набор состоящий из k элементов
    :return : количество сочетаний
    """
    return factorial(n)/(factorial(k)*factorial(n-k))

def bernoulli(n, k, p):
    """
    Функция вычисляет вероятность по формуле Бернулли
    :param n: n различных элементов множества
    :param k: набор состоящий из k элементов
    :param p: заданная вероятность события
    :return : вычисленная вероятность по формуле Бернулли
    """
    return combinations(n, k)*p**k*(1-p)**(n-k)

def poisson(n, m, p):
    """
    Функция вычисляет вероятность по формуле Пуассона
    :param n: n различных элементов множества
    :param m: m элементов для которого вычисляется вероятность
    :param p: заданная вероятность события
    :return : вычисленная вероятность по формуле Пуассона
    """
    return ((n*p)**m)/factorial(m)*e**(-(n*p))

ROUNDING_SIZE = 2


# Задание 1
# Вероятность того, что стрелок попадет в мишень, выстрелив один раз, равна 0.8. 
# Стрелок выстрелил 100 раз. Найдите вероятность того, что стрелок попадет в цель ровно 85 раз.
print(f'Задание 1:   P = {round(bernoulli(100, 85, 0.8)*100,ROUNDING_SIZE)} %')

# Задание 2
# Вероятность того, что лампочка перегорит в течение первого дня эксплуатации, равна 0.0004. 
# В жилом комплексе после ремонта в один день включили 5000 новых лампочек. 
# Какова вероятность, что ни одна из них не перегорит в первый день? 
# Какова вероятность, что перегорят ровно две?
print(f'Задание 2.1: P = {round(poisson(5000, 0, 0.0004)*100,ROUNDING_SIZE)} %')
print(f'Задание 2.2: P = {round(poisson(5000, 2, 0.0004)*100,ROUNDING_SIZE)} %')

# Задание 3
# Монету подбросили 144 раза. Какова вероятность, что орел выпадет ровно 70 раз?
print(f'Задание 3:   P = {round(bernoulli(144, 70, 0.5)*100,ROUNDING_SIZE)} %')

# Задание 4
# В первом ящике находится 10 мячей, из которых 7 - белые. 
# Во втором ящике - 11 мячей, из которых 9 белых. 
# Из каждого ящика вытаскивают случайным образом по два мяча. 
# Какова вероятность того, что все мячи белые? 
# Какова вероятность того, что ровно два мяча белые? 
# Какова вероятность того, что хотя бы один мяч белый?
p_4 = combinations(7, 2)*combinations(9, 2)/(combinations(10, 2)*combinations(11, 2))
p_3 = (combinations(7, 1)*combinations(3, 1)*combinations(9, 2)*combinations(2, 0) + combinations(7, 2)*combinations(3, 0)*combinations(9, 1)*combinations(2, 1))/(combinations(10, 2)*combinations(11, 2))
print(f'Задание 4.1:   P = {round(p_4*100,ROUNDING_SIZE)} %')
p_2 = (combinations(7, 2)*combinations(3, 0)*combinations(9, 0)*combinations(2, 2) + combinations(7, 1)*combinations(3, 1)*combinations(9, 1)*combinations(2, 1) + combinations(7, 0)*combinations(3, 2)*combinations(9, 2)*combinations(2, 0))/(combinations(10, 2)*combinations(11, 2))
print(f'Задание 4.2:   P = {round(p_2*100,ROUNDING_SIZE)} %')
p_1 = (combinations(7, 1)*combinations(3, 1)*combinations(9, 0)*combinations(2, 2) + combinations(7, 0)*combinations(3, 2)*combinations(9, 1)*combinations(2, 1))/(combinations(10, 2)*combinations(11, 2))
print(f'Промежуточные данные: p_1={round(p_1*100,ROUNDING_SIZE)}%, p_2={round(p_2*100,ROUNDING_SIZE)}%, p_3={round(p_3*100,ROUNDING_SIZE)}%, p_4={round(p_4*100,ROUNDING_SIZE)}%')
print(f'Задание 4.3:   P = {round((p_1+p_2+p_3+p_4)*100,ROUNDING_SIZE)} %')
