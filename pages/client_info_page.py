
from selenium.webdriver.common.by import By
from base.base_class import Base

""" Создал класс страницы внесения данных пользователя """

class Client_info_page(Base):

    def __init__(self, driver):

        # Инициализация класса-родителя
        super().__init__(driver)
        self.driver = driver

    """ Locators """

    # Локаторы элементов страницы

    first_name = "//input[@id='first-name']"
    last_name = "//input[@id='last-name']"
    postal_code = "//input[@id='postal-code']"
    continue_button = "//input[@id='continue']"
    main_word = "//div[@class='cart_desc_label']"


    """ Getters """

    # Получение элементов страницы

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

    # Действия с элементами страницы
    def input_first_name(self, first_name):
        # Ввод имени пользователя
        self.get_first_name().send_keys(first_name)
        print("Input first name")

    def input_last_name(self, last_name):
        # Ввод фамилии
        self.get_last_name().send_keys(last_name)
        print("Input last name")

    def input_postal_code(self, postal_code):
        # Ввод индекса
        self.get_postal_code().send_keys(postal_code)
        print("Input postal code")
    def click_continue_button(self):
        # Нажатие на кнопку continue
        self.get_continue_button().click()
        print("Click continue button")


    """ Methods """

    # Метод авторизации пользователя
    def client_info_confirm(self):

        # Получение текущей url в терминале
        self.get_current_url()
        # Ввод имени, фамилии и индекса
        self.input_first_name("Alex")
        self.input_last_name("Mahortov")
        self.input_postal_code("333777")
        # Нажатие кнопки continue
        self.click_continue_button()
        # Проверка того, что внесение данных пользователя прошла успешно, по элементу "Description"
        self.assert_word(self.get_main_word(), "Description")

