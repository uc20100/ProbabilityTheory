import numpy as np
from scipy import stats


# Задание 1
# Условие:  
# Провести дисперсионный анализ для определения того, 
# есть ли различия среднего роста среди взрослых футболистов, хоккеистов и штангистов. 
# Даны значения роста в трех группах случайно выбранных спортсменов:    
# Футболисты: 173, 175, 180, 178, 177, 185, 183, 182.  
# Хоккеисты: 177, 179, 180, 188, 177, 172, 171, 184, 180.  
# Штангисты: 172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170.
football_players = np.array([173, 175, 180, 178, 177, 185, 183, 182])
hockey_players = np.array([177, 179, 180, 188, 177, 172, 171, 184, 180])
weightlifters = np.array([172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170])

# тест на нормальное распределение, если pvalue>0.05 (5%), то распределение нормальное
sh_football_players = stats.shapiro(football_players)
print(sh_football_players)
sh_hockey_players = stats.shapiro(hockey_players)
print(sh_hockey_players)
sh_weightlifters = stats.shapiro(weightlifters)
print(sh_weightlifters)
# тест на однородность дисперсий, если pvalue>0.05 (5%), то дисперсии однородны
b = stats.bartlett(football_players,hockey_players,weightlifters)
print(b)
# однофакторный дисперсионный анализ, если pvalue>0.05 (5%), то различий нет
f = stats.f_oneway(football_players,hockey_players,weightlifters)
print(f)