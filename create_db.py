import os
from dotenv import load_dotenv
load_dotenv()

import pymysql.cursors

labs_conn = pymysql.connect(
                host=os.environ["LABS_RDS_ENDPOINT"],
                user=os.environ["LABS_USERNAME"],
                password=os.environ["LABS_PASSWORD"],
                port=int(os.environ["LABS_PORT"])
                            )

labs_curs = labs_conn.cursor()

Q_create_DB = """
        CREATE DATABASE IF NOT EXISTS labs24;
              """
labs_curs.execute(Q_create_DB)
labs_conn.commit()
labs_curs.close()
labs_conn.close()
print("labs_connection is closed.")