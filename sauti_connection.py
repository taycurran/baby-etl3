import os
from dotenv import load_dotenv
load_dotenv()

import pymysql.cursors

sauti_conn = pymysql.connect(
                host=os.environ["SAUTI_HOST"],
                user=os.environ["SAUTI_USER"],
                password=os.environ["SAUTI_PASSWORD"],
                database=os.environ["SAUTI_DB_NAME"]
                            )

sauti_curs = sauti_conn.cursor()

Q = """SELECT * FROM platform_market_prices2 LIMIT 15;"""

sauti_curs.execute(Q)


result = sauti_curs.fetchmany(10)

print(result)

sauti_curs.close()
sauti_conn.close()