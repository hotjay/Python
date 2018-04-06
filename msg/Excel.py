#-*-coding:utf-8-*-
"""
auther:张振华
version:1.0
Datetime:20180326
"""
import xlrd
import time
import cx_Oracle
import pymssql
import _mssql
import uuid
import decimal

import re
from PyQt5.QtWidgets import QMessageBox



        #带返回值和传入参数的函数

filename=r'F:\Python\msg\a.xlsx'
data=xlrd.open_workbook(filename)
sheet_names=data.sheet_names()#获取excle 文件的所有工作表名
table=data.sheet_by_name(sheet_names[0]) #获取第一个工作表名
rows_count=table.nrows
col_count=table.ncols   #获取最大的行和列
row_date=table.row_values(0)#第一行的内容
msg=''
list=[]
correctCount=int(0)
errorCount=int(0)#计数
for row in range(1,rows_count):  #遍历行
                    for col in range(1,col_count): #遍历列
                        row_date1=table.row_values(row) #获取第row行的数据
                        if row_date1[col]!=0 and col !=3:#判断不等于0的列
                            if col==4:
                                msg += str(row_date[col]) + ':' + str(int(row_date1[col]))  # 组合字符串 将工号进行type转换
                            else:
                                msg+=str(row_date[col])+':'+str(row_date1[col])#组合字符串
                        if len(msg)>250 or col==col_count-1: #判断msg的长度 或者是最后一列
                            list.append(msg)#拆分存入列表
                            msg = ''
                     #加入查询工号对应的电话号码
                    gh=str(int(row_date1[4]))
                    print(list)
                    #print(gh)
                    #sqlsever连接
                    server = '172.16.0.121'
                    user = 'ioffice'
                    passwor = '111111'
                    print('1')

                    con = pymssql.connect(server, user, passwor, 'ioffice',charset="cp936")#charset 是为了解决中文乱码问题

                    cursor = con.cursor()
                    sql = "select mobile from mrbaseinf where empcode='%s'"%(gh)

                    cursor.execute(sql.encode("cp936"))#是为了解决中文乱码问题 执行sql语句
                    print('2')
                    try:
                        for row in cursor:#cursor 空会抛出异常
                            telNum=row[0]
                            print(telNum)
                            con.close()
                            print(list)
                                #correctCount=correctCount+1
                    except:
                        list.clear()  # 失败了也要把列表清空
                        continue

                    for a in list:
                        print('3')
                        db1 = cx_Oracle.connect('yddx/yddx@172.16.0.5:1521/hisdb')
                        cr1 = db1.cursor()
                        sql1 = "insert into sm(user_name,SRC_TELE_NUM,DEST_TELE_NUM,MSG,sm_seq_id,SET_SEND_TIME)values('joke','106573073830','%s','%s',SM_SEQ.nextval,sysdate)" % (row[0],a)
                        cr1.execute(sql1)
                        cr1.close()
                        db1.commit()
                        db1.close()



                        #errorCount=errorCount+1
                        #print(errorCount)



                    list.clear()
       # a=[]  #作为成功和失败计数的列表
       # a.append(correctCount)
        #a.append(errorCount)
       # print(a)
      #  return a  #返回计数列表
