from selenium.webdriver.common.by import By

class ResultPage:
    def __init__(self, driver):
        self.driver = driver
        self.result_value = (By.ID, "outputResult")
        self.back_button = (By.ID, "backHome")

    def fetch_output(self):
        return self.driver.find_element(*self.result_value).text

    def go_back_home(self):
        self.driver.find_element(*self.back_button).click()
