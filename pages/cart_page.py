
import allure
from selenium.webdriver.common.by import By
from base.base_class import Base

""" Создал класс страницы корзины """

class Cart_page(Base):

    """ Locators """

    checkout_button = "//button[@id='checkout']"


    """ Getters """

    def get_checkout_button(self):
        return self.driver.find_element(By.XPATH, self.checkout_button)


    """ Actions """

    def click_checkout_button(self):
        self.get_checkout_button().click()
        print("Click checkout button")


    """ Methods """

    def product_confirm(self):

        with allure.step("Product confirm"):
            self.get_current_url()
            self.click_checkout_button()