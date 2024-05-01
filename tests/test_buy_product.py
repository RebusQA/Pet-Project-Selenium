
import time
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from pages.login_page import Login_page
from selenium.webdriver.chrome.options import Options
from pages.main_page import Main_page

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


def test_buy_product():

    # Очистка терминала от лишних сообщений
    options = Options()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    print("\nStart Test")

    login = Login_page(driver)
    login.authorization()

    # Создам экземпляр класса Main_page и вызываю его метод add_product
    mp = Main_page(driver)
    mp.add_product()

    time.sleep(7)
