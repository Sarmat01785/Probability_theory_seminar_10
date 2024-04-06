"""
Задача:
Провести дисперсионный анализ для определения того, есть ли различия среднего роста среди взрослых футболистов, 
хоккеистов и штангистов. Даны значения роста в трех группах случайно выбранных спортсменов: 
Футболисты: 173, 175, 180, 178, 177, 185, 183, 182. Хоккеисты: 177, 179, 180, 188, 177, 172, 171, 184, 180. 
Штангисты: 172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170.
"""
from scipy import stats


footballers = [173, 175, 180, 178, 177, 185, 183, 182]
hockey_players = [177, 179, 180, 188, 177, 172, 171, 184, 180]
weightlifters = [172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170]

# Выполнение однофакторного ANOVA
f_value, p_value = stats.f_oneway(footballers, hockey_players, weightlifters)

print("F-значение:", f_value)
print("p-значение:", p_value)


if p_value < 0.05:
    print("Есть статистически значимые различия в среднем росте между группами.")
else:
    print("Нет статистически значимых различий в среднем росте между группами.")
