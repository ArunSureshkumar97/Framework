import time
import os
import pytest
from selenium import webdriver
from PageObject.Loginpage import Loginpage
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from Utilities.readproperties import Readconfig
from Utilities.customLogger import LogGen
from Utilities import Xlutils


class Test_002_DDT_Login():

    baseurl = Readconfig.getapplicationurl()
    path = './/TestData/Basics.xlsx'


    logger = LogGen.loggen()

    def test_login(self,setup):
        self.logger.info("**************Data Driven Login Test ******************")
        self.logger.info("**************Veryfying Login DDT Test ******************")
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseurl)
        self.lp = Loginpage(self.driver)
        self.Rows = Xlutils.getRow(self.path,'Basics')
        print('Number of Rows',self.Rows)
        list_status = []

        for r in range(2,self.Rows+1):
            self.user = Xlutils.Readdata(self.path,'Basics',r,1)
            self.passwrd = Xlutils.Readdata(self.path,'Basics',r,2)
            self.exp = Xlutils.Readdata(self.path,'Basics',r,3)
            self.lp.setUserName(self.user)
            self.lp.setPassword(self.passwrd)
            self.lp.clicklogin()
            time.sleep(5)
            act_title = self.driver.title
            exp_title = 'Dashboard / nopCommerce administration'

            if act_title==exp_title:
                if self.exp=='PASS':
                    self.lp.clicklogout()
                    list_status.append('PASS')
                elif self.exp=='FAIL':
                    self.lp.clicklogout()
                    list_status.append('FAIL')
            elif act_title != exp_title:
                if self.exp == 'PASS':
                    list_status.append('FAIL')
                elif self.exp =='FAIL':
                    list_status.append('PASS')
            if 'FAIL' not in list_status:
                print(list_status)
                self.driver.close()
                assert True

            else:
                self.driver.close
                print(list_status)
                assert False
















