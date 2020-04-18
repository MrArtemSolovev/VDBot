import mysql.connector


def article_id_insert(post_raw):
    try:
        connection = mysql.connector.connect(...)

        article_id_to_fct = """INSERT INTO FCT_USED_ID (ID) VALUES (%s) """
        record = [(post_raw[0])]
        cursor = connection.cursor()
        cursor.execute(article_id_to_fct, record)
        connection.commit()
    except mysql.connector.Error as error:
        print(error)
    finally:
        cursor.close()
        connection.close()