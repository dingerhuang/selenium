#!C:\Python27\python
# -*- coding: utf-8 -*-
'''
Created on 2016年6月20日

@author: tc
'''

import unittest,time,sys
from common_actions.commonActions import CommonActions
from common_actions.telePhoneActions import TeleActions


class TeleRecharge(unittest.TestCase):
    
    def setUp(self):

        self.commonActions=CommonActions()
        self.teleActions=TeleActions()
        self.driver=self.commonActions.login()
               
    def qtest_teleRecharge001(self):
        u"""话费充值"""
        #18200583387充值10元
        driver=self.driver
        self.teleActions.teleRecharge(driver,1, 0, 1, 1)
        result=self.commonActions.verifyMbRecharge(driver)
        print result
        self.assertEqual(True, result, u'固话充值校验失败:'+sys._getframe().f_code.co_name)
        driver.close()
        
    def qtest_teleRecharge002(self):
        u"""话费充值"""
        #18200583387充值10元
        driver=self.driver
        self.teleActions.teleRecharge(driver,2, 0, 2, 1)
        result=self.commonActions.verifyMbRecharge(driver)
        print result
        self.assertEqual(True, result, u'固话充值校验失败:'+sys._getframe().f_code.co_name)
        driver.close()
        
    def qtest_teleRecharge003(self):
        u"""话费充值"""
        #18200583387充值10元
        driver=self.driver
        self.teleActions.teleRecharge(driver,3, 0, 3, 1)
        result=self.commonActions.verifyMbRecharge(driver)
        print result
        self.assertEqual(True, result, u'固话充值校验失败:'+sys._getframe().f_code.co_name)
        driver.close()
        
    def qtest_teleRecharge004(self):
        u"""话费充值"""
        #18200583387充值10元
        driver=self.driver
        self.teleActions.teleRecharge(driver,4, 0, 4, 1)
        result=self.commonActions.verifyMbRecharge(driver)
        print result
        self.assertEqual(True, result, u'固话充值校验失败:'+sys._getframe().f_code.co_name)
        driver.close()
    
    def qtest_teleRecharge005(self):
        u"""话费充值"""
        #省市检查
        driver=self.driver
        result=self.teleActions.teleRechargeProvinceCheck(driver,7, 0, 7, 1)
        print result
        self.assertEqual(True, result, u'固话充值校验失败:'+sys._getframe().f_code.co_name)
        driver.close()
        
    def qtest_teleRecharge006(self):
        u"""话费充值"""
        #省市检查
        driver=self.driver
        result=self.teleActions.teleRechargeProvinceCheck(driver,8, 0, 8, 1)
        print result
        self.assertEqual(True, result, u'固话充值校验失败:'+sys._getframe().f_code.co_name)
        driver.close()
        
    def qtest_teleRecharge007(self):
        u"""话费充值"""
        #核对号码
        driver=self.driver
        result=self.teleActions.teleRechargeNumCheck(driver,9, 0, 9, 1)
        print result
        self.assertEqual(True, result, u'固话充值校验失败:'+sys._getframe().f_code.co_name)
        driver.close()
        
    def qtest_teleRecharge008(self):
        u"""话费充值"""
        #取消支付
        driver=self.driver
        area_num=self.teleActions.cancleRecharge(driver,5, 0, 5, 1)
        result=self.teleActions.verifyCancleRecharge(driver, area_num)
        print result
        self.assertEqual(True, result, u'固话充值校验失败:'+sys._getframe().f_code.co_name)
        driver.close()
        
    def qtest_teleRecharge009(self):
        u"""话费充值"""
        #继续支付
        driver=self.driver
        self.teleActions.continueRecharge(driver,6, 0, 6, 1)
        result=self.commonActions.verifyMbRecharge(driver)
        print result
        self.assertEqual(True, result, u'固话充值校验失败:'+sys._getframe().f_code.co_name)
        driver.close()
        
    def qtest_teleRecharge010(self):
        u"""话费充值"""
        #不支持该类号码
        driver=self.driver
        self.teleActions.teleRechargeError(driver,10, 0, 10, 1)
        result=self.teleActions.verifyTeleRechargeNotSupport(driver)
        print result
        self.assertEqual(True, result, u'固话充值校验失败:'+sys._getframe().f_code.co_name)
        driver.close()
        
    def qtest_teleRecharge011(self):
        u"""话费充值"""
        #号码异常
        driver=self.driver
        self.teleActions.teleRechargeError(driver,11, 0, 11, 1)
        result=self.teleActions.verifyTeleRechargeError(driver)
        print result
        self.assertEqual(True, result, u'固话充值校验失败:'+sys._getframe().f_code.co_name)
        driver.close()
        
    def qtest_teleRecharge012(self):
        u"""话费充值"""
        #号码异常
        driver=self.driver
        self.teleActions.teleRechargeError(driver,12, 0, 12, 1)
        result=self.teleActions.verifyTeleRechargeError(driver)
        print result
        self.assertEqual(True, result, u'固话充值校验失败:'+sys._getframe().f_code.co_name)
        driver.close()
        
    def qtest_teleRecharge013(self):
        u"""话费充值"""
        #号码异常
        driver=self.driver
        self.teleActions.teleRechargeError(driver,13, 0, 13, 1)
        result=self.teleActions.verifyTeleRechargeError(driver)
        print result
        self.assertEqual(True, result, u'固话充值校验失败:'+sys._getframe().f_code.co_name)
        driver.close()
        
    def qtest_teleRecharge014(self):
        u"""话费充值"""
        #进货价验证
        driver=self.driver
        result=self.teleActions.teleRechargePriceCheck(driver,14, 0, 14, 1,5,8)
        print result
        self.assertEqual(True, result, u'固话充值校验失败:'+sys._getframe().f_code.co_name)
        driver.close()
        
    def qtest_teleRecharge015(self):
        u"""话费充值"""
        #进货价验证
        driver=self.driver
        result=self.teleActions.teleRechargePriceCheck(driver,15, 0, 15, 1,6,8)
        print result
        self.assertEqual(True, result, u'固话充值校验失败:'+sys._getframe().f_code.co_name)
        driver.close()
        
    def qtest_teleRecharge016(self):
        u"""话费充值"""
        #进货价验证
        driver=self.driver
        result=self.teleActions.teleRechargePriceCheck(driver,16, 0, 16, 1,7,8)
        print result
        self.assertEqual(True, result, u'固话充值校验失败:'+sys._getframe().f_code.co_name)
        driver.close()
        
    def qtest_teleRecharge017(self):
        u"""话费充值"""
        #进货价验证
        driver=self.driver
        result=self.teleActions.teleRechargePriceCheck(driver,17, 0, 17, 1,8,8)
        print result
        self.assertEqual(True, result, u'固话充值校验失败:'+sys._getframe().f_code.co_name)
        driver.close()
        
    def test_teleRecharge018(self):
        u"""话费充值"""
        #订单取消
        driver=self.driver
        area_num=self.teleActions.cancleOrder(driver,18, 0, 18, 1)
        result=self.teleActions.verifyCancleOrder(driver, area_num)
        print result
        self.assertEqual(True, result, u'固话充值校验失败:'+sys._getframe().f_code.co_name)
        driver.close()
        
    def tearDown(self):
        self.driver.quit()
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
        