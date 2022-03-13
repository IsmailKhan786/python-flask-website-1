#importing flask 
from flask import Flask ,render_template

#creatinh variable to store flask obj 
app = Flask(__name__)

#url to website 
@app.route("/")

#return this website page 
def home():
    return render_template("home.html")

@app.route("/about")

def about():
    return render_template("about.html")


@app.route("/contact")

def contact():
    return render_template("contact.html")
if __name__ == "__main__":
    app.run(debug=True)
