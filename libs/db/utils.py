import mysql.connector
import numpy as np
import pandas as pd
from loguru import logger

def connect_db(init_data : dict, is_insert = False) -> mysql.connector.connection.MySQLConnection :
    """Connects to the specified MySQL database using MySQLdb (deprecated).

    Args:
        init_data 
    Returns:
        MySQLdb.connection: A connection object to the MySQL database.

    Raises:
        MySQLdb.Error: If an error occurs during connection.
    """
    logger.info("Connected to database")
    try :
        reportbuilder = init_data["ClientConfigs"]["Host"]["reportbuilder"]
        db_host = reportbuilder["authority"]
        db_user = reportbuilder["username"]
        db_password = reportbuilder["passwordVar"]
        if is_insert :
            db_name = reportbuilder["insertDataBaseName"]
        else :
            db_name = reportbuilder["databaseName"]
        db_port = reportbuilder["port"]
        logger.info("CONNECTING TO DATABASE")
        conn = mysql.connector.connect(
            host = db_host,
            user = db_user,
            password = db_password,
            database = db_name,
            port = db_port
        )
        logger.success("Connected to database !")
        return conn
    except Exception as e :
        logger.error("Error while connecting to db")
        logger.error(e)
        raise e
    



def dtype_to_sql(dtype):
    if np.issubdtype(dtype, np.integer):
        return 'INTEGER'
    elif np.issubdtype(dtype, np.float64):
        return 'REAL'
    elif np.issubdtype(dtype, np.datetime64):
        return 'DATETIME'
    else:
        return 'TEXT'

def create_table_from_data(conn, df, table_name):
    cursor = conn.cursor()
    try:
        columns = ", ".join([f"{col} {dtype_to_sql(dtype)}" for col, dtype in zip(df.columns, df.dtypes)])
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})")
        logger.info(f"Table {table_name} created successfully.")
        conn.commit()
    except Exception as e:
        logger.error(f"Error creating table {table_name}: {e}")
    finally:
        cursor.close()

def insert_into_db(conn, data_row, table_name):
    cursor = conn.cursor()
    try:
        if not table_exists(conn, table_name):
            # Assuming create_table_from_data can use a class instance directly
            create_table_from_data(conn, data_row, table_name)

        row_data = data_row.to_dict()  # Convert class instance to dictionary
        columns = ", ".join(row_data.keys())
        placeholders = ", ".join(["%s"] * len(row_data))
        query = f"INSERT IGNORE INTO {table_name} ({columns}) VALUES ({placeholders})"

        cursor.execute(query, tuple(row_data.values()))
        conn.commit()
        last_inserted_id = cursor.lastrowid
        logger.info(f"Data inserted into table {table_name} successfully.")
        return last_inserted_id  # Return the ID of the inserted row
    except Exception as e:
        logger.error(f"Error inserting data into table {table_name}: {e}")
        return None  # Return None in case of failure
    finally:
        cursor.close()

def table_exists(conn, table_name):
    cursor = conn.cursor()
    try:
        cursor.execute(f"SHOW TABLES LIKE '{table_name}'")
        result = cursor.fetchone() is not None
        if result:
            logger.info(f"Table {table_name} exists.")
        else:
            logger.info(f"Table {table_name} does not exist.")
        return result
    except Exception as e:
        logger.error(f"Error checking if table {table_name} exists: {e}")
    finally:
        cursor.close()