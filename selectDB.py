import sqlite3
import time
from datetime import datetime
# "C:/projects/teamproject/arduinoDB.db"
# "C:/projects/teamproject/testDB.db"
class select_DB:
    con,cur = None,None
    dbPath = ""
    dbpath1 = ""

    def __init__(self, dbPath, dbpath1):
        self.dbPath = dbPath
        self.dbpath1 = dbpath1

    def select(self):
        con = sqlite3.connect(self.dbPath)
        cur = con.cursor()

        cur.execute("SELECT * FROM tempTable")
        rows = cur.fetchall() # 데이터 전체 읽어오기 
        con.commit()
        con.close()
  
        return rows

    def select_count(self): # column = datetime이 가진 모든 데이터의 수
        con = sqlite3.connect(self.dbPath)
        cur = con.cursor()
        cur.execute("SELECT COUNT(datetime) FROM tempTable")
        row = cur.fetchone()
        con.commit()
        con.close()
        return row[0] # 튜플형이므로 인덱스 줘서 값 받아야 함    

    def select_page(self,list_limit, page):
        con = sqlite3.connect(self.dbPath)
        cur= con.cursor()
        offset = (page -1) * list_limit
        sql = "SELECT * FROM tempTable ORDER BY datetime limit ? offset ?"
        cur.execute(sql, (list_limit, offset,)) # offset,limit값 대입
        rows = cur.fetchall()
        con.commit()
        con.close()
        return rows

    def delete(self): # 모든 레코드 삭제
        con = sqlite3.connect(self.dbPath)
        cur = con.cursor()
        cur.execute("DELETE FROM tempTable")
        cur.execute("SELECT * FROM tempTable")
        rows = cur.fetchall() # 데이터 전체 읽어오기
        con.commit()
        con.close()

        return rows

    def selectTest(self):
        con = sqlite3.connect(self.dbpath1)
        cur = con.cursor()
        cur.execute("SELECT * FROM testTable")
    
        rows = cur.fetchall() # 데이터 전체 읽어오기
        con.commit()
        con.close()

        return rows

    def insertData(self,idx,temp):
        sql = ""

        con = sqlite3.connect(self.dbpath1)
        cur = con.cursor()

        # cur.execute("CREATE TABLE testTable (idx int, temp char(8), humidity char(8), time char(15))")
        while True:
            if(temp>=25):
                break;
            strDate = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            sql = "INSERT INTO testTable VALUES(" + str(idx) + ",'" + str(temp) + " *C', '20%'," + "'" + strDate +"')"
            cur.execute(sql)
            con.commit()  
            idx += 1
            temp += 1
            time.sleep(1) # 1초 단위로 입력
        con.close()

