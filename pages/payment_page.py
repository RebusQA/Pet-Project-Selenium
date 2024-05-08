
import allure
from selenium.webdriver.common.by import By
from base.base_class import Base

""" Создал класс страницы оплаты """

class Payment_page(Base):

    """ Locators """

    finish_button = "//button[@id='finish']"


    """ Getters """

    def get_finish_button(self):
        return self.driver.find_element(By.XPATH, self.finish_button)


    """ Actions """

    def click_finish_button(self):
        self.get_finish_button().click()
        print("Click finish button")


    """ Methods """

    def payment(self):

        with allure.step("Payment"):
            self.get_current_url()
            self.click_finish_button()