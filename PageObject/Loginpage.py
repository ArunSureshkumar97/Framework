from selenium.webdriver.common.by import By


class Loginpage:
    textbox_username_id = 'Email'
    textbox_password_id = 'Password'
    loginbutton_xpath = "//button[@type='submit']"
    logoutbutton_Linktext = 'Logout'


    def __init__(self,driver):
        self.driver = driver



    def setUserName(self,username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)



    def setPassword(self,password):
         self.driver.find_element(By.ID, self.textbox_password_id).clear()
         self.driver.find_element(By.ID,self.textbox_password_id).send_keys(password)

    def clicklogin(self):
         self.driver.find_element(By.XPATH,self.loginbutton_xpath).click()


    def clicklogout(self):
         self.driver.find_element(By.LINK_TEXT,self.logoutbutton_Linktext).click()















