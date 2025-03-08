import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class TestSelenium(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_python_firefox(self):
        self.driver.get("http://www.python.org")
        assert "Python" in self.driver.title
        elem = self.driver.find_element(By.NAME, "q")
        elem.clear()
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in self.driver.page_source
    
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()