#!C:\Python27\python
# -*- coding: utf-8 -*- 
'''
Created on 2016年6月20日

@author: tc
'''
import time,re
from selenium import webdriver
from common_actions.commonActions import CommonActions
from setparameters.setparameters import SetParameters
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0

class AdvantageActions():
    '''
    classdocse
    '''
    def __init__(self):

        self.getinfo=SetParameters()
        self.commonActions=CommonActions()
    def adRecharge(self,driver,phone_row,phone_col,amount_row,amount_col):
        #话费充值
        self.enterAdRecharge(driver,phone_row, phone_col, amount_row, amount_col)
        self.adReChargeConfirm(driver)
        
        
    def enterAdRecharge(self,driver,phone_row,phone_col,amount_row,amount_col):
        self.commonActions.publishMsg(driver)
        iframe=self.getinfo.setElementConfig(8, 5)
        item=self.getinfo.setElementConfig(11, 5)
        try:
            #WebDriverWait(driver, 20).until(lambda the_driver: the_driver.find_element_by_xpath(mbRecharge).is_displayed())
            #element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, mbRecharge)))
            time.sleep(5)
            driver.find_element_by_xpath(item).click()
        except:
            print "element error"
        driver.switch_to_frame(iframe)
        phonenumber=self.getinfo.setAdRechargeConfig(phone_row, phone_col)
        rechargeAmount=self.getinfo.setElementConfig(amount_row, amount_col)
        #amount=driver.find_element_by_xpath(rechargeAmount).text
        phonenumberId=self.getinfo.setElementConfig(15,5)
        confirmRechargeId=self.getinfo.setElementConfig(24,5)
        driver.find_element_by_id(phonenumberId).send_keys(phonenumber)
        driver.find_element_by_xpath(rechargeAmount).click()
        driver.find_element_by_xpath(confirmRechargeId).click()
        
    def adReChargeConfirm(self,driver):
        ensureId=self.getinfo.setElementConfig(26,5)
        driver.find_element_by_id(ensureId).click()
        
    def disAdRecharge(self,driver,phone_row,phone_col):
        self.commonActions.publishMsg(driver)
        item=self.getinfo.setElementConfig(11, 5)
        iframe=self.getinfo.setElementConfig(8, 5)
        try:
            #WebDriverWait(driver, 20).until(lambda the_driver: the_driver.find_element_by_xpath(mbRecharge).is_displayed())
            #element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, mbRecharge)))
            time.sleep(5)
            driver.find_element_by_xpath(item).click()
        except:
            print "element error"
        driver.switch_to_frame(iframe)
        phonenumberId=self.getinfo.setElementConfig(15,5)
        phonenumber=self.getinfo.setAdRechargeConfig(phone_row, phone_col)
        driver.find_element_by_id(phonenumberId).send_keys(phonenumber)
        #回到主窗体，因为提示语在主窗体，否则无法定位
        driver.switch_to_default_content()
        infoXpath=self.getinfo.setAdRechargeConfig(1, 5)
        self.commonActions.waitForElement(driver, infoXpath)
        info=driver.find_element_by_xpath(infoXpath).text
        print info
        
        return info
    def verifyDisAdRecharge(self,info):
        result=self.getinfo.setAdRechargeConfig(8, 2)
        flag=False
        if info==result:
            flag=True
            return flag
        
        return flag
    
    def verifyAdRechargeErrorNum(self,info):
        result=self.getinfo.setAdRechargeConfig(9, 2)
        flag=False
        if info==result:
            flag=True
            return flag
        
        return flag