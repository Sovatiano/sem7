import copy
import numpy as np


payoff_matrix = [
    [5, -3, 6, -8, 7, 4],
    [7, 5, 5, -4, 8, 1],
    [1, 3, -1, 10, 0, 2],
    [9, -9, 7, 1, 3, -6]
]


def list_to_str(lst):
    return '  '.join(f'{x:>3}' for x in lst)


def bayes_laplace(matrix, probs=None):
    expectations = []
    variances = []
    risks = []
    if probs is None:
        print(f"===Критерий Байеса-Лапласа при равных вероятностях===")
        probs = [1/len(matrix[0])] * len(matrix[0])
    else:
        print(f"===Критерий Байеса-Лапласа при оценке Фишбейна===")

    best_stragedy = [None, None]
    for row in range(len(matrix)):
        exp = sum(a * p for a, p in zip(matrix[row], probs))
        expectations.append(exp)
        if best_stragedy[-1] is None or exp > best_stragedy[-1]:
            best_stragedy = [row, exp]
        variance = sum((a - exp) ** 2 * p for a, p in zip(matrix[row], probs))
        variances.append(variance)
        risks.append(np.sqrt(variance))
        print(f"A{row + 1}: {list_to_str(matrix[row])}; мат. ожидание: {round(exp, 3)}, риск: {round(risks[-1], 3)}")
    print(f"Лучшая стратегия: A{best_stragedy[0] + 1}: {list_to_str(matrix[best_stragedy[0]])} -> мат. ожидание = "
          f"{round(best_stragedy[1], 3)}, риск = {round(risks[best_stragedy[0]], 3)}")



def wald(matrix):
    minimums = {}
    print(f"===КРИТЕРИЙ ВАЛЬДА===")
    for row_ind in range(len(matrix)):
        minimums[row_ind + 1] = min(matrix[row_ind])
    best_stragedy = [None, None]
    for k, v in minimums.items():
        print(f"Стратегия А{k}: {list_to_str(matrix[k - 1])} -> min = {v}")
        if best_stragedy[-1] is None or v > best_stragedy[-1]:
            best_stragedy = [k, v]
    print(f"Лучшая стратегия: A{best_stragedy[0]}: {list_to_str(matrix[best_stragedy[0] - 1])} -> min = "
          f"{best_stragedy[1]}")


def savage(matrix):
    print(f"===КРИТЕРИЙ Сэвиджа===")
    row_num = len(matrix)
    col_num = len(matrix[0])
    mod_matrix = copy.deepcopy(matrix)
    mod_matrix.append([0 for _ in range(len(matrix[0]))])

    print("Максимумы по столбцам:")
    for col_ind in range(col_num):
        col_max = None
        for row_ind in range(row_num):
            elem = mod_matrix[row_ind][col_ind]
            if col_max is None or elem > col_max:
                col_max = elem
        mod_matrix[row_num][col_ind] = col_max
    for row in range(len(mod_matrix[:-1])):
        print(f"А{row + 1}:  {list_to_str(mod_matrix[row])}")
    print(f"max: {list_to_str(mod_matrix[-1])}")

    print("Матрица рисков:")
    risk_matrix = copy.deepcopy(matrix)
    best_stragedy = [None, None]
    for row in range(len(risk_matrix)):
        for col in range(col_num):
            risk_matrix[row][col] = mod_matrix[-1][col] - risk_matrix[row][col]
        if best_stragedy[-1] is None or max(risk_matrix[row]) < best_stragedy[-1]:
            best_stragedy = [row + 1, max(risk_matrix[row])]
    for row in range(len(risk_matrix)):
        print(f"А{row + 1}:  {list_to_str(risk_matrix[row])} -> max: {max(risk_matrix[row])}")
    print(f"Лучшая стратегия: A{best_stragedy[0]}: {list_to_str(matrix[best_stragedy[0] - 1])}")


def hurwitz(matrix, alpha):
    rows_mins_and_maxes = {}
    print(f"===Критерий Гурвица===")
    print(f"Минимумы и максимумы по строкам:")
    for row in range(len(matrix)):
        rows_mins_and_maxes[row] = [min(matrix[row]), max(matrix[row])]
        print(f"А{row + 1}: {list_to_str(matrix[row])}:   min -> {min(matrix[row])}, max -> {max(matrix[row])}")
    print("Значения Hi:")
    his = []
    row_num = 1
    best_stragedy = [None, None]
    for minn, maxx in rows_mins_and_maxes.values():
        his.append(round(alpha * minn + (1 - alpha) * maxx, 5))
        if best_stragedy[-1] is None or his[-1] > best_stragedy[-1]:
            best_stragedy = [row_num, his[-1]]
        row_num += 1
        print(f"A{row_num}: Hi = {his[-1]}")
    print(f"Лучшая стратегия: A{best_stragedy[0]}: {list_to_str(matrix[best_stragedy[0] - 1])}")


# bayes_laplace(payoff_matrix)
numerators = [2 * (len(payoff_matrix[0]) - i + 1) for i in range(1, len(payoff_matrix[0]) + 1)]
denominator = len(payoff_matrix[0]) * (len(payoff_matrix[0]) + 1)
prob_fishbein = [numerator / denominator for numerator in numerators]
# bayes_laplace(payoff_matrix, prob_fishbein)
# wald(payoff_matrix)
# savage(payoff_matrix)
hurwitz(payoff_matrix, 0.4)