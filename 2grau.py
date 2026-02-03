import math
from dataclasses import dataclass
from typing import Tuple

import matplotlib.pyplot as plt


@dataclass
class QuadraticEquation:
    a: float
    b: float
    c: float

    def discriminant(self) -> float:
        return self.b ** 2 - 4 * self.a * self.c

    def roots(self) -> Tuple[complex, complex]:
        if self.a == 0:
            raise ValueError("O coeficiente 'a' não pode ser zero em uma equação do segundo grau.")
        delta = self.discriminant()
        if delta >= 0:
            sqrt_delta = math.sqrt(delta)
        else:
            sqrt_delta = complex(0, math.sqrt(-delta))
        x1 = (-self.b + sqrt_delta) / (2 * self.a)
        x2 = (-self.b - sqrt_delta) / (2 * self.a)
        return x1, x2

    def value_at(self, x: float) -> float:
        return self.a * x ** 2 + self.b * x + self.c


class QuadraticGrapher:
    def __init__(self, equation: QuadraticEquation) -> None:
        self.equation = equation

    def plot(self, x_min: float = -10, x_max: float = 10, points: int = 400) -> None:
        if points < 2:
            raise ValueError("O número de pontos deve ser pelo menos 2.")
        step = (x_max - x_min) / (points - 1)
        x_values = [x_min + i * step for i in range(points)]
        y_values = [self.equation.value_at(x) for x in x_values]

        plt.figure(figsize=(8, 5))
        plt.plot(x_values, y_values, label=f"y = {self.equation.a}x² + {self.equation.b}x + {self.equation.c}")
        plt.axhline(0, color="black", linewidth=0.8)
        plt.axvline(0, color="black", linewidth=0.8)
        plt.title("Gráfico da Equação do Segundo Grau")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.legend()
        plt.grid(True, linestyle="--", alpha=0.5)
        plt.show()


def main() -> None:
    print("Sistema de Equação do Segundo Grau")
    a = float(input("Informe o valor de a: "))
    b = float(input("Informe o valor de b: "))
    c = float(input("Informe o valor de c: "))

    equation = QuadraticEquation(a=a, b=b, c=c)
    try:
        roots = equation.roots()
        print(f"Raízes: {roots[0]} e {roots[1]}")
    except ValueError as exc:
        print(f"Erro: {exc}")
        return

    grapher = QuadraticGrapher(equation)
    grapher.plot()


if __name__ == "__main__":
    main()
