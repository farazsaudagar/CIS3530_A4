import psycopg2

# Database configuration for PostgreSQL
# Database configuration for PostgreSQL
DATABASE_CONFIG = {
    "dbname": "company",
    "user": "postgres",  
    "password": "",
    "host": "localhost",
    "port": "5432"
}


# Function to get a database connection


def get_db_connection():
    conn = psycopg2.connect(**DATABASE_CONFIG)
    return conn
