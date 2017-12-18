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

class TeleActions():
    '''
    classdocse
    '''
    def __init__(self):

        self.getinfo=SetParameters()
        self.commonActions=CommonActions()
    def accessTeleRecharge(self,driver,area_row,area_col,num_row,num_col):
        #进入固话充值
        try:
            self.commonActions.publishMsg(driver)
        except:
            print "没有推送消息！"
        teleRechargexpath=self.getinfo.setElementConfig(10, 5)
        try:
            WebDriverWait(driver, 30).until(lambda the_driver: the_driver.find_element_by_xpath(teleRechargexpath).is_displayed())
        except:
            print "not found!"
        time.sleep(1)
        driver.find_element_by_xpath(teleRechargexpath).click()
        telephoneAreaId=self.getinfo.setTelePhoneConfig(1, 8)
        telephoneAreaNum=self.getinfo.setTelePhoneConfig(area_row, area_col)
        self.commonActions.switchToIframe(driver)
        driver.find_element_by_id(telephoneAreaId).send_keys(telephoneAreaNum)
        telephoneNumId=self.getinfo.setTelePhoneConfig(2, 8)
        telephoneNum=self.getinfo.setTelePhoneConfig(num_row, num_col)
        driver.find_element_by_id(telephoneNumId).send_keys(telephoneNum)
        
    def clickConfirmRecharge(self,driver):
        confirmPayxpath=self.getinfo.setTelePhoneConfig(10, 8)
        driver.find_element_by_xpath(confirmPayxpath).click()
        
    def teleRecharge(self,driver,area_row,area_col,num_row,num_col):
        self.accessTeleRecharge(driver,area_row,area_col,num_row,num_col)
        amountXpath=self.getinfo.setTelePhoneConfig(5, 8)
        driver.find_element_by_xpath(amountXpath).click()
        quickPayXpath=self.getinfo.setTelePhoneConfig(9, 8)
        driver.find_element_by_xpath(quickPayXpath).click()
        self.clickConfirmRecharge(driver)
        
    def teleRechargeError(self,driver,area_row,area_col,num_row,num_col):
        self.accessTeleRecharge(driver,area_row,area_col,num_row,num_col)
        amountXpath=self.getinfo.setTelePhoneConfig(5, 8)
        driver.find_element_by_xpath(amountXpath).click()
        quickPayXpath=self.getinfo.setTelePhoneConfig(9, 8)
        driver.find_element_by_xpath(quickPayXpath).click()
        
    def verifyTeleRechargeError(self,driver):
        errorResult=self.getinfo.setTelePhoneConfig(16, 7)
        errorResultXpath=self.getinfo.setTelePhoneConfig(16, 8)
        errorInfo=driver.find_element_by_xpath(errorResultXpath).text
        flag=False
        if errorInfo==errorResult:
            flag=True
            return flag
        
        return flag
        
    def verifyTeleRechargeNotSupport(self,driver):
        errorResult=self.getinfo.setTelePhoneConfig(17, 7)
        errorResultXpath=self.getinfo.setTelePhoneConfig(17, 8)
        errorInfo=driver.find_element_by_xpath(errorResultXpath).text
        flag=False
        if errorInfo==errorResult:
            flag=True
            return flag
        
        return flag
        
    def teleRechargeProvinceCheck(self,driver,area_row,area_col,num_row,num_col):
        self.accessTeleRecharge(driver,area_row,area_col,num_row,num_col)
        province=self.getinfo.setTelePhoneConfig(area_row, (area_col+4))
        l_province_xpath=self.getinfo.setTelePhoneConfig(12,8)
        try:
            WebDriverWait(driver, 30).until(lambda the_driver: the_driver.find_element_by_xpath(l_province_xpath).is_displayed())
        except:
            print "not found!"
        l_province=driver.find_element_by_xpath(l_province_xpath).text
        flag=False
        if province==l_province:
            flag=True
            return flag
        else:
            return flag
        
        return flag
    
    def teleRechargeNumCheck(self,driver,area_row,area_col,num_row,num_col):
        self.accessTeleRecharge(driver,area_row,area_col,num_row,num_col)
        l_area=self.getinfo.setTelePhoneConfig(area_row, area_col)
        l_num=str(int(self.getinfo.setTelePhoneConfig(num_row, num_col)))
        l_area_num=l_area+"-"+l_num
        l_area_checkId=self.getinfo.setTelePhoneConfig(3,8)
        l_area_check=driver.find_element_by_xpath(l_area_checkId).text
        l_num_checkId=self.getinfo.setTelePhoneConfig(4,8)
        l_num_check=driver.find_element_by_xpath(l_num_checkId).text
        l_area_num_check=l_area_check+l_num_check
        flag=False
        if l_area_num==l_area_num_check:
            flag=True
            return flag
        
        return flag
    
    def cancleRecharge(self,driver,area_row,area_col,num_row,num_col):
        self.accessTeleRecharge(driver, area_row, area_col, num_row, num_col)
        amountXpath=self.getinfo.setTelePhoneConfig(5, 8)
        driver.find_element_by_xpath(amountXpath).click()
        quickPayXpath=self.getinfo.setTelePhoneConfig(9, 8)
        driver.find_element_by_xpath(quickPayXpath).click()
        canclexpathId=self.getinfo.setTelePhoneConfig(11, 8)
        try:
            WebDriverWait(driver,30).until(lambda the_driver: the_driver.find_element_by_xpath(canclexpathId).is_displayed(), u"没有找到取消按钮")
        except Exception,e:
            print e
            pass
        driver.find_element_by_xpath(canclexpathId).click()
        area_num=self.getAreaNum(area_row, area_col, num_row, num_col)
        
        return area_num
        
    def getAreaNum(self,area_row,area_col,num_row,num_col):
        area=self.getinfo.setTelePhoneConfig(area_row, area_col)
        num=self.getinfo.setTelePhoneConfig(num_row, num_col)
        area_num=area+str(int(num))
        
        return area_num
    
    def cancleOrder(self,driver,area_row,area_col,num_row,num_col):
        self.cancleRecharge(driver, area_row, area_col, num_row, num_col)
        self.clickRefreshBtn(driver)
        self.clickCancleOrderBtn(driver)
        area_num=self.getAreaNum(area_row, area_col, num_row, num_col)
        print area_num
        
        return area_num
        
    def verifyCancleOrder(self,driver,area_num):
        self.clickRefreshBtn(driver)
        cancleNumXpath=self.getinfo.setTelePhoneConfig(13, 8)
        cancleNum=driver.find_element_by_xpath(cancleNumXpath).text
        statusXpath=self.getinfo.setTelePhoneConfig(14, 8)
        status=driver.find_element_by_xpath(statusXpath).text
        flag=False
        print status,area_num,cancleNum
        if area_num==cancleNum and status==u'已撤单':
            flag=True
            return flag
        
        return flag
        
    def clickCancleOrderBtn(self,driver):
        cancleOrderXpath=self.getinfo.setElementConfig(37, 5)
        print cancleOrderXpath
        try:
            driver.find_element_by_xpath(cancleOrderXpath).click()
        except Exception,error:
            print error
            pass
        
    def clickRefreshBtn(self,driver):
        time.sleep(5)
        refreshBtnXpath=self.getinfo.setTelePhoneConfig(15, 8)
        try:
            driver.find_element_by_xpath(refreshBtnXpath).click()
        except Exception,e:
            print e
            pass
        time.sleep(5)
        
    def verifyCancleRecharge(self,driver,area_num):
        refreshXpath=self.getinfo.setTelePhoneConfig(15, 8)
        driver.find_element_by_xpath(refreshXpath).click()
        l_number_Xpath=self.getinfo.setTelePhoneConfig(13, 8)
        l_number=driver.find_element_by_xpath(l_number_Xpath).text
        l_status_xpath=self.getinfo.setTelePhoneConfig(14, 8)
        l_status=driver.find_element_by_xpath(l_status_xpath).text
        print l_status,l_number
        flag=False
        if area_num==l_number and l_status==u'未支付':
            flag=True
            return flag
        
        return flag
     
    def continueRecharge(self,driver,area_row,area_col,num_row,num_col):
        self.cancleRecharge(driver, area_row, area_col, num_row, num_col)
        continueRechargeXpath=self.getinfo.setElementConfig(36, 5)
        driver.find_element_by_xpath(continueRechargeXpath).click()
        self.clickConfirmRecharge(driver)
        
    def teleRechargePriceCheck(self,driver,area_row,area_col,num_row,num_col,amount_row,amount_col):
        self.accessTeleRecharge(driver,area_row,area_col,num_row,num_col)
        amountXpath=self.getinfo.setTelePhoneConfig(amount_row, amount_col)
        driver.find_element_by_xpath(amountXpath).click()
        quickPayXpath=self.getinfo.setTelePhoneConfig(9, 8)
        driver.find_element_by_xpath(quickPayXpath).click()
        priceBtnXpath=self.getinfo.setTelePhoneConfig(18, 8)
        driver.find_element_by_xpath(priceBtnXpath).click()
        priceXpath=self.getinfo.setTelePhoneConfig(19, 8)
        try:
            WebDriverWait(driver,10).until(lambda the_driver: the_driver.find_element_by_xpath(priceXpath).is_displayed(), u"进货价没有找到！")
        except Exception, e:
            print e
            pass
        price=driver.find_element_by_xpath(priceXpath).text
        purchasePrice=self.getinfo.setTelePhoneConfig(area_row, (area_col+3))
        flag=False
        if float(price[0:5])==float(purchasePrice):
            flag=True
            return flag
        
        return flag
        
        
        
        
        