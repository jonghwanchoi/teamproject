import sqlite3
import time
import serial
from datetime import datetime
# "C:/projects/teamproject/arduinoDB.db"
# "C:/projects/teamproject/testDB.db"
class select_DB:
    con,cur = None,None
    dbPath = ""
    table_name = ""
 

    def __init__(self, dbPath, table_name):
        self.dbPath = dbPath
        self.table_name = table_name


    def select(self):
        con = sqlite3.connect(self.dbPath)
        cur = con.cursor()

        cur.execute("SELECT * FROM " + self.table_name)
        rows = cur.fetchall() # 데이터 전체 읽어오기 
        con.commit()
        con.close()
  
        return rows

    def select_count(self,table_idx): # column = datetime이 가진 모든 데이터의 수
        con = sqlite3.connect(self.dbPath)
        cur = con.cursor()
        cur.execute("SELECT COUNT("+ table_idx +") FROM " + self.table_name)
        row = cur.fetchone()
        con.commit()
        con.close()
        return row[0] # 튜플형이므로 인덱스 줘서 값 받아야 함    

    def select_page(self, list_limit, page, table_idx):
        con = sqlite3.connect(self.dbPath)
        cur= con.cursor()
        offset = (page -1) * list_limit
        sql = "SELECT * FROM "+ self.table_name + " ORDER BY "+ table_idx +" limit ? offset ?"
        cur.execute(sql, (list_limit, offset,)) # offset,limit값 대입
        rows = cur.fetchall()
        con.commit()
        con.close()
        return rows

    def delete(self): # 모든 레코드 삭제
        con = sqlite3.connect(self.dbPath)
        cur = con.cursor()
        cur.execute("DELETE FROM " + self.table_name)
        con.commit()
        con.close()
    
    def stop(self):
        serial.Serial('COM5','9600').close()
        sqlite3.connect("C:/projects/teamproject/testDB.db").close()

    

