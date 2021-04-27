import sys
import serial
import time
import threading
import sqlite3
from datetime import datetime

class dutserial:
    con,cur = None,None
    def __init__(self, port, Baud):
        self._port = port
        self._baudrate= Baud
        self._conn = None
        self._con = None

    def dutOpenConn(self, abool):
        data =""
        sql = ""
        idx, humidity= 0, 10
        if(abool==True):
            self._conn = serial.Serial(self._port, self._baudrate)
            self._con = sqlite3.connect("C:/projects/teamproject/testDB.db")  # DB가 저장된 폴더까지 지정
            cur = self._con.cursor()
            while True:
                data = self._conn.readline()
                strData = data[:-2].decode() # 바이트 단위의 데이터를 string 형식으로 변환(-2는 \r\n을 제거하기 위함)
                strDate = datetime.now().strftime('%Y-%m-%d %H:%M:%S') # 현재날짜와 시간값을 문자열로 변환
                sql = "INSERT INTO  testTable VALUES(" + str(idx) + ",'"+ strData + "','" + str(humidity) + "','" + strDate + "')"
                cur.execute(sql)
                self._con.commit()
                idx += 1
                humidity += 1
        else:
            self._conn.close()
            self._con.close()
            print("disconnected..2")

        
        # while abool==True:
        #     try:
        #         data = self._conn.readline()
        #         strData = data[:-2].decode() # 바이트 단위의 데이터를 string 형식으로 변환(-2는 \r\n을 제거하기 위함)
        #         strDate = datetime.now().strftime('%Y-%m-%d %H:%M:%S') # 현재날짜와 시간값을 문자열로 변환
        #         sql = "INSERT INTO  testTable VALUES(" + str(idx) + ",'"+ strData + "','" + str(humidity) + "','" + strDate + "')"
        #         cur.execute(sql)
        #         self._con.commit()
        #         idx += 1
        #         humidity += 1
        #     except: #-------------2
        #         self._conn.close()
        #         self._con.close()
        #         print("disconnected..1")
        #         break

    def dutCloseConn(self): #문제 있어 보임(값을 어떻게 받아와서 동작하는지 모르겠음) ---1
       try: 
           self._conn.close()
           self._con.close()
       except:
            print("End Serial")


