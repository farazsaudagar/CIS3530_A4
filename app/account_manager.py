from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from app.db import get_db_connection
from app import app
import datetime

# Route to view all users (Only for super admins)
@app.route('/users', methods=['GET'])
@login_required
def view_users():
    if current_user.role != 'super_admin':
        flash("You do not have permission to access this page.", "danger")
        return redirect(url_for('index'))
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT u.user_id, u.username, u.role, d.Dname
        FROM users u
        LEFT JOIN Department d ON u.department_id = d.Dnumber               
    """)
    users = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template('view_users.html', users=users)

@app.route('/create_user', methods=['GET', 'POST'])
@login_required
def create_user():
    if current_user.role != 'super_admin':
        flash("You do not have permission to access this page.", "danger")
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        role = request.form['role']
        department_id = request.form['department_id']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (username, password, role, department_id) VALUES (%s, %s, %s, %s)",
            (username, generate_password_hash(password), role, department_id)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('view_users'))

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT Dnumber, Dname FROM Department")
    departments = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template('create_user.html', departments=departments)


# Route to delete a user (Only for super admins)
@app.route('/delete_user/<int:user_id>', methods=['POST'])
@login_required
def delete_user(user_id):
    if current_user.role != 'super_admin':
        flash("You do not have permission to perform this action.", "danger")
        return redirect(url_for('index'))
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        # Delete the user from the database
        cursor.execute("DELETE FROM users WHERE user_id = %s", (user_id,))
        conn.commit()
        flash("User deleted successfully!", "success")
    except Exception as e:
        flash(f"Error deleting user: {str(e)}", "danger")
    finally:
        cursor.close()
        conn.close()
    
    return redirect(url_for('view_users'))

# Route to update a user's role (Only for Super Admins)
@app.route('/update_user_role/<int:user_id>', methods=['GET', 'POST'])
@login_required
def update_user_role(user_id):
    if current_user.role != 'super_admin':
        flash("You do not have permission to access this page.", "danger")
        return redirect(url_for('view_users'))
    
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        new_role = request.form['role']

        try:
            # Update the user's role in the database
            cursor.execute("UPDATE users SET role = %s WHERE user_id = %s", (new_role, user_id))

            # Optionally, update user_roles table if you use it
            time_now = datetime.datetime.now()
            role_id = {'super_admin': 1, 'department_admin': 2, 'normal_user': 3}[new_role]
            cursor.execute("""
                INSERT INTO user_roles (user_id, role_id, assigned_at) 
                VALUES (%s, %s, %s)
                ON CONFLICT (user_id) DO UPDATE SET role_id = %s, assigned_at = %s
            """, (user_id, role_id, time_now, role_id, time_now))

            conn.commit()
            flash("Role updated successfully!", "success")
        except Exception as e:
            flash(f"Error updating role: {str(e)}", "danger")
        finally:
            cursor.close()
            conn.close()

        return redirect(url_for('view_users'))

    # Fetch user details
    cursor.execute("SELECT username, role FROM users WHERE user_id = %s", (user_id,))
    user = cursor.fetchone()

    cursor.close()
    conn.close()

    return render_template('update_user_role.html', user=user, user_id=user_id)
