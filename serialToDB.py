import sys
import glob
import serial
import time
import threading
import sqlite3
from datetime import datetime

class dutserial:
    conn = None #전역변수?
    con = None

    def __init__(self, port, Baud):
        self._port = port
        self._baudrate= Baud

    def SerialControl(self):
        data =""
        sql = ""
        idx, humidity= 0, 10
        global conn
        global con 
        try:
            conn = serial.Serial(self._port, self._baudrate)
            con = sqlite3.connect("C:/projects/teamproject/testDB.db")  # DB가 저장된 폴더까지 지정
            cur = con.cursor()
            print("connnected..!")
            while True:
                data = conn.readline()
                strData = data[:-2].decode() # 바이트 단위의 데이터를 string 형식으로 변환(-2는 \r\n을 제거하기 위함)
                strDate = datetime.now().strftime('%Y-%m-%d %H:%M:%S') # 현재날짜와 시간값을 문자열로 변환
                sql = "INSERT INTO  testTable VALUES(" + str(idx) + ",'"+ strData + "','" + str(humidity) + "','" + strDate + "')"
                cur.execute(sql)
                con.commit()
                idx += 1
                humidity += 1
        finally:
            conn.close()
            con.close()
            print("disconnected..")

    def searchPort(self):
        if sys.platform.startswith('win'):   
            ports = ['COM%s' % (i + 1) for i in range(256)]   
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):   
            # this excludes your current terminal "/dev/tty"   
            ports = glob.glob('/dev/tty[A-Za-z]*')   
        elif sys.platform.startswith('darwin'):   
            ports = glob.glob('/dev/tty.*')   
        else:   
            raise EnvironmentError('Unsupported platform')   

        result = []   
        for port in ports:   
            try:   
                s = serial.Serial(port)   
                s.close()   
                result.append(port)   
            except (OSError, serial.SerialException):   
                pass  
        return result   
        
        

    


