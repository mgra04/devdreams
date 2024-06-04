from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user
from .models import db, Post, Comment, CommentReply, User
from datetime import datetime, timezone


views = Blueprint('views', __name__)

@views.route('/', methods = ['GET', 'POST'])
def home():
    return render_template("home.html")

@views.route('/all-posts', methods=['GET'])
def all_posts():
    posts = Post.query.all()
    return render_template("allposts.html", posts=posts)

@views.route('/figma', methods=['GET'])
def figma():
    posts = Post.query.all()
    return render_template("figma.html", posts=posts)

@views.route('/fundamentals', methods=['GET'])
def fundamentals():
    posts = Post.query.all()
    return render_template("fundamentals.html", posts=posts)

@views.route('/js-frameworks', methods=['GET'])
def js_frameworks():
    posts = Post.query.all()
    return render_template("js-frameworks.html", posts=posts)

@views.route('/python-frameworks', methods=['GET'])
def python_frameworks():
    posts = Post.query.all()
    return render_template("python-frameworks.html", posts=posts)

@views.route('/3d', methods=['GET'])
def three_d():
    posts = Post.query.all()
    return render_template("3d.html", posts=posts)

@views.route('/post/<int:post_id>', methods=['GET', 'POST'])
def post(post_id):
    post = Post.query.get_or_404(post_id)

    if request.method == 'POST':
        if 'content' in request.form:
            content = request.form.get('content')
            print(f"Received content: {content}")
            if not content:
                flash('Comment content cannot be empty', 'error')
            else:
                new_comment = Comment(
                    content=content,
                    user_id=current_user.id,
                    post_id=post_id,
                    created_at=datetime.now(timezone.utc)
                )
                db.session.add(new_comment)
                db.session.commit()
                flash('Comment added successfully', 'success')
                return redirect(url_for('views.post', post_id=post_id))
    if 'reply-content' in request.form:
            reply_content = request.form.get('reply-content')
            comment_id = request.form.get('comment-id')
            print(f"Received reply content: {reply_content}, comment_id: {comment_id}")
            if not reply_content:
                flash('Reply content cannot be empty', 'error')
            else:
                new_reply = CommentReply(
                    content=reply_content,
                    user_id=current_user.id,
                    comment_id=comment_id,
                    created_at=datetime.now(timezone.utc)
                )
                db.session.add(new_reply)
                db.session.commit()
                flash('Reply added successfully', 'success')
                return redirect(url_for('views.post', post_id=post_id))
    
    comments = Comment.query.filter_by(post_id=post_id).all()
    comments_data = []
    for comment in comments:
        comment_data = {
            'id': comment.id,
            'content': comment.content,
            'created_at': comment.added_date(),
            'username': comment.user.username,
            'profile_img': comment.user.profile_img if comment.user.profile_img else url_for('static', filename='img/base-profile-img.jpg'),
            'likes': comment.likes,
            'replies': []
        }
        
        for reply in comment.replies:
            reply_data = {
                'content': reply.content,
                'created_at': reply.added_date(),
                'username': User.query.get(reply.user_id).username,
                'profile_img': User.query.get(reply.user_id).profile_img if User.query.get(reply.user_id).profile_img else url_for('static', filename='img/base-profile-img.jpg'),
                'likes': reply.likes
            }
            comment_data['replies'].append(reply_data)
        
        comments_data.append(comment_data)
    
    comments_count = len(comments_data)
    return render_template('post.html', post=post, comments_count=comments_count, comments_data=comments_data)
