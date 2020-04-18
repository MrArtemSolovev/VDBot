import mysql.connector


mydb = mysql.connector.connect(
  ...
)


def truncate_stg_loader():
    mycursor = mydb.cursor()
    sql = 'TRUNCATE TABLE stg_post_loader'
    mycursor.execute(sql)


def sql_insert_stg_intel(data_frame):
    mycursor = mydb.cursor()
    sql = 'INSERT INTO stg_post_loader (id, date, text, attachments_url, post_url) VALUES (%s, %s, %s, %s, %s)'
    mycursor.executemany(sql, data_frame)
    mydb.commit()
    print(mycursor.rowcount, "inserted.")