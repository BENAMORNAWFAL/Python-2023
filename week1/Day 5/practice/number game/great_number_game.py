from flask import Flask, render_template , request , session ,redirect
import random
app= Flask(__name__)
app.secret_key = 'MY_KEY'


@app.route('/', methods=['GET','POST'])
def comparation(c='green'):
    session['output']=" "
    session['color']=0
    if request.method == 'POST':
        x=int(request.form['number'])
        if x>get_random():
            session['output']="Too high!"
            session['color']=1
            c='red'
        elif x<get_random():
            session['output']="Too low"
            session['color']=1
            c='red'
        elif x==get_random():
            rand=str(get_random())
            session['output']=rand+" was the number!"
            session['color']=1
            c='green'

    return render_template('great.html',bk_color=c)

@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')

@app.route('/random')
def get_random(n=random.randint(1,100)):
    
    return n



if __name__=='__main__':
    app.run(debug=True)