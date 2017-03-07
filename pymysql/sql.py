import pymysql   #提示找不到pymysql.connect时，使用anaconda 安装库     #anaconda命令行输入conda install pymysql
connection = pymysql.connect(host='127.0.0.1',
                             port=3306,
                             user='root',
                             password='ccisme1994815',
                             db='test',
                             charset='utf8mb4')
cursor = connection.cursor()

######################################################################
sql = "insert into motor (WZ,SD,Ia,Ib)values(%lf,%lf,%lf,%lf)"   #增加数据
data =(12,312,412,123)
######################################################################
'''
sql = "delete from motor where WZ = '%lf'"                 #删除数据
data = (1)
######################################################################
sql = "select id,WZ from motor where SD = %lf"              #查询数据
data = (420)
######################################################################
sql = "update motor set WZ = WZ*2 where SD<400"
print(cursor.execute(sql))                     #由于更新数据不需要data 所以换一个execute，注意使用时把下面一句execute注释
######################################################################'''

print(cursor.execute(sql % data))                     #这句话的能够返回受影响的数据条数

'''
######################################################################
for row in cursor.fetchall():                         #用于查询时显示结果
    print("id:%d     位置:%lf" %row)
######################################################################'''
connection.commit()
cursor.close()
connection.close()