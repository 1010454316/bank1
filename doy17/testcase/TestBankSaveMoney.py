import unittest
from ddt import ddt
from ddt import data
from ddt import unpack
from doy17.frame.bank import bank_saveMoney
from doy17.frame.bank import bank_addUser
from doy17.utils.DataRead import DataRead

# data1 = DataRead("database",database="bank",tabaename="person",user="root",password="").list
data1 = DataRead("excel",filename="F:\\python\\PyCharm 2020.2.1\\pythonProject1\\doy17\\testcase\\1.xlsx",sheetname="0").list


# @ddt
# class TestCalc(unittest.TestCase):
#     @data(*data1)
#     @unpack
#     def testSaveUser(self,a,b,c,d,e,f,g,h):
#         s = bank_addUser(username=a,password=b,country=c,province=d,street=e,door=f,money=g)
#         self.assertEqual(s,h)



@ddt
class TestBankSoveMoney(unittest.TestCase):

    @data(*data1)
    @unpack
    def testSaveMoney(self,i,j,k):
        s = bank_saveMoney(ac=i,money=j)
        self.assertEqual(s,k)






























