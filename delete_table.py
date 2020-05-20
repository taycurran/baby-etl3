
import os
from dotenv import load_dotenv
load_dotenv()

import pymysql.cursors

labs_conn = pymysql.connect(
                host=os.environ["LABS_RDS_ENDPOINT"],
                user=os.environ["LABS_USERNAME"],
                password=os.environ["LABS_PASSWORD"],
                database=os.environ["LABS_DB_NAME"],
                port=int(os.environ["LABS_PORT"])
                            )
labs_curs = labs_conn.cursor()

# labs_curs.close()
# labs_conn.close()

def delete_prices_raw():
    # Insert Name of Table to Delete
    delete_Q = """DROP TABLE IF EXISTS raw_data;"""

    labs_curs.execute(delete_Q)
    labs_conn.commit()
    print("Table Deleted.")

if __name__ == "__main__":
    import os
    from dotenv import load_dotenv
    load_dotenv()

    import pymysql.cursors

    labs_conn = pymysql.connect(
                    host=os.environ["LABS_RDS_ENDPOINT"],
                    user=os.environ["LABS_USERNAME"],
                    password=os.environ["LABS_PASSWORD"],
                    database=os.environ["LABS_DB_NAME"],
                    port=int(os.environ["LABS_PORT"])
                                )
    labs_curs = labs_conn.cursor()

    delete_prices_raw()

    labs_curs.close()
    labs_conn.close()
    print("labs_connection is closed.") 