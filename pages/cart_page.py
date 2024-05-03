
import allure
from selenium.webdriver.common.by import By
from base.base_class import Base

""" Создал класс страницы корзины """

class Cart_page(Base):

    def __init__(self, driver):

        # Инициализация класса-родителя
        super().__init__(driver)
        self.driver = driver

    """ Locators """

    # Локаторы элементов страницы

    checkout_button = "//button[@id='checkout']"


    """ Getters """

    # Получение элементов страницы
    def get_checkout_button(self):
        return self.driver.find_element(By.XPATH, self.checkout_button)


    """ Actions """

    # Действия с элементами страницы
    def click_checkout_button(self):
        # Нажатие на кнопку checkout в корзине
        self.get_checkout_button().click()
        print("Click checkout button")



    """ Methods """

    # Метод нажатия на checkout
    def product_confirm(self):

        # Указываю что будет идти шаг Allure
        with allure.step("Product confirm"):
            # Получение текущей url в терминале
            self.get_current_url()
            # Нажатие на checkout в корзине
            self.click_checkout_button()