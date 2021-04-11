from flask import Flask, render_template


app=Flask(__name__)

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
    
    return render_template("success.html")

@app.route('/stories/')
def stories():
    return render_template("stories.html")

if __name__=="__main__":
    app.run(debug=True)