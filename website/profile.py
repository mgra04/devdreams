from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from flask_login import login_required, current_user
from .models import db, User
from werkzeug.utils import secure_filename
import os

profile = Blueprint('profile', __name__)
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@profile.route('/profile', methods=['GET', 'POST'])
@login_required
def profile_view():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part', 'error')
            return redirect(url_for('profile.profile_view'))
        
        file = request.files['file']
        
        if file.filename == '':
            flash('No selected file', 'error')
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            upload_folder = current_app.config['UPLOAD_FOLDER']
                
            if not os.path.exists(upload_folder):
                os.makedirs(upload_folder)

            file_path = os.path.join(upload_folder, filename)
            file.save(file_path)
            image_url = url_for('static', filename='uploads/' + filename)

            user = User.query.get(current_user.id)
            
            if user.profile_img:
                file_to_delete = os.path.join(upload_folder, user.profile_img.split('/')[-1])
                if os.path.exists(file_to_delete):
                    os.remove(file_to_delete)
                else:
                    flash(f"File {file_to_delete} does not exist.", 'error')

            user.profile_img = image_url
            db.session.commit()
                
            flash('Profile picture updated', 'success')
            return redirect(url_for('profile.profile_view'))
    
    return render_template('profile.html', user=current_user)
