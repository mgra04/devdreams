from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required
from .decorators import admin_required
from . import db
from .models import Post, PostSection, User

admin = Blueprint('admin', __name__)

@admin.route('/admin-panel', methods=['GET'])
@login_required
@admin_required
def admin_panel():
    users = User.query.all()
    posts = Post.query.all()
    return render_template('admin_panel.html', users=users, posts=posts)

@admin.route('/admin-panel/delete-user/<int:user_id>', methods=['POST'])
@login_required
@admin_required
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash('Użytkownik został usunięty', 'success')
    return redirect(url_for('admin.admin_panel'))

@admin.route('/admin-panel/delete-post/<int:post_id>', methods=['POST'])
@login_required
@admin_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    flash('Post został usunięty', 'success')
    return redirect(url_for('admin.admin_panel'))

@admin.route('/posts-creator', methods=['GET', 'POST'])
@login_required
@admin_required
def posts_creator():
    if request.method == 'POST':
        try:
            post_title = request.form['post-title']
            post_image_url = request.form['post-image-url']
            post_category = request.form['post-category']
            post_read_time = request.form['post-read-time']
            post_main_technology = request.form['post-main-technology']

            post = Post(title=post_title, image_url=post_image_url, category=post_category, read_time=post_read_time, main_technology=post_main_technology)
            db.session.add(post)

            for field, content in request.form.items():
                for i in range(10):
                    if field.endswith(f'_content_{i}'):
                        type = field.split('_')[0]
                        section = PostSection(type=type, content=content, post=post)
                        db.session.add(section)
                    else:
                        continue

            db.session.commit()
            flash('Post created successfully!', category='success')
            return redirect(url_for('views.blog'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error creating post: {str(e)}', category='error')
            return redirect(url_for('admin.posts_creator'))

    return render_template('posts_creator.html')

