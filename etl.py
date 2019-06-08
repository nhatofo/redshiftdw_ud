import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries

""" 
below we have a funtion that will perform queries that will  loads data from S3 buckets
to Redshift cluster.

parameters: 
    cur, conn
return: none
"""
def load_staging_tables(cur, conn):
    for query in copy_table_queries:
        print('Loading data by: '+query)
        cur.execute(query)
        conn.commit()

""" 
Below we have a funtion that will perform  the INSERT statements to copy data from staging tables to 
the dimension and fact tables.

parameters: 
    cur, conn
return: none
"""
def insert_tables(cur, conn):
    for query in insert_table_queries:
        print('Transform data by: '+query)
        cur.execute(query)
        conn.commit()

"""
Below we have the main function, use the dwh config file with credentials to connect a redshift cluster using 
using the psycopg2 postgress driver and will execute the load process by colling the insert_tables()

"""
        
def main():
    config = configparser.ConfigParser()
    config.read('dwh.cfg')
  
    print('Connecting to redshift')
    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    print('Connected to redshift')
    cur = conn.cursor()
    
    print('Loading staging tables')
    
    print('Transform from staging')
    insert_tables(cur, conn)

    conn.close()
    print('ETL Ended')


if __name__ == "__main__":
    main()