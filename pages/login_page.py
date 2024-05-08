
import allure
from selenium.webdriver.common.by import By
from base.base_class import Base
from utilities.logger import Logger


class Login_page(Base):

    url = "https://www.saucedemo.com/"

    """ Locators """

    # Локаторы элементов страницы

    user_name = "//input[@id='user-name']"
    password = "//input[@id='password']"
    login_button = "//input[@id='login-button']"
    main_word = "//span[@class='title']"


    """ Getters """

    # Получение элементов страницы
    def get_user_name(self):
        return self.driver.find_element(By.XPATH, self.user_name)
    def get_password(self):
        return self.driver.find_element(By.XPATH, self.password)
    def get_login_button(self):
        return self.driver.find_element(By.XPATH, self.login_button)
    def get_main_word(self):
        return self.driver.find_element(By.XPATH, self.main_word)


    """ Actions """

    # Действия с элементами страницы
    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("Input user name")
    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")
    def click_login_button(self):
        self.get_login_button().click()
        print("Click login button")


    """ Methods """

    # Метод авторизации пользователя
    def authorization(self):

        # Подключаю Allure
        with allure.step("Authorization"):
            # Обращаюсь к классу Logger для запуска логирования теста
            Logger.add_start_step(method="authorization")
            # Открытие страницы
            self.driver.get(self.url)
            # Максимизация окна браузера
            self.driver.maximize_window()
            # Получение текущей url в терминале
            self.get_current_url()
            # Ввод имени пользователя и пароля
            self.input_user_name("standard_user")
            self.input_password("secret_sauce")
            # Нажатие кнопки входа
            self.click_login_button()
            # Проверка того, что авторизация прошла успешно, по элементу "Products"
            self.assert_word(self.get_main_word(), "Products")
            # Обращаюсь к классу Logger для завершения логирования теста
            Logger.add_end_step(url=self.driver.current_url, method="authorization")