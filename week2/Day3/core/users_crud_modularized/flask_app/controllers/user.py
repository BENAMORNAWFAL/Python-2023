from flask import Flask,render_template,session,redirect,request
from flask_app.models.users import User
from flask_app import app



# ========================create=======================
@app.route("/users/new")
def show():
    return render_template("create.html")

@app.route('/users/create', methods=['POST'])
def create():
    User.create(request.form)
    fin=User.last_user()
    return redirect(f'/users/{fin.id}')

# ========================Read all=======================
@app.route('/users')
def display():
    disp=User.read()
    return render_template('read_all.html',disp=disp)

# ========================Read one=======================
@app.route('/users/<int:id>')
def display_one(id):
    data={"id":id}
    oneuser=User.read_one(data)
    return render_template('read_one.html', one_user=oneuser)

# ========================update=======================
@app.route("/users/<int:id>/edit")
def showedit(id):
    one=User.read_one({'id':id})
    return render_template("edit.html",one=one)

@app.route('/users/<int:id>/edit', methods=["POST"])
def edit(id):
    data={
        "id":id,
        "first_name":request.form["first_name"],
        "last_name":request.form["last_name"],
        "email":request.form["email"]
        }
    User.update(data)
    return redirect(f"/users/{id}")

# ========================update=======================
@app.route('/users/<int:id>/delete')
def delete_user(id):
    data={'id':id}
    User.delete(data)
    return redirect('/users')

