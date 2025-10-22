import math as m
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk

a = 1.35
l_border = -2
r_border = 4
h = 0.5


def P(x):
    v = count_v(x)
    return min(x, a) * m.log(v) / (abs(v - 4) ** (1 / 5))


def count_v(x):
    if x <= 0.1:
        return (x + 2) ** (1 / 3) + m.sin(x) ** 2
    elif x < 2:
        return a * x / (x ** 2 + 0.32)
    else:
        return (m.atan(a * x / 2)) ** 2


def plot_function():
    x_values = []
    y_values = []

    x = l_border
    while x <= r_border:
        y = P(x)
        x_values.append(x)
        y_values.append(y)
        x += h

    plt.figure(figsize=(10, 6))
    plt.plot(x_values, y_values, 'b-', linewidth=2, marker='o', markersize=4)
    plt.title('График функции P(x)')
    plt.xlabel('x')
    plt.ylabel('P(x)')
    plt.grid(True, alpha=0.3)
    plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
    plt.axvline(x=0, color='k', linestyle='-', alpha=0.3)
    plt.tight_layout()
    plt.show()


def create_table():
    table_window = tk.Tk()
    table_window.title("Таблица значений функции P(x). Савостьянов АА-22-07")
    table_window.geometry("800x600")

    style = ttk.Style()
    style.configure("Custom.Treeview", font=("Arial", 12))
    style.configure("Custom.Treeview.Heading", font=("Arial", 12, "bold"))

    frame = ttk.Frame(table_window)
    frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    columns = ("x", "v(x)", "P(x)")
    tree = ttk.Treeview(frame, columns=columns, show="headings", height=20, style="Custom.Treeview")

    tree.heading("x", text="x")
    tree.heading("v(x)", text="v(x)")
    tree.heading("P(x)", text="P(x)")

    tree.column("x", width=100, anchor=tk.CENTER)
    tree.column("v(x)", width=200, anchor=tk.CENTER)
    tree.column("P(x)", width=200, anchor=tk.CENTER)
    scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    x = l_border
    while x <= r_border:
        v_val = count_v(x)
        p_val = P(x)
        tree.insert("", tk.END, values=(f"{x:.2f}", f"{v_val:.6f}", f"{p_val:.6f}"))

        x += h

    info_label = tk.Label(table_window,
                          text=f"Параметры: a = {a}, интервал: [{l_border}, {r_border}], шаг: {h}",
                          font=("Arial", 12),
                          pady=10)
    info_label.pack()

    close_button = tk.Button(table_window, text="Закрыть", command=table_window.destroy)
    close_button.pack(pady=10)

    table_window.mainloop()


plot_function()
create_table()