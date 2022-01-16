from flask import Flask
app = Flask(__name__)
from flask import render_template
from flask import request, redirect

@app.route("/mypage/me")
def mypage():
    return render_template ("index.html")

@app.route("/mypage/contact", methods = ['POST'] )
def feed():
    return render_template ("index3.html")
