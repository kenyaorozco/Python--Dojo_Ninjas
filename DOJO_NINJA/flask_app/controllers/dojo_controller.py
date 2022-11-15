print("controller file running")

from flask import render_template,redirect,request,session, Flask
from flask_app import app
from flask_app.models.dojos import Dojo
from flask_app.models.ninjas import Ninja





@app.route("/")
def dojo_page():
    all_dojos = Dojo.get_all()
    return render_template("dojo.html",all_dojos=all_dojos)


@app.route("/dojo/<int:id>")
def ninja_page(id):
    data ={
        "id":id,
    }
    one_dojo= Dojo.show_one(data)
    return render_template("display.html", one_dojo = one_dojo)

@app.route("/home")
def home_button():
    return redirect ("/")

@app.route("/create")
def create_button():
    return redirect ("/")

@app.route("/ninja/")
def add_ninja():
    all_dojos = Dojo.get_all()
    return render_template("ninja.html",all_dojos=all_dojos)

@app.route("/ninja/submit",methods=["post"])
def new_ninjas():
    data = {
        "dojos_id": request.form["dojos_id"],
        "first_name":request.form["first_name"],
        "last_name":request.form["last_name"],
        "age":request.form["age"],

    }
    

    new_ninja = Ninja.save(data)
    print(f"the new user id is {new_ninja}")
    return redirect("/")




# @app.route("/create")
# def create_page():
#     return render_template("create.html")

# @app.route("/create/user",methods=["post"])
# def create_user_page():
#     data = {
#         "first_name": request.form["first_name"],
#         "last_name": request.form["last_name"],
#         "email": request.form["email"]
#     }
#     new_user = User.one_all(data)
#     print(f"the new user id is {new_user}")
#     return redirect("/")


# # @app.route("/new/user",methods=["post"])
# # def user_page(): 
# #     data = {
# #         "first_name": request.form["first_name"],
# #         "last_name": request.form["last_name"],
# #         "email": request.form["email"]
# #     }
# #     new_user = User.one_all(data)

# #     return redirect ("/")



# @app.route("/create/show/<int:id>")
# def show(id):
#     data ={ 
#         "id":id
#     }
#     return render_template("user.html",show=User.show(data))

# @app.route("/create/edit/<int:id>")
# def edit():
#     return render_template("edit.html")

# @app.route("/delete")
# def delete():
#     return redirect("/")