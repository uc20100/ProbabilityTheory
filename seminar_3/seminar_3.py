from math import factorial, e
from statistics import mean
from numpy import var, std

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

def unbiased_dispersion(data: list):
    """
    Функция вычисляет несмещенную дисперсию
    :param data: список входных значений
    :return : вычисленное значение несмещенной дисперсии
    """
    result_value = 0
    average_value = sum(data)/len(data)
    for val in salary: 
        result_value += (val-average_value)**2
    return result_value/(len(data)-1)
    
def shifted_dispersion(data: list):
    """
    Функция вычисляет смещенную дисперсию
    :param data: список входных значений
    :return : вычисленное значение смещенной дисперсии
    """
    result_value = 0
    average_value = sum(data)/len(data)
    for val in salary: 
        result_value += (val-average_value)**2
    return result_value/len(data)


ROUNDING_SIZE = 2


# Задание 1
# Даны значения зарплат из выборки выпускников: 100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150. 
# Посчитать (желательно без использования статистических методов наподобие std, var, mean) 
# среднее арифметическое, среднее квадратичное отклонение, смещенную и несмещенную оценки дисперсий для данной выборки.
salary =[100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150]
average_value = sum(salary)/len(salary)
print(f'Задание 1:              среднее арифметическое = {round(average_value,ROUNDING_SIZE)}, несмещенная дисперсия = {round(unbiased_dispersion(salary),ROUNDING_SIZE)}, смещенная дисперсия = {round(shifted_dispersion(salary),ROUNDING_SIZE)}, среднее квадратичное отклонение = {round(shifted_dispersion(salary)**0.5,ROUNDING_SIZE)}')
print(f'Задание 1 (проверка):   среднее арифметическое = {round(mean(salary),ROUNDING_SIZE)}, несмещенная дисперсия = {round(var(salary,ddof=1),ROUNDING_SIZE)}, смещенная дисперсия = {round(var(salary),ROUNDING_SIZE)}, среднее квадратичное отклонение = {round(std(salary),ROUNDING_SIZE)}')

# Задание 2
# В первом ящике находится 8 мячей, из которых 5 - белые. 
# Во втором ящике - 12 мячей, из которых 5 белых. 
# Из первого ящика вытаскивают случайным образом два мяча, из второго - 4. 
# Какова вероятность того, что 3 мяча белые?
p = (combinations(5, 2)*combinations(3, 0)*combinations(5, 1)*combinations(7, 3) + 
     combinations(5, 1)*combinations(3, 1)*combinations(5, 2)*combinations(7, 2) + 
     combinations(5, 0)*combinations(3, 2)*combinations(5, 3)*combinations(7, 1)) / (combinations(8, 2)*combinations(12, 4))
print(f'Задание 2:   P = {round(p*100,ROUNDING_SIZE)} %')

# Задание 3
# На соревновании по биатлону один из трех спортсменов стреляет и попадает в мишень. 
# Вероятность попадания для первого спортсмена равна 0.9, для второго — 0.8, для третьего — 0.6. 
# Найти вероятность того, что выстрел произведен: 
# a). первым спортсменом 
# б). вторым спортсменом 
# в). третьим спортсменом
p = 1/3
p_1 = 0.9
p_2 = 0.8
p_3 = 0.6
p_first = p*p_1/(p*(p_1+p_2+p_3))
p_second = p*p_2/(p*(p_1+p_2+p_3))
p_third = p*p_3/(p*(p_1+p_2+p_3))
print(f'Задание 3:   P1 = {round(p_first*100,ROUNDING_SIZE)} %, P2 = {round(p_second*100,ROUNDING_SIZE)} %, P3 = {round(p_third*100,ROUNDING_SIZE)} %')

# Задание 4
# В университет на факультеты A и B поступило равное количество студентов, 
# а на факультет C студентов поступило столько же, сколько на A и B вместе. 
# Вероятность того, что студент факультета A сдаст первую сессию, равна 0.8. 
# Для студента факультета B эта вероятность равна 0.7, а для студента факультета C - 0.9. 
# Студент сдал первую сессию. Какова вероятность, что он учится: 
# a). на факультете A 
# б). на факультете B 
# в). на факультете C? 
p = 1/4
p_a = 0.8
p_b = 0.7
p_c = 0.9
a = p*p_a/(p*(p_a+p_b+2*p_c))
b = p*p_b/(p*(p_a+p_b+2*p_c))
c = p*2*p_c/(p*(p_a+p_b+2*p_c))
print(f'Задание 4: На факультете А  P={round(a*100,ROUNDING_SIZE)}%, На факультете В  P={round(b*100,ROUNDING_SIZE)}%, На факультете С  P={round(c*100,ROUNDING_SIZE)}%')

# Задание 5
# Устройство состоит из трех деталей. 
# Для первой детали вероятность выйти из строя в первый месяц равна 0.1, 
# для второй - 0.2, для третьей - 0.25. 
# Какова вероятность того, что в первый месяц выйдут из строя: 
# а). все детали 
# б). только две детали 
# в). хотя бы одна деталь 
# г). от одной до двух деталей?
p_1 = 0.1
p_2 = 0.2
p_3 = 0.25
p_all = p_1*p_2*p_3
p_single = p_1 + p_2 + p_3
p_two = p_1*p_2 + p_1*p_3 + p_3*p_2
p_1_2 = p_single + p_two
p_1_3 = p_all + p_single + p_two
print(f'Задание 5: Все: {round(p_all*100,ROUNDING_SIZE)}%, одна: {round(p_single*100,ROUNDING_SIZE)}%, две: {round(p_two*100,ROUNDING_SIZE)}%, от 1-2: {round(p_1_2*100,ROUNDING_SIZE)}%, хотя бы одна: {round(p_1_3*100,ROUNDING_SIZE)}%')
