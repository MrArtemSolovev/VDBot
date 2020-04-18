import mysql.connector


def fct_counts():
    try:
        connection = mysql.connector.connect(...)
                                             
        fct_cnt_query = "SELECT V.table_rows - K.table_rows FROM " \
                        "(SELECT table_rows FROM INFORMATION_SCHEMA.TABLES " \
                        "WHERE TABLE_SCHEMA = 'vdbot' and table_name = 'stg_post_loader') AS V " \
                        "CROSS JOIN " \
                        "(SELECT table_rows FROM INFORMATION_SCHEMA.TABLES " \
                        "WHERE TABLE_SCHEMA = 'vdbot' and table_name = 'FCT_USED_ID') AS K"
        cursor = connection.cursor()
        cursor.execute(fct_cnt_query)
        record = cursor.fetchmany(size=1)
        for row in record:
            cnt = row[0]
            return cnt
    except mysql.connector.Error as error:
        print(error)
    finally:
        cursor.close()
        connection.close()


def truncate_fct_used_article():
    try:
        connection = mysql.connector.connect(...)

        truncate_fct_article = """TRUNCATE TABLE FCT_USED_ID """
        cursor = connection.cursor()
        cursor.execute(truncate_fct_article)
        connection.commit()

    except mysql.connector.Error as error:
        print(error)
    finally:
        cursor.close()
        connection.close()