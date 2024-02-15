class Person:
    #Базовый класс, описывающий человека.
    def __init__(self, name: str, age: int):
        """
        Инициализирует экземпляр класса Person.

        Args:
            name (str): Имя человека.
            age (int): Возраст человека.
        """
        self.name = name
        self.age = age

    def __str__(self):
        """
        Возвращает строковое представление экземпляра класса Person.

        Returns:
            str: Строковое представление экземпляра класса Person.
        """
        return f"{self.name} ({self.age} лет)"

    def __repr__(self):
        """
        Возвращает строковое представление объекта для отладочных целей.

        Returns:
            str: Строковое представление объекта для отладочных целей.
        """
        return f"Person(имя='{self.name}', возраст={self.age})"

    def is_adult(self):
        """
        Проверяет, является ли человек совершеннолетним.

        Returns:
            bool: True, если человек совершеннолетний, иначе False.
        """
        return self.age >= 18

    def get_name(self) -> str:
        """
        Возвращает имя человека.

        Returns:
            str: Имя человека.
        """
        return self.name

class Student(Person):
    """
    Дочерний класс, описывающий студента.
    """
    def __init__(self, name: str, age: int, course: str, grade: float):
        """
        Инициализирует экземпляр класса Student.

        Args:
            name (str): Имя студента.
            age (int): Возраст студента.
            course (str): Направление обучения студента.
            grade (float): Средний балл студента.
        """
        super().__init__(name, age)
        self.course = course
        self._grade = grade  # Непубличный атрибут

    def __str__(self):
        """
        Возвращает строковое представление экземпляра класса Student.

        Returns:
            str: Строковое представление экземпляра класса Student.
        """
        return f"{self.name} ({self.age} лет), направление {self.course}, оценка {self._grade}"

    def __repr__(self):
        """
        Возвращает строковое представление объекта для отладочных целей.

        Returns:
            str: Строковое представление объекта для отладочных целей.
        """
        return f"Студент(ка) (имя='{self.name}', возраст={self.age}, направление='{self.course}', оценка={self._grade})"

    # Переопределенный метод
    def is_adult(self):
        """
        Переопределенный метод, проверяющий, является ли студент совершеннолетним.

        Returns:
            bool: True, если студент совершеннолетний, иначе False.
        """
        return self.age >= 16

    def has_passed(self, threshold: float = 50.0) -> bool:
        """
        Проверяет, сдал ли студент экзамен с оценкой выше или равной порогу.

        Args:
            threshold (float): Порог оценки для сдачи экзамена. Значение по умолчанию равно 50.0.

        Returns:
            bool: True, если студент сдал экзамен, иначе False.
        """
        return self._grade >= threshold

if __name__ == '__main__':
    student = Student("Алина", 17, "ПМИ", 85.5)
    print(student)  # Алина (17 лет), course ПМИ, оценка 85.5

    print(repr(student))  # Student(ка) (имя='Алина', возраст=17, направление='ПМИ', оценка=85.5)

    # Проверка переопределенного метода is_adult
    print(student.is_adult())  # True

    # Оценка проверяется со стандартным 50.0
    print(student.has_passed())  # True

    # Оценка ниже заданного порога
    print(student.has_passed(90))  # False

    # Оценка выше заданного порога
    print(student.has_passed(80))  # True

    # Проверка наследования метода get_name
    print(student.get_name())  # Алина