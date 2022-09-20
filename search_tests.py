from lib2to3.pgen2 import driver
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class HomePageTests(unittest.TestCase):

    @classmethod
    def setUp(cls) :
        service = Service('/usr/bin/chromedriver')
        cls.driver = webdriver.Chrome(service=service)
        driver = cls.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.maximize_window()
        driver.implicitly_wait(15)

    
    def test_search_text_field(cls):
        search_field = cls.driver.find_element("id", "search")

    
    def test_search_text_field_by_name(cls):
        search_field = cls.driver.find_element("name", "q")

    
    def test_search_text_field_class_name(cls):
        search_field = cls.driver.find_element(By.CLASS_NAME, "input-text")

    
    def test_search_button_enabled(cls):
        button = cls.driver.find_element(By.CLASS_NAME, "button")
    
    
    def test_count_of_promo_banner_images(cls):
        banner_list = cls.driver.find_element(By.CLASS_NAME,"promos")
        banners = banner_list.find_elements(By.TAG_NAME,"img")
        cls.assertEqual(3, len(banners))

    def test_vip_promo(cls):
        vip_promo = cls.driver.find_element(By.XPATH,'//*[@id="top"]/body/div[1]/div[2]/div[2]/div/div/div[2]/div[1]/ul/li[4]/a/img')
    
    def test_shopping_cart(cls):
        shopping_cart_icon = cls.driver.find_element(By.CSS_SELECTOR, "div.header-minicart span.icon")


    @classmethod
    def tearDown(cls) :
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity= 2)