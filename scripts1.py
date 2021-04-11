from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:kas4913*@localhost/GirlsIgnite'
db=SQLAlchemy(app)

class Data(db.Model):
    __tablename__="volunteers"
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(50))
    email=db.Column(db.String(120))
    college=db.Column(db.String(120))
    ideas=db.Column(db.String(250))

    def __init__(self, name,email,college,ideas):
        self.name=name
        self.email=email
        self.college=college
        self.ideas=ideas

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about/')
def about():
    return render_template("about.html")


@app.route('/blog/')
def blog():
    return render_template("blog.html")

@app.route('/contact/')
def contact():
    return render_template("contact.html")

@app.route('/success/', methods=['POST'])
def success():
    if request.form=='POST':
        name=request.form["name"]
        email=request.form["email"]
        college=request.form["college"]
        ideas=request.form["ideas"]
        
    return render_template("success.html")

@app.route('/stories/')
def stories():
    return render_template("stories.html")

if __name__=="__main__":
    app.run(debug=True)