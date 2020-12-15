import pymysql

class MysqlUtils:
    con = None
    cursor = None

    @classmethod
    def read(cls,host="localhost",database="bank",user="root",password="",tablename="person"):
        #获取链接
        cls.con = pymysql.connect(host=host,user=user,password=password,database=database,charset="utf8")
        #获取游标
        cls.cursor = cls.con.cursor()
        #返回参数化数据
        sql = '''
            select * from {tablename}
        '''
        cls.cursor.execute(sql.format(tablename=tablename))
        return cls.cursor.fetchall()























