from flask import render_template, request, redirect, url_for
from flask_login import current_user
from app import app
from app.db import get_db_connection

# Route to view all employees

@app.route('/employees')
def view_employees():
    conn = get_db_connection()
    cursor = conn.cursor()
    if current_user.role == 'super_admin':
        cursor.execute("SELECT SSN, Fname, Lname, Salary FROM Employee")
    else:
        cursor.execute("SELECT DISTINCT SSN, Fname, Lname, Salary FROM DepartmentEmployee WHERE Dno = %s", (current_user.department_id,))
    employees = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('employees.html', employees=employees)



@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT SSN, Fname, Lname, Salary FROM Employee")
    employees = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', employees=employees)


@app.route('/update/<ssn>', methods=['GET', 'POST'])
def update_salary(ssn):
    conn = get_db_connection()
    cursor = conn.cursor()
    if request.method == 'POST':
        new_salary = request.form['salary']
        cursor.execute(
            "UPDATE Employee SET Salary = %s WHERE SSN = %s", (new_salary, ssn))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('view_employees'))

    cursor.execute(
        "SELECT SSN, Fname, Lname, Salary FROM Employee WHERE SSN = %s", (ssn,))
    employee = cursor.fetchone()
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
    return render_template('departments.html', departments=departments)


@app.route('/departments/add', methods=('GET', 'POST'))
def add_department():
    if request.method == 'POST':
        dname = request.form['dname']
        dnumber = request.form['dnumber']
        mgr_ssn = request.form['mgr_ssn']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Department (Dname, Dnumber, Mgr_ssn) VALUES (%s, %s, %s)",
            (dname, dnumber, mgr_ssn)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('view_departments'))

    return render_template('add_department.html')


# Route to update a department
@app.route('/departments/update/<int:dnumber>', methods=('GET', 'POST'))
def update_department(dnumber):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        dname = request.form['dname']
        mgr_ssn = request.form['mgr_ssn']

        cursor.execute("UPDATE Department SET Dname = %s, Mgr_ssn = %s WHERE Dnumber = %s",
                       (dname, mgr_ssn, dnumber))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('view_departments'))

    cursor.execute(
        "SELECT Dnumber, Dname, Mgr_ssn FROM Department WHERE Dnumber = %s", (dnumber,))
    department = cursor.fetchone()
    cursor.close()
    conn.close()
    return render_template('update_department.html', department=department)

# Route to delete a department


@app.route('/departments/delete/<int:dnumber>', methods=('POST',))
def delete_department(dnumber):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Department WHERE Dnumber = %s", (dnumber,))
    conn.commit()
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
    return render_template('projects.html', projects=projects)

# Route to add a new project


@app.route('/projects/add', methods=('GET', 'POST'))
def add_project():
    if request.method == 'POST':
        pname = request.form['pname']
        pnumber = request.form['pnumber']
        plocation = request.form['plocation']
        dnum = request.form['dnum']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Project (Pname, Pnumber, Plocation, Dnum) VALUES (%s, %s, %s, %s)", (
                pname, pnumber, plocation, dnum)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('view_projects'))

    return render_template('add_project.html')


# Route to update a project
@app.route('/projects/update/<int:pnumber>', methods=('GET', 'POST'))
def update_project(pnumber):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        pname = request.form['pname']
        plocation = request.form['plocation']
        dnum = request.form['dnum']

        cursor.execute("UPDATE Project SET Pname = %s, Plocation = %s, Dnum = %s WHERE Pnumber = %s",
                       (pname, plocation, dnum, pnumber))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('view_projects'))

    cursor.execute(
        "SELECT Pnumber, Pname, Plocation, Dnum FROM Project WHERE Pnumber = %s", (pnumber,))
    project = cursor.fetchone()
    cursor.close()
    conn.close()
    return render_template('update_project.html', project=project)

# Route to delete a project


@app.route('/projects/delete/<int:pnumber>', methods=('POST',))
def delete_project(pnumber):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Project WHERE Pnumber = %s", (pnumber,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('view_projects'))


@app.route('/joined_data')
def view_joined_data():
    conn = get_db_connection()
    cursor = conn.cursor()

    if current_user.role == "super_admin":
        cursor.execute("""
            SELECT e.Fname, e.Lname, e.Salary, d.Dname, p.Pname, p.Plocation
            FROM Employee e
            JOIN Department d ON e.Dno = d.Dnumber
            JOIN Project p ON d.Dnumber = p.Dnum
            ORDER BY e.Lname, e.Fname;
        """)
    else:
        cursor.execute("""
            SELECT DISTINCT Fname, Lname, Salary, Dname, Pname, Plocation, Dnumber
            FROM DepartmentJoinedData
            WHERE Dnumber = %s
            ORDER BY Lname, Fname;
            """, (current_user.department_id,))

    joined_data = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template('joined_data.html', joined_data=joined_data)