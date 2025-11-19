import numpy as np
import skfuzzy as fuzz
from skfuzzy import control
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Qt5Agg')

x_name = 'Степень эффективности вложения средств'
y_name = 'Качество выполненной работы'
z_name = 'Эффективность проекта'

x_var = fuzz.control.Antecedent(np.arange(0, 1, 10**-4), x_name)
x_var['Низкая'] = fuzz.gaussmf(x_var.universe, 0.2, 0.1)
x_var['Средняя'] = fuzz.gaussmf(x_var.universe, 0.5, 0.1)
x_var['Высокая'] = fuzz.gaussmf(x_var.universe, 0.8, 0.1)
# profit.view()

y_var = fuzz.control.Antecedent(np.arange(0, 1, 10**-4), y_name)
y_var['Низкое'] = fuzz.gaussmf(y_var.universe, 0.2, 0.1)
y_var['Среднее'] = fuzz.gaussmf(y_var.universe, 0.5, 0.1)
y_var['Высокое'] = fuzz.gaussmf(y_var.universe, 0.8, 0.1)
# term.view()

z_var = fuzz.control.Consequent(np.arange(0, 1, 0.1), z_name)
z_var['Низкое'] = fuzz.trimf(z_var.universe, [0, 0, 0.4])
z_var['Среднее'] = fuzz.trimf(z_var.universe, [0.3, 0.5, 0.7])
z_var['Высокое'] = fuzz.trimf(z_var.universe, [0.6, 1, 1])
z_var.view()

#
rule1 = fuzz.control.Rule(x_var['Низкая'] | y_var['Низкое'], z_var['Низкое'])
rule2 = fuzz.control.Rule(x_var['Средняя'] & y_var['Среднее'], z_var['Среднее'])
rule3 = fuzz.control.Rule(x_var['Высокая'] & y_var['Высокое'], z_var['Высокое'])


prob_ctrl = control.ControlSystem(rules=[rule1, rule2, rule3])
probbing = control.ControlSystemSimulation(prob_ctrl)

probbing.input[x_name] = 0.678
probbing.input[y_name] = 0.872

probbing.compute()

print(probbing.output[z_name])
z_var.view(sim=probbing)
y_var.view()
x_var.view()
plt.show()
