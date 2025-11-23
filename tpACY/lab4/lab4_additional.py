import matplotlib.pyplot as plt
import numpy as np

payoff_matrix = [
    [5, -3, 6, -8, 7, 4],
    [7, 5, 5, -4, 8, 1],
    [1, 3, -1, 10, 0, 2],
    [9, -9, 7, 1, 3, -6]
]


def bayes_laplace_criterion(matrix, probabilities=None):
    if probabilities is None:
        n = len(matrix[0])
        probabilities = [1 / n] * n

    expectations = []
    for strategy in matrix:
        expectation = sum(a * p for a, p in zip(strategy, probabilities))
        expectations.append(expectation)

    optimal_idx = np.argmax(expectations)
    return optimal_idx + 1, expectations


def dispersion_model(matrix, probabilities):
    expectations = []
    variances = []
    risks = []

    for strategy in matrix:
        expectation = sum(a * p for a, p in zip(strategy, probabilities))
        expectations.append(expectation)

        variance = sum((a - expectation) ** 2 * p for a, p in zip(strategy, probabilities))
        variances.append(variance)
        risks.append(np.sqrt(variance))

    return expectations, risks


def find_pareto_optimal(expectations, risks):
    n = len(expectations)
    pareto_optimal = []

    for i in range(n):
        dominated = False
        for j in range(n):
            if i != j:
                if (expectations[j] >= expectations[i] and risks[j] <= risks[i] and
                        (expectations[j] > expectations[i] or risks[j] < risks[i])):
                    dominated = True
                    break
        if not dominated:
            pareto_optimal.append(i)

    return pareto_optimal


def plot_pareto_front(expectations, risks, title):
    plt.figure(figsize=(10, 6))

    for i, (exp, risk) in enumerate(zip(expectations, risks)):
        plt.scatter(exp, risk, s=100, label=f'A{i + 1}')
        plt.annotate(f'A{i + 1}', (exp, risk), xytext=(5, 5), textcoords='offset points')

    pareto_idx = find_pareto_optimal(expectations, risks)
    pareto_exp = [expectations[i] for i in pareto_idx]
    pareto_risk = [risks[i] for i in pareto_idx]

    sorted_idx = np.argsort(pareto_exp)
    pareto_exp_sorted = [pareto_exp[i] for i in sorted_idx]
    pareto_risk_sorted = [pareto_risk[i] for i in sorted_idx]

    plt.plot(pareto_exp_sorted, pareto_risk_sorted, 'r--', alpha=0.7)

    plt.xlabel('Математическое ожидание выигрыша')
    plt.ylabel('Риск')
    plt.title(title)
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.show()


# Основные шаги выполнения:
def complete_analysis(payoff_matrix):
    n_states = len(payoff_matrix[0])

    prob_uniform = [1 / n_states] * n_states

    weights = list(range(n_states, 0, -1))
    total_weight = sum(weights)
    prob_fishbein = [w / total_weight for w in weights]

    exp1, risks1 = dispersion_model(payoff_matrix, prob_uniform)
    exp2, risks2 = dispersion_model(payoff_matrix, prob_fishbein)

    plot_pareto_front(exp1, risks1, "Парето-оптимальные решения (равномерное распределение)")
    plot_pareto_front(exp2, risks2, "Парето-оптимальные решения (распределение Фишбейна)")


complete_analysis(payoff_matrix)