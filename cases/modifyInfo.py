#!C:\Python27\python
# -*- coding: utf-8 -*- 
'''
Created on 2016年7月5日

@author: tc
'''
import unittest,sys,time
from common_actions.commonActions import CommonActions
from common_actions.modifyInfo import ModifyInfo

class ModifyInfoCases(unittest.TestCase):


    def setUp(self):
        self.commonActions=CommonActions()
        self.mdActions=ModifyInfo()
        self.driver=self.commonActions.login()


    def tearDown(self):
        self.driver.quit()


    def qtest_md001(self):
        driver=self.driver
        self.mdActions.modifyInfo(driver, 1, 4, 6, 1, 18, 1, 19, 1, 20, 1, 1, 9, 1, 10)
        result=self.mdActions.verifyModifyInfo(driver)
        
        print result
        self.assertEqual(True, result, u'修改个人信息:'+sys._getframe().f_code.co_name)
        time.sleep(20)
        driver.close()
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()