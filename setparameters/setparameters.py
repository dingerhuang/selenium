#!C:\Python27\python
# -*- coding: utf-8 -*-
'''
Created on 2016年6月13日

@author: tc
'''
import xlrd


class SetParameters():
    def __init__(self):
        pass
        
    def getcell(self,sheet,row,col):
        data=xlrd.open_workbook("E:\\workspace\\berbon\\config\\berbon.xls",encoding_override="utf-8")
        #table = data.sheets()[0]
        table = data.sheet_by_name(sheet.encode('utf-8'))
        cell = table.cell(row,col).value

        return cell

    def setCommonConfig(self,row,col):
        result=self.getcell(u'基础配置', row, col)
        return result
    
    def setElementConfig(self,row,col):
        result=self.getcell(u'页面配置', row, col)
        return result
    
    def setMbRecharge(self,row,col):
        phonenumber=self.getcell(u'话费充值', row, col)
        try:
            return int(phonenumber)
        except:
            return phonenumber
        
    def setTelePhoneConfig(self,row,col):
        result=self.getcell(u'固话充值', row, col)
        return result
    
    def setAdRechargeConfig(self,row,col):
        result=self.getcell(u'广西河南移动优势充值', row, col)
        return result
    
    def setContentIframe(self):
        #进入content iframe
        result=self.getcell(u'页面配置', 8, 5)
        return result

    def setAcConfig(self,row,col):
        #获取我的账户xpath
        result=self.getcell(u'账户中心', row, col)
        return result
    
    def setMyAccountXpath(self):
        #获取我的账户xpath
        result=self.getcell(u'账户中心', 10, 3)
        return result
    
    def setAccountCenterXpath(self):
        #获取我的账户xpath
        result=self.getcell(u'账户中心', 11, 3)
        return result
    
    def setTotalBalanceXpath(self):
        #获取账户总资产
        result=self.getcell(u'账户中心', 4, 3)
        return result
    
    def setBalanceXpath(self):
        #获取账户可用余额
        result=self.getcell(u'账户中心', 5, 3)
        return result
    
    def setFrozenXpath(self):
        #获取账户冻结余额
        result=self.getcell(u'账户中心', 6, 3)
        return result
    
    def setCardAddXpath(self):
        #获取添加银行卡按钮xpath
        result=self.getcell(u'账户中心', 8, 3)
        return result
    
    def setChoseOtherCardXpath(self):
        #获取选择其他银行卡
        result=self.getcell(u'账户中心', 12, 3)
        return result
    
    def setChoseJSXpath(self):
        #获取选中国建设银行
        result=self.getcell(u'账户中心', 13, 3)
        return result
    
    def setChoseNYXpath(self):
        #获取选择中国农业银行
        result=self.getcell(u'账户中心', 14, 3)
        return result
    
    def setBankNumXpath(self):
        #获取银行卡号
        result=self.getcell(u'账户中心', 15, 3)
        return result
    
    def setPhoneNumXpath(self):
        #获取手机号码
        result=self.getcell(u'账户中心', 16, 3)
        return result
    
    def setSendVerCodeXpath(self):
        #获取发送验证码
        result=self.getcell(u'账户中心', 17, 3)
        return result
    
    def setVerCodeXpath(self):
        #获取验证码
        result=self.getcell(u'账户中心', 18, 3)
        return result
    
    def setDredgeQuickPay(self):
        #开通快捷支付
        result=self.getcell(u'账户中心', 19, 3)
        return result
    