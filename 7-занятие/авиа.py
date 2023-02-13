# Стюардесса спрашивает, что входит в стоимость авиабилета 'A-380 Москва-Сидней', 1й класс: 5000$, 2й: 2750$, 3й: 1850$.
# Разбейте по классам: общий, в нем укажите общие свойства, ДАЛЬНОСТЬ, БАГАЖ, СТРАХОВКА, ПИТАНИЕ.
# Для каждого класса отдельные свойства придумайте, и унаследованные, назначьте стоимость всему и суммируйте в функции return
# --------------------------
# Atayev Akmuhammet
# Lab 7

class Avia:

    __plane = "A-300 Москва-Сидней"
    __flight_range = 14509

    def __init__(self, food, baggage, insurance):
        self.__food = food
        self.__baggage = baggage
        self.__insurance = insurance

    @property
    def plane(self):
        return self.__plane

    @property
    def flight_range(self):
        return self.__flight_range

    @property
    def food(self):
        return self.__food

    @food.setter
    def food(self, food):
        self.__food = food

    @property
    def baggage(self):
        return self.__baggage

    @baggage.setter
    def baggage(self, baggage):
        self.__baggage = baggage

    @property
    def insurance(self):
        return self.__insurance

    @insurance.setter
    def insurance(self, insurance):
        self.__insurance = insurance

    def info(self):
        print(f'Общая характеристика:\n'
            f'\tРейс: {self.__plane}\n'
            f'\tДальность: {self.__flight_range} км\n'
            f'\tМаксимальный груз: {self.__baggage}тонн\n'
            f'\tПитание: {self.__food}\n'
            f'\tСтраховки: {self.__insurance}\n-------')

a = Avia("завтрак/обед/ужин", 12, 'жизнь пассажира, здоровья, имущества')
a.info()

class Econom(Avia):
    def __init__(self, food, baggage, insurance, seat_pitch):
        super().__init__(food, baggage, insurance)
        self.__seat_pitch = seat_pitch
        self.__price = 1870

    @property
    def seat_pitch(self):
        return self.__seat_pitch

    @seat_pitch.setter
    def seat_pitch(self, seat_pitch):
        self.__seat_pitch = seat_pitch

    @property
    def price(self):
        return self.__price

    def info(self):
        print(f'Эконом класс:\n'
              f'\tПитание: {self.food}\n'
              f'\tБагаж: {self.baggage} кг\n'
              f'\tСтраховка: {self.insurance}\n'
              f'\tШаг кресел: {self.seat_pitch} см\n'
              f'Цена: {self.price}$\n-------')



econom = Econom('Легкие закуски', 23, 'здоровья', 81)
econom.info()

class Business(Econom):
    def __init__(self, food, baggage, insurance, seat_pitch, *args):
        super().__init__(food, baggage, insurance, seat_pitch)
        self.__args = args
        self.__price = 2750

    @property
    def services(self):
        return self.__args

    @services.setter
    def services(self, *services):
        self.__args = services

    @property
    def price(self):
        return self.__price

    def info(self):
        print(f'Бизнес класс:\n'
              f'\tПитание: {self.food}\n'
              f'\tБагаж: {self.baggage} кг\n'
              f'\tСтраховка: {self.insurance}\n'
              f'\tШаг кресел: {self.seat_pitch} см\n'
              f'\tДополнительные услуги: {self.services}\n'
              f'Цена: {self.price}$\n-------')

business = Business('завтрак/обед/ужин', 32, 'здоровья', 117, 'Выход USB и розетка', 'Премиум напитки')
business.info()

class First(Business):
    def __init__(self, baggage, insurance, seat_pitch, *args):
        super().__init__(baggage, insurance, seat_pitch, *args)
        self.__price = 5000

    @property
    def price(self):
        return self.__price

    def info(self):
        print(f'Первый класс:\n'
              f'\tПитание: {self.food}\n'
              f'\tБагаж: {self.baggage} кг\n'
              f'\tСтраховка: {self.insurance}\n'
              f'\tШаг кресел: {self.seat_pitch} см\n'
              f'\tДополнительные услуги: {self.services}\n'
              f'Цена: {self.price}$\n-------')

first = First('завтрак/обед/ужин', 50, 'жизнь пассажира, здоровья, имущества', 229,
              'видео по запросу спинке кресла', 'премиум алкоголь и напитки', 'выход USB и розетка', 'хороший WiFi')
first.info()