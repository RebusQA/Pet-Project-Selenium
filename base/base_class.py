
"""
Этот блок кода представляет базовый класс Base с методом __init__,
который инициализирует объект базового класса и принимает аргумент driver типа WebDriver.
"""

class Base():

    def __init__(self, driver):
        self.driver = driver


    """ Метод, который будет возвращать текущую url """

    def get_current_url(self):

        get_url = self.driver.current_url
        print("Current url is: " + get_url)


    """ Метод, который будет проверять элементы - "слова" """

    def assert_word(self, word, result):

        value_word = word.text
        assert value_word == result
        print("Value word is ok")
