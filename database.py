import sqlite3

class MyDatabase :
    dbPath = ""

    def __init__(self, dbPath):
        self.dbPath = dbPath
    
    def getdbPath(self):
        return self.dbPath  

    def insertData(self, table_name, dataList):
        con = sqlite3.connect(self.dbPath)  # DB가 저장된 폴더까지 지정
        cur = con.cursor()

        #table이 존재하지 않을 경우, 생성
        str_sql = "SELECT COUNT(*) FROM sqlite_master WHERE Name = '"
        cur.execute(str_sql+table_name+"'")
        result = cur.fetchall()
        if result[0][0] == 0 :   
            createSQL = 'CREATE TABLE {} (time text, temp real)'.format(table_name)
            cur.execute(createSQL)
				#####

        insert_sql = "INSERT INTO "+ table_name +" VALUES('" + dataList[0] + "' ," + str(dataList[1]) +")"
        cur.execute(insert_sql)
        print(insert_sql)
        con.commit()
        con.close()
    
    def readData(self, table_name, returnList):
        con = sqlite3.connect(self.dbPath)  # DB가 저장된 폴더까지 지정
        cur = con.cursor()
        
        #유효한 tablename인지 확인
        str_sql = "SELECT COUNT(*) FROM sqlite_master WHERE Name = '"
        cur.execute(str_sql+table_name+"'")
        result = cur.fetchall()
        if result[0][0] == 0 :  
            return 0

        cur.execute("SELECT * FROM " +table_name)
        while (True) :
            row = cur.fetchone()
            if row == None :
                break
            returnList.append(row)

        con.close()