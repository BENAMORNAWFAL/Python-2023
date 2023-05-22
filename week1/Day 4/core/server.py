from flask import Flask, render_template

app= Flask(__name__)

@app.route('/play')
def play():
   return render_template('index.html')

@app.route('/play/<number>')
def playtimes(number):
   return render_template('index.html',times=int(number))

@app.route('/play/<number>/<color>')
def playcolor(number,color):
   return render_template('index.html',times=int(number),txt_color=color)



if __name__=='__main__' :
    app.run(debug=True)