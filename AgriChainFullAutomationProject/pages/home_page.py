from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.input_box = (By.ID, "stringInput")
        self.submit_button = (By.ID, "submitBtn")
        self.error_msg = (By.ID, "errorMessage")

    def enter_input(self, text):
        field = self.driver.find_element(*self.input_box)
        field.clear()
        field.send_keys(text)

    def click_submit(self):
        self.driver.find_element(*self.submit_button).click()

    def get_error_message(self):
        return self.driver.find_element(*self.error_msg).text
