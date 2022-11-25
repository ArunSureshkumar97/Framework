import time
import os
import pytest
from selenium import webdriver
from PageObject.Loginpage import Loginpage
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from Utilities.readproperties import Readconfig
from Utilities.customLogger import LogGen


class Test_001_Login():

    baseurl = Readconfig.getapplicationurl()
    username = Readconfig.getusername()
    password = Readconfig.getpassword()
    logger = LogGen.loggen()
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homepageTitle(self,setup):
        self.logger.info("**************Test_001_Login******************")
        self.logger.info("**************Verifying Home Page Title******************")
        self.driver = setup
        self.driver.get(self.baseurl)
        actualtitle = self.driver.title
        if actualtitle == 'Your store. Login':
            assert True
            self.driver.close()
            self.logger.info("**************Home Page Title is passed******************")
        else:
            self.driver.save_screenshot(".//Screenshots//"+"test_homepageTitle.png")
            self.driver.close()
            self.logger.error("**************Home Page Title is Failed******************")
            assert False


    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("**************Veryfying Login Test ******************")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = Loginpage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clicklogin()
        time.sleep(3)
        actualtitle = self.driver.title
        if actualtitle == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("**************Login Test Passed******************")
        else:
            self.driver.save_screenshot(".//Screenshots//"+"test_login.png")
            self.driver.save_screenshot(os.getcwd(),"macha.png")
            self.driver.close()
            self.logger.error("**************Login Test Failed******************")
            assert False
