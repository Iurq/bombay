from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index/index.html")
@app.route('/why')
def why():
    return render_template("why/why.html")
@app.route('/nearby')
def nearby():
    return render_template("nearby/nearby.html")
@app.route('/contact')
def contact():
    return render_template("contact/contact.html")


if __name__ == "__main__" :
    app.run()
