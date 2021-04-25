import serial
import sqlite3
from datetime import datetime

cur,con = None, None
data = ""
create_date = ""
sql = ""

port = serial.Serial('COM5','9600') # 포트 연결

con = sqlite3.connect("C:/projects/teamproject/arduinoDB.db")  # DB가 저장된 폴더까지 지정
cur = con.cursor()

while True :
    try:
        data = port.readline()
        strDate = datetime.now().strftime('%Y-%m-%d %H:%M:%S') # 현재날짜와 시간값을 문자열로 변환
        strData = data[:-2].decode() # 바이트 단위의 데이터를 string 형식으로 변환(-2는 \r\n을 제거하기 위함)
        sql = "INSERT INTO  tempTable VALUES('" + strData + "','" + strDate + "')"
        cur.execute(sql)
        con.commit()
    except KeyboardInterrupt:
        break; 

port.close()
con.close()