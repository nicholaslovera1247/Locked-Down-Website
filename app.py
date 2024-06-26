import csv
from flask import Flask, render_template, request, url_for, flash, redirect, session
from database import add_user
from authenticate import check_password,check_username, check_locked, add_lock, reset_lock, get_access_level
from passwordsettings import hash_pw, authenticate_password, strong_pw

app = Flask(__name__)
app.secret_key = "CS2660@FinalLab!!!!"

@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('home.html',
                           title="Home Page",
                           heading="Home Page",
                           )

@app.route("/newuser.html", methods=['GET', 'POST'])
def newuser():
    if request.method == "POST":
        username = request.form.get('username')
        if check_username(username):
            flash("Username taken","danger")
        else:
            session['username'] = username
            return redirect(url_for('createpassword'))
    return render_template('newuser.html',
                           title="New User",
                           heading="New User",
                           )

@app.route("/createpassword", methods=['GET', 'POST'])
def createpassword():
    username = session['username']
    if request.method == "POST":
        choice = request.form.get('option')
        if choice == 'strong':
            password = strong_pw()
            if authenticate_password(password):
                add_user(username, password)
                return redirect(url_for('home'))
        elif choice == 'custom':
            password = request.form.get('custom_password')
            if authenticate_password(password):
                add_user(username, password)
                return redirect(url_for('home'))
            else:
                flash("Password not strong enough","danger")
    return render_template('createpassword.html',
                           title="New Password",
                           heading="New Password",
                           username=username,
                           )



@app.route("/login.html", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if check_username(username):
            if check_locked(username):
                flash('Too many attempts to login, contact support')
            elif check_password(username, password) == False:
                flash("Invalid password")
                add_lock(username)
            else:
                reset_lock(username)
                access_level = get_access_level(username)
                session['access_level'] = access_level
                return redirect(url_for('login_success'))

        else:
            flash("Invalid username")
    return render_template('login.html',
                           title="Secure Login",
                           heading="Secure Login"
                           )

@app.route("/login_success", methods=['GET', 'POST'])
def login_success():
    if request.method == 'POST':
        destination = request.form.get()
        return redirect(url_for('destination'))
    access_level= session['access_level']
    return render_template('login_success.html',
                           title = "Login Success",
                           heading="Login Success",
                           access_level = access_level)

@app.route("/admincontrols", methods=['GET', 'POST'])
def admincontrols():
    return render_template('admincontrols.html',
                           title="Admin Controls",
                           heading="Admin Controls"
                           )

@app.route("/finances", methods=['GET', 'POST'])
def finances():
    return render_template('finances.html',
                           title="Finances",
                           heading="Finances"
                           )
@app.route("/scheduling", methods=['GET', 'POST'])
def scheduling():
    return render_template('scheduling.html',
                           title="Scheduling",
                           heading="Scheduling"
                           )

@app.route("/timecards", methods=['GET', 'POST'])
def timecards():
    return render_template('timecards.html',
                           title="Time Cards",
                           heading="Time Cards"
                           )