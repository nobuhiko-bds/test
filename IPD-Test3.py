from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 実際のアプリではデータベースを使用し、パスワードはハッシュ化して保存することが推奨されます
users = {'user1': 'password123'}

@app.route("/", methods=["POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username in users and users[username] == password:
            return f"<h2>Welcome, {username}!</h2>"
        else:
            error = "Invalid credentials"
    return render_template("login.html", error=error)

if __name__ == "__main__":
    app.run(debug=False)
  
