# Author: Nils van der Deen

from flask import Flask, render_template, redirect, request, session
from flask_bcrypt import Bcrypt

from database import do_database


bcrypt = Bcrypt()
app = Flask(__name__)

# Set the secret key (needed for session)
# Normally this would generate a random key like this:
# >>> import os
# >>> os.urandom(24)
# But I'm using a fixed key for this example

app.secret_key = "secret"

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/app/register', methods=['POST'])
def register_user():
    # Get the form data
    username = request.form['username']
    password = request.form['password']

    # Check if the username already exists
    user_id = do_database(f"SELECT COUNT(id) FROM users WHERE username = '{username}'")
    if user_id[0][0] != 0:
        return render_template('register.html', message="Username already exists")


    # Hash the password
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    # Add the user to the database
    do_database(f"INSERT INTO users (username, password) VALUES ('{username}', '{hashed_password}')")

    # Log the user in
    session['username'] = username

    # Redirect to the home page
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)