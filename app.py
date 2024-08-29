from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
import bcrypt  # Import bcrypt for password hashing
import os

# Initialize Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///practice_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.urandom(24)  # Secure random secret key for sessions
db = SQLAlchemy(app)

# Define the database model
class LoginDetails(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<LoginDetails {self.name}>'

# Function to initialize the database
def init_db():
    with app.app_context():
        if not os.path.exists('practice_database.db'):
            db.create_all()
    print("Database and tables created.")

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email').lower()  # Convert input email to lowercase
        password = request.form.get('password')

        # Query the database to find the user by email (case-insensitive)
        user = LoginDetails.query.filter_by(email=email).first()

        if user:
            # Check if the password matches the hashed password stored in the database
            if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                # If password matches, store the user's name in session and redirect
                session['name'] = user.name
                return redirect(url_for('welcome'))
            else:
                flash("Incorrect password. Please try again.")
        else:
            flash("Email not found. Please Register if you have not made an account yet.")

    return render_template('login.html')  # Form will be cleared by default when rendering the page again

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        emailid = request.form.get('email').lower()  # Convert email to lowercase before storing
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        if password != confirm_password:
            flash("Passwords do not match. Please try again.")
            return render_template('register.html', name=name, email=emailid)

        # Hash the password before storing it in the database
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        # Insert the new user into the database with the hashed password
        new_user = LoginDetails(name=name, email=emailid, password=hashed_password.decode('utf-8'))
        db.session.add(new_user)
        db.session.commit()
        print('Record inserted for', name)

        # Store the user's name in session and redirect to the welcome page
        session['name'] = name
        return redirect(url_for('welcome'))

    return render_template('register.html')  # Form will be cleared by default when rendering the page again

@app.route('/welcome')
def welcome():
    name = session.get('name', 'Guest')
    return render_template('welcome.html', name=name)

@app.route('/view')
def view_records():
    users = LoginDetails.query.all()
    return render_template('view_users.html', users=users)

@app.route('/delete_user/<int:user_id>')
def delete_user(user_id):
    user = LoginDetails.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return "User deleted!"
    return "User not found!"

@app.route('/logout')
def logout():
    session.clear()  # Clear the session to log out the user
    return redirect(url_for('login'))

# Initialize the database
init_db()

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
