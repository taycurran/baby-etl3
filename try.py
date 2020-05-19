import os
from dotenv import load_dotenv
load_dotenv()

import pymysql.cursors


labs_conn = pymysql.connect(host=os.environ["LABS_RDS_ENDPOINT"],
                            user=os.environ["LABS_USERNAME"],
                            password=os.environ["LABS_PASSWORD"],
                            database=os.environ["LABS_DB_NAME"],
                            port=os.environ["LABS_PORT"]
                            )



labs_conn.close()
print("Done.")