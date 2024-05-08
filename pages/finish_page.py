
import allure
from base.base_class import Base

""" Создал класс завершения покупки, где парсю по url  и делаю скриншот конечной страницы"""

class Finish_page(Base):

    """ Methods """

    def finish(self):

        with allure.step("Finish"):
            self.get_current_url()
            self.assert_url("https://www.saucedemo.com/checkout-complete.html")
            self.get_screenshot()