import mysql.connector
from datetime import *
time=datetime.now()
mycustom = time.strftime("%Y-%m-%d %H:%M:%S")
mydb= mysql.connector.connect(host="192.168.0.105",user="mysql_user",password="Ahmad:06331913012",database="alnafi", auth_plugin="mysql_native_password")
#mysql connection object create
cur = mydb.cursor()
#Fetching data
data="'zoya@123'"
sql = " update trainer_details set password="+data+ " where t_id=8"


#Executing data for update query
cur.execute(sql)
mydb.commit()

#Fetching mysql data
select_sql = """ select * from trainer_details """
cur.execute(select_sql)
result = cur.fetchall()
for data in result:
    print(data)

mydb.close()