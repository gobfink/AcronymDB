# apps/models.py

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from app import db, login_manager

class User(UserMixin, db.Model):
    """
    Create a user
    """

    __tablename__ = 'tbl_User'
    
    userID = db.Column(db.Integer, primary_key=True)
    id = userID
    userEmail = db.Column(db.String(80), index=True, unique=True)
    username = db.Column(db.String(80), index=True, unique=True)
    userFN = db.Column(db.String(80), index=True)
    userLN = db.Column(db.String(80), index=True)
    userPasswordHash = db.Column(db.String(128))
    userIsAdmin = db.Column(db.Integer, default=False)
    userLastLoginDT = db.Column(db.DateTime, default=False)

    def setPassdate(self):
        self.userLastLoginDT = datetime.now()


    @property
    def password(self):
        """
        Prevent Password being accessed
        """

        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
      
        self.userPasswordHash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """

        return check_password_hash(self.userPasswordHash, password)

    def __repr__(self):
        return '<User: {}>'.format(self.username)

    #Set up user_loader
    @login_manager.user_loader
    def load_user(userID):
        return User.query.get(int(userID))

class Tag(db.Model):
    """
    Create tag table
    """

    __tablename__ = 'tbl_Tag'

    tagID = db.Column(db.Integer, primary_key=True)
    id = tagID
    tag = db.Column(db.String(60), index=True, unique=True)

    def __repr__(self):
       return '<Tag: {}>'.format(self.tag)
