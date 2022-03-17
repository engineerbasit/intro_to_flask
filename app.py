# from bcrypt import methods
from pickle import TRUE
from flask import Flask,render_template, request
# from request import method

app = Flask(__name__)

@app.route("/")
def index():
    my_variable = "This text is passed from flask to HTML"
    return render_template("HelloHTML.html",my_variable=my_variable)

@app.route("/basit")
def abc():
    return "Hello Abdul Basit"
    
@app.route("/bold")
def bold():
    return "<h1> Hello Flask Darling</h1>"

@app.route("/ifelse")
def ifelse():
    newyear = TRUE
    return render_template("IfElse.html", newyear = newyear)
   
@app.route("/foorloop")   
def foorloop():
    names = ["Basit","Hazma","Abdullah","Asad"]
    return render_template("foorloop.html", names = names)
    
@app.route("/firstpage")
def first():
    return render_template("firstpage.html")

@app.route("/secondpage")
def second():
    return render_template("secondpage.html")

## Adding a form in the page
@app.route("/forms")
def forms():
    return render_template("forms.html")

@app.route("/submit",methods = ['POST'])
def submit():
    name = request.form.get("name")
    abc = "this is Basit! okay bye"
    return render_template("submitted.html",input=abc,USER_input = name)