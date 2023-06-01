from flask_app.config.mysqlconnection import MySQLConnection
from flask_app import DB
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]')
PASSWORD_REGEX= re.compile(r'^[a-zA-Z0-9]')

class User:
    def __init__(self,data):
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.email=data['email']
        self.password=data['password']

    
    #======================create user====================
    @classmethod
    def create_user(cls,data):
        query="""INSERT INTO users(first_name,last_name,email,password)
                VALUES(%(first_name)s,%(last_name)s,%(email)s,%(password)s);"""
        
        return MySQLConnection(DB).query_db(query,data)
    
    #======================read user====================
    @classmethod
    def get_users(cls):
        query="""
                SELECT * FROM users;
                """
        result=MySQLConnection(DB).query_db(query)
        users=[]
        for row in result:
            users.append(row)
        print("users==========",users)
        return users
    
    #======================validation registration====================
    @staticmethod
    def validate_user(user):
        is_valid = True # we assume this is true
        if (not NAME_REGEX.match(user['first_name'])) :
            flash("first name must be letters only, at least 2 characters and that it was submitted.","reg")
            is_valid = False
        elif (len(user['first_name']) < 2):
            flash("first name must be letters only, at least 2 characters and that it was submitted.","reg")
            is_valid = False
        if (not NAME_REGEX.match(user['last_name'])) :
            flash("last name must be letters only, at least 2 characters and that it was submitted.","reg")
            is_valid = False
        elif  (len(user['last_name']) < 2):
            flash("last name must be letters only, at least 2 characters and that it was submitted.","reg")
            is_valid = False
        if (not EMAIL_REGEX.match(user['email'])) or (len(user['email']) < 2):
            flash("Your email is not exist.","reg")
            is_valid = False
        if len(user['password']) < 8:
            flash("Password must be at least 8 characters.","reg")
            is_valid = False
        elif (not PASSWORD_REGEX.match(user['password'])):
            flash("Password must be have a least 1 number and 1 uppercase letter.","reg")
            is_valid = False
        if not(user['confirm_password']==user['password']):
            flash("Your confirm password is not compatible to password.","reg")
            is_valid = False
        
        return is_valid