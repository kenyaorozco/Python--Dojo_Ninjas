print("model file running")

from types import ClassMethodDescriptorType
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninjas import Ninja

class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninja = []


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojo_ninja_schema.dojos;"
        results = connectToMySQL('dojo_ninja_schema').query_db(query)
        print(results)

        dojos = []
        for dojo in results:
            print(dojo)
            dojos.append( cls(dojo) ) 
        return dojos
        
    @classmethod
    def show_one(cls,data):

        query ="SELECT * FROM dojos JOIN ninjas on dojos.id = ninjas.dojos_id WHERE dojos.id= %(id)s;" 
        results = connectToMySQL('dojo_ninja_schema').query_db(query,data)
        # print(results)

        one_dojo = cls(results[0])
        print(one_dojo)

        for ninja in results:
            ninja_data = {
                "id": ninja["ninjas.id"],
                "first_name":ninja["first_name"],
                "last_name":ninja["last_name"],
                "age":ninja["age"],
                "dojos_id":ninja["dojos_id"],
                "created_at":ninja["created_at"],
                "updated_at":ninja["updated_at"]
            }
            one_dojo.ninja.append(Ninja(ninja_data))
        return one_dojo

    # @classmethod
    # def save(cls,data):
    #     query ="Select * from ninjas; Insert into dojos (first_name,last_name,age) Values (%(first_name)s,%(last_name)s,% (age)s);"

    #     new_user = connectToMySQL('dojo_ninja_schema').query_db(query,data)
    #     return new_user






    # @classmethod
    # def one_all(cls,data):
    #     query = "INSERT INTO users (first_name,last_name,email) VALUES (%(first_name)s,%(last_name)s,%(email)s);"

    #     new_user = connectToMySQL('users_schema').query_db(query,data)
    #     return new_user

    # @classmethod
    # def show_one(cls,data):
        
        
            
