from flask import Flask, render_template, redirect,request,session

app=Flask(__name__)
app.secret_key = "naruto"


@app.route('/')
def desplay():
    return render_template('index1.html')

@app.route('/process', methods=['POST'])
def create():
    
    session['name']=request.form['name']
    session['location']=request.form['location']
    session['language']=request.form['language']
    session['comment']=request.form['comment']

    return redirect('/result')
    
    

@app.route('/result')
def display_form():
    return render_template('index2.html')

@app.route('/set')
def clear():
    session.clear()
    return render_template('index1.html')


if __name__=='__main__':
    app.run(debug=True)