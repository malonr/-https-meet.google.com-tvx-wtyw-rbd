import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select 

class LanguageOptions(unittest.TestCase):

    def setUp(self):
        service = Service('/usr/bin/chromedriver')
        self.driver = webdriver.Chrome(service=service)
        driver = self.driver
        driver.maximize_window()
        driver.get("http://demo-store.seleniumacademy.com/")

    def test_select_language(self):
        exp_options = ['English', 'French','German']
        act_options = []

        select_language = Select(self.driver.find_element(By.ID,'select-language'))

        self.assertEqual(3, len(select_language.options))

        for options in select_language.options:
            act_options.append(options.text)

        self.assertListEqual(exp_options, act_options)

        self.assertEqual('English', select_language.first_selected_option.text)

        select_language.select_by_visible_text('German')

        self.assertTrue('store=german' in self.driver.current_url)

        select_language = Select(self.driver.find_element(By.ID, 'select-language'))

        select_language.select_by_index(0)

    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity= 2)