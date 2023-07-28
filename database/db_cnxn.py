import sqlite3

def create_table(cursor, table_name):
    table_schema = "CREATE TABLE IF NOT EXISTS {} (symbol TEXT, shortName TEXT, longName TEXT, exchange TEXT, market TEXT, quoteType TEXT, sector TEXT, market_cap INTEGER DEFAULT NULL)".format(table_name)
    cursor.execute(table_schema)

def remove_otc_rows(table_name):
    connection = sqlite3.connect('stock_data.db')
    cursor = connection.cursor()

    try:
        delete_rows_query = "DELETE FROM {} WHERE exchange = 'OTC'".format(table_name)
        cursor.execute(delete_rows_query)

        connection.commit()
    except Exception as e:
        print("An error occurred while removing OTC rows:", e)

    connection.commit()
    connection.close()

def modify_market_cap_column(table_name):
    connection = sqlite3.connect('stock_data.db')
    cursor = connection.cursor()

    modify_column_query = "PRAGMA foreign_keys=off;"  # Turn off foreign key constraints temporarily
    cursor.execute(modify_column_query)

    try:
        alter_table_query = "ALTER TABLE {} RENAME TO temp_table".format(table_name)
        cursor.execute(alter_table_query)

        create_table(cursor, table_name)
        copy_data_query = "INSERT INTO {} SELECT symbol, shortName, longName, exchange, market, quoteType, sector, CAST(market_cap AS INTEGER) FROM temp_table".format(table_name)
        cursor.execute(copy_data_query)
        drop_temp_table_query = "DROP TABLE temp_table"
        cursor.execute(drop_temp_table_query)

        connection.commit()
    except Exception as e:
        print("An error occurred while modifying the column:", e)

    connection.commit()
    connection.close()

if __name__ == "__main__":
    database_name = 'NYSEInfo'

    remove_otc_rows(database_name)
