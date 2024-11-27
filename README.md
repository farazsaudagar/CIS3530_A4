# CIS3530_A4
## Getting Started

Follow these steps to set up the project:

### 1. Extract the Project Files
Download the provided zip file and extract its contents:
1. Locate the zip file (`CIS3530_A4.zip` or similar) on your computer.
2. Right-click the file and select **Extract All** or use a tool like WinRAR/7-Zip to extract the files.
3. Navigate to the extracted project folder.

### 2. Set Up the Virtual Environment
Activate the virtual environment and install the required packages:
```bash
# Navigate to the project directory
cd <extracted_project_folder>

# Activate the virtual environment
source venv/bin/activate

# Install required packages
pip install -r requirements.txt
```
### 3. Set up the database
Follow the steps to configure the PostgreSQL database:
1. Access the PostgreSQL:
```bash
psql postgres
# psql -U postgres -c "drop database company;"
# psql -U postgres -c "create database company;"
# psql -U postgres -d company -f schema.sql 
```
2. Create database:
```bash
CREATE DATABASE company;
```
3. Build the database structure from the schema file:
```bash
# Exit the psql prompt and navigate to the project root directory
psql -U postgres -d company -f schema.sql
```

Alternatively, you can use the following one-liners to drop, recreate, and set up the database:
```bash
psql -U postgres -c "DROP DATABASE IF EXISTS company;"
psql -U postgres -c "CREATE DATABASE company;"
psql -U postgres -d company -f schema.sql
```

### Run the application:
```bash
python run.py
```

### Features

This project includes all assignment features, including the bonus.

#### Bonus Feature: File Upload
To use the upload feature, upload a file with:

A name that matches the table you want to push data into.
The same column headers and data types as defined in the database schema.
Ensure the data aligns with the database structure to avoid errors.