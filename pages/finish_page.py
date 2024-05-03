
import allure
from base.base_class import Base

""" Создал класс завершения покупки, где парсю по url  и делаю скриншот конечной страницы"""

class Finish_page(Base):

    def __init__(self, driver):

        # Инициализация класса-родителя
        super().__init__(driver)
        self.driver = driver


    """ Methods """

    # Метод завершения оплаты и получение скриншота
    def finish(self):

        # Указываю что будет идти шаг Allure
        with allure.step("Finish"):
            # Получение текущей url в терминале
            self.get_current_url()
            # Сверяю url
            self.assert_url("https://www.saucedemo.com/checkout-complete.html")
            # Получение скриншота
            self.get_screenshot()