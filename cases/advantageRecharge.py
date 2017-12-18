#!C:\Python27\python
# -*- coding: utf-8 -*-
'''
Created on 2016年6月20日

@author: tc
'''

import unittest,time,sys
from common_actions.commonActions import CommonActions
from common_actions.advantageRechargeActions import AdvantageActions


class advantageActions(unittest.TestCase):


    def setUp(self):
        self.commonActions=CommonActions()
        self.adActions=AdvantageActions()
        self.driver=self.commonActions.login()


    def tearDown(self):
        self.driver.quit()


    def qtest_adRecharge001(self):
        u"""优势话费充值"""
        driver=self.driver
        self.adActions.adRecharge(driver, 1, 0, 16, 5)
        result=self.commonActions.verifyMbRecharge(driver)
        print result
        self.assertEqual(True, result, u'话费充值校验失败:'+sys._getframe().f_code.co_name)
        driver.close()
        
    def qtest_adRecharge002(self):
        u"""优势话费充值"""
        driver=self.driver
        self.adActions.adRecharge(driver, 2, 0, 17, 5)
        result=self.commonActions.verifyMbRecharge(driver)
        print result
        self.assertEqual(True, result, u'话费充值校验失败:'+sys._getframe().f_code.co_name)
        driver.close()

    def qtest_adRecharge003(self):
        u"""优势话费充值"""
        driver=self.driver
        self.adActions.adRecharge(driver, 3, 0, 18, 5)
        result=self.commonActions.verifyMbRecharge(driver)
        print result
        self.assertEqual(True, result, u'话费充值校验失败:'+sys._getframe().f_code.co_name)
        driver.close()
        
    def qtest_adRecharge004(self):
        u"""优势话费充值"""
        driver=self.driver
        self.adActions.adRecharge(driver, 4, 0, 19, 5)
        result=self.commonActions.verifyMbRecharge(driver)
        print result
        self.assertEqual(True, result, u'话费充值校验失败:'+sys._getframe().f_code.co_name)
        driver.close()

    def qtest_adRecharge005(self):
        u"""优势话费充值"""
        driver=self.driver
        self.adActions.adRecharge(driver, 5, 0, 20, 5)
        result=self.commonActions.verifyMbRecharge(driver)
        print result
        self.assertEqual(True, result, u'话费充值校验失败:'+sys._getframe().f_code.co_name)
        driver.close()
        
    def qtest_adRecharge006(self):
        u"""优势话费充值"""
        driver=self.driver
        self.adActions.adRecharge(driver, 6, 0, 22, 5)
        result=self.commonActions.verifyMbRecharge(driver)
        print result
        self.assertEqual(True, result, u'话费充值校验失败:'+sys._getframe().f_code.co_name)
        driver.close()
        
    def qtest_adRecharge007(self):
        u"""优势话费充值"""
        driver=self.driver
        self.adActions.adRecharge(driver, 7, 0, 23, 5)
        result=self.commonActions.verifyMbRecharge(driver)
        print result
        self.assertEqual(True, result, u'话费充值校验失败:'+sys._getframe().f_code.co_name)
        driver.close()
        
    def qtest_adRecharge008(self):
        u"""优势话费充值-不是优势地区"""
        driver=self.driver
        info=self.adActions.disAdRecharge(driver, 8, 0)
        
        result=self.adActions.verifyDisAdRecharge(info)
        print result
        self.assertEqual(True, result, u'话费充值校验失败:'+sys._getframe().f_code.co_name)
        driver.close()
        
    def qtest_adRecharge009(self):
        u"""优势话费充值-不是优势地区"""
        driver=self.driver
        info=self.adActions.disAdRecharge(driver, 9, 0)
        
        result=self.adActions.verifyAdRechargeErrorNum(info)
        print result
        self.assertEqual(True, result, u'话费充值校验失败:'+sys._getframe().f_code.co_name)
        driver.close()
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()