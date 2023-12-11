# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class ChristmasTree:
    def __init__(self, height, decorations):

        """
                    Создание и подготовка к работе объекта "Рождественская Ель"

                    :param height: Высота елки
                    :param decorations: Массив украшений на елке

                    Примеры:
                     >>> tree = ChristmasTree(3, ['Звезда', 'Гирлянда'])  # инициализация экземпляра класса
         """

        self.height = height
        if not isinstance(height, (int, float)):
            raise TypeError("Высота елки должна быть типа int или float")
        if height <= 0:
            raise ValueError("Высота елки должна быть положительным числом")
        self.decorations = decorations

    def addDecoration(self, decoration: str) -> None:
        """
                Добавляет украшение на елку. Принимает аргумент decoration типа
                int, представляющий количество украшений, которые надо добавить на елку. 
                Метод не возвращает никакого значения.
                
                :param decoration: Украшение
                
                Примеры:
                >>> tree = ChristmasTree(5, 10)
                >>> tree.addDecoration("Звезда")
        """
        ...

    def removeDecoration(self, decoration: str) -> None:
        """
                Удаляет украшение с елки. Принимает аргумент decoration типа str, представляющий
                украшение, которое нужно удалить с елки.
                Метод не возвращает никакого значения.
                
                :param decoration: Украшение
                
                Примеры:
                
                >>> tree = ChristmasTree(5, 10)
                >>> tree.removeDecoration("Звезда")
        """
        ...

    def getCountOfDecorations(self) -> int:
        """
                Возвращает количество всех украшений на елке.
                Метод не принимает аргументов и возвращает число украшений.
                
                :return: Число украшений
                
                Примеры:
                
                >>> tree = ChristmasTree(5, ['Звезда', 'Гирлянда'])
                >>> tree.getCountOfDecorations()
        """
        ...


class Hand:
    def __init__(self, countOffingers, countOfRings):

        """
                            Создание и подготовка к работе объекта "Рука"

                            :param countOffingers: Количество пальцев
                            :param countOfRings: Количество колец

                            Примеры:
                             >>> hand = Hand(5, 2)  # инициализация экземпляра класса
        """

        self.countOffingers = countOffingers
        if countOffingers <= 0:
            raise ValueError("Количество пальцев должно быть положительным числом")
        self.countOfRings = countOfRings
        if countOfRings <= 0:
            raise ValueError("Количество колец должно быть положительным числом")

    def addRing(self, rings: int) -> None:
        """
                    Добавляет кольцо на палец руки.
                    Принимает аргумент rings типа int, представляющий количество колец, которые нужно добавить.
                    Метод не возвращает никакого значения.

                    :param rings: Кольцо

                    Примеры:
                >>> hand = Hand(5, 2)
                >>> hand.addRing(2)
            """
        ...

    def removeRing(self, rings: int) -> None:
        """
                    Удаляет кольцо с пальца руки.
                    Принимает аргумент rings типа int, представляющий количество колец, которые нужно удалить.
                    Метод не возвращает никакого значения.

                    :param rings: Кольца

                    Примеры:

                    >>> hand = Hand(5, 6)
                    >>> hand.removeRing(3)
            """
        ...

    def getCountOfRings(self) -> int:
        """
                    Возвращает количество колец.
                    Метод не принимает аргументов и возвращает число колец.

                    :return: Число колец

                    Примеры:

                    >>> hand = Hand(5, 10)
                    >>> hand.getCountOfRings()
            """
        ...


class Candle:
    def __init__(self, typeOfWick, sizeInMl):
        """
        :param typeOfWick: Тип фитиля свечи
        :param sizeInMl: Размер свечи в миллилитрах
        :raises TypeError: Если размер свечи не является типом int или float
        :raises ValueError: Если размер свечи меньше или равен нулю

        Примеры:

                >>> candle = Candle('деревянный', 100)

        """
        self.typeOfWick = typeOfWick
        self.sizeInMl = sizeInMl
        if not isinstance(sizeInMl, (int, float)):
            raise TypeError("Объем свечи должен быть типа int или float")
        if sizeInMl <= 0:
            raise ValueError("Объем свечи должен быть положительным числом")

    def burn(self, minutes: int) -> str:
        """

            Зажигает свечу и позволяет ей гореть заданное количество минут.

            :param minutes: Количество минут, на которое зажигается свеча
            :return: Сообщение о горении свечи

        """
        ...

    def extinguish(self) -> None:
        """
            Тушит горящую свечу.

            :return: None

        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
    pass
