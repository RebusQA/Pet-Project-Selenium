
import allure
from selenium.webdriver.common.by import By
from base.base_class import Base

""" Создал класс страницы внесения данных пользователя """

class Client_info_page(Base):


    """ Locators """

    first_name = "//input[@id='first-name']"
    last_name = "//input[@id='last-name']"
    postal_code = "//input[@id='postal-code']"
    continue_button = "//input[@id='continue']"
    main_word = "//div[@class='cart_desc_label']"


    """ Getters """

    def get_first_name(self):
        return self.driver.find_element(By.XPATH, self.first_name)
    def get_last_name(self):
        return self.driver.find_element(By.XPATH, self.last_name)
    def get_postal_code(self):
        return self.driver.find_element(By.XPATH, self.postal_code)
    def get_continue_button(self):
        return self.driver.find_element(By.XPATH, self.continue_button)
    def get_main_word(self):
        return self.driver.find_element(By.XPATH, self.main_word)


    """ Actions """

    def input_first_name(self, first_name):
        self.get_first_name().send_keys(first_name)
        print("Input first name")

    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)
        print("Input last name")

    def input_postal_code(self, postal_code):
        self.get_postal_code().send_keys(postal_code)
        print("Input postal code")
    def click_continue_button(self):
        self.get_continue_button().click()
        print("Click continue button")


    """ Methods """

    def client_info_confirm(self):

        with allure.step("Client info confirm"):
            self.get_current_url()
            self.input_first_name("Alex")
            self.input_last_name("Mahortov")
            self.input_postal_code("333777")
            self.click_continue_button()
            self.assert_word(self.get_main_word(), "Description")