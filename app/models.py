from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    vote = db.relationship('Vote',backref = 'user',lazy="dynamic")
            
    password_hash = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))
    pitches = db.relationship('blog',backref = 'user',lazy="dynamic")
    comments = db.relationship('Comment',backref = 'user',lazy="dynamic")
    categories=db.relationship('BlogCategory',backref = 'user',lazy="dynamic")
    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,id):
        reviews = Comment.query.filter_by(blog_id=id).all()
        return comments


    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)


    def __repr__(self):
        return f'User {self.username}'

class Blog(db.Model):
    
    __tablename__ = 'blog'

    id = db.Column(db.Integer,primary_key = True)
    pitch = db.Column(db.String)
    category_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    comments = db.relationship('Comment',backref = 'blog',lazy="dynamic")
            

    def save_blog(self):
        '''
        Function that saves pitches
        '''
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_all_blogs(cls):
       
        return Pitch.query.all()

    @classmethod
    def get_blogs_by_category(cls,cat_id):
        
        return Pitch.query.filter_by(category_id= cat_id)




class Comment(db.Model):

    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    comment= db.Column(db.String)
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitch.id'))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    username =  db.Column(db.String)
    votes= db.Column(db.Integer)
    

    def save_comment(self):
        '''
        Function that saves comments
        '''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def clear_comments(cls):
        Comment.all_comments.clear()

    @classmethod
    def get_comments(cls,id):
        comments = Comment.query.filter_by(pitch_id=id).all()

        return comments

class Subscribe(db.Model):
    __tablename__ = 'subscribe'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
   
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    

    def __repr__(self):
        return f'User {self.name}'  
        db.session.add(self)
        db.session.commit()


class BlogCategory(db.Model):
    '''
    Function that defines different categories of pitches
    '''
    __tablename__ ='blog_categories'


    id = db.Column(db.Integer, primary_key=True)
    name_of_category = db.Column(db.String(255))
    category_description = db.Column(db.String(255))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

    @classmethod
    def get_categories(cls):
        
        categories = BlogCategory.query.all()
        return categories    
if __name__ == '__main__':
    app.manage()         
