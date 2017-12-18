#!C:\Python27\python
# -*- coding: utf-8 -*- 
'''
Created on 2016年6月20日

@author: tc
'''
import time
from common_actions.commonActions import CommonActions
from setparameters.setparameters import SetParameters


class AcountCenterActions():
    '''
    classdocs
    '''


    def __init__(self):
        self.commonActions=CommonActions()
        self.getinfo=SetParameters()
    
    def accessAc(self,driver):
        self.commonActions.readPublishINfo(driver)
        myAccountXpath=self.getinfo.setMyAccountXpath()
        accountCenterXpath=self.getinfo.setAccountCenterXpath()
        self.commonActions.moveToElement(driver, accountCenterXpath)
        self.commonActions.click(driver, myAccountXpath)
        self.commonActions.switchToIframe(driver)
        
    def checkUserInfo(self,driver):
        self.accessAc(driver)
        sql='select balance,credit_amount,frozen_amount from account_fund where account_id='+"'"+'5279'+"'"
        data=self.commonActions.conn(sql)
        
        return data
    
    def verifyUserInfo(self,driver,data):
        totalBalanceXpath=self.getinfo.setTotalBalanceXpath()
        balanceXpath=self.getinfo.setBalanceXpath()
        frozenXpath=self.getinfo.setFrozenXpath()
        totalBalance=self.commonActions.getElementText(driver, totalBalanceXpath)
        balance=self.commonActions.getElementText(driver, balanceXpath)
        frozen=self.commonActions.getElementText(driver, frozenXpath)
        flag=False
        if data[0]==int(float(totalBalance)*100):
            if data[1]==int(float(balance)*100):
                if data[2]==int(float(frozen)*100):
                    flag=True
                    return flag
                else:
                    print "冻结余额不正确！"
                    return flag
            else:
                print "可用余额不正确！"
                return flag            
        else:
            print "总金额不正确！"
            return flag
        
    def cardAdd(self,driver,card_row,card_col,num_row,num_col):
        self.accessAc(driver)
        #点击添加银行卡
        cardAddXpath=self.getinfo.setCardAddXpath()
        self.commonActions.click(driver, cardAddXpath)
        #点击选择其他银行
        choseOtherBankXpath=self.getinfo.setChoseOtherCardXpath()
        self.commonActions.click(driver, choseOtherBankXpath)
        #选择银行卡
        BankXpath=self.getinfo.setAcConfig(card_row, card_col)
        self.commonActions.click(driver, BankXpath)
        bankNum=self.getinfo.setAcConfig(num_row, num_col)
        bankNumXpath=self.getinfo.setBankNumXpath()
        self.commonActions.sendContent(driver, bankNumXpath, bankNum)
        phoneXpath=self.getinfo.setPhoneNumXpath()
        phoneNum=self.commonActions.userName
        self.commonActions.sendContent(driver, phoneXpath, phoneNum)
        sendVercodeXpath=self.getinfo.setSendVerCodeXpath()
        self.commonActions.click(driver, sendVercodeXpath)
        time.sleep(2)
        #获取验证码
        sql='select version from account_fund where account_id='+"'"+'5279'+"'"
        time.sleep(1)
        data=self.commonActions.conn(sql)
        vercodeXpath=self.getinfo.setVerCodeXpath()
        self.commonActions.sendContent(driver, vercodeXpath, data[0])
        dredgeQuickPayXpath=self.getinfo.setDredgeQuickPay()
        self.commonActions.click(driver, dredgeQuickPayXpath)
        
        return data
        
        