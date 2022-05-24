# -*-coding:utf-8 -*-
import pymysql

class Case():
    def __init__(self):
        try:
            self.db = pymysql.connect(host="124.71.80.188",port=13006,user="jmeter",password="5@VR4tOk1#TTz5XY",database="jmeter_test", charset="utf8mb4")
            self.cursor = self.db.cursor()
            print("connect success")
        except Exception as e:
            print("connect fail")

    def insert(self):
        pass

    def delete(self):
        pass

    def edit(self):
        pass

    def query(self,param_dict):
        sql = 'select * from api_case'
        if len(param_dict) > 0:
            sql = sql + ' where'
            for k,v in param_dict.items():
                sql = sql + (" {} like '%{}%' and".format(k,v))
                sql = sql.rstrip('and')
                sql = sql + ';'
        elif len(param_dict) == 0:
            sql = 'select * from api_case;'
        # print(sql)
        # sql = 'select * from api_case where {} like {};'.format(param,value)
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

    def queryProName(self):
        sql = 'select distinct(app_Name) from api_info;'
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        # fetchall把每一行结果作为一个元组返回(result,)
        return result

    def __del__(self):
        self.db.close()


if __name__ == '__main__':
    case = Case()
    case.search({'a':1,'b':2})

