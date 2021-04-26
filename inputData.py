import sqlite3
import time
from datetime import datetime

con,cur = None,None
sql = ""
idx ,temp = 0,17

con = sqlite3.connect("C:/projects/teamproject/testDB.db")
cur = con.cursor()

# cur.execute("CREATE TABLE testTable (idx int, temp char(8), humidity char(8), time char(15))")
while True:
    try:
        strDate = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        sql = "INSERT INTO testTable VALUES(" + str(idx) + ",'" + str(temp) + " *C', '20%'," + "'" + strDate +"')"
        cur.execute(sql)
        con.commit()  
        idx += 1
        temp += 1
        time.sleep(1) # 1초 단위로 입력
    except KeyboardInterrupt:
        break;
con.close()