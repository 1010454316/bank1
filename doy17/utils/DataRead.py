from doy17.utils.DBUtils import MysqlUtils
from doy17.utils.Exls import Exls
import os
class DataRead:
    list = None
    def __init__(self,mode,filename="",sheetname="0",host="localhost",database="",user="",password="",tabaename=""):
        if mode == "excel":
            if filename =="":
                raise Exception("文件名不能为空！")
            elif not os.path.isfile(filename):
                raise Exception("文件不存在！")
            else:
                DataRead.list = Exls.read(filename,sheetname)

        elif mode == "database":
            DataRead.list = MysqlUtils.read(host=host,database=database,user=user,password=password,tablename=tabaename)
        else:
            raise Exception("对不起，您的操作无法识别!")
# d = DataRead("database",database="bank",tabaename="person",user="root",password="")
# d = DataRead("excel",filename="F:\\python\\PyCharm 2020.2.1\\pythonProject1\\doy17\\testcase\\1.xlsx",sheetname="0")
# print(d.list)


















