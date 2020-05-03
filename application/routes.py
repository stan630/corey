from flask import render_template, url_for, flash, redirect, request
from application import app
from application.forms import RegistrationForm, LoginForm
from application.models import User, Book


posts = [
    {
        'author': 'Smedley Doolittle',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Mia Johnson',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template ('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template ('about.html',title='about')

@app.route('/books')
def books():
    return render_template ('books.html',title='Books')

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for { form.fname.data }!','success')
        return redirect(url_for('home'))
    return render_template ('register.html', form=form)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have successfully logged in!','success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful.', 'danger')
    return render_template ('login.html', form=form)