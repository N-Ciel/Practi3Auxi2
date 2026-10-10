from abc import ABC, abstractmethod
import math
# a. Clase base abstracta
class Figura(ABC):
    def __init__(self, color: str):
        self._color = color  # atributo protegido

    @abstractmethod
    def obtenerArea(self) -> float:
        """Cada subclase debe implementar el cálculo de su area."""
        pass

    def getColor(self) -> str:
        return self._color

    def __str__(self):
        return f"{self.__class__.__name__} de color {self._color} - Area: {self.obtenerArea():.2f}"

# b. Subclases que sobrescriben obtenerArea()
class Cuadrado(Figura):
    def __init__(self, color: str, lado: int):
        super().__init__(color)
        self.__lado = lado  # atributo privado (-)

    def obtenerArea(self) -> float:
        return self.__lado ** 2

class Triangulo(Figura):
    def __init__(self, color: str, lado1: int, lado2: int, lado3: int):
        super().__init__(color)
        self.__lado1 = lado1
        self.__lado2 = lado2
        self.__lado3 = lado3

    def obtenerArea(self) -> float:
        # Fórmula de Herón
        s = (self.__lado1 + self.__lado2 + self.__lado3) / 2
        return math.sqrt(
            s * (s - self.__lado1) * (s - self.__lado2) * (s - self.__lado3)
        )

class Redondo(Figura):
    def __init__(self, color: str, radio: int):
        super().__init__(color)
        self.__radio = radio

    def obtenerArea(self) -> float:
        return math.pi * self.__radio ** 2

def color_de_mayor_area(cuadrado: Cuadrado, triangulo: Triangulo) -> str:
    """d. Devuelve el color de la figura con mayor area."""
    if cuadrado.obtenerArea() > triangulo.obtenerArea():
        return cuadrado.getColor()
    elif triangulo.obtenerArea() > cuadrado.obtenerArea():
        return triangulo.getColor()
    return "Ambas figuras tienen la misma area"

# c. Instanciar 2 objetos de cada subclase y mostrarlos
if __name__ == "__main__":
    cuadrado1 = Cuadrado("rojo", 4)
    cuadrado2 = Cuadrado("azul", 6)
    triangulo1 = Triangulo("verde", 3, 4, 5)
    triangulo2 = Triangulo("amarillo", 6, 8, 10)
    redondo1 = Redondo("negro", 2)
    redondo2 = Redondo("blanco", 5)
    figuras = [cuadrado1, cuadrado2, triangulo1, triangulo2, redondo1, redondo2]
    print("=== Figuras creadas ===")
    for figura in figuras:
        print(figura)
        
    # d. Comparar un Cuadrado y un Triángulo
    print("\n=== Comparacion Cuadrado vs Triangulo ===")
    print(f"Cuadrado ({cuadrado1.getColor()}): {cuadrado1.obtenerArea():.2f}")
    print(f"Triangulo ({triangulo1.getColor()}): {triangulo1.obtenerArea():.2f}")
    print("Color de la figura con mayor area:", color_de_mayor_area(cuadrado1, triangulo1))