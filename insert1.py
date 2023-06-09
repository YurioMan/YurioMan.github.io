import pymysql
# open db connection
con = pymysql.connect(
  host = "localhost", 
  user = "root", 
  password = "", 
  db = "ftabname"
  )
#user input
i_d = input("Enter id:- ")
data = input("Enter data:- ")
name = input("Enter name:- ")
discript = input("Enter discription:- ")

# make mycursor
mycursor = con.cursor()

# sql query insert data
sql = """insert into tabname values (%s,%s,%s,%s)"""
val = (i_d,data,name,discript)

# execute sql query
mycursor.execute(sql,val)

# commit data in db table
con.commit()

print(mycursor.rowcount, "\033[1;92m Record inserted..\033[0m ")
