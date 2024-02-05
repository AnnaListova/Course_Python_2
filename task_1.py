class Clock:
    """ Базовый класс чай. """

    def __init__(self, type: str, material: str, price: float):
        """
        Создание и подготовка к работе объекта "Часы"
        :param type: Тип (вид) часов
        :param material: материал, из которого изготовлены часы
        :param price: Цена часов
        """
        self.Type = type
        self.material = material
        self.Price = price

    @property
    def type(self) -> str:
        """Возвращает вид часов. Не позволяет изменять атрибут"""
        return self.Type

    @property
    def price(self) -> float:
        """Возвращает цену за часы. Не позволяет изменять атрибут"""
        return self.Price

    @price.setter
    def price(self, price: float) -> None:
        """Устанавливает цену, накладывает ограничения по типу и допустимым значениям."""
        if not isinstance(price, float):
            raise TypeError("Цена часов должна быть типа float")
        if price <= 0:
            raise ValueError("Цена часов должна быть положительным числом")
        self.Price = price

    def __str__(self):
        """
        Функция. которая возвращает строку формата, где "Тип", "Материал" и "Цена" берутся с помощью
        атрибутов type, material и price
        :return: Строка с типом, материалом и ценой часов с помощью атрибутов type, material и price
        """
        return f"Вид {self.Type}. Материал {self.material}. Цена {self.Price}"

    def __repr__(self):
        """
        Функция. которая возвращает валидную python строку, по которой можно инициализировать точно такой же экземпляр
        :return: Валидная python строка
        """
        return f"{self.__class__.__name__}(country={self.Type!r}, kind_of_tea={self.material!r}, \
        price={self.Price!r})"

    def mech(self) -> None:
        """
        Функция, которая проверяет, что часы механические
        :raise ValueError: Если часы не механические, то вызываем ошибку
        """
        ...

    def buying_clock(self, money: float) -> None:
        """
        Функция, которая проверяет возможность покупателя приобрести часы
        :param money: Количество денег у покупателя
        :raise ValueError: Если цена за часы превышает количество денег у покупателя, то вызываем ошибку
        """
        if not isinstance(money, (int, float)):
            raise TypeError("Количество денег у покупателя должно быть типа int или float")
        if money <= 0:
            raise ValueError("Количество денег у покупателя должно быть положительным числом")

class Watch(Clock):
    """ Дочерний класс часов. Наручные часы."""

    def __init__(self, type: str, material: str, price: float, dial: int):
        """
        Создание и подготовка к работе объекта "Наручные часы"
        :param type: Вид (тип) часов
        :param material: материал, из которого изготовлены часы
        :param price: Цена часов
        :param dial: Циферблат (12  или 24-х часовой)
        """
        super().__init__(type, material, price)
        self.Dial = dial

    @property
    def dial(self) -> int:
        """Возвращает количество чосов на циферблате."""
        return self.Dial

    @dial.setter
    def dial(self, dial: int) -> None:
        """Устанавливает количество часов на циферблате, накладывает ограничения по типу и допустимым значениям."""
        if not isinstance(dial, int):
            raise TypeError("Количество часов должно быть типа int")
        if dial <= 0:
            raise ValueError("Количество часов должно быть положительным числом")
        self.Dial = dial

    def __repr__(self):
        """
        Функция. которая возвращает валидную python строку, по которой можно инициализировать точно такой же экземпляр.
        Перегружаем метод, так как появился новый атрибут
        :return: Валидная python строка
        """
        return f"{self.__class__.__name__}(type={self.Type!r}, material={self.material!r}, \
        price={self.Price!r}, dial={self.Dial!r})"

class Wall_clock(Clock):
    """ Дочерний класс часов. Настенные часы. """

    def __init__(self, type: str, material: str, price: float, noise: float):
        """
        Создание и подготовка к работе объекта "Чай в пакетиках"
        :param type: Вид (тип) часов
        :param material: материал, из которого изготовлены часы
        :param price: Цена часов
        :param noise: Шум в децибелах, который издают настенные часы
        """
        super().__init__(type, material, price)
        self.Noise = noise

    @property
    def noise(self) -> float:
        """Возвращает величину децибел."""
        return self.Noise

    @noise.setter
    def noise(self, noise: float) -> None:
        """Устанавливает количество грамм чая, накладывает ограничения по типу и допустимым значениям."""
        if not isinstance(noise, float):
            raise TypeError("Величина децибел должна быть типа float")
        if noise <= 0:
            raise ValueError("Величина децибел должна быть положительным числом")
        self.Noise = noise

    def __repr__(self):
        """
        Функция. которая возвращает валидную python строку, по которой можно инициализировать точно такой же экземпляр.
        Перегружаем метод, так как появился новый атрибут
        :return: Валидная python строка
        """
        return f"{self.__class__.__name__}(type={self.Type!r}, material={self.material!r}, \
        price={self.Price!r}, noise={self.Noise!r})"

    def alarm(self, standard: float) -> None:
        """
        Функция, которая проверяет превышение шума часов в комнате.
        Перегружаем метод, так как нужно пересчитать величину децибел.
        :param standard: Величина шума норма
        :raise ValueError: Если шум превышает норму, то вызываем ошибку
        """
        if not isinstance(standard, float):
            raise TypeError("Величина децибел должна быть типа float")
        if standard <= 0:
            raise ValueError("Величина децибел должна быть положительным числом")
        ...

if __name__ == "__main__":
    print(Clock("Механические", "Сталь", 10000))
    print(Watch("Механические", "Пластик", 5000, 12))
    print(Wall_clock("Механические", "Сталь", 15100, 50))
    # Write your solution here
    pass
