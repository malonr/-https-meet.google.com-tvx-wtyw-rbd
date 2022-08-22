from lib2to3.pgen2 import driver
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class HelloWorld(unittest.TestCase):

    @classmethod 
    def setUpClass(cls):
        service = Service('/usr/bin/chromedriver')
        cls.driver = webdriver.Chrome(service=service)
        driver = cls.driver
        driver.implicitly_wait(10)

    def test_hello_world(self):
        driver = self.driver
        driver.get('https://www.platzi.com')
    
    def test_visit_wikipedia(self):
        driver = self.driver
        driver.get =('https://www.wikipedia.org')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ =="__main__":
    unittest.main(verbosity= 2, testRunner=HTMLTestRunner(output= 'reports', report_name= 'hello-world-report'))

