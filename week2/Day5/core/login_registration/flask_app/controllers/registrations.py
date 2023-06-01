from flask import render_template,request,redirect,session
from flask_app import app
from flask_app.models.registration import User
from flask import flash

#============================default root=====================
@app.route('/')
def rout():
    return redirect("/logreg")


@app.route('/logreg')
def logreg():
    return render_template("logreg.html")

#=======================register new user==================
@app.route('/create', methods=['POST'])
def register():

    if not User.validate_user(request.form):
        return redirect('/')
    session['name']=request.form['first_name']
    data={
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'email':request.form['email'],
        'password':request.form['password'],
        'confirm_password':request.form['confirm_password']
    }
    User.create_user(data)
    return redirect('/dashboad')

@app.route('/dashboad')
def display():
    return render_template('dashboard.html')

#=======================Login==================
@app.route('/valid', methods=['POST'])
def login():
    data={'email':request.form['log_email'],
          'password':request.form['log_password']
          }
    
    re=User.get_users()
    is_valid=False
    
    for row in re:
        if request.form['log_email']==row['email']:
            is_valid=True                 
            if row['password']!=request.form['log_password']:
                is_valid=False
                
            
                 
       
    if not is_valid:
        flash('check your information','log')
        return redirect('/')
    
    return redirect('/dashboad')

#================================logout==================
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
         
        
        
    


    
    