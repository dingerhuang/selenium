#!C:\Python27\python
# -*- coding: utf-8 -*- 
'''
Created on 2016年7月5日

@author: tc
'''

import xlrd

class ModifyInfoElements(object):
    '''
    classdocs
    '''


    def __init__(self):
        pass
    
    def getcell(self,sheet,row,col):
        data=xlrd.open_workbook("E:\\workspace\\berbon\\config\\berbon.xls",encoding_override="utf-8")
        #table = data.sheets()[0]
        table = data.sheet_by_name(sheet.encode('utf-8'))
        cell = table.cell(row,col).value

        return cell
    
    def getModifyInfo(self,row,col):
        result=self.getcell(u'资料修改', row, col)
        return result
    
    def getSafeCenterXpath(self):
        #安全中心xpath
        result=self.getcell(u'资料修改', 1, 1)
        return result
    
    def getModifyInfoXpath(self):
        #资料修改xpath
        result=self.getcell(u'资料修改', 2, 1)
        return result
    
    def getModifyBtnXpath(self):
        #立即修改xpath
        result=self.getcell(u'资料修改', 3, 1)
        return result
    
    def getShopNameXpath(self):
        #店铺名称xpath
        result=self.getcell(u'资料修改', 4, 1)
        return result
    
    def getShopTypeXpath(self):
        #店铺类型xpath
        result=self.getcell(u'资料修改', 5, 1)
        return result
    
    def getTeleShopXpath(self):
        #通讯店xpath
        result=self.getcell(u'资料修改', 6, 1)
        return result
    
    def getConvenienceShopXpath(self):
        #便利店xpath
        result=self.getcell(u'资料修改', 7, 1)
        return result
    
    def getKioskXpath(self):
        #报刊亭xpath
        result=self.getcell(u'资料修改', 8, 1)
        return result
    
    def getTelePhoneShopXpath(self):
        #手机卖场xpath
        result=self.getcell(u'资料修改', 9, 1)
        return result
    
    def getOtherXpath(self):
        #其他xpath
        result=self.getcell(u'资料修改', 10, 1)
        return result
    
    def getProvinceXpath(self):
        #省份xpath
        result=self.getcell(u'资料修改', 11, 1)
        return result
    
    def getCityXpath(self):
        #地市xpath
        result=self.getcell(u'资料修改', 12, 1)
        return result
    
    def getAreaXpath(self):
        #地区xpath
        result=self.getcell(u'资料修改', 13, 1)
        return result
    
    def getAddressXpath(self):
        #地址xpath
        result=self.getcell(u'资料修改', 14, 1)
        return result
    
    def getQQNumXpath(self):
        #QQ号码xpath
        result=self.getcell(u'资料修改', 15, 1)
        return result
    
    def getConfirmBtnXpath(self):
        #确认xpath
        result=self.getcell(u'资料修改', 16, 1)
        return result
    
    def getSuccessInfoXpath(self):
        #修改成功xpath
        result=self.getcell(u'资料修改', 17, 1)
        return result