"""This module holds the database connection settings"""
import os
import psycopg2

from instance.config import app_config
from .tables import USERS, PARCELS, TABLES_TO_DROP

# url = os.getenv('TEST_DB_URI')
env = os.getenv('APP_SETTINGS')
url = app_config[env].DATABASE_URL


def connection(url):
    con = psycopg2.connect(url)
    return con


def init_db():
    con = connection(url)
    return con


def create_tables():
    conn = connection(url)
    cursor = conn.cursor()
    queries = tables()
    for query in queries:
        cursor.execute(query)
    conn.commit()


def destroy_tables():
    conn = connection(url)
    cursor = conn.cursor()
    for table in TABLES_TO_DROP:
        cursor.execute(table)
    conn.commit()


def tables():
    queries = [USERS, PARCELS]
    return queries
