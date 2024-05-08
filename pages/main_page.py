
import allure
from selenium.webdriver.common.by import By
from base.base_class import Base

""" Создал класс Главной страницы """

class Main_page(Base):

    """ Locators """

    add_product_1 = "//button[@id='add-to-cart-sauce-labs-backpack']"
    cart = "//div[@id='shopping_cart_container']"


    """ Getters """

    def get_add_product_1(self):
        return self.driver.find_element(By.XPATH, self.add_product_1)
    def get_cart(self):
        return self.driver.find_element(By.XPATH, self.cart)

    """ Actions """

    def click_add_product_1(self):
        self.get_add_product_1().click()
        print("Click button add to cart")

    def click_cart(self):
        self.get_cart().click()
        print("Click button cart")


    """ Methods """

    def add_product(self):

        with allure.step("Add product"):
            self.get_current_url()
            self.click_add_product_1()
            self.click_cart()