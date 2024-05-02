
import time
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from pages.cart_page import Cart_page
from pages.client_info_page import Client_info_page
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

    # Создам экземпляр класса Login_page и вызываю его метод authorization
    login = Login_page(driver)
    login.authorization()

    # Создам экземпляр класса Main_page и вызываю его метод add_product
    mp = Main_page(driver)
    mp.add_product()

    # Создам экземпляр класса Cart_page и вызываю его метод product_confirm
    cp = Cart_page(driver)
    cp.product_confirm()

    # Создам экземпляр класса Client_info_page и вызываю его метод client_info_confirm
    cip = Client_info_page(driver)
    cip.client_info_confirm()


    time.sleep(7)
