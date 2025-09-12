from flask import Flask, request, render_template, redirect, url_for
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Use a random secret key for sessions

def authenticate_user(username, password):
    # In a secure implementation, validate username and password against a secure database
    return username == 'admin' and password == 'securepassword123'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if authenticate_user(username, password):
            session['username'] = username  # Store user in session
            return redirect(url_for('secure_page'))
        else:
            error = 'Invalid credentials. Please try again.'
            return render_template('login.html', error=error)
    return render_template('login.html')

@app.route('/secure', methods=['GET'])
def secure_page():
    if 'username' in session:
        return "Welcome to the secure area, {}".format(session['username'])
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=False)  # Disable debug mode in production
