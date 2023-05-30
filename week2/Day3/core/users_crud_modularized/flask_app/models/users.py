from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB
class User:
    def __init__(self,data):
        self.id=data['id']
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.email=data['email']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']



    # =========================Read All======================
    @classmethod
    def read(cls):
        query="""
                SELECT *FROM users;
                """
        result=connectToMySQL(DB).query_db(query)
        this_user=[]
        for row in result:
            this_user.append(cls(row))
        return this_user
    
    # =========================create======================
    @classmethod
    def create(cls,data):
        query="""
            insert into users(first_name,last_name,email)
            value(%(first_name)s,%(last_name)s,%(email)s)
            """
        return connectToMySQL(DB).query_db(query,data)
    
    # =========================Read one======================
    @classmethod
    def read_one(cls,data):
        query="""
                SELECT *FROM users
                WHERE id=%(id)s;
                """
        re=connectToMySQL(DB).query_db(query,data)
        print("*************",re)
        one=cls(re[0])

        return one
    
    # =========================Update======================
    @classmethod
    def update(cls,data):
        query="""
                UPDATE  users
                SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s
                where id=%(id)s;
                """
    
        return connectToMySQL(DB).query_db(query,data)


    # =========================delete======================
    @classmethod
    def delete(cls,data):
        query="""
                delete from users
                where id=%(id)s
                """
        return connectToMySQL(DB).query_db(query,data)
    
    # =========================the last user in table======================
    @classmethod
    def last_user(cls):
        query="""
            select * from users order by id desc
            limit 1;
            """
        result=connectToMySQL(DB).query_db(query)
        return cls(result[0])
