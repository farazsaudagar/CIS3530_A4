import psycopg2

# Database configuration for PostgreSQL
# Database configuration for PostgreSQL
DATABASE_CONFIG = {
    "dbname": "company",
    "user": "postgres", # probably it is postgres
    "password": "",  # be careful about where you save the password for real projects
    "host": "localhost",
    "port": "5433"
}

# Function to get a database connection


def get_db_connection():
    conn = psycopg2.connect(**DATABASE_CONFIG)
    return conn