from flask import render_template, url_for, flash, redirect, request
from application import app, db, bcrypt
from application.forms import RegistrationForm, LoginForm, BookForm
from application.models import User, Book
from flask_login import login_user, current_user, logout_user, login_required


@app.route('/')
@app.route('/home')
def home():
    books = Book.query.all()
    return render_template ('home.html', books=books)

@app.route('/about')
def about():
    return render_template ('about.html',title='about')
    
@app.route('/books')
def books():
    return render_template ('books.html',title='Books')

@app.route('/register', methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(fname=form.fname.data, lname=form.lname.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for { form.fname.data }!','success')
        return redirect(url_for('login'))
    return render_template ('register.html', form=form)

@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check email and password.', 'danger')
    return render_template ('login.html', form=form)

@app.route('/logout')
def logout():
    form = BookForm
    logout_user()
    return redirect(url_for('home'))

@app.route('/account', methods=['GET','POST'])
@login_required
def account():
    image_file = url_for('static', filename='profile_pics/default.jpg')
    return render_template ('account.html', title= 'Account', image_file=image_file)

@app.route("/book/new", methods=['GET','POST'])
@login_required
def new_book():
    form = BookForm()
    if form.validate_on_submit():
        book = Book(isbn=form.isbn.data, title=form.title.data,
        author=form.author.data, year=form.year.data)
        db.session.add(book)
        db.session.commit()
        flash("Your book has been added to the database.", "success")
        return redirect(url_for('home'))
    return render_template('add_book.html', title='Add Book', form=form)
