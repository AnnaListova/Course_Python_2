import doctest # TODO Написать 3 класса с документацией и аннотацией типов

class Farm:
    def __init__(self, name: str, animals: int, area):
        """
        Создание и подготовка к работе объекта "Ферма, хозяйство"

        :param name: Название фермы
        :param animals: Количество животных на ферме
        :param area: Площадь хозяйства

        Примеры:
        >>> farm = Farm('Кроликовая ферма',200,800)
        """
        self.name = name
        self.animals = animals
        self.area = area

    def size_area(self):
        """
        Определяем площадь хозяйства
        :return: Площадь
        """
        if self.area == 0:
            return 'Нет хозяйства'
        elif self.area <= 1000:
            return 'Маленькая ферма'
        else:
            return 'Большая ферма'

    def sale(self,rabbits):
        """
        Продаем кроликов
        :param rabbits: Количество проданных кроликов
        :return: ValueError: Если количество проданных кроликов превышает количество кроликов на ферме

        Примеры:
        >>> farm = Farm('Кроликовая ферма',200,800)
        >>> farm.sale(100)
        """

        if rabbits < 0:
           raise ValueError("Кроликов не могут продать больше, чем есть на ферме")

class Concert:
    def __init__(self, performances: int, hall: int):
        """
        Создание и подготовка к работе объекта "Концерт"

        :param performances: Количество концертных номеров
        :param hall: Вместимость концертного зала

        Примеры:
        >>> concert = Concert(15,250)
        """
        if not isinstance(performances, int):
            raise TypeError("Концертных номеров нет")
        self.performances = performances
        if not isinstance(hall, int):
            raise TypeError("Никто не купил билеты")
        self.hall = hall

    def time(self, length):
        """
        Определяем длительность концерта
        :length: Длительность произведения
        :return: Длительность концерта

        Примеры:
        >>> concert = Concert(15,250)
        >>> length = 15 #минут на произведение
        """
        self.time = length * self.performances

    def size_hall(self):
        """
        Нужен большой зал для концерта или нет
        :return: Насколько большой нужен зал
        """
        if self.hall < 400:
            return 'Большой зал не нужен'
        else:
            return 'Надо искать зал побольше'

class Camera:
    def __init__(self,company: str,focal_length: int,price: int):
        """
        Создание и подготовка к работе объекта "Фотоаппарат"

        :param company: Какой марки фотоаппарат
        :param focal_length: Фокусное расстояние китового объектива
        :param price: Цена фотоаппарата

        Пример:
        >>> camera = Camera('Canon',55,33000)
        """
        if not isinstance(company, str):
            raise TypeError("Марка не выбрана")
        self.company = company
        if not isinstance(focal_length, int):
            raise TypeError("Фотоаппарат без китового объектива")
        self.focal_length = focal_length
        if not isinstance(price, int):
            raise TypeError("Необходимо ввести цену")
        self.price = price

    def lens(self):
        """
        Какой тип объектива
        :return: Тип объектива
        """
        if self.focal_length <= 55:
            return 'Длиннофокусный объектив'
        else:
            return 'Короткофокусный объектив'

    def accessories(self, price_acs: int):
        """
        Добавляем стоимость при покупке аксессуаров
        :param price_acs: стоимость аксессуаров
        :return: Стоимость фотоаппарата с аксессуарами
        """
        if not isinstance(price_acs, int):
            raise TypeError('Стоимость будет целым числом')

        self.price += price_acs

if __name__ == "__main__":
    doctest.testmod() # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
