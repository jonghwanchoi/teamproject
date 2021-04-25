import sqlite3

con,cur = "",""
def select():
    con = sqlite3.connect("C:/projects/teamproject/arduinoDB.db")
    cur = con.cursor()

    cur.execute("SELECT * FROM tempTable")
    rows = cur.fetchall() # 데이터 전체 읽어오기 
    con.commit()
    con.close()
  
    return rows

def select_count(): # column = datetime이 가진 모든 데이터의 수
    con = sqlite3.connect("C:/projects/teamproject/arduinoDB.db")
    cur = con.cursor()
    cur.execute("SELECT COUNT(datetime) FROM tempTable")
    row = cur.fetchone()
    con.commit()
    con.close()
    return row[0] # 튜플형이므로 인덱스 줘서 값 받아야 함    

def select_page(list_limit, page):
    con = sqlite3.connect("C:/projects/teamproject/arduinoDB.db")
    cur= con.cursor()
    offset = (page -1) * list_limit
    sql = "SELECT * FROM tempTable ORDER BY datetime limit ? offset ?"
    cur.execute(sql, (list_limit, offset,)) # offset,limit값 대입
    rows = cur.fetchall()
    con.commit()
    con.close()
    return rows

def delete(): # 모든 레코드 삭제
    con = sqlite3.connect("C:/projects/teamproject/arduinoDB.db")
    cur = con.cursor()
    cur.execute("DELETE FROM tempTable")
    cur.execute("SELECT * FROM tempTable")
    rows = cur.fetchall() # 데이터 전체 읽어오기
    con.commit()
    con.close()

    return rows