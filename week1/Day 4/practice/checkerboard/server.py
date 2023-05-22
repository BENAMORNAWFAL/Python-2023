from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def checker(x=4):
    return render_template('board.html',times=x,times2=4)

@app.route('/4')
def checker2(x=2):
    return render_template('board.html',times=x,times2=2)

@app.route('/<x>/<y>')
def checker3(x,y):
    x=int(x)/2
    y=int(y)/2
    return render_template('board.html',times=int(y),times2=int(x))

@app.route('/<x>/<y>/<color1>/<color2>')
def checker4(x,y,color1,color2):
    x=int(x)/2
    y=int(y)/2
    return render_template('board.html',times=int(y),times2=int(x),bg_color1=color1,bg_color2=color2)

if __name__=='__main__':
    app.run(debug=True)