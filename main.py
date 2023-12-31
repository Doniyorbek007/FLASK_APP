from flask import Flask, render_template
import data

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/blog")
def blog():
    return render_template('blog.html')

@app.route("/user")
def user():
    return render_template('user.html', context = data.users)

@app.route("/admin/<name>")
def admin(name):
    return render_template('admin.html', context = name)

if __name__ == '__main__':
   app.run(debug = True)