
import time
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from pages.cart_page import Cart_page
from pages.client_info_page import Client_info_page
from pages.finish_page import Finish_page
from pages.login_page import Login_page
from selenium.webdriver.chrome.options import Options
from pages.main_page import Main_page
from pages.payment_page import Payment_page

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


def test_buy_product():

    # Очистка терминала от лишних сообщений
    options = Options()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    print("\nStart Test")

    # Создал экземпляр класса Login_page и вызываю его метод authorization
    login = Login_page(driver)
    login.authorization()

    # Создал экземпляр класса Main_page и вызываю его метод add_product
    mp = Main_page(driver)
    mp.add_product()

    # Создал экземпляр класса Cart_page и вызываю его метод product_confirm
    cp = Cart_page(driver)
    cp.product_confirm()

    # Создал экземпляр класса Client_info_page и вызываю его метод client_info_confirm
    cip = Client_info_page(driver)
    cip.client_info_confirm()

    # Создал экземпляр класса Payment_page и вызываю его метод payment
    pp = Payment_page(driver)
    pp.payment()

    # Создал экземпляр класса Finish_page и вызываю его метод finish
    fp = Finish_page(driver)
    fp.finish()


    time.sleep(7)
