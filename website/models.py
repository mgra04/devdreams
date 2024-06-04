from . import db
from flask_login import UserMixin
from datetime import datetime, timezone


'''likes = db.Table('likes',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('post_id', db.Integer, db.ForeignKey('post.id'), primary_key=True)
)'''
#jeszcze jestem za głupi żeby tym operować :(

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150), nullable=False)
    username = db.Column(db.String(150), nullable=False)
    role = db.Column(db.String(50), default='user')
    profile_img = db.Column(db.String(200), nullable=True)
    comments = db.relationship('Comment', backref='user', lazy=True, cascade="all, delete-orphan")
    # liked_posts = db.relationship('Post', secondary=likes, backref=db.backref('liked_by', lazy='dynamic'))


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    image_url = db.Column(db.String(200), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    main_technology = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))
    read_time = db.Column(db.String(10), nullable=False)
    sections = db.relationship('PostSection', backref='post', lazy=True, cascade="all, delete-orphan")
    comments = db.relationship('Comment', backref='post', lazy=True, cascade="all, delete-orphan")

    def created_date(self):
        return self.created_at.strftime("%d %B, %Y")


class PostSection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    type = db.Column(db.String(20), nullable=False)
    content = db.Column(db.Text, nullable=False)


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    likes = db.Column(db.Integer, default=0)
    replies = db.relationship('CommentReply', backref='comment', lazy=True, cascade="all, delete-orphan")

    def added_date(self):
        return self.created_at.strftime("%H:%M, %d %B, %Y")


class CommentReply(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    comment_id = db.Column(db.Integer, db.ForeignKey('comment.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))
    likes = db.Column(db.Integer, default=0)

    def added_date(self):
        return self.created_at.strftime("%H:%M, %d %B, %Y")
