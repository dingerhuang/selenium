#!C:\Python27\python
# -*- coding: utf-8 -*- 
'''
Created on 2016年6月13日

@author: tc
'''
import time,re,MySQLdb,os
from selenium import webdriver
from setparameters.setparameters import SetParameters
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from wx.lib.inspection import Refresh
from MySQLdb.constants import REFRESH
import win32gui,win32api,win32con
from ctypes import *


class CommonActions():
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''

        self.getinfo=SetParameters()
        self.loginUrl=self.getinfo.setCommonConfig(5, 5)
        self.userName=int(self.getinfo.setCommonConfig(6,5))
        self.passwd=self.getinfo.setCommonConfig(7, 5)
        self.userNameId=self.getinfo.setElementConfig(5, 5)
        self.passwdId=self.getinfo.setElementConfig(6, 5)
        self.loginBtn=self.getinfo.setElementConfig(7, 5)
        
    def mouse_click(self,x=None,y=None):
        if not x is None and not y is None:
            self.mouse_move(x,y)
            time.sleep(0.05)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        
        print "ok1"
        
    def mouse_move(self,x,y):
        windll.user32.SetCursorPos(x, y)
        
        print "ok2"
    
    def sendKey(self):
        try:
            print "sends"
            win32api.keybd_event(65,0,0,0) #a键位码是86  
            win32api.keybd_event(65,0,win32con.KEYEVENTF_KEYUP,0)
        except Exception,error:
            print error
    
    def login(self):
        #chorme浏览器
        iedriver = "C:\\Program Files\\Internet Explorer\\IEDriverServer.64.exe"
        os.environ["webdriver.ie.driver"] = iedriver
        driver =  webdriver.Ie(iedriver)
        driver.implicitly_wait(60)
        driver.get(self.loginUrl)
        #driver.maximize_wiandow()
        driver.find_element_by_id(self.userNameId).send_keys(self.userName)

        driver.find_element_by_id(self.loginBtn).click()

        return driver
    
    def login_chorme(self):
        #chorme浏览器
        chromedriver = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        driver =  webdriver.Chrome(chromedriver)
        driver.implicitly_wait(60)
        driver.get(self.loginUrl)
        driver.maximize_window()
        driver.find_element_by_id(self.userNameId).send_keys(self.userName)

        driver.find_element_by_id(self.loginBtn).click()

        return driver
    
    def login_ff(self):
        profileDir = "C:\\Users\\tc\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\44l7rfv8.default"
        profile = webdriver.FirefoxProfile(profileDir)
        driver=webdriver.Firefox(profile)
        driver.implicitly_wait(30)

        driver.get(self.loginUrl)
        driver.maximize_window()
        driver.find_element_by_id(self.userNameId).send_keys(self.userName)
        #xpath='//*[@id="fancy"]'
        #print "=="
        #print driver.find_element_by_xpath(xpath).location
        #self.click(driver, xpath)
        #self.sendKey()
        driver.find_element_by_id(self.loginBtn).click()

        return driver

    def rechargeProvinceCheck(self,driver,phone_row,phone_col):
        #话费充值
        mbRechargeId=self.getinfo.setElementConfig(9, 5)
        iframe=self.getinfo.setElementConfig(8, 5)
        try:
            driver.find_element_by_xpath(mbRechargeId).click()
        except:
            print "有推送消息！"
            self.readAlert(driver)
        time.sleep(1)
        driver.find_element_by_xpath(mbRechargeId).click()
        driver.switch_to_frame(iframe)
        phonenumber=self.getinfo.setMbRecharge(phone_row, phone_col)
        phonenumberId=self.getinfo.setElementConfig(15,5)
        driver.find_element_by_id(phonenumberId).send_keys(phonenumber)
        province=self.getinfo.setMbRecharge(phone_row, (phone_col+2))
        phone_addr=self.getinfo.setElementConfig(31,5)
        time.sleep(2)
        l_province=driver.find_element_by_id(phone_addr).text
        flag=False
        if province == l_province:
            flag=True
            
        return flag
    
    def balanceQuery(self,driver,phone_row,phone_col):
        #话费充值
        mbRechargeId=self.getinfo.setElementConfig(9, 5)
        iframe=self.getinfo.setElementConfig(8, 5)
        try:
            driver.find_element_by_xpath(mbRechargeId).click()
        except:
            print "有推送消息！"
            self.readAlert(driver)
        time.sleep(1)
        driver.find_element_by_xpath(mbRechargeId).click()
        driver.switch_to_frame(iframe)
        phonenumber=self.getinfo.setMbRecharge(phone_row, phone_col)
        phonenumberId=self.getinfo.setElementConfig(15,5)
        driver.find_element_by_id(phonenumberId).send_keys(phonenumber)
        time.sleep(2)
        balanceQueryId=self.getinfo.setElementConfig(32,5)
        print "js执行点击"
        #driver.find_element_by_id(balanceQueryId).click()
        driver.execute_script("$('#mob_reflash').click()")
        time.sleep(10)
        queryInfoId=self.getinfo.setElementConfig(33,5)
        queryInfo=driver.find_element_by_id(queryInfoId).text
            
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
     
    def publishMsg(self,driver):
        mbRecharge=self.getinfo.setElementConfig(9, 5)
        try:
            print "没有推送消息！"
            driver.find_element_by_xpath(mbRecharge).click()
        except:
            print "有推送消息！"
            self.readAlert(driver)
        
        return mbRecharge
    def enterQuickCharge(self,driver,phone_row,phone_col,amount_row,amount_col):
        mbRecharge=self.publishMsg(driver)
        iframe=self.getinfo.setElementConfig(8, 5)
        try:
            #WebDriverWait(driver, 20).until(lambda the_driver: the_driver.find_element_by_xpath(mbRecharge).is_displayed())
            #element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, mbRecharge)))
            time.sleep(2)
            driver.find_element_by_xpath(mbRecharge).click()
        except:
            print "element error"
        driver.switch_to_frame(iframe)
        phonenumber=self.getinfo.setMbRecharge(phone_row, phone_col)
        rechargeAmount=self.getinfo.setElementConfig(amount_row, amount_col)
        #amount=driver.find_element_by_xpath(rechargeAmount).text
        phonenumberId=self.getinfo.setElementConfig(15,5)
        confirmRechargeId=self.getinfo.setElementConfig(24,5)
        driver.find_element_by_id(phonenumberId).send_keys(phonenumber)
        driver.find_element_by_xpath(rechargeAmount).click()
        driver.find_element_by_xpath(confirmRechargeId).click()
        
        return phonenumber
    def mbReChargeConfirm(self,driver):
        ensureId=self.getinfo.setElementConfig(26,5)
        driver.find_element_by_id(ensureId).click()
        
    def mbRecharge(self,driver,phone_row,phone_col,amount_row,amount_col):
        #话费充值
        self.enterQuickCharge(driver,phone_row, phone_col, amount_row, amount_col)
        self.mbReChargeConfirm(driver)
        
    def mbRechargeNumError(self,driver,phone_row,phone_col,amount_row,amount_col):
        pass
    def mbRechargeError(self,driver,phone_row,phone_col,amount_row,amount_col):
        #话费充值
        self.enterQuickCharge(driver,phone_row, phone_col, amount_row, amount_col)
        
    def mbRechargeCancle(self,driver,phone_row,phone_col,amount_row,amount_col):
        #话费充值
        phonenumber=self.enterQuickCharge(driver,phone_row, phone_col, amount_row, amount_col)
        cancleBtn=self.getinfo.setElementConfig(27,5)
        driver.find_element_by_id(cancleBtn).click()
        
        return phonenumber
    
    def mbRechargeContinue(self,driver,phone_row,phone_col,amount_row,amount_col):
        #话费充值
        self.mbRechargeCancle(driver,phone_row, phone_col, amount_row, amount_col)
        refreshBtn=self.getinfo.setElementConfig(35,5)
        driver.find_element_by_xpath(refreshBtn).click()
        continueBtn=self.getinfo.setElementConfig(36,5)
        driver.find_element_by_xpath(continueBtn).click()
        self.mbReChargeConfirm(driver)
    def mbRechargeCancleOrder(self,driver,phone_row,phone_col,amount_row,amount_col):
        self.mbRechargeCancle(driver,phone_row, phone_col, amount_row, amount_col)
        refreshBtn=self.getinfo.setElementConfig(35,5)
        driver.find_element_by_xpath(refreshBtn).click()
        cancleOrderXpath=self.getinfo.setElementConfig(37,5)
        driver.find_element_by_xpath(cancleOrderXpath).click()
        orderStateXpath=self.getinfo.setElementConfig(38,5)
        driver.find_element_by_xpath(refreshBtn).click()
        time.sleep(1)
        orderState=driver.find_element_by_xpath(orderStateXpath).text
        print orderState
        flag=False
        if orderState.strip()==u'已撤单':
            flag=True
            return flag
        
        return flag
        
    def verifymbRechargeCancle(self,driver,number):
        #验证订单状态
        print number
        refreshBtn=self.getinfo.setElementConfig(35,5)
        driver.find_element_by_xpath(refreshBtn).click()
        continueBtn=self.getinfo.setElementConfig(36,5)
        orderState=driver.find_element_by_xpath(continueBtn).text
        phonenumber=driver.find_element_by_xpath('//*[@id="newrecodcont"]/ul[1]/li[3]').text
        print phonenumber
        flag=False
        if int(number) == int(phonenumber) and orderState=='继续支付':
            flag=True
            return flag
        
        return flag
        
    def verifyMbRechargeError(self,driver):
        
        errorInfo=self.getinfo.setMbRecharge(14, 7)
        errorInfoXpath=self.getinfo.setElementConfig(34,5)
        resInfo=driver.find_element_by_xpath(errorInfoXpath).text
        print errorInfo,resInfo
        flag=False
        if resInfo==errorInfo:
            flag=True
            return flag
        return flag
    
    def verifyMbRecharge(self,driver):
        
        flag=False
        result=self.getinfo.setElementConfig(28,5)
        resultId=self.getinfo.setElementConfig(30,5)
        webRes=driver.find_element_by_css_selector(resultId).text
        if result==webRes:
            flag=True
            return flag
        else:
            return flag
        
        return flag
    def closeAlert(self,driver):
        driver.implicitly_wait(5)
        driver.switch_to_alert()
        msgId=self.getinfo.setCommonConfig(10,5)
        driver.find_element_by_xpath(msgId).click()
        
    def readAlert(self,driver):
        driver.implicitly_wait(5)
        driver.switch_to_alert()
        #driver.find_element_by_css_selector('body > div.form_box > div.box_content > div').click()
        self.scrollDown(driver)
        hasReadBtn=self.getinfo.setCommonConfig(11, 5)
        driver.execute_script("$('#hasReadBtn').click()")
        
    def scrollUp(self,driver):
        js="var q=document.documentElement.scrollTop=0"
        driver.execute_script(js)
        
    def scrollDown(self,driver):
        driver.find_element_by_xpath("/html/body/div[12]/div[2]/div").send_keys(Keys.DOWN)
        driver.find_element_by_xpath("/html/body/div[12]/div[2]/div").send_keys(Keys.DOWN)
        driver.find_element_by_xpath("/html/body/div[12]/div[2]/div").send_keys(Keys.DOWN)
        driver.find_element_by_xpath("/html/body/div[12]/div[2]/div").send_keys(Keys.DOWN)
        driver.find_element_by_xpath("/html/body/div[12]/div[2]/div").send_keys(Keys.DOWN)
        driver.find_element_by_xpath("/html/body/div[12]/div[2]/div").send_keys(Keys.DOWN)
        driver.find_element_by_xpath("/html/body/div[12]/div[2]/div").send_keys(Keys.DOWN)
        driver.find_element_by_xpath("/html/body/div[12]/div[2]/div").send_keys(Keys.DOWN)
        driver.find_element_by_xpath("/html/body/div[12]/div[2]/div").send_keys(Keys.DOWN)
        #driver.find_element_by_xpath("/html/body/div[12]/div[2]/div").send_keys(Keys.DOWN)
        
    def waitForElement(self,driver,xpath):
        try:
            WebDriverWait(driver,10).until(lambda the_driver: the_driver.find_element_by_xpath(xpath), "not found!")
            print "found!"
        except Exception,error:
            print error
            pass
        
    def switchToIframe(self,driver):
        contentIframe=self.getinfo.setContentIframe()
        driver.switch_to_frame(contentIframe)
            
    def readPublishINfo(self,driver):
        try:
            #self.scrollDown(driver)
            PubBtnXpath=self.getinfo.setElementConfig(39, 5)
            self.click(driver, PubBtnXpath)
            #driver.execute_script("$('#hasReadBtn').click()")
            time.sleep(2)
            print "读取推送消息成功！"
        except:
            print "没有推送消息！"
    
    def click(self,driver,xpath):
        try:
            driver.find_element_by_xpath(xpath).click()
        except Exception,error:
            print "element did not found!"+xpath
            print error
            
    def sendContent(self,driver,xpath,content):
        try:
            self.clearContent(driver, xpath, content)
            driver.find_element_by_xpath(xpath).send_keys(content)
        except Exception,error:
            print "content did not sended!"
            print error
            
    def clearContent(self,driver,xpath,content):
        try:
            driver.find_element_by_xpath(xpath).clear()
        except Exception,error:
            print "content did not clean!"
            print error
            
    def getElementText(self,driver,xpath):
        try:
            result=driver.find_element_by_xpath(xpath).text
        except Exception,error:
            print "element value did not found!"
            print error
        
        return result
           
    def moveToElement(self,driver,xpath):
        element=driver.find_element_by_xpath(xpath)
        try:
            ActionChains(driver).move_to_element(element).perform()
            time.sleep(2)
        except Exception,error:
            print "Can't move to element:"+xpath
            print error
            
    def conn(self,sql):
        try:
            conndb=MySQLdb.Connect(host='10.28.6.55', user='root', passwd='123456', db='onepay',port=3307)
            cur=conndb.cursor()
            #cur.select_db('onepay3')
            cur.execute(sql)
            result=cur.fetchone()
            cur.close
            conndb.close
            return result
        except MySQLdb.Error,e:
            print (e.args[0], e.args[1])
            
        