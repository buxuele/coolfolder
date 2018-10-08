from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def home():
    return "<h1 style='color: pink'>this is home page</h1>"


@app.route('/video/')
def video():
    return render_template('base.html')


if __name__ == "__main__":
    app.run(debug=True)


