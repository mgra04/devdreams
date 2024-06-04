from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from .models import User
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        login_email = request.form.get('login-email')
        login_password = request.form.get('login-password')
        remember = request.form.get('remember')

        sign_in_user = User.query.filter_by(email = login_email).first()
        if sign_in_user:
            if check_password_hash(sign_in_user.password, login_password):
                flash('Logged in successfully!', category = 'success')
                # print(bool(remember))
                login_user(sign_in_user, remember = bool(remember))
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category = 'error')
        else:
            flash('Email does not exist.', category = 'error')

    return render_template('sign.html', sign_in_user=current_user)

@auth.route('/sign', methods = ['GET', 'POST'])
def sign():   
    if request.method == 'POST':
        sign_username = request.form.get('sign-username')
        sign_email = request.form.get('sign-email')
        sign_password1 = request.form.get('sign-password')
        sign_password2 = request.form.get('sign-confirm-password')

        sign_user = User.query.filter_by(email = sign_email).first()
        if sign_user:
            flash('Email already exists.', category='error')
        elif len(sign_email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif sign_password1 != sign_password2:
            flash("Passwords do not match.", category='error')
        elif len(sign_password1) < 8:
            flash('Password must be at least 8 characters.', category='error')
        else:
            new_user = User(email=sign_email, username=sign_username, password=generate_password_hash(sign_password1, method = 'pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember = False)
            flash('Account created!.', category='success')
            return redirect(url_for('views.home'))

    return render_template('sign.html', sign_user = current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully!', category='success')
    return redirect(url_for('auth.login'))
