from flask import Flask,render_template,session,redirect,request
from users import User

app=Flask(__name__)
app.secret_key="hiiiii"

@app.route("/users/new")
def show():
    return render_template("create.html")

@app.route('/users/new', methods=['POST'])
def create():
    print("===============",request.form)
    User.create(request.form)
    return redirect('/users')

@app.route('/users')
def display():
    disp=User.read()
    return render_template('read_all.html',disp=disp)

if __name__=='__main__':
    app.run(debug=True,port=8000)