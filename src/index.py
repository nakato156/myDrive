from flask import Flask, render_template, session, redirect, request
from socket import gethostname

app = Flask(__name__)

@app.route("/")
def index():
    if "user" not in session:
        print(gethostname())
        return render_template("login.html")
    return render_template("index.html")
    
@app.route("/login")
def login():
    if "user" in session:
        return render_template("index.html")

if __name__=="__main__":
    app.run(port=5555, debug=True)