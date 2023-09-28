"""SINGLETON"""


class PlanetEarth:
    """
    Создаем атрибут класса который проверяет есть ли уже экземпляр данного класса или нет
    """
    __instance = None

    def __new__(cls, *args, **kwargs):
        """
        Магический метод для создания экземпляра класса
        Если атрибут __instance имеет значение NONE
        """
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __del__(self):
        """
        Магический метод, который возвращает атрибуту __instance значение None,
        если объект будет удален сборщиком мусора
        """
        PlanetEarth.__instance = None

    def __init__(self):
        """
        Параметры замели
        """
        self.__square = 510072000 ** 2
        self.__mass = (5.97 * 10) ** 24
        self.__averagetemperature = 14.8

    def square(self):
        return f"Площадь земли: {self.__square}"

    def mass(self):
        return f"Масса земли: {self.__mass}"

    def averagetemperature(self):
        return f"Средняя температура по цельсию: {self.__averagetemperature}"


if __name__ == '__main__':
    p = PlanetEarth()
    p2 = PlanetEarth()
    print(id(p))
    print(id(p2))



