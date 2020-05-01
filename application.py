from flask import Flask, render_template, url_for, flash, redirect, request
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY']= 'mysecretkey'

@app.route('/')
@app.route('/home')
def home():
    return render_template ('home.html')

@app.route('/about')
def about():
    return render_template ('about.html')

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for { form.username.data }!','success')
        return redirect(url_for('home'))
    return render_template ('register.html', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template ('login.html', form=form)


if __name__=='__main__':
    app.run(debug=True)