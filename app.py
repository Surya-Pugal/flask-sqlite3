from flask import Flask, request,render_template
from sqlitedb import insert,select
# from details import Details
app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def home():
    if(request.method=='POST'):
        name = request.form.get('name')
        city = request.form['city']
        
        print(name,city)
        # data = Details(name,city)
        # insert(data)
        data ={}
        data['name'] = name
        data['city'] = city
        insert(data)
        
        print("success")
        print(select())
    return render_template('index.html')


if(__name__ == '__main__'):
    app.run(debug=True)