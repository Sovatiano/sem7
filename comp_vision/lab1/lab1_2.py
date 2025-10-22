b = None
while b is None:
    try:
        b = float(input("Введите значение b: "))
    except ValueError:
        print("Недопустимое значение")
    else:
        if not(b < 1):
            print("Значение не входит в ОДЗ (b < 1)")
            b = None


def fill_matrix():
    matrix = [[0 for _ in range(5)] for _ in range(5)]
    max_elem = None
    max_elem_string = 0
    for i in range(1, 6):
        for j in range(1, 6):
            if i > 3:
                new_elem = i ** 2 + (i - j ** b) ** 0.5
            else:
                new_elem = (b - 0.375) * ((b - i) / (j + 5)) / (1 + i + j)
            matrix[i - 1][j - 1] = f"{new_elem:.3f}"
            if i == j:
                if max_elem is None or max_elem < new_elem:
                    max_elem = new_elem
                    max_elem_string = i
    return matrix, matrix[max_elem_string - 1], max_elem_string


matrix, matrix_string, max_string_ind = fill_matrix()
for _ in matrix:
    print(_)
print("="*30)
print(matrix_string, max_string_ind)

with open("result.txt", 'w') as f:
    f.write("Матрица:\n")
    for elem in matrix:
        f.write(" ".join(elem) + "\n")
    f.write("=" * 30 + "\n")
    f.write("Строка с наибольшим элементом главной диагонали:\n")
    f.write(" ".join(matrix_string) + "\nНомер строки: " + str(max_string_ind))
f.close()
