
"""
Этот блок кода представляет базовый класс Base с методом __init__,
который инициализирует объект базового класса и принимает аргумент driver типа WebDriver.
"""
import datetime

class Base():

    def __init__(self, driver):
        self.driver = driver


    """ Метод, который будет возвращать текущую url """

    def get_current_url(self):

        get_url = self.driver.current_url
        print("Current url is: " + get_url)


    """ Метод, который будет сверять элементы / парсить """

    def assert_word(self, word, result):

        value_word = word.text
        assert value_word == result
        print("Value word is ok")


    """ Метод, который будет парсить url """

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Final url is: " + get_url)


    """ Метод, который будет делать скрин конечной страницы """

    def get_screenshot(self):

        # Создание скриншота
        now_date = datetime.datetime.now().strftime("%Y.%m.%d-%H.%M.%S")
        name_screenshot = "screenshot " + now_date + ".png"
        # ./screen - точка указывает на текущий каталог, то есть система найдёт в этом проекте папку screen
        self.driver.save_screenshot(f"./screen/{name_screenshot}")
        print("Screenshot done")



