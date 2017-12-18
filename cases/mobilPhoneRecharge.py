#!C:\Python27\python
# -*- coding: utf-8 -*-
'''
Created on 2016年5月27日

@author: tc
'''
import unittest,time,sys
from common_actions.commonActions import CommonActions
from setparameters.setparameters import SetParameters

class MobilePhoneRecharge(unittest.TestCase):
    def setUp(self):

        self.actions=CommonActions()
        self.driver=self.actions.login()
        self.settIng=SetParameters()
        
    def qtest_mpRecharge001(self):
        u"""话费充值"""
        #18200583387充值10元
        driver=self.driver
        self.actions.mbRecharge(driver,6, 4, 16, 5)
        result=self.actions.verifyMbRecharge(driver)
        print result
        self.assertEqual(True, result, u'话费充值校验失败:'+sys._getframe().f_code.co_name)
        
        self.driver.close()
        
    def qtest_mpRecharge002(self):
        u"""话费充值"""
        driver=self.driver
        #18200583387充值10元
        self.actions.mbRecharge(driver,7, 4, 17, 5)
        result=self.actions.verifyMbRecharge(driver)
        print result
        self.assertEqual(True, result, u'话费充值校验失败:'+sys._getframe().f_code.co_name)
        
        self.driver.close()
        
    def qtest_mpRecharge003(self):
        u"""话费充值"""
        #18200583387充值10元
        driver=self.driver
        self.actions.mbRecharge(driver,8, 4, 18, 5)
        result=self.actions.verifyMbRecharge(driver)
        print result
        self.assertEqual(True, result, u'话费充值校验失败:'+sys._getframe().f_code.co_name)
        
        self.driver.close()
        
    def qtest_mpRecharge004(self):
        u"""话费充值"""
        #18200583387充值10元
        driver=self.driver
        self.actions.mbRecharge(driver,8, 4, 19, 5)
        result=self.actions.verifyMbRecharge(driver)
        print result
        self.assertEqual(True, result, u'话费充值校验失败:'+sys._getframe().f_code.co_name)
        
        self.driver.close()
        
    def qtest_mpRecharge005(self):
        u"""话费充值"""
        #18200583387充值10元
        driver=self.driver
        self.actions.mbRecharge(driver,9, 4, 20, 5)
        result=self.actions.verifyMbRecharge(driver)
        print result
        self.assertEqual(True, result, u'话费充值校验失败:'+sys._getframe().f_code.co_name)
        
        self.driver.close()
        
    def qtest_mpRecharge006(self):
        u"""话费充值"""
        #18200583387充值10元
        driver=self.driver
        self.actions.mbRecharge(driver,10, 4, 21, 5)
        result=self.actions.verifyMbRecharge(driver)
        print result
        self.assertEqual(True, result, u'话费充值校验失败:'+sys._getframe().f_code.co_name)
        
        self.driver.close()
        
    def qtest_mpRecharge007(self):
        u"""话费充值"""
        #18200583387充值10元
        driver=self.driver
        self.actions.mbRecharge(driver,11, 4, 22, 5)
        result=self.actions.verifyMbRecharge(driver)
        print result
        self.assertEqual(True, result, u'话费充值校验失败:'+sys._getframe().f_code.co_name)
        
        self.driver.close()
        
    def qtest_mpRecharge008(self):
        u"""话费充值"""
        #18200583387充值10元
        driver=self.driver
        self.actions.mbRecharge(driver,12, 4, 23, 5)
        result=self.actions.verifyMbRecharge(driver)
        print result
        self.assertEqual(True, result, u'话费充值校验失败:'+sys._getframe().f_code.co_name)
        
        self.driver.close()
    def qtest_mpRecharge009(self):
        u"""话费充值"""
        #18200583387省市检查
        driver=self.driver
        result=self.actions.rechargeProvinceCheck(driver,12, 4)
        print result
        self.assertEqual(True, result, u'话费充值校验失败:'+sys._getframe().f_code.co_name)
        
        self.driver.close()
    def qtest_mpRecharge010(self):
        u"""话费充值"""
        #18200583387省市检查
        driver=self.driver
        result=self.actions.rechargeProvinceCheck(driver,11, 4)
        print result
        self.assertEqual(True, result, u'话费充值校验失败:'+sys._getframe().f_code.co_name)
        
        self.driver.close()
        
    def qtest_mpRecharge011(self):
        u"""话费充值"""
        #18200583387省市检查
        driver=self.driver
        result=self.actions.rechargeProvinceCheck(driver,10, 4)
        print result
        self.assertEqual(True, result, u'话费充值校验失败:'+sys._getframe().f_code.co_name)
        
        self.driver.close()
        
    def qtest_mpRecharge012(self):
        u"""话费充值"""
        #18200583387省市检查
        driver=self.driver
        result=self.actions.rechargeProvinceCheck(driver,9, 4)
        print result
        self.assertEqual(True, result, u'话费充值校验失败:'+sys._getframe().f_code.co_name)
        
        self.driver.close()
        
    def qtest_mpRecharge013(self):
        u"""话费充值"""
        #18200583387省市检查
        driver=self.driver
        result=self.actions.rechargeProvinceCheck(driver,8, 4)
        print result
        self.assertEqual(True, result, u'话费充值校验失败:'+sys._getframe().f_code.co_name)
        
        self.driver.close()
        
    def qtest_mpRecharge014(self):
        u"""话费充值"""
        #18200583387省市检查
        driver=self.driver
        result=self.actions.rechargeProvinceCheck(driver,7, 4)
        print result
        self.assertEqual(True, result, u'话费充值校验失败:'+sys._getframe().f_code.co_name)
        
        self.driver.close()
        
    def qtest_mpRecharge015(self):
        u"""话费充值"""
        #18200583387省市检查
        driver=self.driver
        result=self.actions.rechargeProvinceCheck(driver,6, 4)
        print result
        self.assertEqual(True, result, u'话费充值校验失败:'+sys._getframe().f_code.co_name)
        
        self.driver.close()
        
    def qtest_mpRecharge016(self):
        u"""话费充值"""
        #18200583387余额查询
        driver=self.driver
        queryInfo=self.actions.balanceQuery(driver,6, 4)
        result=self.actions.varifybalanceQuery(queryInfo)
        print result
        self.assertEqual(True, result, u'话费充值校验失败:'+sys._getframe().f_code.co_name)
        
        self.driver.close()
        
    def qtest_mpRecharge017(self):
        u"""话费充值"""
        #电话号码位数不够
        driver=self.driver
        self.actions.mbRechargeError(driver,14, 4, 16, 5)
        result=self.actions.verifyMbRecharge(driver)
        print result
        self.assertEqual(True, result, u'话费充值校验失败:'+sys._getframe().f_code.co_name)
        
        self.driver.close()
        
    def qtest_mpRecharge018(self):
        u"""话费充值"""
        #不是电话号码
        driver=self.driver
        self.actions.mbRechargeError(driver,15, 4, 16, 5)
        result=self.actions.verifyMbRechargeError(driver)
        print result
        self.assertEqual(True, result, u'话费充值校验失败:'+sys._getframe().f_code.co_name)
        
        self.driver.close()
 
    def qtest_mpRecharge019(self):
        u"""话费充值"""
        #取消支付
        driver=self.driver
        number=self.actions.mbRechargeCancle(driver,16, 4, 16, 5)
        result=self.actions.verifymbRechargeCancle(driver,number)
        print result
        self.assertEqual(True, result, u'话费充值校验失败:'+sys._getframe().f_code.co_name)
        
        self.driver.close()
        
    def qtest_mpRecharge020(self):
        u"""话费充值"""
        #继续支付
        driver=self.driver
        self.actions.mbRechargeContinue(driver,16, 4, 16, 5)
        result=self.actions.verifyMbRecharge(driver)
        print result
        self.assertEqual(True, result, u'话费充值校验失败:'+sys._getframe().f_code.co_name)
        
        self.driver.close()
        
    def test_mpRecharge023(self):
        u"""话费充值"""
        #订单取消
        driver=self.driver
        result=self.actions.mbRechargeCancleOrder(driver,17, 4, 16, 5)
        print result
        self.assertEqual(True, result, u'话费充值校验失败:'+sys._getframe().f_code.co_name)
        
        self.driver.close()
        
    
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()