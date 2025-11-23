import numpy as np
import skfuzzy as fuzz
from skfuzzy import control
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Qt5Agg')

profit = fuzz.control.Antecedent(np.arange(10**5, 5*10**7, 10**5), 'Уровень финансовых вложений')
profit['Низкий'] = fuzz.gaussmf(profit.universe, 5*10**6, 5*10**6)
profit['Средний'] = fuzz.gaussmf(profit.universe, 2.5*10**7, 5*10**6)
profit['Высокий'] = fuzz.gaussmf(profit.universe, 4.5*10**7, 5*10**6)
# profit.view()

term = fuzz.control.Antecedent(np.arange(1, 30, 1/12), 'Срок окупаемости проекта')
term['Маленький'] = fuzz.trapmf(term.universe, (0, 3, 9, 12))
term['Средний'] = fuzz.trapmf(term.universe, (10, 13, 17, 20))
term['Большой'] = fuzz.trapmf(term.universe, (18, 21, 27, 30))
# term.view()

efficiency = fuzz.control.Consequent(np.arange(0, 1, 0.1), 'Степень эффективности вложения средств')
efficiency['Низкая'] = fuzz.trimf(efficiency.universe, [0, 0, 0.4])
efficiency['Средняя'] = fuzz.trimf(efficiency.universe, [0.3, 0.5, 0.7])
efficiency['Высокая'] = fuzz.trimf(efficiency.universe, [0.6, 1, 1])
efficiency.view()


rule1 = fuzz.control.Rule(profit['Низкий'] | term['Большой'], efficiency['Низкая'])
rule2 = fuzz.control.Rule(profit['Средний'] & term['Средний'], efficiency['Средняя'])
rule3 = fuzz.control.Rule(profit['Высокий'] & term['Маленький'], efficiency['Высокая'])


prob_ctrl = control.ControlSystem(rules=[rule1, rule2, rule3])
probbing = control.ControlSystemSimulation(prob_ctrl)

probbing.input['Уровень финансовых вложений'] = 3*10**7
probbing.input['Срок окупаемости проекта'] = 3

probbing.compute()

print(probbing.output['Степень эффективности вложения средств'])
efficiency.view(sim=probbing)
term.view()
profit.view()
plt.show()