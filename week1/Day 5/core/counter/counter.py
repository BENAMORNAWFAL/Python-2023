from flask import Flask, render_template, request, redirect, session

app=Flask(__name__)
app.secret_key = "nawfal"

@app.route('/')
def counter():
    if 'count' not in session:
        session['count'] = 1
    else:
        session['count'] += 1
    return render_template('counter.html')

@app.route('/plus2')
def counter2():
    if 'count' not in session:
        session['count'] = 1
    else:
        session['count'] += 2
    return render_template('counter.html')

@app.route('/destroy_session')
def clear():
    session.clear()
    return redirect('/')

@app.route('/add2' )
def add():
    session["count"] += 2
    return render_template('counter.html')

if __name__=='__main__':
    app.run(debug=True, port=8000)