from flask import Flask,render_template

app = Flask(__name__)

@app.route("/hello")
def index():
    my_variable = "This text is passed from flask to HTML"
    return render_template("HelloHTML.html",my_variable=my_variable)

if __name__ == "__main__":  
    app.run()