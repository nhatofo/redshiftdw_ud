import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries


""" 
below we have a funtion that will perform drop table statements that will  verify if the
table exists on a  Redshift database before create it.

parameters: 
    cur, conn
return: none
"""
def drop_tables(cur, conn):
    for query in drop_table_queries:
        print('Executing drop: '+query)
        cur.execute(query)
        conn.commit()

""" 
below we have a funtion that will perform create queries statements that will  create database tables
on a Redshift database.

parameters: 
    cur, conn
return: none
"""
def create_tables(cur, conn):
    for query in create_table_queries:
        print('Executing create: '+query)
        cur.execute(query)
        conn.commit()

"""
Below we have the main function, use the dwh config file with credentials to connect a redshift cluster using 
using the psycopg2 postgress driver and will execute the load process by colling the drop_tables() 
and the create_table() funtion.  

"""
def main():
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    print('Connecting to redshift')
    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    print('Connected to redshift')
    cur = conn.cursor()

    print('Dropping existing tables if any')
    drop_tables(cur, conn)
    
    print('Creating tables')
    create_tables(cur, conn)

    conn.close()
    print('Create table Ended')


if __name__ == "__main__":
    main()