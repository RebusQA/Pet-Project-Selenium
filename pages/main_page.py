
import allure
from selenium.webdriver.common.by import By
from base.base_class import Base

""" Создал класс Главной страницы """

class Main_page(Base):

    def __init__(self, driver):

        # Инициализация класса-родителя
        super().__init__(driver)
        self.driver = driver

    """ Locators """

    # Локаторы элементов страницы

    add_product_1 = "//button[@id='add-to-cart-sauce-labs-backpack']"
    cart = "//div[@id='shopping_cart_container']"


    """ Getters """

    # Получение элементов страницы
    def get_add_product_1(self):
        return self.driver.find_element(By.XPATH, self.add_product_1)
    def get_cart(self):
        return self.driver.find_element(By.XPATH, self.cart)

    """ Actions """

    # Действия с элементами страницы
    def click_add_product_1(self):
        # Нажатие на кнопку добавления товара в корзину
        self.get_add_product_1().click()
        print("Click button add to cart")

    def click_cart(self):
        # Нажатие на кнопку корзины и вход в неё
        self.get_cart().click()
        print("Click button cart")


    """ Methods """

    # Метод добавления товара в корзину
    def add_product(self):

        # Указываю что будет идти шаг Allure
        with allure.step("Add product"):
            # Получение текущей url в терминале
            self.get_current_url()
            # Добавление товара в корзину
            self.click_add_product_1()
            # Вход в корзину
            self.click_cart()