import mysql.connector


def create_post():
    try:
        connection = mysql.connector.connect(...)

        select_query = """SELECT id, text, attachments_url, post_url FROM stg_post_loader WHERE ID NOT IN (SELECT ID FROM FCT_USED_ID) ORDER BY date DESC LIMIT 1"""
        cursor = connection.cursor()
        cursor.execute(select_query)
        record = cursor.fetchmany(size=1)
        for row in record:
            data_raw = [row[0], row[1], row[2], row[3]]
            return data_raw
    except mysql.connector.Error as error:
        print(error)
    finally:
        cursor.close()
        connection.close()