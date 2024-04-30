
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from pages.login_page import Login_page

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


def test_buy_product():

    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    print("Star Test")

    login = Login_page(driver)
    login.authorization()







