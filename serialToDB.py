import serial
import sqlite3
from datetime import datetime

def startInput(Port, Baud_Rate):
    cur,con = None, None
    data = ""
    sql = ""
    idx, humidity= 0, 10

    port = serial.Serial(Port, Baud_Rate) # 포트 연결

    # cur.execute("CREATE TABLE testTable (idx int, temp char(8), humidity char(8), time char(15))")
    con = sqlite3.connect("C:/projects/teamproject/testDB.db")  # DB가 저장된 폴더까지 지정
    cur = con.cursor()

    while True :
        try:
            data = port.readline()
            strDate = datetime.now().strftime('%Y-%m-%d %H:%M:%S') # 현재날짜와 시간값을 문자열로 변환
            strData = data[:-2].decode() # 바이트 단위의 데이터를 string 형식으로 변환(-2는 \r\n을 제거하기 위함)
            sql = "INSERT INTO  testTable VALUES(" + str(idx) + ",'"+ strData + "','" + str(humidity) + "','" + strDate + "')"
            cur.execute(sql)
            con.commit()
            idx += 1
            humidity += 1
        except KeyboardInterrupt:
            break
    
    port.close()
    con.close()

