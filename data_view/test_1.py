# -*- coding: utf-8 -*-

import pymysql
import matplotlib.pyplot as plt

# plt.rcParams['font.sas-serig']=['SimHei'] #用来正常显示中文标签
# plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

def get_sql():
    ##获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库
    db=pymysql.connect(host="127.0.0.1",user='root',passwd="ljc123",port=3306,db="wyjob",charset='utf8')
    cursor=db.cursor()#获取一个游标
    sql="select place,salary from wyjob_php"
    cursor.execute(sql)
    result=cursor.fetchall() #result为元组
    cursor.close()#关闭游标
    db.close()#关闭数据库
    return result


def make_bar():

    #将元组数据存进列表中
    city=[]
    salary=[]

    result = get_sql()
    for x in result:
        city.append(x[0])
        salary.append(x[1])


    #直方图
    plt.bar(range(len(salary)), salary, color='steelblue', tick_label=city)
    plt.xlabel("所属城市")
    plt.ylabel("平均薪水")
    plt.title("城市职位需求图")
    for  x,y in enumerate(salary):
        plt.text(x-0.4, y+0.4, '%s' % y)
    plt.show()


def change_data():
    print(111)
    # for id in range(1,1500):
    id = 1
    # 打开数据库连接
    db = pymysql.connect(host="localhost", user='root', passwd="ljc123", port=3306, db="wyjob")

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    s = 'select * from wyjob_php'

    cursor.execute(s)

    res = cursor.fetchall()

    print(res)

    cursor.close()#关闭游标
    db.close()#关闭数据库

