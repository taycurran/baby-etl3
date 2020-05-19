
def create_prices_raw():
    create_table_Q = """
                    CREATE TABLE IF NOT EXISTS prices_raw (
                        id_sauti INTEGER,
                        source VARCHAR(200),
                        country VARCHAR(50),
                        market VARCHAR(25),
                        product_cat VARCHAR(50),
                        product_agg VARCHAR(50),
                        product VARCHAR(50),
                        date DATETIME,
                        retail INTEGER,
                        wholesale INTEGER,
                        currency VARCHAR(50),
                        unit VARCHAR(50),
                        active VARCHAR(50),
                        udate DATETIME
                    );
                    """
    labs_curs.execute(create_table_Q)
    labs_conn.commit()
    print("Table Created Successfully.")


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

    create_prices_raw()

    labs_curs.close()
    labs_conn.close()
    print("labs_connection is closed.") 