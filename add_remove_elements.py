import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddRemoveElements(unittest.TestCase):

    def setUp(self):
        service = Service('/usr/bin/chromedriver')
        self.driver = webdriver.Chrome(service=service)
        driver = self.driver
        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com/")
        driver.find_element(By.LINK_TEXT, 'Add/Remove Elements').click()

    def test_add_remove_elements(self):
        driver = self.driver

        elements_added = int(input('How many elements do you want to add? '))
        elements_removed = int(input('How many elements do you want to remove? '))
        total_elements = elements_added - elements_removed

        add_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/button')))


        for i in range(elements_added):
            add_button.click()

        for i in range(elements_removed):
            try: 
                delete_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/button')
                delete_button.click()
            except:
                print("You're trying to delete more elements than the existent")
                break

        if total_elements > 0:
            print(f"There are {total_elements} elements on screen")
        else:
            print("There are 0 elements on screen")
        
    
    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity= 2)


