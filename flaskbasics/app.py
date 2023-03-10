'''
Created on 

@author: Surya Pugal

source:
    https://www.w3schools.com/html/html_forms.asp
    https://www.javatpoint.com/flask-app-routing
'''




from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/home/<name>')
def home(name):
    return "hello," + name

    # return render_template('home.html')

@app.route('/login',methods = ['GET', 'POST'])
def login():
        if(request.method == 'POST'):
             name = request.form.get('name')
             password = request.form['pass']
             if name=="Anita" and password=="root":
                  return "Welcome %s" %name
        return render_template("home.html")

        # print("Logegd in... Logged in")
#         







if(__name__ == '__main__'):
    app.run(debug=True)