#!C:\Python27\python
# -*- coding: utf-8 -*- 
'''
Created on 2016年6月20日

@author: tc
'''
import unittest,time,sys
from common_actions.commonActions import CommonActions
from common_actions.accountCenterActions import AcountCenterActions


class AccountCenter(unittest.TestCase):


    def setUp(self):
        self.commonActions=CommonActions()
        self.acActions=AcountCenterActions()
        self.driver=self.commonActions.login()


    def tearDown(self):
        self.driver.quit()


    def qtest_ac001(self):
        u"""账户中心-账户金额校验"""
        driver=self.driver
        data=self.acActions.checkUserInfo(driver)
        result=self.acActions.verifyUserInfo(driver, data)
        print result
        self.assertEqual(True, result, u'话费充值校验失败:'+sys._getframe().f_code.co_name)
        driver.close()
        
    def qtest_ac002(self):
        u"""账户中心-添加银行卡"""
        driver=self.driver
        data=self.acActions.cardAdd(driver,13,3,13,4)
        
        driver.close()

    def test_ac003(self):
        u"""账户中心-添加银行卡"""
        driver=self.driver
        data=self.acActions.cardAdd(driver,14,3,14,4)
        
        driver.close()
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()