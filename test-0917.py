from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = os.urandom(16)  # Generate a random secret key for session

# Sample authentication credentials
USERNAME = 'user'
PASSWORD = 'pass'

# Login form HTML
login_page = '''
<!doctype html>
<title>Login</title>
<h2>Login</h2>
<form method="post">
  <input type="text" name="username" placeholder="Username" required>
  <input type="password" name="password" placeholder="Password" required>
  <input type="submit" value="Login">
</form>
{% if error %}
<p style="color:red">{{ error }}</p>
{% endif %}
'''

# Login page
@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] == USERNAME and request.form['password'] == PASSWORD:
            session['logged_in'] = True
            return redirect(url_for('protected'))
        else:
            error = 'Incorrect username or password'
    return render_template('login.html', error=error)

# Protected page
@app.route('/protected')
def protected():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return 'Login successful!'

# Logout
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=False)  # Set debug mode to False for production use
