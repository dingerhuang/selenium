#!C:\Python27\python
# -*- coding: utf-8 -*- 
'''
Created on 2016年7月5日

@author: tc
'''
import unittest,sys,time
from common_actions.commonActions import CommonActions
from common_actions.queryOrder import QueryOrder

class QueryInfo(unittest.TestCase):


    def setUp(self):
        print "==="
        self.commonActions=CommonActions()
        self.queryOrder=QueryOrder()
        self.driver=self.commonActions.login_ff()
        print "1"


    def tearDown(self):
        self.driver.quit()


    def test_md001(self):
        driver=self.driver
        self.queryOrder.accessQueryOrder(driver)
        print "2"
        

        time.sleep(20)
        driver.close()
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()