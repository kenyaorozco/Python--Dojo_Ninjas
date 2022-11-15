print("model file running")


from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojos_id = data['dojos_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojo_ninja_schema.ninjas;"
        results = connectToMySQL('dojo_ninja_schema').query_db(query)
        print(results)

        ninjas = []
        for ninja in results:
            print(ninja)
            ninjas.append( cls(ninja) ) 
        return ninjas

    # @classmethod
    # def show_one(cls,data):
    #     query = "SELECT * FROM dojos JOIN ninjas on dojos.id = ninjas.dojos_id WHERE dojos_id = (%(id)s);"

    #     results = connectToMySQL('dojo_ninja_schema').query_db(query,data)

    #     # if (len(results) < 1):
    #     #     return False
    #     ninjas = []
    #     for ninja in results:
    #         ninja_info = cls(ninja)
    #         print(ninja_info.dojo_name)
    #         # print(ninja)


    #         dojo_data = {
    #             "id":ninja["dojos_id"],
    #             "name":ninja["name"],
    #             "created_at":ninja["created_at"],
    #             "updated_at":ninja["updated_at"]
    #         }
    #         ninja_info.dojo = Dojo(dojo_data)
    #         ninjas.append(ninja_info) 
    #     return ninjas

    @classmethod
    def save(cls,data):
        query = "INSERT INTO ninjas (first_name,last_name,age,dojos_id) VALUES (%(first_name)s,%(last_name)s,%(age)s,%(dojos_id)s);"

        new_ninja = connectToMySQL('dojo_ninja_schema').query_db(query,data)

        return new_ninja
