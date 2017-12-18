#!C:\Python27\python
# -*- coding: utf-8 -*- 
'''
Created on 2016年6月13日

@author: tc
'''
import time,re
from selenium import webdriver
from setparameters.setparameters import SetParameters
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from wx.lib.inspection import Refresh
from MySQLdb.constants import REFRESH

class MBActions():
        
    def rechargeProvinceCheck(self,phone_row,phone_col):
        #话费充值
        mbRechargeId=self.setup.setElementConfig(9, 5)
        iframe=self.setup.setElementConfig(8, 5)
        time.sleep(5)
        try:
            self.driver.find_element_by_xpath(mbRechargeId).click()
        except:
            print "有推送消息！"
            self.readAlert()
        self.driver.find_element_by_xpath(mbRechargeId).click()
        self.driver.switch_to_frame(iframe)
        phonenumber=self.setup.setMbRecharge(phone_row, phone_col)
        phonenumberId=self.setup.setElementConfig(15,5)
        self.driver.find_element_by_id(phonenumberId).send_keys(phonenumber)
        province=self.setup.setMbRecharge(phone_row, (phone_col+2))
        phone_addr=self.setup.setElementConfig(31,5)
        time.sleep(2)
        l_province=self.driver.find_element_by_id(phone_addr).text
        flag=False
        if province == l_province:
            flag=True
            
        return flag
    
    def balanceQuery(self,phone_row,phone_col):
        #话费充值
        mbRechargeId=self.setup.setElementConfig(9, 5)
        iframe=self.setup.setElementConfig(8, 5)
        time.sleep(5)
        try:
            self.driver.find_element_by_xpath(mbRechargeId).click()
        except:
            print "有推送消息！"
            self.readAlert()
        self.driver.find_element_by_xpath(mbRechargeId).click()
        self.driver.switch_to_frame(iframe)
        phonenumber=self.setup.setMbRecharge(phone_row, phone_col)
        phonenumberId=self.setup.setElementConfig(15,5)
        self.driver.find_element_by_id(phonenumberId).send_keys(phonenumber)
        time.sleep(2)
        balanceQueryId=self.setup.setElementConfig(32,5)
        print "js执行点击"
        #self.driver.find_element_by_id(balanceQueryId).click()
        self.driver.execute_script("$('#mob_reflash').click()")
        time.sleep(5)
        queryInfoId=self.setup.setElementConfig(33,5)
        queryInfo=self.driver.find_element_by_id(queryInfoId).text
            
        return queryInfo
    def varifybalanceQuery(self,queryInfo):
        flag=False
        reg=u'余额'
        if re.search(reg,queryInfo):
            flag=True
            return flag
        elif queryInfo == '查询失败':
            print queryInfo
            return flag
        else:
            print queryInfo
            return flag
     
    def publishMsg(self):
        mbRecharge=self.setup.setElementConfig(9, 5)
        try:
            self.driver.find_element_by_xpath(mbRecharge).click()
        except:
            print "有推送消息！"
            self.readAlert()
        
        return mbRecharge
    def enterQuickCharge(self,phone_row,phone_col,amount_row,amount_col):
        mbRecharge=self.publishMsg()
        iframe=self.setup.setElementConfig(8, 5)
        try:
            #WebDriverWait(self.driver, 20).until(lambda the_driver: the_driver.find_element_by_xpath(mbRecharge).is_displayed())
            #element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, mbRecharge)))
            time.sleep(2)
            self.driver.find_element_by_xpath(mbRecharge).click()
        except:
            print "element error"
        self.driver.switch_to_frame(iframe)
        phonenumber=self.setup.setMbRecharge(phone_row, phone_col)
        rechargeAmount=self.setup.setElementConfig(amount_row, amount_col)
        #amount=self.driver.find_element_by_xpath(rechargeAmount).text
        phonenumberId=self.setup.setElementConfig(15,5)
        confirmRechargeId=self.setup.setElementConfig(24,5)
        self.driver.find_element_by_id(phonenumberId).send_keys(phonenumber)
        self.driver.find_element_by_xpath(rechargeAmount).click()
        self.driver.find_element_by_xpath(confirmRechargeId).click()
        
        return phonenumber
    def mbReChargeConfirm(self):
        ensureId=self.setup.setElementConfig(26,5)
        self.driver.find_element_by_id(ensureId).click()
        
    def mbRecharge(self,phone_row,phone_col,amount_row,amount_col):
        #话费充值
        self.enterQuickCharge(phone_row, phone_col, amount_row, amount_col)
        self.mbReChargeConfirm()
       
    def mbRechargeError(self,phone_row,phone_col,amount_row,amount_col):
        #话费充值
        self.enterQuickCharge(phone_row, phone_col, amount_row, amount_col)
        
    def mbRechargeCancle(self,phone_row,phone_col,amount_row,amount_col):
        #话费充值
        phonenumber=self.enterQuickCharge(phone_row, phone_col, amount_row, amount_col)
        cancleBtn=self.setup.setElementConfig(27,5)
        self.driver.find_element_by_id(cancleBtn).click()
        
        return phonenumber
    
    def mbRechargeContinue(self,phone_row,phone_col,amount_row,amount_col):
        #话费充值
        self.mbRechargeCancle(phone_row, phone_col, amount_row, amount_col)
        refreshBtn=self.setup.setElementConfig(35,5)
        self.driver.find_element_by_xpath(refreshBtn).click()
        continueBtn=self.setup.setElementConfig(36,5)
        self.driver.find_element_by_xpath(continueBtn).click()
        self.mbReChargeConfirm()
    def mbRechargeCancleOrder(self,phone_row,phone_col,amount_row,amount_col):
        self.mbRechargeCancle(phone_row, phone_col, amount_row, amount_col)
        refreshBtn=self.setup.setElementConfig(35,5)
        self.driver.find_element_by_xpath(refreshBtn).click()
        cancleOrderXpath=self.setup.setElementConfig(37,5)
        self.driver.find_element_by_xpath(cancleOrderXpath).click()
        orderStateXpath=self.setup.setElementConfig(38,5)
        self.driver.find_element_by_xpath(refreshBtn).click()
        time.sleep(1)
        orderState=self.driver.find_element_by_xpath(orderStateXpath).text
        print orderState
        flag=False
        if orderState.strip()==u'已撤单':
            flag=True
            return flag
        
        return flag
       
        

        
    def verifymbRechargeCancle(self,number):
        #验证订单状态
        refreshBtn=self.setup.setElementConfig(35,5)
        self.driver.find_element_by_xpath(refreshBtn).click()
        continueBtn=self.setup.setElementConfig(36,5)
        orderState=self.driver.find_element_by_xpath(continueBtn).text
        phonenumber=self.driver.find_element_by_xpath('//*[@id="newrecodcont"]/ul[1]/li[3]').text
        flag=False
        if int(number) == int(phonenumber) and orderState=='继续支付':
            flag=True
            return flag
        
        return flag
        
    def verifyMbRechargeError(self):
        
        errorInfo=self.setup.setMbRecharge(14, 7)
        errorInfoXpath=self.setup.setElementConfig(34,5)
        resInfo=self.driver.find_element_by_xpath(errorInfoXpath).text
        print errorInfo,resInfo
        flag=False
        if resInfo==errorInfo:
            flag=True
            return flag
        return flag
    
    def verifyMbRecharge(self):
        
        flag=False
        result=self.setup.setElementConfig(28,5)
        resultId=self.setup.setElementConfig(30,5)
        webRes=self.driver.find_element_by_css_selector(resultId).text
        if result==webRes:
            flag=True
            return flag
        else:
            return flag
        
        return flag
    def closeAlert(self):
        self.driver.implicitly_wait(5)
        self.driver.switch_to_alert()
        msgId=self.setup.setCommonConfig(10,5)
        self.driver.find_element_by_xpath(msgId).click()
        
    def readAlert(self):
        self.driver.implicitly_wait(5)
        self.driver.switch_to_alert()
        self.driver.find_element_by_css_selector('body > div.form_box > div.box_content > div').click()
        self.scrollDown()
        hasReadBtn=self.setup.setCommonConfig(11, 5)
        self.driver.execute_script("$('#hasReadBtn').click()")
        
    def scrollUp(self):
        js="var q=document.documentElement.scrollTop=0"
        self.driver.execute_script(js)
    def scrollDown(self):
        self.driver.find_element_by_xpath("/html/body/div[12]/div[2]/div").send_keys(Keys.DOWN)
        self.driver.find_element_by_xpath("/html/body/div[12]/div[2]/div").send_keys(Keys.DOWN)
        self.driver.find_element_by_xpath("/html/body/div[12]/div[2]/div").send_keys(Keys.DOWN)
        self.driver.find_element_by_xpath("/html/body/div[12]/div[2]/div").send_keys(Keys.DOWN)
        self.driver.find_element_by_xpath("/html/body/div[12]/div[2]/div").send_keys(Keys.DOWN)
        self.driver.find_element_by_xpath("/html/body/div[12]/div[2]/div").send_keys(Keys.DOWN)
        self.driver.find_element_by_xpath("/html/body/div[12]/div[2]/div").send_keys(Keys.DOWN)
        self.driver.find_element_by_xpath("/html/body/div[12]/div[2]/div").send_keys(Keys.DOWN)
        self.driver.find_element_by_xpath("/html/body/div[12]/div[2]/div").send_keys(Keys.DOWN)
        #self.driver.find_element_by_xpath("/html/body/div[12]/div[2]/div").send_keys(Keys.DOWN)