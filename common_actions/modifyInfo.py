#!C:\Python27\python
# -*- coding: utf-8 -*- 
'''
Created on 2016年7月5日

@author: tc
'''
import time
from common_actions.commonActions import CommonActions
from setparameters.modifyInfoElements import ModifyInfoElements
class ModifyInfo():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.commonActions=CommonActions()
        self.getinfo=ModifyInfoElements()
        
    def accessModifyInfo(self,driver):
        self.commonActions.readPublishINfo(driver)
        safeCenterXpath=self.getinfo.getSafeCenterXpath()
        modifyInfoXpath=self.getinfo.getModifyInfoXpath()
        modifyNowXpath=self.getinfo.getModifyBtnXpath()
        self.commonActions.moveToElement(driver, safeCenterXpath)
        #self.commonActions.switchToIframe(driver)
        self.commonActions.click(driver, modifyInfoXpath)
        self.commonActions.switchToIframe(driver)
        self.commonActions.click(driver, modifyNowXpath)
        
    def modifyInfo(self,driver,sn_row,sn_col,st_row,st_col,p_row,p_col,c_row,c_col,a_row,a_col,ad_row,ad_col,qq_row,qq_col):
        self.accessModifyInfo(driver)
        #填写店铺名称
        shopNameXpath=self.getinfo.getShopNameXpath()
        shopName=self.getinfo.getModifyInfo(sn_row,sn_col)
        self.commonActions.sendContent(driver, shopNameXpath, shopName)
        #填写店铺类型
        shopTypeXpath=self.getinfo.getShopTypeXpath()
        shopType=self.getinfo.getModifyInfo(st_row,st_col)
        self.commonActions.click(driver, shopTypeXpath)
        self.commonActions.click(driver, shopType)
        #选择省份
        provinceXpath=self.getinfo.getProvinceXpath()
        self.commonActions.click(driver, provinceXpath)
        province=self.getinfo.getModifyInfo(p_row,p_col)
        self.commonActions.click(driver, province)
        #选择城市
        cityXpath=self.getinfo.getCityXpath()
        self.commonActions.click(driver, cityXpath)
        city=self.getinfo.getModifyInfo(c_row,c_col)
        self.commonActions.click(driver, city)
        #选择地区
        areaXpath=self.getinfo.getAreaXpath()
        self.commonActions.click(driver, areaXpath)
        area=self.getinfo.getModifyInfo(a_row,a_col)
        self.commonActions.click(driver, area)
        #填写地址
        addressXpath=self.getinfo.getAddressXpath()
        address=self.getinfo.getModifyInfo(ad_row,ad_col)
        self.commonActions.sendContent(driver, addressXpath, address)
        qqNumXpath=self.getinfo.getQQNumXpath()
        qqNum=self.getinfo.getModifyInfo(qq_row,qq_col)
        self.commonActions.sendContent(driver, qqNumXpath, qqNum)
        
        #点击确定
        confirmXpath=self.getinfo.getConfirmBtnXpath()
        self.commonActions.click(driver, confirmXpath)
        
    def verifyModifyInfo(self,driver):
        standard=self.getinfo.getModifyInfo(17, 0)
        resultXpath=self.getinfo.getSuccessInfoXpath()
        result=self.commonActions.getElementText(driver, resultXpath)
        flag=False
        print standard,result
        if standard==result:
            flag=True
            return flag
        
        return flag
        