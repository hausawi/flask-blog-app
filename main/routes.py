from flask import render_template, url_for, flash, redirect
from main.forms import RegistrationForm, LoginForm
from main.models import User, Post
from main.posts import Data
from main import app


@app.route("/")
def home():
    return render_template('home.html', posts=Data, title='Home')

@app.route("/about")
def about():
    return render_template('about.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'sudastack@gmail.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Loging Unseccessful. Please enter the correct cridentials', 'danger')

    return render_template('login.html', title='Login', form=form)


@app.route("/alert")
def alert():
    return render_template('alert.html')