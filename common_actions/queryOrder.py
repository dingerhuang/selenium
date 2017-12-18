#!C:\Python27\python
# -*- coding: utf-8 -*- 
'''
Created on 2016年8月2日

@author: tc
'''
import time
from common_actions.commonActions import CommonActions
from setparameters.modifyInfoElements import ModifyInfoElements

class QueryOrder():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.commonActions=CommonActions()
        self.getinfo=ModifyInfoElements()
        
    def accessQueryOrder(self,driver):
        self.commonActions.readPublishINfo(driver)
        queryOrderXpath='//*[@class="menu_list clearfix"]/li[4]/a/span[2]'
        self.commonActions.click(driver, queryOrderXpath)
        iframe='contentIframeTwo'
        driver.switch_to_frame(iframe)
        #时间选择
        bgnTimeXpath='//*[@id="myCommissonStart"]'
        self.commonActions.click(driver, bgnTimeXpath)
        time.sleep(2)
        driver.switch_to_default_content()
        iframeXpath='//*[@src="about:blank"]'
        iframe1=driver.find_element_by_xpath(iframeXpath)
        print "123"
        driver.switch_to_frame(iframe1)
        
        yesterdayXpath='//*[@class="WdayTable"]/tbody/tr[7]/td[2]'
        self.commonActions.click(driver, yesterdayXpath)
        
        
        time.sleep(6)
        driver.switch_to_default_content()
        driver.switch_to_frame(iframe)
        queryOrderBtnXpath='//*[@id="reSearch"]'
        self.commonActions.click(driver, queryOrderBtnXpath)
        
        