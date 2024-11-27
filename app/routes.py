from flask import render_template, request, redirect, url_for, flash, send_file
from flask_login import current_user
from app import app
from app.db import get_db_connection
import os
from werkzeug.utils import secure_filename
import pandas as pd
from psycopg2 import sql
import io


UPLOAD_FOLDER = 'uploads'  # Specify the directory to save uploaded files
ALLOWED_EXTENSIONS = {'xlsx', 'xls'}  # Allow Excel files
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Limit file size to 16 MB

def allowed_file(filename):
    """Check if the uploaded file is allowed."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



# Route to view all employees

@app.route('/employees')
def view_employees():
    conn = get_db_connection()
    cursor = conn.cursor()
    print(current_user.role)
    if current_user.role == 'super_admin':
        cursor.execute("SELECT SSN, Fname, Lname, Salary FROM Employee")
    else:
        cursor.execute("SELECT DISTINCT SSN, Fname, Lname, Salary FROM DepartmentEmployee WHERE Dno = %s", (current_user.department_id,))
    employees = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('employees.html', employees=employees, user_role=current_user.role)



@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT SSN, Fname, Lname, Salary FROM Employee")
    employees = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('base.html', employees=employees)


from flask import session, flash, redirect, url_for

@app.route('/update/<ssn>', methods=['GET', 'POST'])
def update_salary(ssn):
    # Ensure the user is authenticated
    if not current_user.is_authenticated:
        flash('You must be logged in to update salaries.', 'danger')
        return redirect(url_for('login'))

    # Restrict access based on user role
    if current_user.role == 'normal_user':
        flash('Normal users are not allowed to update salaries.', 'danger')
        return redirect(url_for('view_employees'))

    # Connect to the database
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        new_salary = request.form['salary']
        try:
            cursor.execute(
                "UPDATE Employee SET Salary = %s WHERE SSN = %s", (new_salary, ssn))
            conn.commit()
            flash('Salary updated successfully!', 'success')
        except Exception as e:
            conn.rollback()
            flash(f'Error updating salary: {e}', 'danger')
        finally:
            cursor.close()
            conn.close()
        return redirect(url_for('view_employees'))

    try:
        cursor.execute(
            "SELECT SSN, Fname, Lname, Salary FROM Employee WHERE SSN = %s", (ssn,))
        employee = cursor.fetchone()
    except Exception as e:
        flash(f'Error fetching employee data: {e}', 'danger')
        employee = None
    finally:
        cursor.close()
        conn.close()

    return render_template('update_salary.html', employee=employee)



# NEW DEPARTMENT ROUTES

# Route to view all departments


@app.route('/departments')
def view_departments():
    conn = get_db_connection()
    cursor = conn.cursor()
    if current_user.role == 'super_admin':
        cursor.execute("SELECT Dnumber, Dname, Mgr_ssn FROM Department")
    else:
        cursor.execute("SELECT DISTINCT Dnumber, Dname, Mgr_ssn FROM DepartmentView WHERE Dnumber = %s", (current_user.department_id,)) 
    departments = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return render_template('departments.html', departments=departments, user_role=current_user.role)


@app.route('/departments/add', methods=('GET', 'POST'))
def add_department():
    # Restrict normal users
    if current_user.role == 'normal_user':
        flash('You do not have permission to add departments.', 'danger')
        return redirect(url_for('view_departments'))

    if request.method == 'POST':
        dname = request.form['dname']
        dnumber = request.form['dnumber']
        mgr_ssn = request.form['mgr_ssn']

        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO Department (Dname, Dnumber, Mgr_ssn) VALUES (%s, %s, %s)",
                (dname, dnumber, mgr_ssn)
            )
            conn.commit()
            flash('Department added successfully!', 'success')
        except Exception as e:
            conn.rollback()
            flash(f'Error adding department: {e}', 'danger')
        finally:
            cursor.close()
            conn.close()

        return redirect(url_for('view_departments'))

    return render_template('add_department.html')



@app.route('/departments/update/<int:dnumber>', methods=('GET', 'POST'))
def update_department(dnumber):
    # Restrict normal users
    if current_user.role == 'normal_user':
        flash('You do not have permission to update departments.', 'danger')
        return redirect(url_for('view_departments'))

    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        dname = request.form['dname']
        mgr_ssn = request.form['mgr_ssn']

        try:
            cursor.execute(
                "UPDATE Department SET Dname = %s, Mgr_ssn = %s WHERE Dnumber = %s",
                (dname, mgr_ssn, dnumber)
            )
            conn.commit()
            flash('Department updated successfully!', 'success')
        except Exception as e:
            conn.rollback()
            flash(f'Error updating department: {e}', 'danger')
        finally:
            cursor.close()
            conn.close()

        return redirect(url_for('view_departments'))

    try:
        cursor.execute(
            "SELECT Dnumber, Dname, Mgr_ssn FROM Department WHERE Dnumber = %s", (dnumber,))
        department = cursor.fetchone()
    except Exception as e:
        flash(f'Error fetching department data: {e}', 'danger')
        department = None
    finally:
        cursor.close()
        conn.close()

    return render_template('update_department.html', department=department)


# Route to delete a department


@app.route('/departments/delete/<int:dnumber>', methods=('POST',))
def delete_department(dnumber):
    # Restrict normal users
    if current_user.role == 'normal_user':
        flash('You do not have permission to delete departments.', 'danger')
        return redirect(url_for('view_departments'))

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM Department WHERE Dnumber = %s", (dnumber,))
        conn.commit()
        flash('Department deleted successfully!', 'success')
    except Exception as e:
        conn.rollback()
        flash(f'Error deleting department: {e}', 'danger')
    finally:
        cursor.close()
        conn.close()

    return redirect(url_for('view_departments'))



# Route to view all projects
@app.route('/projects')
def view_projects():
    conn = get_db_connection()
    cursor = conn.cursor()
    if current_user.role == 'super_admin':
        cursor.execute("SELECT Pnumber, Pname, Plocation, Dnum FROM Project")
    else:
        cursor.execute("SELECT DISTINCT Pnumber, Pname, Plocation, Dnum FROM DepartmentProject WHERE Dnum = %s", (current_user.department_id,))
    projects = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('projects.html', projects=projects, user_role=current_user.role)

# Route to add a new project


@app.route('/projects/add', methods=('GET', 'POST'))
def add_project():
    # Restrict normal users
    if current_user.role == 'normal_user':
        flash('You do not have permission to add projects.', 'danger')
        return redirect(url_for('view_projects'))

    if request.method == 'POST':
        pname = request.form['pname']
        pnumber = request.form['pnumber']
        plocation = request.form['plocation']
        dnum = request.form['dnum']

        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO Project (Pname, Pnumber, Plocation, Dnum) VALUES (%s, %s, %s, %s)",
                (pname, pnumber, plocation, dnum)
            )
            conn.commit()
            flash('Project added successfully!', 'success')
        except Exception as e:
            conn.rollback()
            flash(f'Error adding project: {e}', 'danger')
        finally:
            cursor.close()
            conn.close()
        return redirect(url_for('view_projects'))

    return render_template('add_project.html')


@app.route('/projects/update/<int:pnumber>', methods=('GET', 'POST'))
def update_project(pnumber):
    # Restrict normal users
    if current_user.role == 'normal_user':
        flash('You do not have permission to update projects.', 'danger')
        return redirect(url_for('view_projects'))

    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        pname = request.form['pname']
        plocation = request.form['plocation']
        dnum = request.form['dnum']

        try:
            cursor.execute(
                "UPDATE Project SET Pname = %s, Plocation = %s, Dnum = %s WHERE Pnumber = %s",
                (pname, plocation, dnum, pnumber)
            )
            conn.commit()
            flash('Project updated successfully!', 'success')
        except Exception as e:
            conn.rollback()
            flash(f'Error updating project: {e}', 'danger')
        finally:
            cursor.close()
            conn.close()
        return redirect(url_for('view_projects'))

    try:
        cursor.execute(
            "SELECT Pnumber, Pname, Plocation, Dnum FROM Project WHERE Pnumber = %s", (pnumber,))
        project = cursor.fetchone()
    except Exception as e:
        flash(f'Error fetching project data: {e}', 'danger')
        project = None
    finally:
        cursor.close()
        conn.close()

    return render_template('update_project.html', project=project)

# Route to delete a project


@app.route('/projects/delete/<int:pnumber>', methods=('POST',))
def delete_project(pnumber):
    # Restrict normal users
    if current_user.role == 'normal_user':
        flash('You do not have permission to delete projects.', 'danger')
        return redirect(url_for('view_projects'))

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM Project WHERE Pnumber = %s", (pnumber,))
        conn.commit()
        flash('Project deleted successfully!', 'success')
    except Exception as e:
        conn.rollback()
        flash(f'Error deleting project: {e}', 'danger')
    finally:
        cursor.close()
        conn.close()

    return redirect(url_for('view_projects'))



@app.route('/joined_data')
def view_joined_data():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Get filter parameters from query string
    department = request.args.get('department')
    project = request.args.get('project')
    min_salary = request.args.get('min_salary')
    max_salary = request.args.get('max_salary')

    # Base query
    query = """
        SELECT e.Fname, e.Lname, e.Salary, d.Dname, p.Pname, p.Plocation
        FROM Employee e
        JOIN Department d ON e.Dno = d.Dnumber
        JOIN Project p ON d.Dnumber = p.Dnum
    """
    filters = []
    params = []

    if current_user.role != "super_admin":
        filters.append("d.Dnumber = %s")
        params.append(current_user.department_id)

    # Add filters based on user input
    if department:
        filters.append("d.Dname = %s")
        params.append(department)
    if project:
        filters.append("p.Pname ILIKE %s")
        params.append(f"%{project}%")
    if min_salary:
        filters.append("e.Salary >= %s")
        params.append(min_salary)
    if max_salary:
        filters.append("e.Salary <= %s")
        params.append(max_salary)

    # Append filters to the query
    if filters:
        query += " WHERE " + " AND ".join(filters)

    query += " ORDER BY e.Lname, e.Fname;"

    cursor.execute(query, tuple(params))
    joined_data = cursor.fetchall()

    # Fetch all departments for the filter dropdown
    cursor.execute("SELECT Dnumber, Dname FROM Department ORDER BY Dname;")
    departments = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template(
        'joined_data.html',
        joined_data=joined_data,
        departments=departments
    )




@app.route('/joined_data/download')
def download_joined_data():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Get filter parameters from query string
    department = request.args.get('department')
    project = request.args.get('project')
    min_salary = request.args.get('min_salary')
    max_salary = request.args.get('max_salary')

    # Base query
    query = """
        SELECT e.Fname, e.Lname, e.Salary, d.Dname, p.Pname, p.Plocation
        FROM Employee e
        JOIN Department d ON e.Dno = d.Dnumber
        JOIN Project p ON d.Dnumber = p.Dnum
    """
    filters = []
    params = []

    if current_user.role != "super_admin":
        filters.append("d.Dnumber = %s")
        params.append(current_user.department_id)

    # Add filters based on user input
    if department:
        filters.append("d.Dname = %s")
        params.append(department)
    if project:
        filters.append("p.Pname ILIKE %s")
        params.append(f"%{project}%")
    if min_salary:
        filters.append("e.Salary >= %s")
        params.append(min_salary)
    if max_salary:
        filters.append("e.Salary <= %s")
        params.append(max_salary)

    # Append filters to the query
    if filters:
        query += " WHERE " + " AND ".join(filters)

    query += " ORDER BY e.Lname, e.Fname;"

    cursor.execute(query, tuple(params))
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    # Convert the data to a Pandas DataFrame
    columns = ['First Name', 'Last Name', 'Salary', 'Department', 'Project', 'Project Location']
    df = pd.DataFrame(data, columns=columns)

    # Create an Excel file in memory
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Joined Data')

    output.seek(0)  # Move to the beginning of the file

    # Send the file as a download
    return send_file(
        output,
        as_attachment=True,
        download_name='joined_data.xlsx',
        mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if the file part is present
        if 'file' not in request.files:
            flash('No file part', 'danger')
            return redirect(request.url)

        file = request.files['file']

        # Check if the file has a valid name and extension
        if file.filename == '':
            flash('No selected file', 'danger')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            table_name = os.path.splitext(filename)[0]  # Extract the table name from the file name (without extension)

            # Save the file temporarily
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            # Read the Excel file into a DataFrame
            try:
                df = pd.read_excel(file_path)
            except Exception as e:
                flash(f"Error reading Excel file: {e}", 'danger')
                return redirect(request.url)

            # Connect to the database
            conn = get_db_connection()
            cursor = conn.cursor()

            try:
                # Check if the table exists
                cursor.execute("""
                    SELECT EXISTS (
                        SELECT FROM information_schema.tables
                        WHERE table_name = %s
                    );
                """, (table_name,))
                table_exists = cursor.fetchone()[0]

                if not table_exists:
                    flash(f"Table '{table_name}' does not exist in the database.", 'danger')
                    return redirect(request.url)

                # Get the column names from the database
                cursor.execute(sql.SQL("""
                    SELECT column_name
                    FROM information_schema.columns
                    WHERE table_name = %s;
                """), (table_name,))
                table_columns = [col[0] for col in cursor.fetchall()]

                # Validate the headers in the Excel file
                if list(df.columns) != table_columns:
                    flash(f"Headers in the file do not match the table columns: {table_columns}", 'danger')
                    return redirect(request.url)

                # Insert rows into the table
                for _, row in df.iterrows():
                    placeholders = ", ".join(["%s"] * len(row))
                    insert_query = sql.SQL("""
                        INSERT INTO {table} ({columns}) VALUES ({values});
                    """).format(
                        table=sql.Identifier(table_name),
                        columns=sql.SQL(", ").join(map(sql.Identifier, table_columns)),
                        values=sql.SQL(placeholders)
                    )
                    try:
                        cursor.execute(insert_query, tuple(row))
                    except Exception as e:
                        conn.rollback()
                        flash(f"Failed to insert row: {e}", 'danger')
                        return redirect(request.url)

                conn.commit()
                flash(f"Data successfully inserted into '{table_name}'.", 'success')

            except Exception as e:
                conn.rollback()
                flash(f"Error processing file: {e}", 'danger')

            finally:
                cursor.close()
                conn.close()
                os.remove(file_path)  # Clean up the uploaded file

            return redirect(url_for('index'))

        else:
            flash('Invalid file type. Please upload an Excel file.', 'danger')
            return redirect(request.url)

    return render_template('upload_file.html')




