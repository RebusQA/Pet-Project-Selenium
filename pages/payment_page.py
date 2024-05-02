
from selenium.webdriver.common.by import By
from base.base_class import Base

""" Создал класс страницы оплаты """

class Payment_page(Base):

    def __init__(self, driver):

        # Инициализация класса-родителя
        super().__init__(driver)
        self.driver = driver

    """ Locators """

    # Локаторы элементов страницы

    finish_button = "//button[@id='finish']"


    """ Getters """

    # Получение элементов страницы
    def get_finish_button(self):
        return self.driver.find_element(By.XPATH, self.finish_button)


    """ Actions """

    # Действия с элементами страницы
    def click_finish_button(self):
        # Нажатие на кнопку завершения покупки
        self.get_finish_button().click()
        print("Click finish button")


    """ Methods """

    # Метод завершения оплаты и нажатие на кнопку finish
    def payment(self):

        # Получение текущей url в терминале
        self.get_current_url()
        # Нажатие на кнопку finish
        self.click_finish_button()
