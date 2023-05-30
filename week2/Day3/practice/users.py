from mysqlconnection import connectToMySQL
DB="users_practice"
class User:
    def __init__(self,data):
        self.id=data['id']
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.email=data['email']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']



# =========================read======================
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