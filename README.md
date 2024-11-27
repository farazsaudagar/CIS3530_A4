# CIS3530_A4

## Getting Started

Follow these steps to set up the project:

1. **Clone this repository**:
   ```bash
   git clone <repository_url>
   cd <repository_name>
Activate the virtual environment:
source venv/bin/activate
Install required packages:
pip install -r requirements.txt
Run the application:
python run.py
Set up the database:
Access your PostgreSQL prompt:
psql postgres
Create the database:
CREATE DATABASE company;
Build the database structure from schema.sql:
\c company
\i schema.sql
Features

This project includes all assignment features, including the bonus.

Bonus Feature: File Upload
To use the upload feature, upload a file with:

A name that matches the table you want to push data into.
The same column headers and data types as defined in the database schema.
Ensure the data aligns with the database structure to avoid errors.