import pymysql
# open db connection
con = pymysql.connect(
  host = "localhost", 
  user = "root", 
  password = "", 
  db = "ftabname"
  )
# make mycursor
mycursor = con.cursor()

# sql query insert data
sql = """insert into tabname(id, data, name, discript ) values (\s, \s, \s, \s)"""
val = (1, '0607', 'news', 'it my first data')
# execute sql query
mycursor.execute(sql,val)

# commit data in db table
con.commit()
print(mycursor.rowcount, "Record inserted.. ")
