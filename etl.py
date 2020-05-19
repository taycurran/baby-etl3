# From Files in Directory
from create_table import create_prices_raw
from delete_table import delete_prices_raw

# For Environment Variables
import os
from dotenv import load_dotenv
load_dotenv()

# For Establishing Connection and Cursor with the DB
import pymysql.cursors

# ----- Sauti DB Connection -----
sauti_conn = pymysql.connect(
                host=os.environ["SAUTI_HOST"],
                user=os.environ["SAUTI_USER"],
                password=os.environ["SAUTI_PASSWORD"],
                database=os.environ["SAUTI_DB_NAME"]
                            )

sauti_curs = sauti_conn.cursor()

# ----- Labs DB Connection -----
labs_conn = pymysql.connect(
                host=os.environ["LABS_RDS_ENDPOINT"],
                user=os.environ["LABS_USERNAME"],
                password=os.environ["LABS_PASSWORD"],
                database=os.environ["LABS_DB_NAME"],
                port=int(os.environ["LABS_PORT"])
                            )

labs_curs = labs_conn.cursor()
# ----------------------------------------------------------------------------
# ----- ETL -----

# Drop Table If Exists
delete_prices_raw()
# Recreate Table
create_prices_raw()

# Query Sauti DB
Q_select_all = """SELECT * FROM platform_market_prices2;"""
sauti_curs.execute(Q_select_all)
print("SELECT Query Excecuted")

# Create List of Sauti Rows
rows = sauti_curs.fetchall()
print("Cursor Fetch Completed")

# Insert Row by Row Into Labs DB
for row in rows:
  insert_row = """
  INSERT INTO prices_raw
  (id_sauti, source, country, market, product_cat,
  product_agg, product, date, retail, wholesale,
  currency, unit, active, udate) VALUES 
  (%(id_sauti)s, %(source)s, %(country)s, %(market)s, %(product_cat)s, 
  %(product_agg)s, %(product)s, %(date)s, %(retail)s, %(wholesale)s, 
  %(currency)s, %(unit)s, %(active)s, %(udate)s);"""

  vals = {'id_sauti': row[0],
          'source': row[1],
          'country': row[2],
          'market': row[3],
          'product_cat': row[4],
          'product_agg': row[5],
          'product': row[6],
          'date': row[7],
          'retail': row[8],
          'wholesale': row[9],
          'currency': row[10],
          'unit': row[11],
          'active': row[12],
          'udate': row[13]
         }
  labs_curs.execute(insert_row, vals)
  labs_conn.commit()
print("Rows Inserted")

# Final Commit Just Incase ;)
labs_conn.commit()

# Close Sauti DB
sauti_curs.close()
sauti_conn.close()
print("Sauti DB Connection Closed.")

# Close Labs DB
labs_curs.close()
labs_conn.close()
print("Labs DB Connection Closed.")

