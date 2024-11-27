from flask import Flask, render_template, redirect, url_for, request, flash, session
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from app import app
from app.db import get_db_connection
import datetime
import psycopg2
from functools import wraps

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Decorator for roles
def role_required(*roles):
    """Decorator to restrict access to users with specific roles."""
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if current_user.is_authenticated and current_user.role in roles:
                return f(*args, **kwargs)
            flash("You do not have permission to access this page.", "danger")
            return redirect(url_for('index'))  # Redirect to a safe page
        return decorated_function
    return decorator

# Define User class for Flask-Login
class User(UserMixin):
    def __init__(self, id, username, password, role, department_id):
        self.id = id
        self.username = username
        self.password_hash = password
        self.role = role
        self.department_id = department_id
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
# Load user function for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE user_id = %s", (user_id,))
    user_data = cur.fetchone()
    cur.close()
    conn.close()
    if user_data:
        return User(id=user_data[0], username=user_data[1], password=user_data[2], role=user_data[3], department_id=user_data[4])
    return None

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username = %s", (username,))
        user_data = cur.fetchone()
        cur.close()
        conn.close()

        if user_data and check_password_hash(user_data[2], password):
            user = User(id=user_data[0], username=user_data[1],
                        password=user_data[2], role=user_data[3], department_id=user_data[4])
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password', 'danger')

    return render_template('login.html')

# Logout route
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        role = request.form['role']
        department_name = request.form['department']  # Get the department name from the form

        conn = get_db_connection()
        cur = conn.cursor()

        try:
            # Check if username already exists
            cur.execute("SELECT * FROM users WHERE username = %s", (username,))
            if cur.fetchone():
                flash('Username already exists!', 'danger')
                return redirect(url_for('register'))

            # Look up the department ID (Dnumber) based on the department name
            cur.execute("SELECT Dnumber FROM Department WHERE Dname = %s", (department_name,))
            department = cur.fetchone()

            if not department:
                flash('Invalid department selected.', 'danger')
                return redirect(url_for('register'))

            department_id = department[0]  # Extract the Dnumber

            # Hash the password and insert the new user
            hashed_password = generate_password_hash(password)
            cur.execute(
                "INSERT INTO users (username, password, role, department_id) VALUES (%s, %s, %s, %s)",
                (username, hashed_password, role, department_id)
            )

            # Retrieve the newly created user's ID
            cur.execute("SELECT user_id FROM users WHERE username = %s", (username,))
            user_id = cur.fetchone()[0]
            time_now = datetime.datetime.now()

            # Insert the user's role into the user_roles table
            if role == 'super_admin':
                role_id = 1
            elif role == 'department_admin':
                role_id = 2
            elif role == 'normal_user':
                role_id = 3
            else:
                flash('Invalid role selected.', 'danger')
                return redirect(url_for('register'))

            cur.execute(
                "INSERT INTO user_roles (user_id, role_id, assigned_at) VALUES (%s, %s, %s)",
                (user_id, role_id, time_now)
            )

            # Commit the transaction
            conn.commit()
            flash('Registration successful! You can now log in.', 'success')

        except Exception as e:
            flash(f"An error occurred: {e}", 'danger')
            conn.rollback()
        finally:
            cur.close()
            conn.close()

        return redirect(url_for('login'))

    return render_template('register.html')



@app.before_request
def set_pg_session_user():
    if current_user.is_authenticated:
        conn = get_db_connection()
        cur = conn.cursor()
        try:
            # Set the session variable for the current user
            cur.execute("SET myapp.current_user_id = %s", (current_user.id,))
            conn.commit()
        except Exception as e:
            app.logger.error(f"Failed to set PostgreSQL session variable: {e}")
        finally:
            cur.close()
            conn.close()
