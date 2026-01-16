from selenium.webdriver.common.by import By


class login:
    #text_box_username_name="Email"
    #text_box_password_id="Password"
    #button_login_xpath= "//button[@type='submit']"
    #logout_linktext= "/logout"

    def __init__(self,driver):
        self.driver = driver
    def setUsername(self,username):
        self.driver.find_element(By.NAME, "Email").clear()
        self.driver.find_element(By.NAME, "Email").send_keys(username)
    def setpassword(self,password):
        self.driver.find_element(by=By.NAME, "Password").clear()
        self.driver.find_element(by=By.ID, "Password").send_keys(password)
    def clickLoginButton(self):
        self.driver.find_element(by=By.XPATH, "//button[@type='submit']").click()

    def clickLogoutButton(self):
        self.driver.find_element(by=By.LINK_TEXT, "/logout").click()
