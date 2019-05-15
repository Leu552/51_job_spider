# -*- coding: utf-8 -*-

import pymysql
import matplotlib.pyplot as plt
import re
import urllib3
import requests
import time
from bs4 import BeautifulSoup
import base64
from fake_useragent import UserAgent
ua = UserAgent()

# 打开数据库连接
db = pymysql.connect(host="localhost", user='root', passwd="ljc123", port=3306, db="wyjob")
# 使用cursor()方法获取操作游标
cursor = db.cursor()
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

    for id in range(1,1386):

        # 打开数据库连接
        db = pymysql.connect(host="localhost", user='root', passwd="ljc123", port=3306, db="weibo_cxk")

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        s = 'select salary from wyjob_php where id = %d' % (id)

        cursor.execute(s)

        res = cursor.fetchone()

        print(str(res[0]))
        # print('万'.encode('utf-8'))
        # words = 'study in 山海大学'
        # regex_str = ".*?([\u4E00-\u9FA5]+大学)"
        regex_str = ".*?([0-9]+千)"
        check = re.match(regex_str,str(res[0]))
        # print(check)
        if check:
            try:
                res = str(res[0]).split('千')
                res = str(res[0]).split('-')
                res = (float(res[0])+float(res[1]))/20.0
                print('+++++++++'+str(id)+'+++++++++++')


                u = "UPDATE wyjob_php SET salary = %f WHERE id = '%d'" % (res,id)
                cursor.execute(u)
                # 提交到数据库执行
                db.commit()

            except:
                pass

        cursor.close()#关闭游标
        db.close()#关闭数据库




def get_num(place):

    s = "SELECT id FROM wyjob_php WHERE place = '%s'" % (str(place))

    cursor.execute(s)

    res = cursor.fetchall()

    print(len(res))

    cursor.close()  # 关闭游标
    db.close()  # 关闭数据库
    return len(res)


def get_avr(place):

    s = "SELECT salary,id FROM wyjob_php where salary > 0 AND salary <10 AND place = '%s'" % (str(place))

    cursor.execute(s)

    res = cursor.fetchall()

    salarys = 0

    for i in res:
        print(i[0],i[1])
        salarys += float(i[0])
    avr = salarys/float(len(res))
    print(avr)

    return avr

def delete_data ():

    s = 'select salary,id from wyjob_php'

    cursor.execute(s)

    res = cursor.fetchall()

    for i in res:

        #print(str(i[0]),str(i[1]))
        # print('万'.encode('utf-8'))
        # words = 'study in 山海大学'
        # regex_str = ".*?([\u4E00-\u9FA5]+大学)"
        regex_str = ".*?([0-9]+万)"
        check = re.match(regex_str,str(i[0]))
        # print(check)
        if check:
            print(str(i[0]),str(i[1]))
            try:
                u = "DELETE FROM wyjob_php WHERE id = '%d'" % (i[1])
                cursor.execute(u)
                # 提交到数据库执行
                db.commit()

            except:
                pass

    cursor.close()#关闭游标
    db.close()#关闭数据库

def test():
    # 打开数据库连接
    db = pymysql.connect(host="localhost", user='root', passwd="ljc123", port=3306, db="weibo_cxk")

    # 使用cursor()方法获取操作游标


    cursor = db.cursor()
    print(cursor)
    sql = "INSERT INTO cxk_repost(uid, uname, uurl,  \
          word, gender, urank, followers_count, follow_count)  \
          VALUES(%s, '%s', '%s', '%s', '%s', %s, %s, %s) " % \
          (66, 'unhh', 'ufvawurl', 'uworasfd', 'gendeasr', 11, 999, 888888)
    cursor.execute(sql)
    print(sql)
    res = cursor.fetchall()

    print(res)

def get_ip():
    headers = {'User-Agent': ua.random}
    good_ip = []
    for u in range(1,10):
        res = requests.get('https://www.xicidaili.com/nn/'+str(u), headers=headers).text
        soup = BeautifulSoup(res, 'html.parser')
        # 获取子节点下多个字符串分割并除去换行空格
        content = soup.select('#ip_list .odd')

        for m in content:
            # print(m)
            iplist = []
            for i in m.stripped_strings:
                # print(i)
                iplist.append(i)
                # print('+++++++++++++++++')

            ip = "'"+iplist[0]+':'+iplist[1]+"'"
            ip1 = ip.lower()
            print(ip1)
            check = testConnection(ip1)
            if check:
                good_ip.append(ip1)
            else:
                continue
            time.sleep(5)
        print('即将开始下一页：',u+1)
        time.sleep(10)

    print(good_ip[0])


# 检查代理的匿名性及可连接性
def testConnection(ip):
    headers = {'User-Agent': ua.random}

    proxies = {
        'http': ip,
        'https': ip
    }  # 代理ip
    print(proxies['http'])
    targeturl = 'http://icanhazip.com/'
    try:
        response = requests.get(url=targeturl, proxies=proxies, headers=headers, timeout=5)
        ipurl = response.content
        stcode = response.status_code
        print(ipurl)
        print(stcode)
        if stcode == 200:
            print('OK')
            return True
        else:
            print('FAILED')
            return False
    except:
        print('ERROR')
        return False




if __name__ == '__main__':
    # testConnection(ip)
    get_ip()