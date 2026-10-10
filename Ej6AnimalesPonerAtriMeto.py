class Animal:
    def __init__(self, edad: int, peso: float, especie: str):
        self._edad = edad
        self._peso = peso
        self._especie = especie

    # c. Método respirar() general
    def respirar(self):
        print(f"{self._especie} toma oxigeno para vivir.")

    # d. Método mover() general
    def mover(self):
        print(f"{self._especie} se mueve de un lugar a otro.")

    def mostrar_datos(self):
        print(f"Especie: {self._especie}, Edad: {self._edad} años, Peso: {self._peso} kg")


# a. Cada clase derivada tiene 2 atributos y 2 métodos propios
class Terrestre(Animal):
    def __init__(self, edad: int, peso: float, especie: str, num_patas: int, tipo_alimentacion: str):
        super().__init__(edad, peso, especie)
        self._num_patas = num_patas
        self._tipo_alimentacion = tipo_alimentacion

    def caminar(self):
        print(f"{self._especie} camina con sus {self._num_patas} patas.")

    def cazar_o_pastar(self):
        print(f"{self._especie} es {self._tipo_alimentacion} y busca su alimento en tierra.")

    def respirar(self):
        super().respirar()
        print("Respira con pulmones.")

    def mover(self):
        print(f"{self._especie} se desplaza caminando o corriendo sobre {self._num_patas} patas.")

    def mostrar_datos(self):
        super().mostrar_datos()
        print(f"Patas: {self._num_patas}, Alimentacion: {self._tipo_alimentacion}")


class Acuatico(Animal):
    def __init__(self, edad: int, peso: float, especie: str, tipo_agua: str, profundidad_maxima: float):
        super().__init__(edad, peso, especie)
        self._tipo_agua = tipo_agua
        self._profundidad_maxima = profundidad_maxima

    def nadar(self):
        print(f"{self._especie} nada en agua {self._tipo_agua}.")

    def bucear(self):
        print(f"{self._especie} puede sumergirse hasta {self._profundidad_maxima} m.")

    def respirar(self):
        super().respirar()
        print("Respira por branquias, tomando el oxigeno disuelto en el agua.")

    def mover(self):
        print(f"{self._especie} se desplaza nadando con aletas o movimientos ondulantes.")

    def mostrar_datos(self):
        super().mostrar_datos()
        print(f"Agua: {self._tipo_agua}, Profundidad maxima: {self._profundidad_maxima} m,")


class Aereo(Animal):
    def __init__(self, edad: int, peso: float, especie: str, envergadura: float, altitud_maxima: float):
        super().__init__(edad, peso, especie)
        self._envergadura = envergadura
        self._altitud_maxima = altitud_maxima

    def volar(self):
        print(f"{self._especie} vuela con alas de {self._envergadura} m de envergadura.")

    def aterrizar(self):
        print(f"{self._especie} desciende y aterriza suavemente.")

    def respirar(self):
        super().respirar()
        print("Respira con pulmones y sacos aereos, muy eficientes en altura.")

    def mover(self):
        print(f"{self._especie} se desplaza volando hasta {self._altitud_maxima} m de altura.")

    def mostrar_datos(self):
        super().mostrar_datos()
        print(f"Envergadura: {self._envergadura} m, Altitud máxima: {self._altitud_maxima} m")


# b. Instanciar un objeto de cada tipo y mostrar sus datos
if __name__ == "__main__":
    leon = Terrestre(5, 190.5, "Tigre", 4, "carnivoro")
    delfin = Acuatico(8, 150.0, "Delfin", "salada", 300)
    condor = Aereo(12, 11.5, "Condor", 3.2, 5500)

    animales = [leon, delfin, condor]

    print("=== Datos de los animales ===")
    for animal in animales:
        animal.mostrar_datos()
        print()

    print("=== Métodos propios ==")
    leon.caminar()
    leon.cazar_o_pastar()
    delfin.nadar()
    delfin.bucear()
    condor.volar()
    condor.aterrizar()

    print("\n=== Respirar (poli) ===")
    for animal in animales:
        animal.respirar()

    print("\n=== Mover (poli) ===")
    for animal in animales:
        animal.mover()